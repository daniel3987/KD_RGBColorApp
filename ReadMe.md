# Színkeverő alkalmazás (KD_RGBColorApp)

**Készítette:** Kékesi Dániel

## Feladat leírása
Az alkalmazás egy egyszerű RGB színkeverő grafikus program.  
Három csúszka segítségével (piros, zöld, kék) lehet beállítani a színt, amely megjelenik egy színes mezőben.  
A program tud:
- véletlenszerű RGB színt generálni,
- HEX színt RGB-vé átalakítani,
- kiszámítani az aktuális szín világosságát,
- az RGB színt HSV-re átalakítani, majd vissza RGB-re (colorsys modul).

A kiválasztott színeket fájlba is el tudja menteni.

## Használt modulok és függvények

- **math**
  - `floor`, `ceil`, `round`


- **tkinter**
  - `Tk`, `Scale`, `Canvas`, `Label`, `Button`, `Frame`, `Entry`, `messagebox`.


- **colorsys**
  - `rgb_to_hsv(r, g, b)`
  - `hsv_to_rgb(h, s, v)`


- **KD_modul.py**
  - Osztály: `KdColorManager`
  - Függvények:
    - `save_color_to_file(rgb, filename="saved_colors.txt")`
    - `generate_random_color()`
    - `hex_to_rgb(hex_color)`
    - `calculate_brightness(rgb)`
    - `rgb_to_hsv_normalized(rgb)`
    - `hsv_to_rgb_normalized(h, s, v)`
