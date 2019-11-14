_author_ = "aman"
import time
import random
from time import time as my_time

input("Hit enter to start")
wait_time = random.randint(1 , 5)
time.sleep(wait_time)
start_time = my_time()
input("Hit enter to stop")
end_time = my_time()

print("Start time "+ time.strftime("%X", time.localtime(start_time)))
print("End time "+ time.strftime("%X", time.localtime(end_time)))

print("Reaction time is {}".format(end_time - start_time))
