import tkinter as tk
from tkinter import messagebox
from KD_modul import KdColorManager

app = tk.Tk()
app.title("Színkeverő (KD_RGBColorApp)")
app.geometry("380x480")

def update_color(_event=None):
    r, g, b = red.get(), green.get(), blue.get()
    color_hex = f'#{r:02x}{g:02x}{b:02x}'
    canvas.config(bg=color_hex)
    color_label.config(text=f"RGB: {r}, {g}, {b} | HEX: {color_hex}")

def save_color():
    rgb = (red.get(), green.get(), blue.get())
    KdColorManager.save_color_to_file(rgb)
    messagebox.showinfo("Mentés", "A szín elmentve!")

def random_color():
    r, g, b = KdColorManager.generate_random_color()
    red.set(r)
    green.set(g)
    blue.set(b)
    update_color()

def set_color_from_hex():
    hex_value = hex_entry.get().strip()
    try:
        r, g, b = KdColorManager.hex_to_rgb(hex_value)
        red.set(r)
        green.set(g)
        blue.set(b)
        update_color()
        messagebox.showinfo("Átváltás sikeres", f"HEX: {hex_value.upper()} -> RGB: {r}, {g}, {b}")
    except Exception as e:
        messagebox.showerror("Hiba", str(e))

def show_brightness():
    rgb = (red.get(), green.get(), blue.get())
    brightness = KdColorManager.calculate_brightness(rgb)
    messagebox.showinfo("Világosság", f"Az aktuális szín világossága: {brightness}")

red = tk.IntVar(value=0)
green = tk.IntVar(value=0)
blue = tk.IntVar(value=0)

tk.Scale(app, from_=0, to=255, variable=red, label="Piros", orient="horizontal", command=update_color).pack()
tk.Scale(app, from_=0, to=255, variable=green, label="Zöld", orient="horizontal", command=update_color).pack()
tk.Scale(app, from_=0, to=255, variable=blue, label="Kék", orient="horizontal", command=update_color).pack()

canvas = tk.Canvas(app, width=170, height=60)
canvas.pack(pady=10)
canvas.config(bg="#000000")

color_label = tk.Label(app, text="RGB: 0, 0, 0 | HEX: #000000")
color_label.pack(pady=5)

frame = tk.Frame(app)
frame.pack(pady=5)

hex_entry = tk.Entry(frame, width=10)
hex_entry.pack(side="left", padx=3)
hex_entry.insert(0, "#000000")

tk.Button(frame, text="HEX beállítása", command=set_color_from_hex).pack(side="left", padx=3)
tk.Button(app, text="Véletlen szín", command=random_color).pack(pady=3)
tk.Button(app, text="Világosság mutatása", command=show_brightness).pack(pady=3)
tk.Button(app, text="Szín mentése", command=save_color).pack(pady=3)

update_color()
app.mainloop()

