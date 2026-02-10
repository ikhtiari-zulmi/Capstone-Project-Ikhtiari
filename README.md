# Short Project Overview
This Store Management System is a Python-based application developed as a Capstone Project for the Business Data Analyst Program at Purwadhika. The application implements fundamental CRUD (Create, Read, Update, Delete) concepts to manage store product data through a Command Line Interface (CLI).

All data is stored in a hardcoded format within the program without using a database, making the application intended for learning and simulation purposes rather than production use. The system includes features for product data management, searching and filtering, as well as a Recycle Bin mechanism to safely handle data deletion. All data will reset to its initial state each time the program is restarted.

notes: This app runs using Bahasa Indonesia as Interface language.

# Introduction to the App

== SISTEM PENJUALAN TOKO ==

Aplikasi ini digunakan untuk mengelola data barang toko. 
Fitur yang tersedia dalam aplikasi ini meliputi:
- Menampilkan seluruh data barang
- Memfilter data barang berdasarkan kategori
- Mencari data barang berdasarkan kode atau nama
- Menambahkan data barang baru
- Mengubah data barang yang sudah ada
- Menghapus data barang dengan mekanisme Recycle Bin
- Mengembalikan atau menghapus permanen data dari Recycle Bin

<img width="665" height="245" alt="image" src="https://github.com/user-attachments/assets/4f94218e-3582-41ec-a504-e17285aac6cb" />


## Features

1. Show Daftar Barang
   
<img width="784" height="806" alt="image" src="https://github.com/user-attachments/assets/df48a8b1-884c-4fb8-ac19-26d49aad1360" />

Pada menu ini, user dapat melihat seluruh daftar barang yang tersedia di toko.
Informasi yang ditampilkan meliputi ID Barang, Nama Barang, Kategori, Harga, dan Stok.
Selain menampilkan seluruh data, menu ini juga dilengkapi dengan opsi:
- Memfilter barang berdasarkan kategori
- Mencari barang berdasarkan kode atau nama

<img width="677" height="601" alt="image" src="https://github.com/user-attachments/assets/9930c798-7fe9-494a-ab9f-352bd87890f7" />

Jika user memilih untuk memfilter data berdasarkan kategori, sistem akan menampilkan daftar kategori yang tersedia. Setelah kategori dipilih, data barang dari kategori tersebut akan ditampilkan, disertai opsi untuk melakukan filter kategori lain.

Selain itu, tersedia fitur pencarian barang berdasarkan kode ID atau nama barang. Pencarian bersifat fleksibel, sehingga user tidak perlu memasukkan kata atau kode secara penuh—cukup sebagian karakter yang sesuai.

<img width="695" height="821" alt="image" src="https://github.com/user-attachments/assets/06ab5ef8-26c9-4115-a3fc-5abc02b66b6e" />

Jika user tidak ingin melakukan filter maupun pencarian, sistem akan kembali ke menu utama.

2. Input Barang

Pada menu input barang, sistem akan menampilkan tabel daftar barang yang sudah ada untuk memudahkan user dalam melihat data sebelumnya.
User kemudian diminta memilih kategori barang berdasarkan nomor yang tersedia.

<img width="504" height="285" alt="image" src="https://github.com/user-attachments/assets/c32e4f5f-47f2-4bcb-90d2-2783f6b69086" />

Setelah kategori dipilih, user dapat langsung memasukkan data barang lainnya seperti nama barang, harga, dan stok.
Data barang yang berhasil ditambahkan akan langsung ditampilkan pada tabel, disertai notifikasi bahwa data berhasil ditambahkan serta konfirmasi apakah user ingin menambahkan barang lagi atau tidak.

<img width="729" height="793" alt="image" src="https://github.com/user-attachments/assets/a532f9b7-0f4c-4c89-b1ce-14b8f2e71573" />

3. Update Barang

