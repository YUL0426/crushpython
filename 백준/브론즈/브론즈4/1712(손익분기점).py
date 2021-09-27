분류) 수학적사고

코드1) 아예 틀림
a, b, c = map(int, input().split())
tot = 1

while 1:
    won = a + b*tot
    pan = c * tot
    tot += 1
    if pan > won:
        print(tot)
        break
    else:
        print(-1)
        
        
