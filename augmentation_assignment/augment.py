from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import numpy as np
import os

input_folder = "dataset"
output_folder = "augmented"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):

    if file.lower().endswith((".jpg", ".jpeg", ".png")):

        img = Image.open(os.path.join(input_folder, file))

        name = os.path.splitext(file)[0]

        img.save(f"{output_folder}/{name}_original.jpg")

        rotated = img.rotate(45)
        rotated.save(f"{output_folder}/{name}_rotated.jpg")

        flip_h = img.transpose(Image.FLIP_LEFT_RIGHT)
        flip_h.save(f"{output_folder}/{name}_flip_horizontal.jpg")

        flip_v = img.transpose(Image.FLIP_TOP_BOTTOM)
        flip_v.save(f"{output_folder}/{name}_flip_vertical.jpg")

        crop = img.crop((50, 50, img.width - 50, img.height - 50))
        crop.save(f"{output_folder}/{name}_cropped.jpg")

        bright = ImageEnhance.Brightness(img).enhance(1.5)
        bright.save(f"{output_folder}/{name}_bright.jpg")

        dark = ImageEnhance.Brightness(img).enhance(0.5)
        dark.save(f"{output_folder}/{name}_dark.jpg")

        contrast = ImageEnhance.Contrast(img).enhance(2)
        contrast.save(f"{output_folder}/{name}_contrast.jpg")

        saturation = ImageEnhance.Color(img).enhance(2)
        saturation.save(f"{output_folder}/{name}_saturation.jpg")

        blur = img.filter(ImageFilter.BLUR)
        blur.save(f"{output_folder}/{name}_blur.jpg")

        sharpen = img.filter(ImageFilter.SHARPEN)
        sharpen.save(f"{output_folder}/{name}_sharpen.jpg")

        grayscale = img.convert("L")
        grayscale.save(f"{output_folder}/{name}_grayscale.jpg")

        img_array = np.array(img)
        noise = np.random.normal(0, 25, img_array.shape)
        noisy_img = img_array + noise
        noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)
        Image.fromarray(noisy_img).save(f"{output_folder}/{name}_gaussian_noise.jpg")

print("all augmentations completed")