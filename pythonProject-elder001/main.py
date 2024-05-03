rate=float(input('rate?: '))
stake=int(input('srake?: '))
time= int(input('for how long?: '))
for t in range(0, time):
   stake*=rate
   print (round(stake))