# Program menghitung substr pada inputan string

#string = input digunakan untuk melakukan sebuah inputan yg dilakukan oleh user
#tipe data yang digunakan yaitu tipe data string
string = input ("masukkan sebuah string : ")

#pendeklarasian variabel serta method 
# method yang digunakan yaitu Metode count() dimana method ini akan
# menghitung berapa kali substr muncul di dalam string str
a = string.count('a') #sebagai contoh, disini variabel a memanggil string dengan menggunakan method count() untuk menghitung berapa kali huruf vokal a yang muncul
b = string.count('i')
c = string.count('u')
d = string.count('e')
e = string.count('o')
f = string.count('a', 0 and 4) #disini, angka 1,4 adalah index, dimana method count() akan menghitung huruf a yang muncul di index ke 1-4

#output program
print("Huruf 'a' dalam string : ", a)
print("Huruf 'i' dalam string : ", b)
print("Huruf 'u' dalam string : ", c)
print("Huruf 'e' dalam string : ", d)
print("Huruf 'o' dalam string : ", e)
print("Huruf 'a' dari index 1-4 : ", f)