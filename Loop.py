#Looping
#While
angka = 1;
while(angka <= 10): #lopping dari angka sampai kurang dari 10
    print(angka);
    angka += 1; #setiap step ditambah 1

#For
for i in range(1,6): #Perulangan antara 1 sampai kurang dari 6
    print("Perulangan ke- ", i)
    
#For Loop and List
listItem = list(range(1,11,2)); #looping list, mulai dari 1 sampai kurang dr 11, setiap angka +2
print(listItem);

for i in range(1,11,2): #urutan kebawah
    print(i);
    


#Latihan No 1
n = int(input("Masukan Range: "))
for i in range (n,0,-1):
    z=''
    z+=i*'*'
    print(z)


#Coba no 1
for i in range (5, 0, -1):
     z=''
     z+=i*'*'
     print(z)
for j in range(1, 6, +1):
      x=''
      x=j*'*'
      print(x)
       

















