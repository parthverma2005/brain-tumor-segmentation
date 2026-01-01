Overview
This project focuses on the automatic segmentation of brain tumors from MRI images using the U-Net deep learning architecture. 
The model accurately identifies and highlights tumor regions, assisting in earlydiagnosis and medical analysis.
U-Net is widely used in medical image segmentation due to its ability to capture both context and fine-grained details, making it ideal for pixel-level predictions.

Features-
 1. Automatic tumor segmentation from MRI scans
 2. Pixel-wise tumor mask generation
 3. High accuracy with clear tumor boundary detection
 4. End-to-end deep learning pipeline

Model Architecture-
 1. U-Net (CNN-based encoder–decoder)
 2. Skip connections for better spatial information
 3. Optimized for medical image segmentation

Tech Stack-
1. Python
2. TensorFlow / PyTorch
3. OpenCV
4. NumPy
5. Matplotlib
6. Pillow

Results
1. Segmentation Accuracy: ~97.66%
2. Successfully highlights tumor regions on MRI images
3. Produces clear and interpretable output masks

How to Run-
-pip install -r requirements.txt
-python train.py
-python predict.py
