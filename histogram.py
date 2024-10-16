import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

# Path ke gambar
path = "C:\\Users\\JARKOM 17\\Downloads\\RGB.jpg"

# Membaca gambar
image = img.imread(path)

# Mengonversi gambar RGB menjadi grayscale
gray_image = 0.2989 * image[:,:,0] + 0.5870 * image[:,:,1] + 0.1140 * image[:,:,2]
gray_image = gray_image.astype(np.uint8)  # Konversi ke tipe data uint8

# Menghitung histogram untuk gambar RGB
hist_r, bins_r = np.histogram(image[:,:,0].flatten(), bins=256, range=[0, 256])
hist_g, bins_g = np.histogram(image[:,:,1].flatten(), bins=256, range=[0, 256])
hist_b, bins_b = np.histogram(image[:,:,2].flatten(), bins=256, range=[0, 256])

# Menghitung histogram untuk gambar grayscale
hist_gray, bins_gray = np.histogram(gray_image.flatten(), bins=256, range=[0, 256])

# Menampilkan gambar dan histogram
plt.figure(figsize=(12, 12))

# Gambar RGB
plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title("Gambar RGB")
plt.axis("off")

# Histogram RGB
plt.subplot(2, 2, 2)
plt.plot(hist_r, color='red', label='Red Channel')
plt.plot(hist_g, color='green', label='Green Channel')
plt.plot(hist_b, color='blue', label='Blue Channel')
plt.title("Histogram RGB")
plt.xlim([0, 256])
plt.xlabel("Intensitas")
plt.ylabel("Frekuensi")
plt.legend()

# Gambar Grayscale
plt.subplot(2, 2, 3)
plt.imshow(gray_image, cmap='gray')
plt.title("Gambar Grayscale")
plt.axis("off")

# Histogram Grayscale
plt.subplot(2, 2, 4)
plt.plot(hist_gray, color='gray')
plt.title("Histogram Grayscale")
plt.xlim([0, 256])
plt.xlabel("Intensitas")
plt.ylabel("Frekuensi")

plt.tight_layout()
plt.show()

# Menyimpan gambar grayscale
img.imwrite("C:\\Users\\JARKOM 17\\Downloads\\grayscale_image.jpg", gray_image)
