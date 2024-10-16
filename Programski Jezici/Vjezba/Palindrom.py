def palindrom(rec):
  return rec==rec[::-1]

rec= input("Unesi rijec")

if palindrom(rec):
  print("Jeste palindrom")
else:
  print("Nije palindrom")
