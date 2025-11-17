from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from PIL import Image
import numpy as np
import cv2
import base64
import os

from backend.model.UNet import UNet

app = Flask(__name__)
CORS(app)



device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = UNet(in_ch=1, out_ch=1).to(device)

MODEL_PATH = os.path.join("backend","model", "best_model_finetuned.pth")

model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.eval()




def preprocess_image(image: Image.Image):
    img = np.array(image).astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=(0, 1))
    return torch.tensor(img, dtype=torch.float32)


def postprocess_mask(mask_tensor):
    mask = mask_tensor.squeeze().detach().cpu().numpy()
    mask = (mask > 0.5).astype(np.uint8) * 255
    return mask




@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    image = Image.open(file.stream).convert("L")
    img_tensor = preprocess_image(image).to(device)

    with torch.no_grad():
        output = torch.sigmoid(model(img_tensor))

        raw_mask = output.squeeze().detach().cpu().numpy()
        tumor_pixels = raw_mask[raw_mask > 0.5]

        confidence = float(tumor_pixels.mean()) if tumor_pixels.size > 0 else 0.0
        mask = postprocess_mask(output)

    img_np = np.array(image.resize((256, 256)))
    mask_resized = cv2.resize(mask, (256, 256))

    overlay = cv2.cvtColor(img_np, cv2.COLOR_GRAY2BGR)
    overlay[mask_resized > 127] = [255, 0, 0]

    blended = cv2.addWeighted(
        cv2.cvtColor(img_np, cv2.COLOR_GRAY2BGR), 0.7,
        overlay, 0.3,
        0
    )

    _, buffer = cv2.imencode(".png", blended)
    overlay_base64 = base64.b64encode(buffer).decode("utf-8")

    return jsonify({
        "model": "U-Net",
        "confidence": round(confidence, 4),
        "overlay": overlay_base64
    })




# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)
