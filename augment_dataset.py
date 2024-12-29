import os
import cv2
import albumentations as A
from tqdm import tqdm

# Define augmentations
transform = A.Compose([
    A.ToGray(p=1.0),
    A.RandomBrightnessContrast(brightness_limit=0.1, contrast_limit=0.1, p=0.5),
])

# Paths to the original dataset and the new augmented dataset
input_images_dir = '/path/to/original/images'
input_labels_dir = '/path/to/original/labels'
output_images_dir = '/path/to/augmented/images'
output_labels_dir = '/path/to/augmented/labels'

# Create output directories
os.makedirs(output_images_dir, exist_ok=True)
os.makedirs(output_labels_dir, exist_ok=True)

def augment_dataset():
    # Print progress bar with tqdm
    for img_filename in tqdm(os.listdir(input_images_dir)):
        if img_filename.endswith('.jpg'):
            base_filename = os.path.splitext(img_filename)[0]

            # Load image
            img_path = os.path.join(input_images_dir, img_filename)
            image = cv2.imread(img_path)

            # Load YOLO labels
            label_path = os.path.join(input_labels_dir, base_filename + '.txt')
            with open(label_path, 'r') as f:
                labels = f.readlines()

            # Apply augmentation
            try:
                augmented = transform(image=image)
            except:
                print(f"Skipping {img_filename} due to an augmentation error")
                continue

            # Save augmented image
            augmented_image = augmented['image']
            cv2.imwrite(os.path.join(output_images_dir, f'{base_filename}.jpg'), augmented_image)

            # Copy labels
            augmented_label_path = os.path.join(output_labels_dir,  f'{base_filename}.txt')
            with open(augmented_label_path, 'w') as f:
                for line in labels:
                    f.write(line)

augment_dataset()