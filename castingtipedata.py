#belajar casting tipe data python

#integer
print("=============INTEGER================")
data_integer = 1
print("data = ", data_integer, ", bertipe data : ", type(data_integer))  # mencetak variabel dan tipe datanya

data_float = float(data_integer)  # mengubah tipe data integer menjadi float
data_str = str(data_integer)  # mengubah tipe data integer menjadi string
data_bool = bool(data_integer)  # mengubah tipe data integer menjadi boolean
print("data = ", data_float, ", bertipe data : ", type(data_float))
print("data = ", data_str, ", bertipe data : ", type(data_str))
print("data = ", data_bool, ", bertipe data : ", type(data_bool))

#float
print("=============FLOAT================")
data_float = 9.7
print("data = ", data_float, ", bertipe data : ", type(data_float))  # mencetak variabel dan tipe datanya

data_int = int(data_float)  
data_str = str(data_float)  
data_bool = bool(data_float)  
print("data = ", data_int, ", bertipe data : ", type(data_int))
print("data = ", data_str, ", bertipe data : ", type(data_str))
print("data = ", data_bool, ", bertipe data : ", type(data_bool))

#boolean
print("=============BOOLEAN================")
data_boolean = False
print("data = ", data_boolean, ", bertipe data : ", type(data_boolean))  # mencetak variabel dan tipe datanya

data_int = int(data_boolean)  
data_str = str(data_boolean)  
data_float = bool(data_boolean)  
print("data = ", data_int, ", bertipe data : ", type(data_int))
print("data = ", data_str, ", bertipe data : ", type(data_str))
print("data = ", data_float, ", bertipe data : ", type(data_float))

#string
print("=============STRING===================")
data_str = False
print("data = ", data_boolean, ", bertipe data : ", type(data_str))  # mencetak variabel dan tipe datanya

data_int = int(data_str)  
data_float = bool(data_str)  
data_boolean = str(data_str)  
print("data = ", data_int, ", bertipe data : ", type(data_int))
print("data = ", data_float, ", bertipe data : ", type(data_float))
print("data = ", data_boolean, ", bertipe data : ", type(data_boolean))