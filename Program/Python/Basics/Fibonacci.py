a=0;b=1;c=a+b;d=0;e=int(input("How many repititions?"))
while d < e:
  print(c);d+=1;c=a+b
  if a < b: a = a+b
  if b <= a: b = a+b
