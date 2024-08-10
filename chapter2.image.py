from PIL import Image

# Memuat gambar
image = Image.open('/workspaces/multimedia-python/image.jpg')

# Menyimpan gambar
image.save('result.jpg')