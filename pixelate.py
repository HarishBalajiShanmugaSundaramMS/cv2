from PIL import Image
image = Image.open("IronMan.jpg")
image_resized = image.resize((100, 100))
#The image is resized into a 100 x 100 matrix
result_01 = image_resized.resize(image.size, Image.BILINEAR)
result_01.save('Bilinear IronMan.png')
result_02 = image_resized.resize(image.size, Image.NEAREST)
result_02.save('Nearest IronMan.png')
