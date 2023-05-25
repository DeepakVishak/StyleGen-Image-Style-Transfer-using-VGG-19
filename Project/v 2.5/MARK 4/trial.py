from craiyon import Craiyon, craiyon_utils
from PIL import Image # pip install pillow
from io import BytesIO
import base64

generator = Craiyon() # Instantiates the api wrapper
result = generator.generate("Professional photo of Obama flashing a flag with his last name") # Generates 9 images by default and you cannot change that
print(result.description) # >>> Obama holding up a flag with his last name, smiling confidently
images = craiyon_utils.encode_base64(result.images)
for i in images:
    image = Image.open(BytesIO(base64.decodebytes(i)))
    # To convert the .webp images to .jpg or .png, you can proceed like this
    image.convert("RGB").resize((640, 480)).save("image.jpg", "JPEG") # For ".jpg" images
    #image.convert("RGBA").save("image.png", "PNG") # For ".png" images
    
    # Use the PIL's Image object as per your needs
