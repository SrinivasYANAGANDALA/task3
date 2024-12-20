import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="1234567890"
charactor="~!@#$%^&*()_+:,./[]{}"
all=upper + lower + number+charactor
length=16
for i in range(5):
  password="".join( random .sample(all,length))
  print("random password was : ",password)