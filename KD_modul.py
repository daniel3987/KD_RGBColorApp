import math
import colorsys

class KdColorManager:

    @staticmethod
    def save_color_to_file(rgb, filename="saved_colors.txt"):
        with open(filename, "a") as f:
            f.write(f"{rgb}\n")

    @staticmethod
    def generate_random_color():
        import random
        r = math.floor(random.random() * 256)
        g = math.ceil(random.random() * 255)
        b = round(random.random() * 255)
        return r, g, b

    @staticmethod
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        if len(hex_color) != 6:
            raise ValueError("A HEX színnek pontosan 6 karakter hosszúnak kell lennie.")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def calculate_brightness(rgb):
        r, g, b = rgb
        brightness = 0.299 * r + 0.587 * g + 0.114 * b
        return round(brightness, 2)

    @staticmethod
    def rgb_to_hsv_normalized(rgb):
        r, g, b = rgb
        rf, gf, bf = r / 255.0, g / 255.0, b / 255.0
        h, s, v = colorsys.rgb_to_hsv(rf, gf, bf)
        return h, s, v

    @staticmethod
    def hsv_to_rgb_normalized(h, s, v):
        rf, gf, bf = colorsys.hsv_to_rgb(h, s, v)
        r, g, b = int(rf * 255), int(gf * 255), int(bf * 255)
        return r, g, b


