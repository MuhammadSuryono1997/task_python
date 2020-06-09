numbers = [11,2,5,23,15,8,7,6,19,21,18]

nilai_terkecil = numbers[0]
nilai_terbesar = numbers[0]
for nilai in numbers:
  
  #nilai terbesar
  if nilai_terbesar < nilai:
    nilai_terbesar = nilai
    print("Nilai terbesar adalah %i" % (nilai_terbesar))
  
  #nilai terkecil
  if nilai_terkecil > nilai:
    nilai_terkecil = nilai
    print("Nilai terkecil adalah %i" % (nilai_terkecil))

