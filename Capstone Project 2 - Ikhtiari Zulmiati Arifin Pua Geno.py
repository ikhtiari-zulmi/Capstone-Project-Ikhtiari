from prettytable import PrettyTable

#===========================
# List Data Barang Toko
#===========================

Toko = [
    # === MAKANAN ===
    ["MKN01", "Mie Instan", "Makanan", 3000, 50],
    ["MKN02", "Biskuit Coklat", "Makanan", 8000, 30],
    ["MKN03", "Roti Tawar", "Makanan", 15000, 20],
    ["MKN04", "Snack Kentang", "Makanan", 10000, 25],

    # === MINUMAN ===
    ["MNM01", "Air Mineral", "Minuman", 5000, 100],
    ["MNM02", "Teh Botol", "Minuman", 7000, 60],
    ["MNM03", "Kopi Kaleng", "Minuman", 12000, 40],
    ["MNM04", "Susu UHT", "Minuman", 9000, 35],

    # === KEBERSIHAN ===
    ["KBR01", "Sabun Mandi", "Kebersihan", 6000, 45],
    ["KBR02", "Shampo", "Kebersihan", 18000, 25],
    ["KBR03", "Pasta Gigi", "Kebersihan", 12000, 30],
    ["KBR04", "Deterjen", "Kebersihan", 20000, 20],

    # === KEBUTUHAN RUMAH ===
    ["RMT01", "Tisu Gulung", "Kebutuhan Rumah", 15000, 40],
    ["RMT02", "Minyak Goreng", "Kebutuhan Rumah", 28000, 25],
    ["RMT03", "Gula Pasir", "Kebutuhan Rumah", 16000, 30],
    ["RMT04", "Beras 5kg", "Kebutuhan Rumah", 65000, 15],

    # === ATK ===
    ["ATK01", "Pulpen", "ATK", 3000, 100],
    ["ATK02", "Buku Tulis", "ATK", 7000, 60],
    ["ATK03", "Pensil", "ATK", 2500, 80],
    ["ATK04", "Penghapus", "ATK", 2000, 70],
]

RecycleBin = []

# ====================
# Function show table (PrettyTable)
# ====================
def show_table(Toko):
    print('\nToko Kelontong')
    table = PrettyTable()
    table.field_names = ["No", "ID", "Nama Barang", "Kategori", "Harga", "Stok"]

    for no, brg in enumerate(Toko, start=1):
        table.add_row([no, brg[0], brg[1], brg[2], brg[3], brg[4]])

    print(table)
    print()

# Function cari barang berdasarkan kode
def cari_index_barang(data, kode):
    for i in range(len(data)):
        if data[i][0] == kode:
            return i
    return -1


#===========================
# Menu > Harus looping terus sampai user pilih menu Exit.
#===========================

