tahun = int(input("Masukkan tahun: "))

if tahun%400 == 0 | tahun%100 == 0 | tahun%4 == 0:
  print("%i merupakan tahun kabisat" % (tahun))
else:
  print("%i merupakan bukan tahun kabisat" % (tahun))
