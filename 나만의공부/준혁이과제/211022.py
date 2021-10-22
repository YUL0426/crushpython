course = [["calculus 1",3],["calculus 2",3],["python ",3],["chemistry 2",3],["physics 2",3],
           ["english presentation",2],["english writing",2],["creative writing",2],
          ["critical writing",2],["coding thinking",2]]
backpack = [[],[0]] #[[courses],[total credits]]

for i in range(len(course)):
    print(i, course[i])
tmp=0

while 1:
    n = int(input())
    if -1 < n < 10 and backpack[1][0] <=20:
        backpack[0].append(course[n][0])
        backpack[1][0] = backpack[1][0] + course[n][1]
        print(backpack)
    if 12 <= backpack[1][0] <=20:
        print("you can add", 20-backpack[1][0], "more credit")
    if backpack[1][0] > 20:
        print("you put too much")
    elif n==-1 and backpack[1][0] < 15:
        print(backpack)
        print("you have to pick more subject next time")
        break
    elif n <-1 and n >= 10:
        print("error")
