_author_ = "aman"
import time

print(time.gmtime(0))
print(time.localtime())
print(time.time())
print("=" * 40)

time_now = time.localtime()
print("Year : ", time_now[0], time_now.tm_year)
print("Month : ", time_now[1], time_now.tm_mon)
print("Day : ", time_now[2], time_now.tm_mday)
