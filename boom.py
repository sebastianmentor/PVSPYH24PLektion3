import time
import os

def time_to_detonation(x):
    y = os.system('cls')
    for i in range(x,0, -1):
        print(i, end='')
        time.sleep(1)
        print("  \r", end='')
    print('BOOOOMMMM!!!💣💣💣💣')

time_to_detonation(10)