from PIL import Image
import cmath
import pygame

# print(complex(num*num))


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


image = Image.new('RGB', (900, 900), (0, 10, 15))

max_iter = 1000

for x in range(900):
    for y in range(900):
        a = translate(x, 0, 900, -2, 1.5)
        b = translate(y, 0, 900, -2, 1.5)

        savez = complex(a, b)
        n = 0
        z = complex(a, b)
        while(n < 100):
            if(abs(z) > 16):
                break
            z = z*z
            z += savez
            n += 1

        bright = translate(n, 0, 100, 0, 255)
        # pix = (x+y*500)*4
        # print(bright)
        # if(bright != 255):
        image.putpixel((x, y), (0+int(bright), 0+int(bright), 0+int(bright)))
        # else:
        #image.putpixel((x, y), (0, 0, 0))

image.show()
