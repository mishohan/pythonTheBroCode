# Countdown Timer Program
# time.sleep(3) # program sleeps for 3 seconds

import time

my_time = int(input("Enter the time in seconds: "))

for X in range(my_time, 0, -1): # or range(my_time, 0, -1) do the same as reversed(range(1, my_time+1))
    seconds = X % 60
    minutes = int(X / 60) % 60
    hours = int(X/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's UP!")