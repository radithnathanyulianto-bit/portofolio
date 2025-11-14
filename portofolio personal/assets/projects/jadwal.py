# Dictionary berisi jadwal tiap hari
import datetime as dt
jadwal = {
    "Monday": ["DDPK PPLG ", "Istirahat", 
    "Sejarah", "Istirahat2", "IPAS", "Matematika"],
    "Tuesday": ["Informatika", "Baca Tulis Qur'an", "Bahasa Indonesia", "Seni Budaya", "Bahasa Arab"],
    "Wednesday": ["HW", "Pendidikan Pancasila", "Bahasa Inggris", "Bahasa Indonesia", "Pendidikan Agama Islam dan Budi Pekerti"],
    "Thursday": ["TPS", "Bahasa Sunda", "PJOK", "DDPK PPLG", "IPAS"],
    "Friday": ["Bimbingan Konseling/BK", "DDPK PPLG", "Kemuhammadiyahan"],
}
hari_ini = dt.date.today()
print(hari_ini)
hari = (f"{hari_ini:%A}")
if hari == "Monday" :
        print("Senin")
elif hari == "Tuesday" :
        print("Selasa")
elif hari == "Wednesday" :
        print("Rabu")
elif hari == "Thursday" :
        print("Kamis")
elif hari == "Friday" :
        print("Jumat")
# Cek dan tampilkan jadwal
if hari in jadwal:
    for i, pelajaran in enumerate(jadwal[hari], start=1):
        print(f"{i}. {pelajaran}")