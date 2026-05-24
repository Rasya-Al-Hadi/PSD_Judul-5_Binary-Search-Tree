Judul Program : Sistem Data Nomor Rak Perpustakaan

Deskripsi : Program ini bertujuan untuk mendata nomor rak di perpustakaan. Program ini merupakan Implementasi dari BTSDasar yang dimana Binary Search Tree yang menggunakan Penyusunan dengan Inorder/Preorder/Postorder

Source Code :

<img width="1710" height="5916" alt="Tugas Akhir 5" src="https://github.com/user-attachments/assets/2ad627a0-6442-4d3f-942f-f0d209435dec" />


Baris 1: Membuat kelas bernama Node

Baris 2: menyimpan nilai yang dimasukkan ke dalam node

Baris 3: menyimpan nilai yang diterima ke dalam atribut key

Baris 4: awalnya kosong disebelah kiri

Baris 5: awalnya kosong disebelah kanan

Baris 8: membuat kelas binary seach tree

Baris 9: mendefinisikan konstruktor binary search tree

Baris 10: akar pohon BST masih kosong

Baris 12: mendefiniskan fungsi rekursif untuk memasukkan data

Baris 13: Jika posisi kosong ditemukan

Baris 14: Membuat node baru

Baris 15: Jika nilai lebih kecil dari root

Baris 16: masuk ke subtree kiri

Baris 17: Jika nilai lebih besar dari root

Baris 18: masuk ke subtree kanan

Baris 19: Mengembalikan root yang sudah diperbarui

Baris 21:  mendefinisikan fungsi yang dipanggil pengguna

Baris 22: Memulai proses insert dari akar pohon

Baris 24: mendefinisikan fungsi mencari data

Baris 25: Jika node kosong

Baris 26: data tidak ditemukan

Baris 27: Jika data ditemukan

Baris 28: Mengembalikan nilai benar

Baris 29: Jika data lebih kecil

Baris 30: Rekursi ke subtree kiri

Baris 31: Jika lebih besar, cari ke kanan

Baris 33: Fungsi yang dipanggil pengguna

Baris 34: Mulai pencarian dari akar

Baris 36: mendefinisikan fungsi inorder

Baris 37: Jika node kosong

Baris 38: Berhenti

Baris 39: Kunjungi sebelah kiri

Baris 40: menampilkan root

Baris 41: Kunjungi sebelah kanan

Baris 43: mendefinisikan fungsi preorder

Baris 44: Jika node kosong

Baris 45: Berhenti

Baris 46: menampilkan root

Baris 47: Kunjungi sebelah kiri

Baris 48: Kunjungi sebelah kanan

Baris 50: mendefinisikan fungsi postorder

Baris 51: Jika node kosong

Baris 52: Berhenti

Baris 53: Kunjungi sebelah kiri

Baris 54: Kunjungi sebelah kanan

Baris 55: menampilkan root

Baris 57: mendefenisikan fungsi mencari node paling kiri

Baris 58: Jika node kosong

Baris 59: tidak ada data yang dicari

Baris 60: Mulai dari root

Baris 61: bergerak ke kiri

Baris 62: Pindah ke anak kiri

Baris 63: Kembalikan nilai terkecil
 
Baris 65: mendefenisikan fungsi mencari node paling kanan

Baris 66: Jika node kosong

Baris 67: tidak ada data yang dicari

Baris 68: Mulai dari root

Baris 69: bergerak ke kanan

Baris 70: Pindah ke anak kanan

Baris 71: Kembalikan nilai terbesar

Baris 73: mendefinisikan fungsi menghitung banyak node

Baris 74: Jika node kosong

Baris 75: kembali ke nilai 0

Baris 76: menghitung banyak node

Baris 78: mendefinisikan fungsi menghitung total seluruh nomor rak

Baris 79: Jika node kosong

Baris 80: kembali ke nilai 0

Baris 81: menghitung keseluruhan nomor rak

Baris 84: mendefenisikan fungsi utama program

Baris 85: perpustakaan sebagai BSTDasar

Baris 86: Variabel menu

Baris 88: program berjalan sampai pengguna memilih 10

Baris 89: Menampilkan judul menu

Baris 90: menampilkan pilihan 1

Baris 91: menampilkan pilihan 2

Baris 92: menampilkan pilihan 3

Baris 93: menampilkan pilihan 4

Baris 94: menampilkan pilihan 5

Baris 95: menampilkan pilihan 6

Baris 96: menampilkan pilihan 7

