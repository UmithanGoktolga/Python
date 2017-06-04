from PIL import Image

myImage = Image.open("manzara.jpg").convert('L')
myImage.rotate(45).show()

secondImage = myImage.resize((64,64))
#secondImage.show()

myImage.paste(secondImage.rotate(45))
myImage.show()