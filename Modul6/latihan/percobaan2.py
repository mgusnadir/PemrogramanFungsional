# TODO 0 : Import beberapa library lain yang dibutuhkan
from PIL import Image

# TODO 1 : Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open("assets\jude.jpeg")
overlay_image = Image.open("assets\kue.jpg")

# TODO 2 : Konversi overlay image ke mode RGBA (menghilangkan alpha channel)
overlay_image = overlay_image.convert("RGBA")
overlay_image.load()

# TODO 3 : (optional) Perkecil ukuran gambar overlay menggunakan method resize()
width, height = overlay_image.size
new_width = 200
new_height = int((new_width / width) * height)
overlay_image = overlay_image.resize((new_width, new_height), Image.LANCZOS)

# Tentukan/Hitung koordinat untuk menempatkan overlay di pojok kanan atas
x_top_right = background_image.width - overlay_image.width
y_top_right = 0

# TODO 4 : Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_top_right, y_top_right), mask=overlay_image)

# TODO 5 : Simpan gambar hasil edit
background_image.save("assets\latihan2.jpeg")

# TODO 6 : Tampilkan
background_image.show()
