#belajar variable python

#tipe data string
#string adalah tipe data yang digunakan untuk menyimpan teks
iniVariable = "Rasya Wiryawan"
print(type(iniVariable))  # mencetak tipe data dari variabel iniVariable
print(iniVariable, ", bertipe data : ", type(iniVariable))  # mencetak variabel dan tipe datanya

#tipe data integer
#integer adalah tipe data yang digunakan untuk menyimpan bilangan bulat
iniVariable = 14.5566
print(type(iniVariable))  # mencetak tipe data dari variabel iniVariable
print(iniVariable, ", bertipe data : ", type(iniVariable))  # mencetak variabel dan tipe datanya

#tipe data float
#float adalah tipe data yang digunakan untuk menyimpan bilangan desimal
iniVariable = 14
print(type(iniVariable))  # mencetak tipe data dari variabel iniVariable
print(iniVariable, ", bertipe data : ", type(iniVariable))  # mencetak variabel dan tipe datanya

#tipe data boolean
#boolean adalah tipe data yang hanya memiliki dua nilai, yaitu True dan False
iniVariable = True
print(type(iniVariable))  # mencetak tipe data dari variabel iniVariable    
print(iniVariable, ", bertipe data : ", type(iniVariable))  # mencetak variabel dan tipe datanya

#tipe data kompleks
#kompleks adalah tipe data yang digunakan untuk menyimpan bilangan kompleks
iniVariable = 3 + 4j
print(type(iniVariable))  # mencetak tipe data dari variabel iniVariable    
print(iniVariable, ", bertipe data : ", type(iniVariable))  # mencetak variabel dan tipe datanya

#tipe data dari C

from ctypes import c_double

data_c_double = c_double(14.5566)
print(type(data_c_double))  # mencetak tipe data dari variabel data_c_double
print(data_c_double.value, ", bertipe data : ", type(data_c_double))  
