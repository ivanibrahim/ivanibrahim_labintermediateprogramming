var1 = "Apel"
var2 = "Jeruk"
print("Sebelum ditukar:")
print("var1 =", var1)
print("var2 =", var2)
# Menukar nilai var1 dan var2  
var1, var2 = var2, var1
print("Setelah ditukar:")
print("var1 =", var1)
print("var2 =", var2)

tebak_aku = str(input("Tebak huruf apa yang aku pikirkan :").lower())
pilihan = ["a", "b", "c", "d"]
if tebak_aku in pilihan:
    print("Tebakanmu benar!")
else:
    print("Tebakanmu salah!")

#() ini adalah tuple, fungsinya untuk menyimpan beberapa item dalam satu variabel dan tidak dapat diubah elemen-elemennya
# [] ini adalah list, fungsinya untuk mengakses atau mengubah elemen dalam list
ini_list = [10, 20, 30, 40, 50]
ini_list[0] = 0
print(ini_list)

#Tugas 7 Januari 2026
#1. Create a secret word
#2. Ask user to give a letter
