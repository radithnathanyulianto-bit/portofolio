#Menggambar ketupat menggunakan python

sisi = int(input("Masukan angka : "))

count = 1
spasi = int(sisi/2)
count1 = count*sisi
spasi1 = 1
gambar = "$"

while True:
        if count < sisi :
                if count%2 :
                        print(" "*spasi, gambar*count)
                        count += 1
                        spasi -= 1
                else :
                        count += 1
        elif count1%2:
                print(" "*spasi1, gambar*count1)
                count1 -= 1
                spasi1 += 1
        else :
                count1 -= 1
        if count1 < 1 :
                break

print("hasil akhir")