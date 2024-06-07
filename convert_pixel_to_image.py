from PIL import Image, ImageEnhance, ImageFilter
import panda as pd
import os

def create_grayscale_image(pixel_data, width, height):
    # Create a new grayscale image with the given width and height
    image = Image.new('L', (width, height))

    # Put pixel data into the image
    image.putdata(pixel_data)

    return image

def enhance_image(image):
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)

    image = image.filter(ImageFilter.SHARPEN)
    return image

def foo():
    # load the pixel info from the csv file
    csv_data = pd.read_csv('pixel_data.csv')
    for i in range(len(csv_data)):
        # ignore the first column which is the index
        pixel_data = csv_data.iloc[i][1:]
        width = 28
        height = 28
        image = create_grayscale_image(pixel_data, width, height)
        enhanced_image = enhance_image(image)
        enhanced_image.show()
        # Create a new folder called 'output_images' if it doesn't exist
        if not os.path.exists('train'):
            os.makedirs('train')
        
        # Create a new file named output_images_csv, which has first column as the name of the image and second column as the pixel label i.e.., csv_data.iloc[i][0]
        
        output_images_csv = 'output_images_csv.csv'
        image_name =  str(i+1) + '.png'
        image_label = csv_data.iloc[i][0]
        image_info = pd.DataFrame({'Image Name': [image_name], 'Image Label': [image_label]})
        image_info.to_csv(output_images_csv, index=False, mode='a', header=not os.path.exists(output_images_csv))
        
        
        
            
        # Save the image to the 'output_images' folder with names as output_image_0.png, output_image_1.png, etc.  
        
        enhanced_image.save(str(i+1) + '.png')
        
        
    
    
        


def basic_driver():
        
    # Example pixel data for a 2x2 grayscale image
    # Each value represents the intensity of the pixel
    pixel_data = [
        0, 255,   # Black, White
        128, 64   # Medium gray, Dark gray
    ]

    # Image dimensions
    width = 28
    height = 28

    # Create the image
    image = create_grayscale_image(pixel_data, width, height)

    #Enhance the image
    enhanced_image = enhance_image(image)

    # Display the image
    enhanced_image.show()

    # Save the image to a file
    enhanced_image.save('output_grayscale_image.png')

if __name__ == "__main__":
    foo()
