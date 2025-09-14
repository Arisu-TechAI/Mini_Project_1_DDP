## Mini Project 1 Dasar-Dasar Pemrograman ##
## Aplikasi Forum diskusi komunitas player Visual Novel ##


# Header
print("=" *25, "Selamat datang di Komunitas Player Visual Novel", "=" *25 )

#List topik diskusi
topik_diskusi = []

#Buat data pengguna
def buat_user():
    print("\nSilakan masukkan data pengguna terlebih dahulu")
    username = input("Masukkan username: ")
    user_data = (username,)
    print(f"\nSelamat datang, {user_data[0]}!\n")
    return user_data

user_aktif = buat_user()

    ### mendefinisikan tampilan dari setiap pilihan menu ###
# program/function untuk tampilan menu : 1. Lihat semua topik
def lihat_semua_topik():
    if not topik_diskusi:
        print("\nBelumm ada topik yang diunggah pengguna\n")
        return
    print("\n Daftar Topik Komunitas :")
    for i, topik in enumerate(topik_diskusi):
        print(f"{i + 1}. {topik['judul']}")

# program/function untuk tampilan menu : 2. Buat Topik Diskusi
def buat_topik_diskusi():
    judul = input("\nJudul Topik: ")
    isi = input("Apa yang anda pikirkan? ")
    topik = {
        "judul": judul,
        "isi": isi,
        "komentar": []
    }
    topik_diskusi.append(topik)
    print("Topik diskusi berhasil ditambahkan!\n")

# program/function untuk tampilan menu : 3. Buka Topik Diskusi (Lihat & Komentar)
# buka komentar #
def buka_komentar (list_komentar):
    if not list_komentar:
        print(" Belum ada komentar. ")
    else:
        for i, komentar in enumerate(list_komentar):
            print(f" {i + 1}. {komentar}")

# lihat postingan topik diskusi
def buka_topik():
    lihat_semua_topik()
    if not topik_diskusi:
        return
    try:
        index = int(input("\nPilih nomor topik: ")) - 1
        if index < 0 or index >= len(topik_diskusi):
            print("Topik tidak ditemukan.")
            return
        topik = topik_diskusi[index]
        while True:
            print(f"\n--- {topik['judul']} ---")
            print(f"Isi: {topik['isi']}")
            print("Komentar: \n")
            buka_komentar(topik["komentar"])

            print("\nAksi:")
            print("1. Tambah Komentar")
            print("2. Edit Komentar (Coming Soon)")
            print("3. Hapus Komentar (Coming Soon)")
            print("4. Kembali ke Menu Utama")
            aksi = input("Pilih Tindakan (1-4): \n")

            if aksi == "1":
                komentar = input("Komentar Anda: ")
                topik["komentar"].append(komentar)
                print("Komentar ditambahkan!")
            elif aksi == "2":
                print("Pilihan Menu Belum Tersedia! \n")
                return
            elif aksi == "3":
                print("Pilihan Menu Belum Tersedia! \n")
                return
            elif aksi == "4":
                break
            else:
                print("Pilihan tidak valid.")
    except ValueError:
        print("Input tidak valid.")

#tampilan halaman menu
def tampilkan_menu () :
        print("=" *25, "Silahkan Pilih Menu (1-4)", "=" *25)
        print("1. Lihat Daftar Semua Topik")
        print("2. Buat Topik Diskusi")
        print("3. Buka Postingan Diskusi (Lihat & Komentar)")
        print("4. Keluar") 
        
while True: 
    tampilkan_menu()
    pilihan = input("\nPilih menu: ") 

#function unutk pilihan menu
    if pilihan == "1":
            lihat_semua_topik()
    elif pilihan == "2":
            buat_topik_diskusi()
    elif pilihan == "3":
            buka_topik()
    elif pilihan == "4":
            print(" ")
            print("=" *25, "Sampai Jumpa!", "=" *25, "\n")
            break
    else: 
            print("Pilihan tidak valid. ")











