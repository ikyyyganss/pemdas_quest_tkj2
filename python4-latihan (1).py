print("halo semuanya")
print("perkenalkan")
nama_depan =input("nama depan saya")
nama_belakang =input("nama belakang saya")
nama_lengkap_saya_adalah =input("nama lengkap saya adalah")

a = int(input("masukan nilai A: "))
b = float(input("masukan nilai B: "))
c = a + b

print("A =", a)
print("B =", b)
print(a,"+",b,"=", c)

x = int(input("masukan suhu celcius"))
y = (9/5 * x) + 32
print(x, "celcius = ", y, "fahreheit")

print("===================")
print("Rumus Bangun Datar")
print("====================\n")

print("1. Persegi\n")

alas = int(input("Masukan nilai alas: "))
tinggi = int(input("Masukan nilai tinggi: "))
luas_s = alas * tinggi / 2 # or 1/2 * alas * tinggi
print("luas segitiga adalah: ", luas_s)