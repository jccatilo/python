'''
for loop and increment decrement
'''
'''
a = 0
start = 0
end = 11

for x in range(start, end):
    print(a)
    a+=1
'''
'''
End Tutorial
'''





'''
While Loop
'''

from time import sleep
a=0
LOOP = 0

while True:
    while LOOP == 0:
        print(a)
        a+=1
        if a ==11:
            LOOP = 1
            print("GO TO LOOP = 1")
        sleep(0.5)
    while LOOP == 1:
        print(a)
        a-=1
        if a == 0:
            LOOP = 0
            print("GO TO LOOP = 0")
        sleep(0.5)



