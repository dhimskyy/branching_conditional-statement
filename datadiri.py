print("=====INPUT DATA DIRI=====")
nama = input("Masukkan nama anda: ")
jk = input("Masukkan jenis kelamin anda(L/P): ")
agama = int(input("Masukkan agama anda: "))
if (agama == 1):
    agama = "Islam"
elif (agama == 2):
    agama = "Protestan"
elif (agama == 3):
    agama = "Katolik"
elif (agama == 4):
    agama = "Hindu"
elif (agama == 5):
    agama = "Budha"
else:
    agama = "Agama tidak diketahui"

print("=====OUTPUT DATA DIRI=====")
print("Nama: ", nama)
print("Jenis Kelamin: ", jk)
print("Agama: ", agama)
    
    