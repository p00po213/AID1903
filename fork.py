import os
from time import sleep
pid=os.fork()
if pid<0:
    print('Creat failed')
elif pid==0:
    sleep(3 )
    print('The new process')
else:
    sleep(4)
    print('old process')
print('test over')
print('第二种方法')

print('Tom改的')

print('Jame修改的')

