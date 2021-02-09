'''
    Post-its
    Computing
    Benj Carter
'''
from datetime import datetime
import time

def newsticky(time):
    f = open("sticky.txt", "a")
    message = str(input("What do you want to write on this post it?: "))
    f.write(message + " [" + time + "] " + "\n")
    f.close()
    f = open("sticky.txt", "r")
    #print(f.read())
    print("Sticky added!")
    f.close()


def readsticky():
    f = open("sticky.txt", "r")
    lines = f.readlines()

    count = 0
    for line in lines:
        count += 1
        print("Line
              {}: {}".format(count, line.strip()))
        time.sleep(0.2)

    if count == 0:
        print("There are no stickies")
    
    f.close()

def clearstickies():
    x = input("Are you sure?: [ENTER]")
    f = open("sticky.txt", "w").close()
    print("All stickies erased")


finished = bool(0)

while finished != bool(1):
    print("\nType 1 to make a new sticky")
    time.sleep(0.2)
    print("Type 2 to read through all stickies")
    time.sleep(0.2)
    print("Type 3 to erase all stickies")
    time.sleep(0.2)
    print("Type 9 to exit")
    time.sleep(0.2)
    newread = int(input("\nNew sticky or read them all?: "))
    if newread == 1:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        newsticky(current_time)
    elif newread == 2:
        readsticky()
    elif newread == 3:
        clearstickies()
    elif newread == 9:
        print("The program will end now")
        time.sleep(0.2)
        print("But your postits will be safe")
        time.sleep(2)
        exit()

    

