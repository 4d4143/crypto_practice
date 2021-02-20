from PIL import Image
from PIL import ImageChops


def main():

    trianglePath = './triangle.jpeg'
    circlePath = './circle.jpeg'
    keyPath = './square.jpeg'

    image1 = Image.open(trianglePath).convert('1')
    image2 = Image.open(circlePath).convert('1')
    keyImage = Image.open(keyPath).convert('1')

    cipher1 = ImageChops.logical_xor(image1, keyImage)
    cipher2 = ImageChops.logical_xor(image2, keyImage)

    cipher1.save('cipher1.jpeg')
    cipher2.save('cipher2.jpeg')

    xorCiphers = ImageChops.logical_xor(cipher1, cipher2)

    xorCiphers.save('xorCiphers.jpeg')


if __name__ == '__main__':
    main()
