import time

print(time.time())
print(time.asctime())
print(time.localtime())

now_time = time.time()
atf_two_day = now_time+60*60*24*2
print(time.strftime("%Y年%m月%d日 %H时%M分%S秒",time.localtime(atf_two_day)))