Pada menu update barang, sistem akan menampilkan tabel data barang terlebih dahulu.
User diminta memasukkan ID barang yang ingin diubah. ID digunakan sebagai acuan karena bersifat unik dan mewakili satu data barang, sehingga dapat meminimalkan kesalahan saat proses update.

<img width="771" height="395" alt="image" src="https://github.com/user-attachments/assets/2bfddf71-a349-4ee2-be7e-698a77c55029" />

User dapat memilih kolom yang ingin diubah, yaitu:
- Nama
- Harga
- Stok

Kategori tidak dapat diubah karena berkaitan langsung dengan ID barang.
Setelah nilai baru dimasukkan, data akan diperbarui dan tabel terbaru akan ditampilkan beserta notifikasi bahwa data berhasil diupdate.

<img width="785" height="820" alt="image" src="https://github.com/user-attachments/assets/7caa3ca0-fb48-454e-8290-9a119da9af03" />

4. Delete Barang
   
Menu delete barang akan menampilkan tabel daftar barang.
User diminta memasukkan ID barang yang ingin dihapus. Sistem akan menampilkan data barang tersebut untuk memastikan bahwa data yang dipilih sudah benar sebelum dihapus.

Sebagai pengembangan fitur, sistem ini dilengkapi dengan Recycle Bin, sehingga data yang dihapus tidak langsung hilang, melainkan dipindahkan ke Recycle Bin dan masih dapat dikembalikan.

<img width="800" height="310" alt="image" src="https://github.com/user-attachments/assets/544b9e4b-bee4-4e26-8abf-2cdc1dfd5689" />

Jika user mengonfirmasi penghapusan, data akan dipindahkan ke Recycle Bin dan sistem akan menampilkan notifikasi bahwa data berhasil dipindahkan.

<img width="746" height="845" alt="image" src="https://github.com/user-attachments/assets/65eefd26-1eca-43f6-b057-f9a2a0aa0e78" />

5. Recycle Bin

Menu Recycle Bin menyediakan beberapa opsi untuk mengelola data yang telah dihapus, yaitu:
- Melihat data dalam Recycle Bin
- Restore data ke tabel utama
- Menghapus data secara permanen
- Kembali ke menu utama

<img width="526" height="218" alt="image" src="https://github.com/user-attachments/assets/71ca9a4a-5c31-45e8-9908-19a5ece2d9fd" />

piihan menu 1 untuk melihat daftar barang dalam recycle bin

<img width="722" height="499" alt="image" src="https://github.com/user-attachments/assets/6a7794fc-365d-4c68-8332-366dc97b5829" />

kemudian user bisa langsung memilih menu lain dalam recycle bin lagi.
pilihan 2, restore data.
Pada menu restore, user cukup memasukkan ID barang yang ingin dikembalikan dan melakukan konfirmasi. Jika dikonfirmasi, data akan dikembalikan ke daftar barang utama.

<img width="718" height="553" alt="image" src="https://github.com/user-attachments/assets/41a7fcfd-c5db-4dc6-ad5c-db8c6e9c4d13" />

pilihan 3, hapus permanen (empty recycle bin)
Pada menu hapus permanen, seluruh data di dalam Recycle Bin akan dihapus secara permanen setelah user melakukan konfirmasi.

<img width="679" height="294" alt="image" src="https://github.com/user-attachments/assets/98519e3d-9b85-4478-b152-8122b3c516eb" />

jika user memilih ya, maka akan muncul notif recycle bin berhasil dikosongkan. user bisa langsung memilih pilihan 4 untuk kembali ke menu utama.

6. Exit

Menu Exit digunakan untuk mengakhiri penggunaan aplikasi.
Saat user memilih menu ini, aplikasi akan berhenti dan menampilkan pesan “Terimakasih!”.

<img width="556" height="262" alt="image" src="https://github.com/user-attachments/assets/d4218282-314d-4434-a518-3135e4a90a91" />
