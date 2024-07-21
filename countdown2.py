
import time

def timer(hours_minutes_seconds):
    hours, minutes, seconds = hours_minutes_seconds, 60, 60
    format = '{:2d}:{:2d}:{:2d}'.format(hours, minutes, seconds)
    
    time.sleep(1)
    for t in  'hours', 'minutes', 'seconds':
        return t - 1
    print('stop')

x = timer(int(input('enter time')))
print(x)