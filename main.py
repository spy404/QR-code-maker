# ------ libs ------ #
import os
import qrcode
from pystyle import *

# ------ setup ------ #  

banner_1 = Center.XCenter("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n")
banner_2 = Center.XCenter("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n")
banner_3 = Center.XCenter("▓▓░░░░░▓▓░░▓░░░▓▓▓░░░▓▓▓░░░▓▓▓▓▓▓░▓░░░▓▓▓▓▓▓░░░▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓▓▓\n")
banner_4 = Center.XCenter("▓░░░▓▓▓▓▓░░▓▓░░░▓▓▓░░░▓░░░▓▓▓▓▓▓░░▓░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓░░▓░░░▓▓▓\n")
banner_5 = Center.XCenter("▓▓▓░░░░▓▓░░▓▓▓░░░▓▓▓▓░░░░▓▓▓▓▓░░░▓▓░░░▓▓▓▓░░░▓▓▓▓▓▓░░░▓▓▓░░░▓▓░░░▓▓▓\n")
banner_6 = Center.XCenter("▓▓▓▓▓░░░▓░░░▓░░░▓▓▓▓▓▓░░░▓▓▓░░░░░░▓░░░░░░▓▓░░░▓▓▓▓░░░▓▓░░░░░░▓░░░░░░\n")
banner_7 = Center.XCenter("▓░░░░░░▓▓░░░▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓\n")
banner_8 = Center.XCenter("▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n")

os.system("cls" if os.name == "nt" else "clear")
Write.Print(banner_1 + "\n", Colors.rainbow, interval = 0.000000009)
Write.Print(banner_2 + "\n", Colors.rainbow, interval = 0.000000009)
Write.Print(banner_3 + "\n", Colors.rainbow, interval = 0.000000009)
Write.Print(banner_4 + "\n", Colors.rainbow, interval = 0.000000009)
Write.Print(banner_5 + "\n", Colors.rainbow, interval = 0.000000009)
Write.Print(banner_6 + "\n", Colors.rainbow, interval = 0.000000009)
Write.Print(banner_7 + "\n", Colors.rainbow, interval = 0.000000009)
Write.Print(banner_8 + "\n", Colors.rainbow, interval = 0.000000009)
data = Write.Input("data -> ", Colors.rainbow, interval = 0.000000009)
version = Write.Input("version -> ", Colors.rainbow, interval = 0.000000009)
box_size = Write.Input("box size -> ", Colors.rainbow, interval = 0.000000009)
border = Write.Input("border -> ", Colors.rainbow, interval = 0.000000009)
fill_color = Write.Input("fill color -> ", Colors.rainbow, interval = 0.000000009)
back_color = Write.Input("back color -> ", Colors.rainbow, interval = 0.000000009)
name = Write.Input("File name -> ", Colors.rainbow, interval = 0.000000009)

Write.Print("Creating...", Colors.rainbow, interval = 0.000000009)

qr = qrcode.QRCode(
    version = version,
    box_size = box_size,
    border = border
)

qr.add_data(data)

qr.make(fit = True)

img = qr.make_image(
    fill_color = fill_color,
    back_color = back_color
)

img.save(f"{name}.png")

Write.Print("Done!", Colors.rainbow, interval = 0.000000009)
