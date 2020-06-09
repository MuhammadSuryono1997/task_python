for nilai in range(100,201):
  if nilai > 1:
    for i in range(2, nilai):
      if nilai % i == 0:
        break
    else:
      print(nilai)
      
