from PIL import Image, ImageFilter

img = Image.open(
    "C:/laragon/www/learn-python/source-1/scripting/pokedex/pikachu.jpg")

print(img.size)  # Output the size of the image
print(img.format)  # Output the format of the image
print(img.mode)  # Output the mode of the image (e.g., RGB, L)
print(img.info)  # Output additional information about the image
img.show()  # Display the image


# Perform some image manipulations
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save(
    "C:/laragon/www/learn-python/source-1/scripting/pokedex/pikachu_blurred.jpg")
filtered_img = img.convert("L")  # Convert to grayscale
filtered_img.save(
    "C:/laragon/www/learn-python/source-1/scripting/pokedex/pikachu_grayscale.jpg")
crooked = filtered_img = img.rotate(90)  # Rotate the image by 90 degrees
crooked.save(
    "C:/laragon/www/learn-python/source-1/scripting/pokedex/pikachu_rotated.jpg")
resized = img.resize((200, 200))  # Resize the image to 200x200 pixels
resized.save(
    "C:/laragon/www/learn-python/source-1/scripting/pokedex/pikachu_resized.jpg")
cropped = img.crop((100, 100, 400, 400))  # Crop the image
cropped.save(
    "C:/laragon/www/learn-python/source-1/scripting/pokedex/pikachu_cropped.jpg")
