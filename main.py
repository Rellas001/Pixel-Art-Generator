import random
from PIL import Image

imagePath = "image.jpg"


def create_pixel_art(img, size, colors, color_option):
    # Resize the image to a smaller size
    small_size = int(size / 4)
    img = img.resize((small_size, small_size), resample=Image.NEAREST)

    # Resize the image again to the desired pixel art size
    img = img.resize((size, size), resample=Image.NEAREST)

    # Convert the image to a 2D array of RGB values
    pixels = list(img.getdata())
    pixels = [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]

    # Replace each pixel with the closest color from the list of colors
    for i in range(img.height):
        for j in range(img.width):
            if color_option == "greyscale":
                closest_color = min(
                    colors, key=lambda x: abs(x[0]-pixels[i][j][0]))
            else:
                closest_color = min(colors, key=lambda x: sum(
                    [(x[k]-pixels[i][j][k])**2 for k in range(3)]))
            pixels[i][j] = closest_color

    # Create a new image using the modified pixels
    new_img = Image.new("RGB", (img.width, img.height))
    new_img.putdata([pixel for row in pixels for pixel in row])

    return new_img


def get_greyscale_colors():
    return [(i, i, i) for i in range(256)]


def get_random_colors():
    return [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for i in range(256)]


def get_pastel_colors():
    return [(random.randint(200, 255), random.randint(200, 255), random.randint(200, 255)) for i in range(256)]


def get_cool_tone_colors():
    return [(random.randint(0, 127), random.randint(0, 255), random.randint(255, 255)) for i in range(256)]


def get_hot_tone_colors():
    return [(random.randint(255, 255), random.randint(0, 127), random.randint(0, 127)) for i in range(256)]


if __name__ == "__main__":
    # Load the original image
    img = Image.open(imagePath)

    # Prompt the user for the size of the pixel art
    size = int(input("Enter the size of the pixel art (in pixels): "))

    # Prompt the user for the color option
    color_option = input(
        "Enter color option (greyscale, random, pastel, cool, hot): ")

    # Get the color palette based on the user's choice
    if color_option == "greyscale":
        colors = get_greyscale_colors()
    elif color_option == "random":
        colors = get_random_colors()
    elif color_option == "pastel":
        colors = get_pastel_colors()
    elif color_option == "cool":
        colors = get_cool_tone_colors()
    elif color_option == "hot":
        colors = get_hot_tone_colors()
    else:
        print("Invalid color option.")

    pixel_art = create_pixel_art(img, size, colors, color_option)

    # Save the pixel art image
    pixel_art.save("pixel_art.jpg")
