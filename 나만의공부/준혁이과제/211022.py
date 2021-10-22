course = [["calculus 1",3],["calculus 2",3],["python ",3],["chemistry 2",3],["physics 2",3],
           ["english presentation",2],["english writing",2],["creative writing",2],
          ["critical writing",2],["coding thinking",2]]
backpack = [[],[0]] #[[courses],[total credits]]

for i in range(len(course)):
    print(i, course[i])
tmp = -99

while 1:
    n = int(input())
    if backpack[1][0] >=19 and n!= -1:
        print("you put too much")
    if -1 < n < 10 and n==tmp and backpack[1][0] < 19:
        print("you already have that")
    if -1 < n < 10 and n!=tmp and backpack[1][0] < 19:
        backpack[0].append(course[n][0])
        backpack[1][0] = backpack[1][0] + course[n][1]
        print(backpack)
    if n != -1 and 12 <= backpack[1][0] <19:
        print("you can add", 20-backpack[1][0], "more credit")
    if n==-1 and backpack[1][0] >= 15:
        print(backpack)
        break
    if n == -1 and backpack[1][0] < 15:
        print(backpack)
        print("you have to pick more subject next time")
        break
    elif n <-1 or n >= 10:
        print("error")
    tmp = n
