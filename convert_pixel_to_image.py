from PIL import Image

def create_grayscale_image(pixel_data, width, height):
    # Create a new grayscale image with the given width and height
    image = Image.new('L', (width, height))

    # Put pixel data into the image
    image.putdata(pixel_data)

    return image

# Example pixel data for a 2x2 grayscale image
# Each value represents the intensity of the pixel
pixel_data = [
    0, 255,   # Black, White
    128, 64   # Medium gray, Dark gray
]

# Image dimensions
width = 2
height = 2

# Create the image
image = create_grayscale_image(pixel_data, width, height)

# Display the image
image.show()

# Save the image to a file
image.save('output_grayscale_image.png')

