from PIL import Image
import cmath
import pygame
import sys
print(sys.version)

# print(complex(num*num))
c = complex(-0.8, 0.156)  # can be changed to liking


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


screen_width = 900
screen_height = 900
#image = pygame.display.set_mode((screen_width, screen_height))
image = Image.new('RGB', (900, 900), (0, 10, 15))
# pygame.display.flip

max_iter = 1000

for x in range(900):
    for y in range(900):
        a = translate(x, 0, 900, -2, 2)
        b = translate(y, 0, 900, -2, 2)

        savez = complex(a, b)
        n = 0
        z = complex(a, b)
        while(n < 100):
            if(abs(z) > 16):
                break
            z = z*z
            z += c
            n += 1

        bright = translate(n, 0, 100, 0, 255)
        """spe_color = translate(bright, 0, 255, 0, 84)
        if(bright>=0 and bright<=84):
            image.putpixel((x, y), (0, 0, int(spe_color)))
        elif(bright>82 and bright<168):
            image.putpixel((x, y), (0, int(spe_color), 0))
        elif(bright>=164 and bright<252):
            image.putpixel((x, y), (int(spe_color), 0, 0))
        else:
            image.putpixel((x, y), (255, 255, 255))
        """
        #pix = (x+y*500)*4
        # print(bright)
        image.putpixel((x, y), (0+int(bright), 0+int(bright), 0+int(bright)))


image.show()
