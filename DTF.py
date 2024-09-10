HH, MM, SS = map(int, input().split(":"))
CH, CM, CS = map(int, input().split(":"))

HH = HH + 5
gmt7 = HH * 3600 + MM * 60 + CS
gmt2 = CH * 3600 + CM * 60 + CS

if gmt7 > gmt2:
    print ("Sampai jumpa di Acara Pear berikutnya!")
else:
    waiting_time = gmt2 - gmt7   
# pengonversian waiting time ke jam, menit, detik kembali
H = waiting_time // 3600
waiting_time % 3600 # untuk sisa detik setelah dikonversikan ke jam
M = waiting_time // 60
waiting_time % 60 # untuk sisa detik setelah dikonversikan ke menit
S = waiting_time % 60

print (f"{H} Hours,{M} Minute,{S} Second")




