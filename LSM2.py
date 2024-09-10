N, C = map(int, input().split())

turn = C  
while N > 0:

    if N >= 5:
        N -= 5
    elif N >= 2:
        N -= 2
    else:
        N -= 1

    turn = 1 if turn == 2 else 2

if turn == 1:
    print("Lili")
else:
    print("Lala")