Baris 97: menampilkan pilihan 8

Baris 98: menampilkan pilihan 9

Baris 99: menampilkan pilihan 10

Baris 100: digunakan untuk menangani error input

Baris 101: Membaca pilihan pengguna

Baris 102: Menangkap error jika input bukan angka

Baris 103: menampilkan Input tidak valid!

Baris 104: Menangkap error jika input bukan angka

Baris 105: Pilihan menambah nomor rak

Baris 106: digunakan untuk menangani error input

Baris 107: Input nomor rak

Baris 108: menambahkan nomor rak yang ditambahkan

Baris 109: menampilkan Nomor rak berhasil ditambahkan

Baris 110: Menangkap error jika input bukan angka

Baris 111: menampilkan Nomor rak harus berupa angka!

Baris 112: Pilihan mengecek nomor rak

Baris 113: digunakan untuk menangani error input

Baris 114: input nomor rak yang dicari

Baris 115: Memanggil fungsi search

Baris 116: menampilkan Nomor rak ditemukan

Baris 117: jika nomor rak tidak ada

Baris 118: menampilkan Nomor rak tidak ditemukan

Baris 119: menangkap error jika input bukan angka

Baris 120: menampilkan input harus berupa angka

Baris 121: Jika memlilih pilihan 3

Baris 122: menampilkan Daftar nomor rak (urut naik)

Baris 123: mengurutkan data inorder

Baris 124: menampilkan data inorder

Baris 125: Jika memlilih pilihan 4

Baris 126: menampilkan Nomor rak (Preorder)

Baris 127: mengurutkan data preorder

Baris 128: menampilkan data preorder

Baris 129: Jika memilih pilihan 5

Baris 130: menampilkan Tampilkan rak (Postorder)

Baris 131: mengurutkan data postorder

Baris 132: menampilkan data postorder

Baris 133: Jika memilih pilihan 6

Baris 134: menampilkan Nomor Rak Terkecil

Baris 135: Jika memilih pilihan 7

Baris 136: menampilkan Nomor Rak Terbesar

Baris 137: Jika memilih pilihan 8

Baris 138: menampilkan Jumlah Rak Terdaftar

Baris 139: Jika memilih pilihan 9

Baris 140: menampilkan Total Seluruh Nomor Rak

Baris 141: Jika memilih pilihan 10

Baris 142: menampilkan Program selesai

Baris 143: jika tidak memilih pilihan menu

Baris 144: menampilkan Pilihan tidak valid!

Baris 147: Mengecek apakah file dijalankan langsung

Baris 148: Memanggil fungsi utama program

Output :

<img width="250" height="469" alt="Output 1" src="https://github.com/user-attachments/assets/e2fd6a1d-2f4c-4a1b-ba6c-d1a9cb398fce" />
<img width="272" height="469" alt="Output 2" src="https://github.com/user-attachments/assets/42254cb2-7ee6-418d-a721-8548b0b1770f" />
<img width="269" height="469" alt="Output 3" src="https://github.com/user-attachments/assets/f8322ef5-024d-44c9-afd1-2d7fef2c02c7" />
<img width="306" height="470" alt="Output 4" src="https://github.com/user-attachments/assets/6a08e5c7-3de1-474e-9fa5-3640bde64f9c" />
<img width="278" height="473" alt="Output 5" src="https://github.com/user-attachments/assets/1b38fabc-045d-4e4c-afe8-27e98131e63d" />
<img width="242" height="467" alt="Output 6" src="https://github.com/user-attachments/assets/b7a0b770-563f-4b17-b080-33c5720bd3f8" />
<img width="337" height="239" alt="Output 7" src="https://github.com/user-attachments/assets/2b284195-6e16-43e2-bd1f-b40f3f097dca" />

Penjelasan : User memlih dari 10 Pilihan menu. Pilihan 1 untuk menambahkan nomor rak, Pilihan 2 unduk mencari nomor rak, Pilihan 3 untuk menampilkan data inorder, Pilihan 4 untuk menampilkan data preorder, Pilihan 5 untuk menampilkan data postorder, Pilihan 6 untuk mencari rak sebelah kiri (Nilai terkecil), Pilihan 7 untuk mencari rak sebelah kanan (Nilai terbesar), Pilihan 8 untuk menghitung jumlah nomor rak, Pilihan 9 untuk menghitung total seluruh rak, Pilihan 10 untuk menghentikan program.

Link Dokumentasi : https://www.youtube.com/watch?v=SP94Ig8mxrc
