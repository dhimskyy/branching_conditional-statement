gender = input("Perempuan/Laki-laki? (L/P): ")
if (gender == 'L'):
    status = input("Anda sudah menikah atau belum?(Y/N): ")
    if (status == 'Y'):
        print("Hallo bapak!")
    elif (status == 'N'):
        print("Hallo mas!")
    else:
        print("Tidak diketahui")
elif (gender == 'P'):
    status = input("Anda sudah menikah atau belum?(Y/N): ")
    if (status == 'Y'):
        print("Hallo ibu!")
    elif (status == 'N'):
        print("Hallo mbak!")
    else:
        print("Tidak diketahui")
else:
    print("Tidak ada dalam pilihan")