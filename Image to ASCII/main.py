from PIL import Image
import os

asciiChars = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def resizeImage(image, newWidth = 100):
    width, height = image.size
    aspectRatio = height / width
    newHeight = int(newWidth * aspectRatio * 0.75)
    resizedImage = image.resize((newWidth, newHeight))
    return resizedImage

def grayify(image):
    grayscaleImage = image.convert("L")
    return grayscaleImage

def pixelsToASCII(image):
    pixels = list(image.getdata())
    characters = "".join(asciiChars[pixel//25] for pixel in pixels)
    return characters

def main(newWidth = 100):
    filename = input("Enter the filename of the image (with extension):\n")
    cwd = os.getcwd()
    path = os.path.join(cwd, filename)
    
    try:
        image = Image.open(path)
    except Exception as e:
        print(path, "is not a valid pathname to an image:", e)
        return
        
    newImageData = pixelsToASCII(grayify(resizeImage(image)))
    
    pixelCount = len(newImageData)
    asciiImage = "\n".join(newImageData[i:(i+newWidth)] for i in range(0, pixelCount, newWidth))
    
    print(asciiImage)
    
    with open("asciiImage.txt", "w") as f:
        f.write(asciiImage)
    
main()
