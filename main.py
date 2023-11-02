import time, os


def clear():
    os.system('cls' or 'clear')


def main():
    clear()
    suhu = float(input("Masukkan Suhu (°C) : "))

    # Pilihan Konversi Suhu
    clear()
    print("Pilih satuan suhu konversi:")
    print("1. Reamur")
    print("2. Fahrenheit")
    print("3. Kelvin")
    pilihan_konversi = int(input("Masukkan nomor pilihan: "))

    # Konversi Suhu
    if pilihan_konversi == 1:
        clear()
        hasil = suhu * 4/5
        print("-"*30)
        print(f"Hasil Konversi : {hasil}°R")
        print("-"*30)
        pilihan = input("Ingin mengkonversi lagi? (y/n) ")
        if pilihan == 'y':
            main()
        elif pilihan == 'n':
            exit()

    elif pilihan_konversi == 2:
        clear()
        hasil = (suhu * 9/5) + 32
        print("-"*30)
        print(f"Hasil Konversi : {hasil}°F")
        print("-"*30)
        pilihan = input("Ingin mengkonversi lagi? (y/n) ")
        if pilihan == 'y':
            main()
        elif pilihan == 'n':
            exit()

    elif pilihan_konversi == 3:
        clear()
        hasil = suhu + 273
        print("-"*30)
        print(f"Hasil Konversi : {hasil}°K")
        print("-"*30)
        pilihan = input("Ingin mengkonversi lagi? (y/n) ")
        if pilihan == 'y':
            main()
        elif pilihan == 'n':
            exit()

    else:
        clear()
        print("Pilhan anda tidak valid!")
        time.sleep(1)
        main()

if __name__ == "__main__":
    main()
