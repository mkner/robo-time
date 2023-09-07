#
#
# robo-clocks - time
# for mobile robotics and related applications
#
# (c) 2022 - 2023  Mike Knerr
#
# 
#

#from threading import Thread
import threading

import time
import threading

from robobase import Object # from robot_object import Object

def delay(delay_time):
    #
    # aka arduino delay function
    # uses the most accurate, valid monotonic time 
    # that only goes forward in time
    
    timer_seconds = abs(delay_time/1000)
    start_time = time.monotonic()
    while (time.monotonic() - start_time) < timer_seconds:
       # dont run cpu 100% 
       # 1/10 nano may be problem if delay_time = 1
       #time.sleep(0.0000000001)# 1/10 nanosec 0.000 000 000 1 
       time.sleep(0.000000001)# 1 nanosec 0.000 000 001 
       #time.sleep(0.0001) # 1/10 millisecond
    return



def delayMicros(delay_time):
    #
    # same as delay (msec) but for microseconds
    
    timer_seconds = abs(delay_time/1000000) #millionth
    start_time = time.monotonic()
    while (time.monotonic() - start_time) < timer_seconds:
       # dont run cpu 100%
       time.sleep(0.0000000001)# 1/10 nanosec 0.000 000 000 1          
    return



def delay_sp(delay_time):
     # sleep version for comparison 
     ## not as accurate monotonic time
     ## can be accurate to 1 ms 
     # if chop the microseconds
     # included here only for doing comparative tests
     # or for stalling a process from racing a cpu
    timer_seconds = abs(delay_time/1000)
    #start_time = time.monotonic() #c.getMonotime()
    time.sleep(timer_seconds)
    return


def delay_tc(delay_time):
    
    # time.clock() process time
    # can go backward/forward & other issues
    # when underlying hw/sw system adjusts clock
    # not as accurate as monotonic time
   
    timer_seconds = abs(delay_time/1000)
    start_time = time.clock()
    
    while (time.clock() - start_time) < timer_seconds:
         time.sleep(0.0000000001)# 1/10 nanosec 0.000 000 000 1   
    return


def delay_tm(delay_time):
    
    # uses time.time() system time
    # can go backward/forward 
    # when underlying os/hw/sw system adjusts clock
    # not as accurate as monotone time
    # included here for doing comparative tests
    
    timer_seconds = abs(delay_time/1000)
    start_time = time.time()
    
    while (time.time() - start_time) < timer_seconds:
         time.sleep(0.0000000001)# 1/10 nanosec 0.000 000 000 1   
    return


def delay_mn(delay_time):
    # included for comparative purposes
    # uses monotonic time.monotonic() explicitly
    # same as delay above
    timer_seconds = abs(delay_time/1000)
    start_time = time.monotonic()
    
    while (time.monotonic() - start_time) < timer_seconds:
         time.sleep(0.0000000001)# 1/10 nanosec 0.000 000 000 1      
    return

def delay_test(delay_time):
    
    thread = threading.Thread(target=delay_threaded, args=(delay_time,))
    #thread1 = Thread(target = function01, args = (10,'thread1', ))
    thread.start()
    
    
def delay_threaded(delay_time):

    timer_seconds = abs(delay_time/1000)
    start_time = time.monotonic() #c.getMonotime()
    while (True):
        
       if (time.monotonic() - start_time) >= timer_seconds:
           print("delay_threaded finished",delay_time)
           break;
           
       time.sleep(0.000000001)
      
    return


"""
time() -- return current time in seconds since the Epoch as a float
clock() -- return CPU time since process start as a float
sleep() -- delay for a number of seconds given as a float
gmtime() -- convert seconds since Epoch to UTC tuple
localtime() -- convert seconds since Epoch to local time tuple
asctime() -- convert time tuple to string
ctime() -- convert time in seconds to string
mktime() -- convert local time tuple to seconds since Epoch
strftime() -- convert time tuple to string according to format specification
strptime() -- parse string to time tuple according to format specification
tzset() -- change the local timezone

"""

    

