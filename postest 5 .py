#Menu
menu = {
    'Ayam Bakar'    : 25000, 
    'Ayam Geprek'   : 20000, 
    'Ayam Goreng'   : 10000, 
    'Ayam Guling'   : 30000, 
    "Ayam Bantal"   : 32000, 
    "Ayam selimut"  : 40000, 
    "Ayam Bacem"    : 50000, 
    "Ayam Batutu"   : 80000 
}

def list_menu():
    menu
    for key, value in menu.items():
        print(key, ':', value)

def tambah():
    input_baru = input('masukan menu: ')
    in_baru = int(input('masukan harga: '))
    menu[input_baru] = in_baru

def update():
    input_baru = input('Update menu: ')
    in_baru = int(input('Update harga: '))
    menu[input_baru] = in_baru

def delete():
    del menu [input('menu yang ingin dihapus: ')]

#CRUD
def main_menu():
    while True:
        print('menu')
        print('1. List menu\n2. Tambahkan\n3. Update\n4. Hapus\n5. Exit')
        choice = input('Masukan pilihan: ')
        if choice == '1':
            list_menu()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif choice == '2':
            tambah()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif choice == '3':
            update()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif choice == '4':
            delete()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif choice == '5':
            print('Anda telah keluar')
            break

def kasir():
    menu
    for key, value in menu.items ():
        print (key,":", value)
    pilih = menu [input("masukkan menu yang anda inginkan: ")]
    Jumlah = int(input("masukan jumlah menu yang dibeli: "))
    Total = pilih*Jumlah 
    Hari = input('masukan hari pembelian: ')
    if Hari == 'senin':
          diskon = 0.1*Total
          print('-Diskon 10 %-')

    elif Hari == 'jumat':
          diskon = 0.25*Total
          print('-Diskon 25 %-')

    else:
          diskon = 0
          print('maaf,tidak dapat diskon')

    totalbayar=int(Total-diskon)

    uang = int(input("Uang Tunai Pembeli: Rp"))
    kembalian = int(uang - totalbayar)
    print(f"Kembalian: Rp{kembalian}")

    print(f"""
    --------------------------------------------------
    ----------------- S T R U K   B E L I ------------
    --------------------------------------------------
    Beli          :  {pilih} porsi {Jumlah}
    Total         : Rp{Total}
    Diskon        : - Rp{diskon}
    Total Tagihan : Rp{totalbayar}
    Uang          : Rp{uang}
    Kembalian     : Rp{kembalian}
    --------------------------------------------------
        Terima Kasih Telah Makan DI RM BEBEK LEPAS
    --------------------------------------------------
    """)
while True : 
    print('selamat datang')
    print('1. database')
    print('2. kasir')
    x = input('masukkan pilihan: ')
    if   x == "1" :
        main_menu ()
    elif x == "2" :
        kasir()