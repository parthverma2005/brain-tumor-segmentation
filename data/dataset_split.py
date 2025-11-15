import os
import random
import shutil

root_dir = r"E:\mini project sem 5\data"  
image_dir = os.path.join(root_dir, "images_folder")
mask_dir = os.path.join(root_dir, "masks_folder")
overlay_dir = os.path.join(root_dir, "overlays_folder")

output_dir = os.path.join(root_dir, "split")
train_ratio, val_ratio, test_ratio = 0.7, 0.15, 0.15 

for split in ["train", "val", "test"]:
    for sub in ["images", "masks", "overlays"]:
        os.makedirs(os.path.join(output_dir, split, sub), exist_ok=True)


all_images = [f for f in os.listdir(image_dir) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
all_images.sort()
random.shuffle(all_images)

n_total = len(all_images)
n_train = int(n_total * train_ratio)
n_val = int(n_total * val_ratio)
n_test = n_total - n_train - n_val

train_files = all_images[:n_train]
val_files = all_images[n_train:n_train+n_val]
test_files = all_images[n_train+n_val:]


def copy_files(file_list, split_name):
    missing_masks = 0
    missing_overlays = 0

    for f in file_list:
        img_src = os.path.join(image_dir, f)
        base_name = os.path.splitext(f)[0]

        mask_src = os.path.join(mask_dir, f"{base_name}_jpg_mask.png")
        overlay_src = os.path.join(overlay_dir, f"{base_name}_jpg_overlay.png")  

        img_dst = os.path.join(output_dir, split_name, "images", f)
        shutil.copy(img_src, img_dst) 

        if os.path.exists(mask_src):
            mask_dst = os.path.join(output_dir, split_name, "masks", os.path.basename(mask_src))
            shutil.copy(mask_src, mask_dst)
        else:
            missing_masks += 1

        if os.path.exists(overlay_src):
            overlay_dst = os.path.join(output_dir, split_name, "overlays", os.path.basename(overlay_src))
            shutil.copy(overlay_src, overlay_dst)
        else:
            missing_overlays += 1

    print(f" {split_name.upper()}: Copied {len(file_list)} images, Missing Masks: {missing_masks}, Missing Overlays: {missing_overlays}")


copy_files(train_files, "train")
copy_files(val_files, "val")
copy_files(test_files, "test")

print(f"\n Done splitting dataset!")
print(f"Train: {len(train_files)}, Val: {len(val_files)}, Test: {len(test_files)}")
