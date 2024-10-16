def faktorijel(broj):
  if broj<=1:
    return 1
  else:
    tmp=1
    for i in range(1,broj+1):
      tmp=tmp*i
    
    return tmp


broj= int(input("Unesi broj"))

print(faktorijel(broj))    
