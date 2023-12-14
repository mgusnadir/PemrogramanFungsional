# TODO 0 : Import library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open("assets\jude.jpeg")

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype("font\ini_arial.ttf", 24)
text = "Muhammad Gus Nadir-202110370311481"
text_width = draw.textlength(text, font)
text_x = (gambarku.width - text_width) // 2
text_y = 20
draw.text((text_x, text_y), text, font=font, fill="white")


# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save("assets\latihan1.jpeg")

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()