while True:
    print("""
          === SISTEM PENJUALAN TOKO ===
          1. Show Daftar Barang
          2. Input Barang
          3. Update Barang
          4. Delete Barang
          5. Recycle Bin
          6. Exit
          """)
    
    menu = int(input("Pilih Menu: "))

    #================================
    # MENU 1 = Show Daftar Barang
    #================================
    if menu == 1:
        # tampilkan semua data dulu
        show_table(Toko)

        # pilihan jika ingin filter
        filter_kat = input("\nIngin filter barang berdasarkan kategori? (y/n): ").lower()
        while filter_kat == "y":
            print("\nPilih kategori:")
            print("1. Makanan")
            print("2. Minuman")
            print("3. Kebersihan")
            print("4. Kebutuhan Rumah")
            print("5. ATK")

            pilih_kat = input("\nMasukkan nomor kategori: ")

            if pilih_kat == "1":
                kategori = "Makanan"
            elif pilih_kat == "2":
                kategori = "Minuman"
            elif pilih_kat == "3":
                kategori = "Kebersihan"
            elif pilih_kat == "4":
                kategori = "Kebutuhan Rumah"
            elif pilih_kat == "5":
                kategori = "ATK"
            else:
                print("❌ Kategori tidak valid.")
                continue

            data_filter = []
            for barang in Toko:
                if barang[2] == kategori:
                    data_filter.append(barang)

            if len(data_filter) == 0:
                print("\nTidak ada data untuk kategori ini.")
            else:
                show_table(data_filter)

            # tanya lagi, mau filter lagi atau tidak
            filter_kat = input("\nIngin filter kategori lain? (y/n): ").lower()

        # Pilihan untuk cari barang
        cari = input("\nIngin cari barang berdasarkan kode atau nama? (y/n): ").lower()
        while cari == "y":
            while True:
                keyword = input("\nMasukkan kode atau nama barang: ").lower()

                hasil_cari = []
                for barang in Toko:
                    if keyword in barang[0].lower() or keyword in barang[1].lower():
                        hasil_cari.append(barang)

                if len(hasil_cari) == 0:
                    print("\n❌ Barang tidak ditemukan.")
                else:
                    print("\n🔍 Hasil Pencarian:")
                    show_table(hasil_cari)
                    break

            cari = input("\nIngin cari barang lagi? (y/n): ").lower()

    #================================
    # MENU 2 = Input barang
    #================================
    elif menu == 2 :
        show_table(Toko)

        print("\nPilih nomor kategori barang:")
        print("1. Makanan")
        print("2. Minuman")
        print("3. Kebersihan")
        print("4. Kebutuhan Rumah")
        print("5. ATK")

        pilih = input('Masukkan nomor kategori barang: ')

        # tentukan prefix kode berdasarkan kategori yg dipilih
        if pilih == "1":
            kategori = "Makanan"
            prefix = "MKN"
        elif pilih == "2":
            kategori = "Minuman"
            prefix = "MNM"
        elif pilih == "3":
            kategori = "Kebersihan"
            prefix = "KBR"
        elif pilih == "4":
            kategori = "Kebutuhan Rumah"
            prefix = "RMT"
        elif pilih == "5":
            kategori = "ATK"
            prefix = "ATK"
        else:
            print("❌ Pilihan kategori tidak valid")
            continue
        
        # loop input barang di kategori yang sama
        while True:
            nama = input('Masukkan nama barang: ')
            harga = int(input('Masukkan harga barang: '))
            stok = int(input('Masukkan stok barang: '))

            # Penomoran ID -> Cari nomor TERBESAR yang sudah ada di kategori itu, lalu +1
            nomor = 0
            for barang in Toko:
                if barang[2] == kategori:
                    angka = int(barang[0][3:])
                    if angka > nomor:
                        nomor = angka
            kode = f"{prefix}{nomor+1:02}"

            # insert data tepat dibawah kategori yang sama
            ## cari index terakhir kategori yang sama
            posisi = -1
            for i in range(len(Toko)):
                if Toko[i][2] == kategori:
                    posisi = i

            ## kalau kategori sudah ada, insert di bawahnya
            if posisi != -1:
                Toko.insert(posisi + 1, [kode, nama, kategori, harga, stok])
            else:
                Toko.append([kode, nama, kategori, harga, stok])


            show_table(Toko)
            print('\n ✅ Data barang berhasil ditambahkan!')

            lanjut = input("Tambah barang di kategori ini lagi? (y/n): ").lower()
            if lanjut != "y":
                break
            

    #================================
    # MENU 3 = Update barang
    #================================
    elif menu == 3:
        while True:
            show_table(Toko)

            # cari barang berdasarkan ID
            while True:
                kode_cari = input("\n Masukkan ID barang yang ingin diubah: ").upper()

                idx_barang = cari_index_barang(Toko, kode_cari)

                if idx_barang == -1:    #cek apakah ID ditemukan, kalo masih -1 berarti tidak ditemukan dan update dibatalkan
                    print("❌ ID barang tidak ditemukan, coba lagi!")
                else:
                    break

            # pilih kolom yang mau di update
            while True:
                print("\nPilih yang ingin diubah:")
                print("1. Nama")
                print("3. Harga")
                print("4. Stok")

                idx_data = (input("\nMasukkan index kolom: "))

                if not idx_data.isdigit():
                    print("❌ Input harus berupa angka.")
                    continue

                idx_data = int(idx_data)

                if idx_data in [1, 3, 4]:
                    break
                else:
                    print("❌ Index tidak valid. Coba lagi.")

            # input nilai baru 
            while True:
                nilai_baru = input("Masukkan nilai baru: ").strip()

                if idx_data in [3, 4]:
                    if not nilai_baru.isdigit():
                        print("❌ Nilai harus berupa angka.")
                        continue
                    nilai_baru = int(nilai_baru)
                break    

            Toko[idx_barang][idx_data] = nilai_baru #data ke update

            show_table(Toko)
            print("\n✅ Data berhasil diupdate!")

            lanjut = input("\nIngin update data lagi? (y/n): ").lower()
            if lanjut != "y":
                break

    #================================
    # MENU 4 = Delete barang (Recycle Bin)
    #================================
    elif menu == 4:
        
            show_table(Toko)

            # cari barang berdasarkan ID
            while True:
                kode_hapus = input("\nMasukkan ID barang yang ingin dihapus: ").upper()

                idx_barang = cari_index_barang(Toko, kode_hapus)

                if idx_barang == -1:
                    print("❌ ID barang tidak ditemukan.")
                else:
                    print("\nData yang akan dipindahkan ke Recycle Bin:")
                    print(Toko[idx_barang])

                    konfirmasi = input("\nYakin ingin menghapus data ini? (y/n): ").lower()
                    if konfirmasi == "y":
                        RecycleBin.append(Toko[idx_barang])
                        del Toko[idx_barang]
                        print("\n✅ Data dipindahkan ke Recycle Bin.")
                    else:
                        print("\n❌ Penghapusan dibatalkan.")
                
                show_table(Toko)

                lanjut = input("\nIngin hapus data lagi? (y/n): ").lower()
                if lanjut != "y":
                    break

    #================================
    # MENU 5 = Recycle Bin
    #================================
    elif menu == 5:
        while True:
            print("\n=== RECYCLE BIN MENU ===")
            print("1. Lihat Recycle Bin")
            print("2. Restore Data")
            print("3. Hapus Permanen (Empty Recycle Bin)")
            print("4. Kembali ke Menu Utama\n")

            pilih_rb = input("Pilih menu: ")

            # Lihat Recycle Bin
            if pilih_rb == "1":
                if len(RecycleBin) == 0:
                    print("\nRecycle Bin kosong.")
                else:
                    show_table(RecycleBin)

            # Restore Data
            elif pilih_rb == "2":
                while True:
                    if len(RecycleBin) == 0:
                        print("\nRecycle Bin kosong.")
                        break
                    
                    show_table(RecycleBin)
                    kode_restore = input("\nMasukkan ID barang yang ingin direstore: ").upper()

                    idx_rb = cari_index_barang(RecycleBin, kode_restore)

                    if idx_rb == -1:
                        print("❌ ID tidak ditemukan di Recycle Bin, coba lagi!")
                        continue
                    else:
                        konfirmasi = input("Yakin ingin restore data ini? (y/n): ").lower()
                        if konfirmasi == "y":
                            Toko.append(RecycleBin[idx_rb])
                            del RecycleBin[idx_rb]
                            print("✅ Data berhasil direstore.")
                        else:
                            print("❌ Restore dibatalkan.")
                        break

            # Empty Recycle Bin
            elif pilih_rb == "3":
                if len(RecycleBin) == 0:
                    print("\nRecycle Bin sudah kosong.")
                else:
                    konfirmasi = input(
                        "Yakin ingin menghapus SEMUA data di Recycle Bin? (y/n): ").lower()
                    if konfirmasi == "y":
                        RecycleBin.clear()
                        print("✅ Recycle Bin berhasil dikosongkan.")
                    else:
                        print("❌ Dibatalkan.")

            # Keluar submenu
            elif pilih_rb == "4":
                break

            else:
                print("❌ Pilihan tidak valid.")
                

    #================================
    # MENU 6 = keluar 
    #================================
    elif menu == 6 :
        print('Terimakasih!')
        break

    else :
        print('Pilih menu 1-4!') 