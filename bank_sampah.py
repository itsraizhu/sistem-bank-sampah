data_setoran = []
jumlah_data = 0

JENIS_PLASTIK = ("Plastik", 500)
JENIS_KERTAS  = ("Kertas", 300)
JENIS_LOGAM   = ("Logam", 1000)
JENIS_KACA    = ("Kaca", 400)

while True:
    print("PROGRAM BANK SAMPAH")
    print("1. Tambah Setoran Sampah")
    print("2. Lihat Data Setoran")
    print("3. Ubah Data Setoran")
    print("4. Hapus Data Setoran")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        print("Tambah Setoran Sampah")
        nama = input("Masukkan nama: ")
        
        while True:
            print("Pilih Jenis Sampah:")
            print("1. Plastik (500 poin/kg)")
            print("2. Kertas  (300 poin/kg)")
            print("3. Logam   (1000 poin/kg)")
            print("4. Kaca    (400 poin/kg)")
            pilih_jenis = input("Pilih jenis (1-4): ")
            
            if pilih_jenis == "1":
                jenis_nama = JENIS_PLASTIK[0]
                poin_per_kg = JENIS_PLASTIK[1]
                break
            elif pilih_jenis == "2":
                jenis_nama = JENIS_KERTAS[0]
                poin_per_kg = JENIS_KERTAS[1]
                break
            elif pilih_jenis == "3":
                jenis_nama = JENIS_LOGAM[0]
                poin_per_kg = JENIS_LOGAM[1]
                break
            elif pilih_jenis == "4":
                jenis_nama = JENIS_KACA[0]
                poin_per_kg = JENIS_KACA[1]
                break
            else:
                print("Pilihan tidak ada, pilih 1-4!")

        input_berat = input("Masukkan berat sampah (kg): ")
        berat = float(input_berat)
        
        poin_didapat = int(berat * poin_per_kg)
        
        item_setoran = [nama, jenis_nama, berat, poin_didapat]
        data_setoran.append(item_setoran)
        jumlah_data += 1

        print("Data setoran berhasil ditambahkan.")
        print("Detail:", nama, "|", jenis_nama, "|", berat, "kg |", poin_didapat, "poin")

    elif pilihan == "2":
        print("Daftar Setoran Sampah")
        if jumlah_data == 0:
            print("Belum ada data setoran.")
        else:
            total_poin_semua = 0
            total_berat_semua = 0
            print("No. | Nama | Jenis Sampah | Berat (kg) | Poin")
            
            no = 1
            for item in data_setoran:
                nama_warga = item[0]
                jenis = item[1]
                berat = item[2]
                poin = item[3]
                
                total_berat_semua = total_berat_semua + berat
                total_poin_semua = total_poin_semua + poin
                
                print(no, "|", nama_warga, "|", jenis, "|", berat, "kg |", poin, "poin")
                no += 1
                
            print("Total Berat :", total_berat_semua, "kg")
            print("Total Poin  :", total_poin_semua, "poin")

    elif pilihan == "3":
        print("Ubah Data Setoran")
        if jumlah_data == 0:
            print("Data masih kosong.")
        else:
            print("Daftar Setoran:")
            no = 1
            for item in data_setoran:
                print(no, ".", item[0], "-", item[1], "(", item[2], "kg )")
                no += 1
            
            input_no = input("Masukkan nomor data yang mau diubah: ")
            no_index = int(input_no) - 1
            
            if no_index >= 0 and no_index < jumlah_data:
                data_lama = data_setoran[no_index]
                print("Ubah data milik:", data_lama[0])
                
                nama_baru = input("Masukkan nama baru: ")
                
                print("Pilih Jenis Sampah Baru:")
                print("1. Plastik (500 poin/kg)")
                print("2. Kertas  (300 poin/kg)")
                print("3. Logam   (1000 poin/kg)")
                print("4. Kaca    (400 poin/kg)")
                pilih_j = input("Pilih jenis (1-4): ")
                
                if pilih_j == "1":
                    jenis_baru = JENIS_PLASTIK[0]
                    poin_rate = JENIS_PLASTIK[1]
                elif pilih_j == "2":
                    jenis_baru = JENIS_KERTAS[0]
                    poin_rate = JENIS_KERTAS[1]
                elif pilih_j == "3":
                    jenis_baru = JENIS_LOGAM[0]
                    poin_rate = JENIS_LOGAM[1]
                elif pilih_j == "4":
                    jenis_baru = JENIS_KACA[0]
                    poin_rate = JENIS_KACA[1]
                else:
                    jenis_baru = JENIS_PLASTIK[0]
                    poin_rate = JENIS_PLASTIK[1]

                input_b = input("Masukkan berat baru (kg): ")
                berat_baru = float(input_b)
                poin_baru = int(berat_baru * poin_rate)
                
                data_setoran[no_index] = [nama_baru, jenis_baru, berat_baru, poin_baru]
                print("Data berhasil diperbarui.")
            else:
                print("Nomor data tidak ditemukan!")

    elif pilihan == "4":
        print("Hapus Data Setoran")
        if jumlah_data == 0:
            print("Data masih kosong.")
        else:
            print("Daftar Setoran:")
            no = 1
            for item in data_setoran:
                print(no, ".", item[0], "-", item[1], "(", item[2], "kg )")
                no += 1
                
            input_no = input("Masukkan nomor data yang mau dihapus: ")
            no_index = int(input_no) - 1
            
            if no_index >= 0 and no_index < jumlah_data:
                nama_terhapus = data_setoran[no_index][0]
                del data_setoran[no_index]
                jumlah_data -= 1
                print("Data milik", nama_terhapus, "berhasil dihapus.")
            else:
                print("Nomor data tidak ditemukan!")

    elif pilihan == "5":
        print("Terima kasih!")
        break

    else:
        print("Pilihan menu tidak valid, silakan coba lagi.")
