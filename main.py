import os
import random , time

os.system('clear')
world = list()

col = int(input("Enter number of col : "))
row = int(input("Enter number of row : "))


print()
for i in range(row):
    world.append(list())
    for j in range(col):
        if (j==0 or j==(col-1) or i==0 or i==(row-1) ):
            world[i].append("#")
        else:
            world[i].append(" ")

while 1 :
    colRand = random.randint(1,(col-2))
    rowRand = random.randint(1,(row-2))
    world[rowRand][colRand] = "X"

    for i in range(len(world)):
        for j in range(len(world[i])):
            item = world[i][j]
            print(f"{item:^3}",end=' ')
        print("\n")
    time.sleep(0.7)
    world[rowRand][colRand] = " "
    os.system('clear')













##############backup


# world = [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]

# print()
# for i in range(len(world)):
#     for j in range(len(world[i])):
#         # print(f"({i} {j})     " , end='')
#         if (j==0 or j==9 or i==0 or i==9 ):
#             print(f"{'#':^3}",end=' ')
#         else:
#             print(f"{' ':^3}",end=' ')
#     print('\n')







##############random

# colRand = random.randint(1,8)
# rowRand = random.randint(1,8)
# world[rowRand][colRand] = "#"

# for i in range(len(world)):
#     for j in range(len(world[i])):
#         item = world[i][j]
#         print(f"{item:^3}",end=' ')
#     print("\n")

