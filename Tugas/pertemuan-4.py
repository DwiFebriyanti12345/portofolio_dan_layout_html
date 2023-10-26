kendaraan =["b 4030 rfs","vespa","150","white"]
kendaraan.append("36 juta")
kendaraan.append("2 roda")
kendaraan.insert(2,"honda")
kendaraan.insert(3,"motor")
print(kendaraan)
 
rumus = input("masukan angka:")
match rumus:
    case "1":
        sisi = float(input("masukan panjang persegi:"))
        luas = sisi * sisi
        print("luas persegi panjang adalah" ,luas)
    case "2":
        jari = float(input("masukan jari jari:"))
        phi = 3.14
        lingkaran = phi * jari**2
        print("luas lingkaran adalah" ,lingkaran)
    case "3":
        print("luas segitiga adalah:",segitiga)
        alas = float(input("masukan alas :"))
        tinggi = float(input("masukan tinggi :"))
        segitiga = alas * tinggi /2
    case _:
        print("salah masukan pilihan") 








