import tkinter as tk
from tkinter import messagebox
from KD_modul import KdColorManager

app = tk.Tk()
app.title("Színkeverő (KD_RGBColorApp)")
app.geometry("400x520")

def update_color():
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
    except ValueError:
        messagebox.showerror("Hiba", "6 karakteres HEX számot adj meg !")

def show_brightness():
    rgb = (red.get(), green.get(), blue.get())
    brightness = KdColorManager.calculate_brightness(rgb)
    messagebox.showinfo("Világosság", f"Az aktuális szín világossága: {brightness}")

def show_hsv():
    rgb = (red.get(), green.get(), blue.get())
    h, s, v = KdColorManager.rgb_to_hsv_normalized(rgb)
    h_deg = round(h * 360, 1)
    s_pct = round(s * 100, 1)
    v_pct = round(v * 100, 1)
    messagebox.showinfo(
        "HSV értékek",
        f"H: {h_deg}°, S: {s_pct}%, V: {v_pct}%"
    )

def set_from_hsv():
    try:
        h_val = float(h_entry.get().strip())
        s_val = float(s_entry.get().strip())
        v_val = float(v_entry.get().strip())
        h = h_val / 360.0
        s = s_val / 100.0
        v = v_val / 100.0
        r, g, b = KdColorManager.hsv_to_rgb_normalized(h, s, v)
        red.set(r)
        green.set(g)
        blue.set(b)
        update_color()
        messagebox.showinfo(
            "HSV -> RGB",
            f"HSV: ({h_val}, {s_val}%, {v_val}%) -> RGB: {r}, {g}, {b}"
        )
    except ValueError:
        messagebox.showerror("Hiba", "Számot adj meg a HSV mezőkben!")


red = tk.IntVar(value=0)
green = tk.IntVar(value=0)
blue = tk.IntVar(value=0)

tk.Scale(app, from_=0, to=255, variable=red, label="Piros", orient="horizontal",
         command=lambda _x: update_color()).pack()
tk.Scale(app, from_=0, to=255, variable=green, label="Zöld", orient="horizontal",
         command=lambda _x: update_color()).pack()
tk.Scale(app, from_=0, to=255, variable=blue, label="Kék", orient="horizontal",
         command=lambda _x: update_color()).pack()

canvas = tk.Canvas(app, width=170, height=60)
canvas.pack(pady=10)
canvas.config(bg="#000000")

color_label = tk.Label(app, text="RGB: 0, 0, 0 | HEX: #000000")
color_label.pack(pady=5)

hex_frame = tk.Frame(app)
hex_frame.pack(pady=5)

hex_entry = tk.Entry(hex_frame, width=10)
hex_entry.pack(side="left", padx=3)
hex_entry.insert(0, "#000000")

tk.Button(hex_frame, text="HEX beállítása", command=set_color_from_hex).pack(side="left", padx=3)

hsv_frame = tk.Frame(app)
hsv_frame.pack(pady=5)

tk.Label(hsv_frame, text="H:").pack(side="left")
h_entry = tk.Entry(hsv_frame, width=5)
h_entry.pack(side="left", padx=2)
h_entry.insert(0, "0")

tk.Label(hsv_frame, text="S%:").pack(side="left")
s_entry = tk.Entry(hsv_frame, width=5)
s_entry.pack(side="left", padx=2)
s_entry.insert(0, "0")

tk.Label(hsv_frame, text="V%:").pack(side="left")
v_entry = tk.Entry(hsv_frame, width=5)
v_entry.pack(side="left", padx=2)
v_entry.insert(0, "0")

tk.Button(hsv_frame, text="HSV -> RGB", command=set_from_hsv).pack(side="left", padx=4)
tk.Button(app, text="RGB -> HSV", command=show_hsv).pack(pady=3)

tk.Button(app, text="Véletlen szín", command=random_color).pack(pady=3)
tk.Button(app, text="Világosság mutatása", command=show_brightness).pack(pady=3)
tk.Button(app, text="Szín mentése", command=save_color).pack(pady=3)

update_color()
app.mainloop()


