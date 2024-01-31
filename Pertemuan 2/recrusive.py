def myFunction(a):
  if a == 0:
    return
  print(a)
  a -= 1
  myFunction(a)

myFunction(10)