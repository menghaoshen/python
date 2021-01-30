color = 0XF0384E
red = color >> 16
green = color >> 8 & 0XFF
blue = color & 0XFF
print(hex(red),hex(green),hex(blue))