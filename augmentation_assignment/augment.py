from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import os

input_folder = "dataset"
output_folder = "augmented"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):

    if file.endswith(".jpg") or file.endswith(".png"):

        img = Image.open(os.path.join(input_folder, file))

        name = file.split(".")[0]

        img.save(f"{output_folder}/{name}_original.jpg")

        rotated = img.rotate(45)
        rotated.save(f"{output_folder}/{name}_rotated.jpg")

        flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
        flipped.save(f"{output_folder}/{name}_flipped.jpg")

        bright = ImageEnhance.Brightness(img).enhance(1.5)
        bright.save(f"{output_folder}/{name}_bright.jpg")

        dark = ImageEnhance.Brightness(img).enhance(0.5)
        dark.save(f"{output_folder}/{name}_dark.jpg")

        contrast = ImageEnhance.Contrast(img).enhance(2)
        contrast.save(f"{output_folder}/{name}_contrast.jpg")

        saturation = ImageEnhance.Color(img).enhance(2)
        saturation.save(f"{output_folder}/{name}_saturation.jpg")

        crop = img.crop((50, 50, img.width-50, img.height-50))
        crop.save(f"{output_folder}/{name}_crop.jpg")

        blur = img.filter(ImageFilter.BLUR)
        blur.save(f"{output_folder}/{name}_blur.jpg")

print("augmentation completed")