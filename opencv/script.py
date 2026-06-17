import piexif

image_path = "image.jpg"

exif_data = piexif.load("D:\Coding\DIC\opencv\Images\mewo.jpg")

print("0th IFD Tags:\n")

for tag_id, value in exif_data["0th"].items():
    tag_name = piexif.TAGS["0th"][tag_id]["name"]
    print(f"{tag_name}: {value}")