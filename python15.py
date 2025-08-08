#kondisi if else adalah jika kondisi bernilai TRUE maka akan di eksekusi gaada if,


nilai = int(input("Masukan Nilai : "))
# Jika pernyataan pada if bernilai TRUE maka if akan dieksekusi,
#tetapi jika FALSE kode pada else yang akan dieksekusi

if(nilai > 85):
    print("A")
elif(nilai > 79):
    print("B")
elif(nilai > 74):
    print("C")
elif(nilai > 69):
    print("D")
elif(nilai < 70):
    print("E")
else:
    print("Max 100")