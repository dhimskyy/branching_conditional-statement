suhu = int (input("Masukkan suhu: "))
if (suhu <= 0):
    print("Pada suhu", suhu, "derajat celcius, air akan berwujud es")
elif (suhu > 0 & suhu < 100):
    print("Pada suhu", suhu, "derajat celcius, air akan berwujud cair")
else:
     print("Pada suhu", suhu, "derajat celcius, air akan berwujud gas")