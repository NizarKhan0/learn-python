from PIL import Image, ImageFilter

img = Image.open(
    "C:/laragon/www/learn-python/source-1/scripting/pokedex/pikachu.jpg")
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save(
    "C:/laragon/www/learn-python/source-1/scripting/pokedex/pikachu_blurred.jpg")
filtered_img = img.convert("L")  # Convert to grayscale
filtered_img.save(
    "C:/laragon/www/learn-python/source-1/scripting/pokedex/pikachu_grayscale.jpg")


print(img.size)  # Output the size of the image
print(img.format)  # Output the format of the image
print(img.mode)  # Output the mode of the image (e.g., RGB, L)
print(img.info)  # Output additional information about the image
img.show()  # Display the image
