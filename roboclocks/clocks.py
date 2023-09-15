#
#
# robo-clocks - clocks
# for mobile robotics and related applications
#
# (c) 2022 - 2023  Mike Knerr
#
# 

# SIX
#package release: 0.01.6b


import numpy as np
#import math as m
import math

import time

from datetime import datetime, timezone
from datetime import timedelta
import calendar
import ntplib

from robobase import Object
from roboclocks.time import delay


class Clock(Object):

    def __init__(self):
        
        super(Clock, self).__init__()
         
        self._name = "Clock"
        self._vers = "v01.02.08" 
        self._desc = "Clock" #" - "+self._vers
        self._model = ""
        
        self._debug_flag = False
        
        self._init_monotime = self.getMonotime() # init base time as monotonic
        #self._init_monotime_offset = 0 # same for monotonic time
        self._init_system_time = self.getSystemTime() # only if avail 
        self._init_system_time_offset = 0 # offset to sync w/ external clock
        # derivative clocks classescan use there own override for the epoch
        self._start_epoch_time = 0.0 # this is different for each derived Clock type
        self._epoch_days_in_year = 360 # can have a custom year size
        # from this clocks viewpoint
        self._start_unix_epoch = 1969*365*24*60*60 # clock uses zero based  
        
        self._up_monotime = 0.0
        
        # last updated uptime values
        self._uptime = 0.0 #same as above ?
        
        # these are totals,not fractional result of fptime
        self._up_total_millisec = 0 
        self._up_total_microsec = 0
        
        self._up_years = 0  
        self._up_days = 0 # days in the year not total days up
        self._up_hours = 0
        self._up_minutes = 0
        self._up_seconds = 0
   
        # remainders of floating point uptime
        self._up_microsec = 0 # remainder of 
        self._up_millisec = 0
        self._up_nanosec = 0 # future
        
        # timestamp formatting parameters
        #mk list in logical order
        self._timestamp_date_sep = '-' # in YYYY-MM-DD
        self._timestamp_dt_sep = ' ' # between date & time parts
        self._timestamp_time_sep = ':' # in HH:MM:SS
        self._timestamp_res = 'micro' #- none = dont show, milli nano, pico 
        self._timestamp_res_sep = ' ' # between date/time & resolution separator 
        self._timestamp_use_ztail = True # use tail end Z for +00:00
        self._timestamp_format = 'default' 
        self._timestamp_compressed = False
        
        # calendar parameters for calender system used
        self._cal_days_in_year = 360 #365 # greg =  365.2425  epoch days in year different
        self._cal_hours_in_day = 24
        self._cal_minutes_in_hour = 60
        self._cal_seconds_in_minute = 60
        
        self._cal_months_in_year = 12 # or 
        self._cal_days_in_month = 30
        
        #self._cal_weeks_in_year = 52
        self._cal_weeks_in_month = 5
        self._cal_days_in_week = 6
        
        # from init above
        self._current_cal_type = 'sym360'
        
        # uptime is always zero based
        # set display format type dor timestamp YYYY-MM-DD
        self._cal_zerobased_format = True
      
        # values below get updated 
        # Clock only uses year,month,day,day in year
        # emulation of calendar like partitions
        # are here as framework for decendant classes
        self._cal_year = 0
        self._cal_month = 0
        self._cal_day = 0
        self._cal_day_in_year = 0
        self._cal_week = 0
        self._cal_day_of_week = 0
        
        self._cal_hours = 0
        self._cal_min = 0
        self._cal_sec = 0
        self._cal_millisec = 0
        self._cal_microsec = 0
        
        # testing
        self._cal_ntest_offset = 0
        self._cal_ntest = 0 #for testing
    
     
    def getMonotime(self): #getMonotime(self):
        
        # returns monotonic time in floating point seconds 
        # sometimes since the system board started running
        # or system OS/HW startup (if using millis() w/ arduino uno)
        
        # uptime representation not guaranteed with python call time.monotonic()
        # from the python docs
        # "As the reference point of the returned value of monotonic clock
        # is undefined, only the difference between the results of 
        # consecutive calls is valid"

        # Clock only binds to underlying OS/HW here for counting
        # except for sleep related functions to waste some nanos
        # other class functions call this as a reference
        
        mt = time.monotonic()
      
        return (mt)#time.monotonic())
    
    
    def getSystemTime(self):
        
        # not a primary  function of Clock
        # Clock only knows uptime!
        # that is its system time
        # override this in derived classes
        
           return self.getMonotime()
   
    ## timing functions ##
    
    #mk
    # timing functions
    # these are duplicated from roboclocks/time.py
    # here as part of the primordal Clock and available 
    # to all derivative clock types
    # future may callback to the freestanding ones
    # but process threading and speed can be factors
    # so they are de-coupled for now 

    def delay(self,delay_time):
 
        # aka arduino delay function
        # uses the most accurate, valid monotonic time available
        # that only goes forward in time
    
        timer_seconds = abs(delay_time/1000)
        start_time = time.monotonic()
        
        while (time.monotonic() - start_time) < timer_seconds:
                # dont run cpu 100% 
                time.sleep(0.0000000001)# 1/10 nanosec 0.000 000 000 1   
                #time.sleep(0.000000001) #1/1000000000)    
        return


    def delayMicros(self,delay_time):
 
        # uses the most accurate, valid monotonic time available
        # that only goes forward in time
       
        timer_seconds = abs(delay_time/1000000)
        start_time = time.monotonic()
        
        while (time.monotonic() - start_time) < timer_seconds:
                # dont run cpu 100%
                 time.sleep(0.0000000001)# 1/10 nanosec 0.000 000 000 1   
                #time.sleep(1/1000000000)    
        return

    
    
    def millis(self):
        # aka arduino millis() function
        # uptime in milliseconds
        # don'i use anything like time.time() can go backwards 
        # monotonic time increasing fowrard in time only
        
        dt=self.getMonotime()-self._init_monotime
        millisec = int(dt*1000)
        return(millisec)  
    
    
    def micros(self):
        # uptime in microseconds
        # monotonic time increasing fowrard in time only
        dt=self.getMonotime()-self._init_monotime 
        microsec = int(dt*1000000)
        return(microsec)  
    
    
    def nanos(self):
        # uptime in nanoseconds
        # resolution may or not be supported by underlying OS/HW
        # will end up with a bunch of ?? on end fp numeric churn?
        dt=self.getMonotime()-self._init_monotime 
        nanosec = int(dt*1000000000)#int(dt*1 000 000 000)
        return(nanosec)  


    def getUptimeFp(self):
        # want this call for the floating point
        # uptime to be fast so keep it clean & simple
        self._up_monotime = self.getMonotime() - self._init_monotime
        return self._up_monotime 
    
    
    def _parseFptime(self,fptime):
        
        # fptime is in seconds floating point
        
        # basic, uncomplicated algorithm, without reliance on
        # language specific modules  so it is more portable
        # to the most basic system board that will always have 
        # a clock that counts into the future
        
        # want general purpose algo here to use with timestamping
        # returns years & day in the year NOT the day in the month
        # or week or day of week - these are realworld calendar oriented 
        # does NOT update any internal parameter
        # returns:
        # year, day in year, hours, min, sec, 
        # remainder after seconds in milliseconds, microseconds
        # with (year, day_in_year) there is enough for
        # a calling program to calc for very specific calendar types
        # 
        # in future, nanoseconds, milli or micro can choose which one
        # uses dimensions for time partitioning from internal parameters
        # set in advance for dimensions of calendar system to use
        
        # calculate the remainder after seconds in microseconds & milliseconds
        # break apart floqt on sides of decimal point
        
        mtup_rem, mtup_sec = math.modf(fptime) # v0.11 self._up_monotime)
        
        fp_micros = mtup_rem*1000000
        _,int_micros = math.modf(fp_micros)
        rem_int_micros=int(int_micros)
        
        # v0.11 this way, 
        fp_millis = mtup_rem*1000
        _,int_millis = math.modf(fp_millis)
        rem_int_millis=int(int_millis)
    
        # can have a custom year size
        days_in_year = self._cal_days_in_year 
        ## THIS IS OKdays_in_year = self._epoch_days_in_year 

        days_in_month = self._cal_days_in_month
        
        sec_in_min = self._cal_seconds_in_minute
        sec_in_hour = self._cal_minutes_in_hour*self._cal_seconds_in_minute
        sec_in_day = sec_in_hour*self._cal_hours_in_day
        sec_in_year = sec_in_day * days_in_year
        
        min_in_hour = self._cal_minutes_in_hour #_seconds_in_minute
      
        n = up_seconds = int(mtup_sec)#+ self._cal_days_in_year *sec_in_day + sec_in_day-1 # add days to test
        
        self._ntest = n #for testing
        
        #print();print(" in algo debug = ",self.debug())
        
        if (self.debug() == True):
            # *here
            # can move ahead tyesx
            #yrs = 0
            #print();print(" in algo debug is ON");print()    
            n += self._cal_ntest_offset #v0.17 was FUTURE
             
        years = n / sec_in_year
        years = int(years) 
        
        total_days = (n / sec_in_day) #  divide seconds into days
        total_days = int(total_days) 
        
        day_in_year = total_days%days_in_year
        
        # get seconds into the day
        n %= sec_in_day  # modulo seconds in a day
        hours = (n / sec_in_hour)   # divide into hours
        hours = int(hours) #chop
        
        # get minutes into the hour
        n %= sec_in_hour; # modulo seconds in hour
        minutes = (n / min_in_hour) # divide into minutes
        minutes = int(minutes) #chop
        
        # get seconds into the minute
        n %= sec_in_min; # modulo seconds in a minute
        seconds =n
        ## END
        
        # ok return in tuple
        x = ( years,  day_in_year, hours, \
               minutes, seconds, \
               rem_int_millis, rem_int_micros)
            
        return x
    
       
    def _updateUptime(self):
        
        # update internal & floating point representations of uptime
        # in plain ordinary uncomplicated integers
        # keep it simple, 
        # parse out this way instead of relying on
        # underlying libraries, modules functions
        # with unknown algorithms, 
        # this Clock class needs to be clean, simple, accurate, 
        # when there is always varying resolution
        # depending on underlying system HW/OS or system board
  
        fpUptime = self.getUptimeFp() # get current floating point uptime
        
        # update absolute reference 1st in fp
        self._uptime = fpUptime
        
     
        # multipy to shift fp time over then CHOP, DONT ROUND 
        # rounding off can skew digits on 4/5 splits
        # with high resolution floating point
        # chop  always divides up non-discrete floating
        # point simulation of the real number system that
        # has infinite resolution into quasi-discrete units evenly 
 
        # v0.11  want it faster
        self._up_total_microsec = int(fpUptime*1000000)
        self._up_total_millisec = int(fpUptime*1000)
        
        # THIS IS THE ONLY PLACE THESE GET UPDATED 
        
        years, day_in_year, hours, \
        minutes, seconds, \
        rem_int_millis, rem_int_micros =  self._parseFptime(fpUptime)
            
        self._up_years = years # new v0,10
        self._up_days = day_in_year ## was up to v0.08
        self._up_hours = hours
        self._up_minutes = minutes
        self._up_seconds = seconds
        
        # for timestamping
        self._up_microsec = rem_int_micros
        self._up_millisec = rem_int_millis
        
        return
    
 
    def _getUptimeTuple(self):
        
        self._updateUptime()
        
        # easy integers just return (d,h,m,s)
        years = self._up_years
        days = self._up_days
        hours = self._up_hours 
        mins = self._up_minutes
        secs = self._up_seconds
        # millis,micro? not timestamp, just uptime?
        
        return(years,days,hours,mins,secs) #,millisec)


    def uptime(self):
        
          # simple shell mode display
          # for command line
          # getUptimeStr() to get string
          # getUptime to get a tuple of the numerics
          # days is days in year, use timestamp for year,month,day...

        print(self.getUptimeStr())
        return
       
          
    def getUptime(self):
        # returns tuple of integers 
        # nice uncomplicated easy to work with
        # tuple of integers in the format
        # (days, hours, minutes, seconds)
        
        self._updateUptime()
        
        return(self._getUptimeTuple())
    
    
    def getUptimeStr(self):
        
        # returns the same format as 
        # uptime() but in a string
        # nice uncomplicated easy to work with
        # tuple of integers in the format
        # (days, hours, minutes, seconds)
        
        x=""
        
        y,d,h,m,s = self.getUptime()
        
        ys = str(y).zfill(4)
        ds = str(d).zfill(2) # total days into year from uptime
        hs = str(h).zfill(2)
        ms = str(m).zfill(2)
        sc = str(s).zfill(2)
        
        # show only what is needed
        # FUTURE flag to turn  full version on or use minimal
        # self._show_uptime_?
        
        if (y > 0):
                x = ys+"-"+ds+" - "+hs+":"+ms+":"+sc
        elif (d > 0):
                 x = ds+" - "+hs+":"+ms+":"+sc
        else:
                  x = hs+":"+ms+":"+sc
                    
        return x
    
    
    def epoch(self):
        
       # NOTE! want epoch  ZEROBASED for Clock 
       # but not SystemClock or others
       
      #print(time.asctime(self._start_epoch_time))
      if( not self.isCalFormatZeroBased() ):
          self.setZeroBasedFormatOff()
          print(self.mkTimestampStr(self._start_epoch_time))
          self.setZeroBasedFormatOn()
      else:
           print(self.mkTimestampStr(self._start_epoch_time))
    
   
    
    def _isCalSymmetric(self):
         # keep this function!!!
        days_in_year = self._cal_days_in_year
        days_in_month = self._cal_days_in_month
        months_in_year = self._cal_months_in_year
        
        if (days_in_year % months_in_year == 0 
              and
              days_in_year % days_in_month == 0):
            return True
        else:
            return False
     

    def getCalMoDay(self, day_in_year, up_year):
        
        days_in_year = self._cal_days_in_year
        days_in_month = self._cal_days_in_month
        months_in_year = self._cal_months_in_year
        
        epoch_days_in_year = self._epoch_days_in_year
        
        # ck first if this is a gregorian calender w/ 365 days
        if (days_in_year == 365 and months_in_year == 12):
            
            # the year up_year is from uptime 
            
            # get the gregorian month, day in month
            # various global/historical/geo-politco calendar systems 
            # are outside the basic functions of Clock,
            # calendar  is used here for
            # formatting timestamps based on the uptime counter
            # into the gregorian calendar 
            # without any UTC zone, leap years leap seconds
           
            # ckeck that day in year starts at zero for uptime clock
            # not other calendar types unless they are set to 
            # use zero-based indexing instead of 1-based for first of whatever
           
            dt_year=up_year+1 #datetime index starts at 1
            #dt_start = startDate = datetime(year=dt_year, month=1, day=1)
            dt_start  = datetime(year=dt_year, month=1, day=1)
            days_offset = day_in_year #- 1
            #dt_end  = startDate + timedelta(days=days_offset)
            dt_end  = dt_start + timedelta(days=days_offset)
            
            cal_month = dt_end.month #endDate.month
            cal_day = dt_end.day
            
        # check FIRST if a symmetric calendar
        # so then not using "usual" calendar days in year 
        
        elif (self._isCalSymmetric() == True):
            
              #if (self.debug() ):
                 # print("using symmetric calendar ")
                  #print()
                 #ok v0.12, chop w/ int to take floor of
              cal_month = int(day_in_year/days_in_month) #chop for floor
              
                #ok v0.12
              day_in_month = day_in_year%days_in_month
              cal_day=day_in_month
              
        else:
            # bail out with something
            # will show up
            cal_month=0
            cal_day=0
            
        return cal_month,cal_day
        
    
    def _updateCal(self): 
        # Clock() version
        #mk
        # this is primary def of _updateCal()
        # for Clock() only
        # derived classes need to override this function
        
        # used for timestamps 
        # make any format adjustments here ONLY?
        
        # UPDATES ms & microseconds als0 same time
        y,d,h,m,s = self.getUptime()
        
        # calendar stuff from uptime
        cal_year=y
        
        cal_month, cal_day = self.getCalMoDay(d,cal_year) 
        
        #adjust for timestamp formats
        #zbf ck for symcal? also?
        
        if (self._cal_zerobased_format == True):
            
            cal_month -=1
            cal_day -=1
            
            ### UNDO IT
            if (self._isCalSymmetric() == True):
                cal_month +=1
                cal_day +=1
        
        else: # 1 is first format
            cal_year +=1 
            
            # ck for symmetric cal
            # then inc month & day
           
            if (self._isCalSymmetric() == True):
                cal_month +=1
                cal_day +=1
                
        ## UPDATE THESE HERE
        ## timestamp functions use these
        #v0.14+ ?
        self._cal_year = cal_year
        self._cal_month = cal_month
        self._cal_day = cal_day
        
        self._cal_hours = h
        self._cal_min = m
        self._cal_sec = s
        
        return
    
    
    def setCalType(self,caltype):
        
        # only 2 presets here so far
       
        if (caltype == 'sym360'):
            
            # Clock indigenous calendar type
            # is symmetric 360 days in year
            # based on degrees in circle (360)
            # calendar parameters for calender system used
            
            # if (self.debug()):
                #print("setting calendar type: ",caltype)
            self._current_cal_type = caltype
            
            self._cal_days_in_year = 360
            self._cal_hours_in_day = 24
            self._cal_minutes_in_hour = 60
            self._cal_seconds_in_minute = 60
            
            self._cal_months_in_year = 12 # or 
            self._cal_days_in_month = 30
            
            # not used, just placeholders
            # so still symmetric
            self._cal_weeks_in_month = 5
            self._cal_days_in_week = 6
            
           
        elif (caltype == 'gregorian'):
            
            #if (self.debug()):
             #   print("setting calendar type: ",caltype)
            
            self._current_cal_type = caltype
             
            self._cal_days_in_year = 365
            self._cal_hours_in_day = 24
            self._cal_minutes_in_hour = 60
            self._cal_seconds_in_minute = 60
            
            self._cal_months_in_year = 12 # or 
            self._cal_days_in_month = 30
            
            # not really used? here for ?
            self._cal_weeks_in_year = 52
            self._cal_weeks_in_month = 4
            self._cal_days_in_week = 7
            #self._cal_weeks_in_year = 52
        else:
            if (self.debug()):
                print("unknown calendar type")
        
        return
    
    
    def getCalType(self):
        return self._current_cal_type 
    
    def isCalFormatZeroBased(self):
        return self._cal_zerobased_format
    
    def isCalFormatFirstBased(self):
        return not(self._cal_zerobased_format)
    
        
    ## timestamp functions ##
    
    def setTimestampRes(self,x):
        
       # print("setting timestamp res to: ",x)
        
        if ((x == 'micro') or (x == 'milli') or (x == 'none')):
            self._timestamp_res = x
        #otherwise do nothing
        return
    
    def setTimestampDateSep(self,x):
        # separator for  date YYYY-MM-DD part
         if (len(x) <= 3): #limit for now
             self._timestamp_date_sep = x
             
           
    def setTimestampSep(self,x):
        # what is used to between output 
        # of date YYYY-MM-DD and the hh:mm:ss time
        
        if (len(x) <= 3): #limit for now
         self._timestamp_dt_sep = x
    
    #mk
    #NEW 
    def setTimestampTimeSep(self,x):
        # what is used for ':"
        # in time string hh:mm:ss 
        
        if (len(x) <= 3): #limit for now
         self._timestamp_time_sep = x
    
    
    def setTimestampResSep(self,x):
        
        if (len(x) <= 3): #limit for now
         self._timestamp_res_sep = x
         
    #mk
    #NEW
    #*here
    def setTimestampCompressedOn(self):
        # make all delimiter/separators ''
        # to compress into compact ascii string
        #need a flag for tail end stuff utc
        self._timestamp_compressed = True
        
        self.setTimestampDateSep('')
        self.setTimestampSep('')
        self.setTimestampTimeSep('')
        self.setTimestampResSep('')
        # utc local time offset sep 
        # which one?
    
    
    def setTimestampCompressedOff(self):
         #FUTURE preserve prev settings
         if self._timestamp_compressed == True:
             # restore previous delimiter settings 
             self._timestamp_compressed = False
         #otherwise do nothing

    
    
    #FUTURE
    #def unsetTimestampCompressed(self):
         # restored delimiters
         # from last saved compressed call
         # return
    
    
    def setIsoZtailOn(self):
        self._timestamp_use_ztail = True
        
    def setIsoZtailOff(self):
        self._timestamp_use_ztail = False 
        
   
    def setTimestampFormat(self,tsformat): 
        
        if (self.debug()):
            print()
            print("Setting timestamp format to: ",tsformat)
            print()
            
        if (tsformat == 'basic' or tsformat == 'default'):
            
            #self._timestamp_use_ztail == False
           
            self._timestamp_date_sep = '-' # in YYYY-MM-DD
            self._timestamp_dt_sep = ' ' # between date & time
            self._timestamp_time_sep = ':' # in HH:MM:SS
            self._timestamp_res = 'micro' #- none = dont show, milli nano, pico 
            self._timestamp_res_sep = ' ' # resolution char separator 
            
            self._timestamp_format = 'default' # iso-local, iso-utc
            self._timestamp_use_ztail = False # use tail end Z for +00:00
            #new dont use compressed
            self._timestamp_compressed = False
      

        # Clock sense of uptime
        # doesnt know geograpphic or standards based timekeeping
        # but can still use iso formatting for timestamps
        # derived classes call back here for the same presets functionality
        # formats can be adjusted on the fly after using a preset
        # for variations within whatever spec is being used
        
        elif (tsformat == 'iso-local'):
            self._timestamp_res = 'micro' #- none = dont show, milli nano, pico 
            self._timestamp_res_sep = '.' # resolution char seperator 
            self._timestamp_dt_sep = 'T' # between date & time
            self._timestamp_date_sep = '-' # between YYYY-MM-DD
            self._timestamp_time_sep = ':' # in HH:MM:SS
            self._timestamp_format = 'iso-local' # iso-local, iso-utc
            self._timestamp_use_ztail = False # use tail end Z for +00:00
            #new
            self._timestamp_compressed = False
            #9/15 probably not used now after pkg 0.1.6b
            self._cal_utc_offset = 0 #mk ZERO! its "flag" was ZERO! 
            

        elif (tsformat == 'iso-utc'):
            self._timestamp_res = 'micro' #- none = dont show, milli nano, pico 
            self._timestamp_res_sep = '.' # resolution char seperator 
            self._timestamp_dt_sep = 'T' # between date & time
            self._timestamp_date_sep = '-' # between YYYY-MM-DD
            self._timestamp_time_sep = ':' # in HH:MM:SS
            self._timestamp_format = 'iso-utc' # iso-local, iso-utc
            self._timestamp_use_ztail = True # use tail end Z for +00:00
            #new
            self._timestamp_compressed = False
         
        return
    
    #mk
    #NEW
    def getTimestampFormat(self): 
        return self._timestamp_format
    
    def setZeroBasedFormatOff(self):
        self._cal_zerobased_format = False
        return
        
    def setZeroBasedFormatOn(self): 
        self._cal_zerobased_format = True
        return
    
    
    def getTimestamp(self):
        # derived classes call back upstream here as default
        # ONE call only , takes a snapshot 
        # returns a tuple 
        
        self._updateCal() # updates uptime also hour,min,sec etc 
        
        micros = self._up_microsec
        millis = self._up_millisec
        
        if (self._timestamp_res == 'micro'):
            res = micros
        elif (self._timestamp_res == 'milli'):
            res = millis
        else:
            res = 0 # since numeric zero if no resolution
               
        #is NOW v0.15 was FUTURE 
        cal_year = self._cal_year 
        cal_month = self._cal_month
        cal_day = self._cal_day
        
        h = self._cal_hours
        m = self._cal_min
        s = self._cal_sec
        
        return (cal_year,cal_month, cal_day, h,m,s,res)
    
    #*here
    def getTimestampStr(self):
        #mk 9/14
        # all derived classes override this now
        # just override now in SystemClock

        #x= "2022-12-01 15:58:51 000000"
        
        # easy, work right from tuple
        y,mo,dy,h,m,s,res= self.getTimestamp()
        
        ys = str(y).zfill(4)
        #ds = str(d).zfill(2) # total days into year from uptime
        hs = str(h).zfill(2)
        ms = str(m).zfill(2)
        sc = str(s).zfill(2)
        
        mostr=  str(mo).zfill(2)
        dystr  = str(dy).zfill(2)

        # micros = str(self._up_microsec).zfill(6)
        # millis = str(self._up_millisec).zfill(3)

        ddsep = self._timestamp_date_sep # date digit sep
        dtsep = self._timestamp_dt_sep
        tmsep = self._timestamp_time_sep #mk NEW 9/10
        resep = self._timestamp_res_sep
        
        # current resolution on tail end if any is used
        if (self._timestamp_res == 'micro'):
            resz = str(res).zfill(6)
        elif (self._timestamp_res == 'milli'):
            resz = str(res).zfill(3)
        elif (self._timestamp_res == 'none'):
            resz = ""
            #v0.23
            resep = ""
        else:
            resz = ""
            #0.23
            resep = ""
        
        # only one format now
        tsz =  ys + ddsep + mostr + ddsep + dystr + dtsep + \
                      hs + tmsep + ms + tmsep + sc + resep + resz
     
        return tsz
    
       
    
    def getTimestampFp(self):
        return self.getUptimeFp() 
        #return self.getUptimefp() 
    
    
    def mkTimestamp(self,fptime):
        
        # make a timestamp from 
        # from any floating point time
        # uses Clock current calendar settings
        # return tuple
    
        year, day_in_year, hours, \
               minutes, seconds, \
               rem_int_millis, rem_int_micros = self._parseFptime(fptime)
             
        # day is day in month
        month, day = self.getCalMoDay(day_in_year,year)
        
        #### have to do this here also !
        
        if (self._cal_zerobased_format == True):
            
            month -=1
            day -=1
            
            ## UNDO IT
            if (self._isCalSymmetric() == True):
                month +=1
                day +=1
        
        else: # 1 is first format
            
            year +=1 
            # ck for symmetric cal
            # then inc month & day
           
            if (self._isCalSymmetric() == True):
                month +=1
                day +=1
                
        # mkTimeStampStr now puts in string form
        x = (year, month, day, hours, minutes, seconds, \
             rem_int_millis, rem_int_micros) #""
        
        return(x)
    
    
    #mk is this function used anywhere?
    def mkTimestampStr(self, fptime):
        
        # maka a timestamp from any floating point time
        # based on settings in Clock
        # return string w/ formatted 
        
        y,mo,dy,h,m,s, res_millis, res_micros= self.mkTimestamp(fptime)
         
        ys = str(y).zfill(4)
        #ds = str(d).zfill(2) # total days into year from uptime
        hs = str(h).zfill(2)
        ms = str(m).zfill(2)
        ss = str(s).zfill(2)
        
        # from total days into current year
        
        #print("timestamp:  mo,dy = ",mo,dy)
        
        mostr=  str(mo).zfill(2)
        dystr  = str(dy).zfill(2)
    
        resep = self._timestamp_res_sep 
        #mk new
        tmsep = self._timestamp_time_sep
        
        # decide on resolution of remainder
        # finest resolution on tail end if any is used
        if (self._timestamp_res == 'micro'):
            resz = str(res_micros).zfill(6)
        elif (self._timestamp_res == 'milli'):
            resz = str(res_millis).zfill(3)
        #FUTURE - ck for nanos & none?
        else:
            resz = ""
        
        dtsep = self._timestamp_dt_sep
        
        tsz = ys+"-"+mostr+"-"+ dystr + dtsep + \
            hs + tmsep + ms + tmsep + ss + resep + resz #mk new tmsep
          
        return tsz
        #return 
       

    def timestamp(self):
        # easy now 
        print(self.getTimestampStr())
        return 
    
    
    def ts(self):
        #shortform
        self.timestamp()
        
        
    ## command line functions ##
    
    def time(self):
        # HH:MM:SS
        up=self.getUptime()
        hh = str(up[2]).zfill(2)
        mm = str(up[3]).zfill(2)
        ss = str(up[4]).zfill(2)
        tm = hh+":"+mm+":"+ss
        print(tm)
        return 
    
    
    def date(self):
        # YYYY-DD-MM
        ts = self.getTimestamp()
        yyyy=str(ts[0]).zfill(4)
        mm = str(ts[1]).zfill(2)
        dd = str(ts[2]).zfill(2)
        d=yyyy+"-"+mm+"-"+dd
        print(d)
        return
    
    
    def now(self):

        # Clock onlyy returns timestamp without res
        # x= "0000-00-00 00:00:00"
        # SystemClock would include cal/locale attributes
        
        y,mo,dy,h,m,s,res = self.getTimestamp()
        
        ys = str(y).zfill(4)
        hs = str(h).zfill(2)
        ms = str(m).zfill(2)
        sc = str(s).zfill(2)
        
        mostr=  str(mo).zfill(2)
        dystr  = str(dy).zfill(2)       
        
        x = ys+"-"+mostr+"-"+ dystr +" "+hs+":"+ms+":"+sc
        print(x)
        return 
 
    
    def today(self):
        #Clock doesnt know calenders 
        #just do this
        self.now()
        
    
    ## testing & debug ##
    
    def _setNtest(self,x ):
        self._cal_ntest_offset = x
        return

    def _test_numerics(self, iterations=5, retres=False):
    
        # test timing, sync & numeric calculations of:
        # seconds, milliseconds, microseconds
        # using
        # delay(),uptime(),millis(),micros()
        
        results = []
        
        for i in range(iterations):
            t= self.millis()
            tmc = self.micros()
            results.append(tmc)
            self.uptime()
            print(t,round(t/1000));#print(t/1000)
            # ok below!
            print(tmc,tmc/1000,tmc/1000000) # microseconds,ms,sec
            print(tmc,round(tmc/1000),round(tmc/1000000)) # microseconds,ms,sec
            #print()
            print()
            delay(1000)
        
        print();print("test millis()")
        print();print("count in 1 ms interval")
        #up_monotime = self.getMonotime() - self.init_monotime
        print()
        self.uptime()
        print()
        print("time.sleep(0.001) ")
        
        for i in range(16):
            print (self.millis()) 
            time.sleep(0.001)
        
        print()
        self.uptime()
        print()
        print("delay(1)")
        
        for i in range(16):
            print (self.millis()) 
            delay(1)
            
        print()
        print();print("test clock function micros()")
        print("uptime in microseconds");print()
        print();print("count up 1 ms intervals")
        #up_monotime = self.getMonotime() - self.init_monotime
        print()
        self.uptime()
        print()
        print("time.sleep(0.001) numeric errors on msec")
        
        for i in range(16):
            print (self.micros()) 
            time.sleep(0.001)
        
        print()
        self.uptime()
        print()
        print("delay(1) numeric ok on the msec")
        
        for i in range(16):
            print (self.micros()) 
            delay(1)
            
        print()
        
        if (retres == True):
            return results
        
        return

#/**********************************************/

class SystemClock(Clock):
    # OS/HW system Clock functions & timestamping
    def __init__(self):
        
        Clock.__init__(self)
        Clock.setCalType(self,'gregorian') # or utc-gregorian
        
        self._name = "System Clock"
        self._vers = "v0.01.12a"
        self._desc = "System Clock Class - "+str(self._vers)
        
        # system does not use zero based
        # but uptime does so will only affect uptime, 
        # cal stuff uses system datetime functions
        # Clock.setZeroBasedFormatOff()
     
        # monotime is ONLY ONE source 
        # calls back to primordal base Clock class
        #self._init_monotime =  Clock.monotime(self)
        self._init_monotime =  self.getMonotime() # calls Clock anyway 
        self._init_time = self.getSystemTime() #init time NEVER changes once set
        self._init_time_offset = 0 # offset to sync w/ external clock
        #self._init_monotime_offset = 0 # same for monotonic time
        
        #self._start_unix_epoch = 1969*365*24*60*60 # clock uses zero based  
        self._start_epoch_time = 0.0 # use UTC formatting for printout
        
     
        self._current_cal_type ='gregorian'# 'utc-gregorian'
            
        self._cal_days_in_year = 365 #365.24
        self._cal_hours_in_day = 24
        self._cal_minutes_in_hour = 60
        self._cal_seconds_in_minute = 60
        
        self._cal_months_in_year = 12 # or 
        self._cal_days_in_month = 30.44
        #elf._cal_weeks_in_month = varies
        self._cal_days_in_week = 7
        
        # not in Clock
        # set for this instance
        self._cal_timezone=""
        self._cal_tz = ""
        self._cal_utc_offset = 0 #time.strftime('%z')
        self._cal_dst = None #unknown or True/False 
        
        # the locale time set on underlying system
        self._sys_timezone = ""
        self._sys_tz = ""
        self._sys_utc_offset = 0
        self._sys_dst= None
        
        # uptime state ( NOT Timekeeping from calendar)
        self._up_monotime = 0
        self._up_days = 0
        self._up_hours = 0
        self._up_minutes = 0
        self._up_seconds = 0
        self._up_millisec = 0
        self._up_microsec = 0
        
        # calendar state 
        # init to unix epoch start
        self._cal_year = 1
        self._cal_month = 1
        self._cal_day = 1
        self._cal_day_in_year = 1
        self._cal_week = 1
        self._cal_day_of_week = 3 # 1970-01-01 is thursday
        
        self._cal_hours = 0
        self._cal_min = 0
        self._cal_sec = 0
      
        

    def getSystemTime(self):
        # override from Clock base class
        # return fpoint
     return time.time()


    #def setTimeZone(self,tz):
        #FUTURE
        # sets for everything!
        # currently only use what is already set by
        # the underlying system same as local 
        # other is utc ztime
    #   return
    
    
    def _initSystemTimezone(self):
        # setup timezone parameters
        # to the locale of underlying system
        self._sys_timezone = ""
        self._sys_tz = ""
        self._sys_utc_offset = 0
        self._sys_dst= None
        
        self._sys_timezone=time.strftime('%Z')
        self._sys_tz=time.strftime('%Z')
        self._sys_utc_offset = time.strftime('%z')
        
        
    def _updateCal(self):
        # sysclock override from Clock._updateCal
        # depends on current format selected
        # in local timezone as set by system

      if ( self._timestamp_format == 'default'):
          #default
          dt = datetime.now()
          self._cal_timezone=time.strftime('%Z')
          
      elif (self._timestamp_format == 'iso-local'):
           #mk, ok
           dt = datetime.now()
           self._cal_timezone=time.strftime('%Z')
     
      elif (self._timestamp_format == 'iso-utc'):
 
         dt = datetime.now()
         dt.isoformat() 
         
         self._cal_tz="UTC"
         self._cal_timezone="UTC"
     
         self._cal_utc_offset = time.strftime('%z')
      
          
      tt = dt.timetuple()
      # numerics
      weekday=tt[6]
      day_in_year = tt[7] 
    
      # last but now leastca
      self._cal_leapyear = self.isLeapYear(dt.year)
      #TEST, OK 2022-12-18 V0.06
      #self._cal_leapyear = self.isLeapYear(2020)
      
      if (self._cal_leapyear==True):  
          self._cal_days_in_year = 366
      else:
           self._cal_days_in_year = 365
      
      # update days in current month
      modays = calendar.monthrange(dt.year, dt.month)[1]
      self._cal_days_in_month = modays
       
     # dst=self._cal_dst=
      if (tt[8] <= 0 ): # -1 ? , 0 no, 1 yes
          # is not or unknown
          self._cal_dst = False
      else:
          self._cal_dst = True

      ## easier
      self._cal_year = dt.year
      self._cal_month = dt.month   
      self._cal_day= dt.day
      self._cal_day_in_year = day_in_year
      #self._cal_week = 
      self._cal_day_of_week = weekday
     
      self._cal_hours = dt.hour
      self._cal_min =  dt.minute
      self._cal_sec = dt.second
      self._cal_microsec = dt.microsecond
      self._cal_millisec = int(dt.microsecond/1000) #chop fp not round
      
      return
    
    #mk
    def getTimestampStr(self):

        # easy, work right from tuple
        y,mo,dy,h,m,s,res= self.getTimestamp()
        
        ys = str(y).zfill(4)
        #ds = str(d).zfill(2) # total days into year from uptime
        hs = str(h).zfill(2)
        ms = str(m).zfill(2)
        sc = str(s).zfill(2)
        
        mostr=  str(mo).zfill(2)
        dystr  = str(dy).zfill(2)

        ddsep = self._timestamp_date_sep # date digit sep
        dtsep = self._timestamp_dt_sep
        tmsep = self._timestamp_time_sep #mk NEW 9/10
        resep = self._timestamp_res_sep
        
        # current resolution on tail end if any is used
        if (self._timestamp_res == 'micro'):
            resz = str(res).zfill(6)
        elif (self._timestamp_res == 'milli'):
            resz = str(res).zfill(3)
        elif (self._timestamp_res == 'none'):
            resz = ""
            #v0.23
            resep = ""
        else:
            resz = ""
            #0.23
            resep = ""
  
        tsz = "" # for derived class 
        
        if (self._timestamp_format == 'default'):
                 
            #mk new tmsep
            tsz =  ys + ddsep + mostr + ddsep + dystr + dtsep + \
                      hs + tmsep + ms + tmsep + sc + resep + resz
                     
        if ( self._timestamp_format == 'iso-local'):
            
            # iso local 
            # basic iso-8601 formatting but not offset from UTC
            
            #mk  time sep char
            tsz =  ys + ddsep + mostr + ddsep + dystr + dtsep + \
                      hs + tmsep + ms + tmsep + sc + resep + resz 
  
        if (self._timestamp_format == 'iso-utc'):
            
            # iso utc
            #use utc offset 
            uf = self._cal_utc_offset 
        
            #*THIS ONE
            #mk
            #new 9/15 ck for compressed mode
            if self._timestamp_compressed == True:
                # remove delimiters form offset
                # have to do this way strings are not mutable
                uf1 = uf.replace('+','')
                uf2 = uf1.replace('-','')
                uf3 = uf2.replace(':','')
                uf = uf3
                
            #mk new tmsep
            tsz =  ys + ddsep + mostr + ddsep + dystr + dtsep + \
                      hs + tmsep + ms + tmsep + sc + resep + resz +uf

        return tsz
    
    
    ## Clock base class overrides ##

    def epoch(self):
        # keep it simple, works
        print(datetime.utcfromtimestamp( self._start_epoch_time ))
         
        
    def time(self):
        # HH:MM:SS
        self._updateCal()
        
        hh = str(self._cal_hours).zfill(2)  #str(up[2]).zfill(2)
        mm = str(self._cal_min).zfill(2)
        sc = str(self._cal_sec).zfill(2)  #str(up[4]).zfill(2)
        tm = hh+":"+mm+":"+sc
        
        print(tm)
        return
    
    
    def date(self):
        # YYYY-DD-MM
        self._updateCal()
        
        yyyy=str(self._cal_year).zfill(4)
        mm = str(self._cal_month).zfill(2)
        dd = str(self._cal_day).zfill(2)
        d=yyyy+"-"+mm+"-"+dd
        print(d)
        return
  
    
    def now(self):
        
      self._updateCal() #mk 9/14
      
          # in local timezone as set by system
      if (self._timestamp_format == 'iso-local'):
            now = datetime.now().replace(microsecond=0).isoformat(' ')
            now = now + " "+ self._cal_timezone
      #mk 
      # for now keep usual
      # use utc format only for timestamping related functions
      # decide on this format later 
      
      elif  (self._timestamp_format == 'iso-utc'):
            # utc_dt = datetime.now(timezone.utc) 
            
            now = datetime.now().replace(microsecond=0).isoformat(' ')
            #mk 9/14
            # override updateCal setting
            tz=time.strftime('%Z')
            now = now + " "+ tz
            
            #WAS
            #now = now + " "+ self._cal_timezone
            # now = datetime.now(timezone.utc).replace(microsecond=0).isoformat(' ')
            # now = now[0:19]+ " UTC" #"Z"
            # #dt = datetime.now(timezone.utc)
    
      else: #fall back to local system setting
           now = datetime.now().replace(microsecond=0).isoformat(' ')
           now = now + " "+ self._cal_timezone

      print(now)
      return
  
    
    def today(self):
        
        self._updateCal()
        
        # dayname=self.cal_weekday_en[self._cal_day_of_week]
        # day = str(self._cal_day).zfill(2)
        
        yyyy=str(self._cal_year).zfill(4)
        mo = str(self._cal_month).zfill(2)
        dd = str(self._cal_day).zfill(2)
        
        hh = str(self._cal_hours).zfill(2)  #str(up[2]).zfill(2)
        mm = str(self._cal_min).zfill(2)
        sc = str(self._cal_sec).zfill(2)  #str(up[4]).zfill(2)
        tm = hh+":"+mm+":"+sc
        
        if (self._timestamp_format == 'iso-local'):
            now = datetime.now()
            tzone = self._cal_timezone
            
        elif  (self._timestamp_format == 'iso-utc'):
            #mk keep local for now
            # for now only iso utc for timestamps
            
            now = datetime.now()
            #mk 9/14
            # use sys locale not UTC
            tzone=time.strftime('%Z')
           # tzone = self._cal_timezone
        else:
            now = datetime.now()
            
            tzone = self._cal_timezone
        # want day name in timestamp setting for "locale" 
        day_name = now.strftime("%A")
        day_name_short = now.strftime("%a")
        month_name=now.strftime("%B") # long name
        month_name_short = now.strftime("%b")
            
        tdsz = day_name_short +" "+ month_name_short+\
            " " +dd+" "+yyyy+" "+ tm + " "+ tzone
          
        print(tdsz)


    ## timestamp overrides ##
    # the rest follow along 
    
    def getTimestamp(self):
      # override Clock function
      # starts here
      # the other timestamp functions call this one
      # y,mo,dy,h,m,s,res= self.getTimestamp()
      # based on system settings
      
      self._updateCal() #  get date/time state
      
      # these are from Clock uptime  
      #micros = self._up_microsec
      #millis = self._up_millisec
      
      # SystemClock uses the res attached 
      # date/time with calendar attributes
      micros = self._cal_microsec
      millis = self._cal_millisec
        
      if (self._timestamp_res == 'micro'):
            res = micros
      elif (self._timestamp_res == 'milli'):
            res = millis
      else:
            res = 0 # since numeric zero if no resolution

      yr = self._cal_year #= dt.year
      mo = self._cal_month# = dt.month   
      dy = self._cal_day#= dt.day
     
     
      h = self._cal_hours #= dt.hour
      m = self._cal_min #=  dt.minute
      s = self._cal_sec# = dt.second
   
      return (yr,mo,dy,h,m,s,res)

    
    def getTimestampFp(self):
        # and the fp variant
        if (self._timestamp_format == 'iso-local'):
            now = datetime.now()
            tzone = self._cal_timezone
            
        elif  (self._timestamp_format == 'iso-utc'):
            now = datetime.now(timezone.utc)
            tzone = "UTC"
        else:
            now = datetime.now()
            tzone = self._cal_timezone
       
        #datetime.now().timestamp()
        return(now.timestamp())
        

    def isLeapYear(self,year):
        # leap year ck algo
        # leapyears = [2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060]
        # notleapyears = [2019,2021,2022,2023,2025,2026]
        #v0.18 WORKS
        
        leap = False
        
        if year%4 ==0:
            if year%100 != 0:
                leap = True
            else:
                if year%400 == 0:
                    leap = True
        else:
            leap = False
        
        return leap


#/**********************************************/

class WorldClock(Clock):
    # for system
    def __init__(self):
        Clock.__init__(self) #base class
        Clock.setCalType(self,'gregorian') # or utc-gregorian
        
        self._name = "World Clock"
        self._vers = "v0.01.14a"
        self._desc = "World Clock - "+str(self._vers)
        self._about = "World clock"+\
                      "NTP/UTC global reference time\n"
         
        self._init_monotime =  self.getMonotime() # call back to Clock anyway
        
        #self._init_time = self._systemTime() # init times  NEVER changes
        #self._init_time_offset = 0 # offset to sync w/ external clock
        #self._init_monotime_offset = 0 # same for monotonic time
        
        # note python standard lib is time.gmtime(0) across all platforms
        self._start_epoch_time = 0.0 # UTC reads this as 1970-01-01....
        self._init_ntp_time = 0.0 # will be initialized in UTC
        self._current_ntp_time = 0.0
        self._ntp_time_offset = 0.0 # is delta from current utc
        
        self._init_done_ok = False #mk 9/12 use this now
          
        #self._start_epoch_time = Clock._start_unix_epoch
        #self._epoch_days_in_year = 365
        
        # UNIX/UTC
        self._current_cal_type ='gregorian'# 'utc-gregorian'
            
        self._cal_days_in_year = 365 #365.24
        self._cal_hours_in_day = 24
        self._cal_minutes_in_hour = 60
        self._cal_seconds_in_minute = 60
        
        self._cal_months_in_year = 12 # or 
        self._cal_days_in_month = 30
        #elf._cal_weeks_in_month = varies
        self._cal_days_in_week = 7
        
        # not in Clock
        # set for this instance
        self._cal_timezone="UTC"
        self._cal_tz = "UTC"
        self._cal_utc_offset = 0 #time.strftime('%z')
        self._cal_dst = None #unknown or True/False 
        
        # the locale time set on underlying system
        self._sys_timezone = ""
        self._sys_tz = ""
        self._sys_utc_offset = 0
        self._sys_dst= None
        
        # uptime state ( NOT Timekeeping from calendar)
        self._up_monotime = 0
        self._up_days = 0
        self._up_hours = 0
        self._up_minutes = 0
        self._up_seconds = 0
        self._up_millisec = 0
        self._up_microsec = 0
        
        # calendar state 
        # init to unix epoch start
        self._cal_year = 1
        self._cal_month = 1
        self._cal_day = 1
        self._cal_day_in_year = 1
        self._cal_week = 1
        self._cal_day_of_week = 3 # 1970-01-01 is thursday
        
        self._cal_hours = 0
        self._cal_min = 0
        self._cal_sec = 0
        
        # other parameters

        self._ntp_delta_threshold = 0.050 # 50ms ntp stack cant get much better
        self._ntp_avg_adj = 0.0
        self._ntp_last_delta_adj = 0.0
        
        #self._init_process_flag = False # running init?
        
    
    def _get_new_ntp_time(self):
               
        # get NTP time from global server(s) 
        
        """
        orig_time - local time that NTP packet was sent to NTP server by client
        recv_time - time at the server when the NTP server receives packet 
        tx_time  -  time at server when server replies to request
        dest_time - local time the client receives reply from server
      
        """  
        """
           0.north-america.pool.ntp.org
           1.north-america.pool.ntp.org
           2.north-america.pool.ntp.org
           3.north-america.pool.ntp.org
        """
        
        #FUTURE multiple attempts
        
        #for i in range(2):
      
        try:
           
           client = ntplib.NTPClient()
           
           #FUTURE
           # add config 
           server = 'pool.ntp.org'
           #server =  '2.north-america.pool.ntp.org'
           #server =  '1.north-america.pool.ntp.org'
           
           ntp_time_when_req_sent = self._getTimeNow()
           
           response = client.request(server)#, version=3)
           # as of v0.09+
           # fetch current ntp/utc time this way ONLY!
           ntp_time_when_rsp_rcvd = self._getTimeNow()
           
           #current_ntp_time = self._getTimeNow()
           #print("response packet:")
           #print("offset :", response.offset)
           #print("delay  :", response.delay)
           #print()
       
           #get local system TIME ZONE code
           #local_system_time=time.time()
           
           # this is underlying system local tz
           #tz_string = datetime.now().astimezone().tzname()
           #print("system local time (" + tz_string + ") :",\
           #datetime.fromtimestamp(local_system_time))
           #print("system local time (UTC) :", datetime.utcfromtimestamp(local_system_time))
           #print()
           
           #now?  was #FUTURE for debug
           if self.debugIsOn():
                #print("orig_time:", datetime.utcfromtimestamp(response.orig_time))
                # same as utc not local timeprint("orig_time :",datetime.utcfromtimestamp(response.orig_time))
                print("UTC")
                print("orig_time:", datetime.utcfromtimestamp(response.orig_time))
                print("recv_time:", datetime.utcfromtimestamp(response.recv_time))
                print("tx_time  :", datetime.utcfromtimestamp(response.tx_time))
                print("dest_time:", datetime.utcfromtimestamp(response.dest_time))
                print()
                print("LOCAL TIMEZONE")
                print("orig_time:", datetime.fromtimestamp(response.orig_time))
                print("recv_time:", datetime.fromtimestamp(response.recv_time))
                print("tx_time  :", datetime.fromtimestamp(response.tx_time))
                print("dest_time:", datetime.fromtimestamp(response.dest_time))
              
           # for easy reading
           orig_time = response.orig_time
           recv_time =response.recv_time
           tx_time = response.tx_time    
           dest_time = response.dest_time
           
           #and the round trip time is
           
           send_time = recv_time - orig_time
           return_time = dest_time - tx_time
           roundtrip_time = send_time + return_time
           avg_oneway_time = roundtrip_time/2
           
           # tx time was in the current time in past when the packet left
           # bring it into its future that is now
           # by adding the travel time to here (geo) and now!
           ntp_reference_time = tx_time + (avg_oneway_time)
       
           #print("NTP epoch start        (UTC):", \
           #  datetime.utcfromtimestamp(self._start_epoch_time))
           #print()
           
           if self.debugIsOn():   #isDebugOn()):
               # too early -- print("WorldClock NTP time (sent) (UTC):", datetime.utcfromtimestamp(ntp_time_when_req_sent))
               print("NTP reference time  (UTC)       :", datetime.utcfromtimestamp(ntp_reference_time))
               print("WorldClock NTP time (rcvd) (UTC):", datetime.utcfromtimestamp(ntp_time_when_rsp_rcvd))
               print()
               
           # this time is from ntp module
           # and is system time in UTC floating point, dont use it, doesnt apply
           #print("WorldClock NTP time (resp) (UTC):", datetime.utcfromtimestamp(recv_time))
           
           delta_time = ntp_reference_time - ntp_time_when_rsp_rcvd
           
           x = math.modf(delta_time)
           dt_millis = int(x[0]*1000)
           dt_micros = int(x[0]*1000000)
         
           # return delta time NOW closest to measurement
           return ntp_reference_time,delta_time,True
       
        except:
          #print()
          #print("World clock unable to connect to NTP global server!")
          print("Unable to connect to NTP server!")
          #print("Unable to connect to NTP global server!")
          
          #print()
          
          return 0,0,False # true     #(0.000000000000001,0.000000000000001)

    
    def _adjust_ntp_time(self):
        
        #print()
        print("Resynchronizing world clock...")
        #print()
        
        # get current ntp utc 
        current_global_utc_time, delta_ntp, was_ntp_ok = self._get_new_ntp_time()
       
        if (was_ntp_ok == True):
            print("Connection to NTP server OK!")
            
        # adjust time
         #a=0
            if self.debugIsOn():
                print()
                #print("Current Delta")
                #print()
                #print()
                #print("FP time")
                #print("current",self._current_ntp_time )
                #print("global ", current_global_utc_time)
               
                print("delta:",delta_ntp,"(fp)") #d
                   
                x = math.modf(delta_ntp)
                dt_millis = x[0]*1000
                dt_micros = x[0]*1000000  
                print("delta",int(dt_millis),"(ms)")
                #print()
                    
       
            delta_adj = delta_ntp
            
            if self.debugIsOn():
            #if self.isDebugOn():      
                print("Adjusting offset...") #= "#,self._ntp_time_offset)
                #print()
                print("Previous offset:",self._ntp_time_offset)
            
            #*THIS
            if self.debugIsOn():
                print("Checking delta threshold: "+"||"+str(round(delta_adj,5))+"|| < "\
                 +str(round(self._ntp_delta_threshold,5 )))     
            else:
                print("Checking delta threshold...")
            #print("Checking delta threshold: "+"||"+str(round(delta_adj,10))+"|| < "\
            #      +str(round(self._ntp_delta_threshold,10 )))     
                
            # ck threshold  
            if (abs(delta_adj) > self._ntp_delta_threshold ):
                  #print()
                  print("Above threshold. Not updating time")
                  #print("Above threshold. Not updating time from NTP!")
                  #print()
                  #print("delta above threshold. Not updating time from NTP")
                  #print()
            else:
                #print()
                print("Within range. Updating...")
                #print("delta within range. Updating...")
                #print()
                self._ntp_time_offset += delta_adj
                self._ntp_last_delta_adj = delta_adj
                self._recalc_ntp_time()
 
                if self.debugIsOn(): #isDebugOn():      
                    print("new offset:",self._ntp_time_offset)
                    #print()
                    # and update time state
                     
                # get a read on possible results
                # this is not an update

                delay(1023) #cute aka base 2
                
                print("Get time check...")
                #print()
                current_global_utc_time, delta_after, was_ntp_ok = self._get_new_ntp_time()
                
                if (was_ntp_ok == True):
                    
                    # this was here for testing purposes
                    # not sure if a valid comparison
                    # take out for production
                    # was worse possibly or ntp usual timeouts etc???
                    if abs(delta_after) > abs(delta_ntp): #+0.20*delta_ntp):
                        # fetch again to get better reading
                        delay(1050)
                        current_global_utc_time, delta_after, was_ntp_ok = self._get_new_ntp_time()
                        if self.debugIsOn():
                            if was_ntp_ok == True:
                             print("Recheck delta after adjustment... ",end='')
                                # print()
                             x = math.modf(delta_after)
                             dt_millis = x[0]*1000
                             dt_micros = x[0]*1000000
                             print("delta:",int(round(dt_millis,1)),"(ms)",end='')
                             if (self.debugIsOn):
                                 print(round(delta_after,6),"(fp)")
                             print() #nl 
                      
                    else: 
                        #if (was_ntp_ok == True):
                        #print()
                            if self.debugIsOn():
                                # was ok adj
                                print("After adjustment... ",end='')
                                # print()
                                x = math.modf(delta_after)
                                dt_millis = x[0]*1000
                                dt_micros = x[0]*1000000
                                print("delta:",int(round(dt_millis,1)),"(ms)",round(delta_after,6),"(fp)")
                                #print("After adjustment... ")
                                #print("delta:",int(dt_millis),"(ms)",round(delta_after,6),"(fp)")
                                #print("delta:",round(delta_after,6),"(fp)")
                                #print()
        else:
            
            #if self.debugIsOn()
            #print()
            print("Not adjusting time. No NTP server connection!")
            #print()
            
        return
   

    def _recalc_ntp_time(self):
        #more accurate desc than 
        #update sounds like a server fetch
        self._current_ntp_time = self._init_ntp_time + self.getUptimeFp()\
            + self._ntp_time_offset 
      
     
 
    def _getTimeNow(self):
        # return the current time in floating point
        # has to be recalc 1st
        # the is the ONLY function to use to 
        # access the current ntp/utc time
        # don't access the memory location directly
        self._recalc_ntp_time()
        return self._current_ntp_time
    
    
    def _init_ntp_clock(self):
        
        # set flag for resync
        #self._init_process_flag = True
        
        print();print()
        print("WorldClock version: "+str(self.getVersion()))
        print()
        if  self._init_done_ok == False:
        #if self._current_ntp_time == 0:
          print("Starting up...")
        else:
            print("Re-initializing..")
            
        print("Current WorldClock NTP (UTC) time:", \
                 datetime.utcfromtimestamp(self._getTimeNow()))
        #print("WorldClock version: "+str(self.getVersion())+" starting up...")
        #print()
        print("Begin initialization from global NTP system...")
        #print()
        print("Checking NTP connection...")
        #print()
        
        now_ntp_time,_,ok = self._get_new_ntp_time()
        
        if (ok == False):
            
            #print()
            if self._init_done_ok == False:
              print("WorldClock not initialized!")# No NTP server connection. ")
              print()
            else: # was re-init?
              print("WorldClock not re-initialized!")
              
            return # just bail out
            
        # for now manual only?
        # dont use resync too complicated to flag stuff?
         
        else: #ok
            print("Connection established...")
            #print()
            print("Initializing UTC time from NTP reference signal...")
            
            self._ntp_time_offset = 0.0
            self._init_ntp_time = now_ntp_time #current ntp_reference_time 
            # well, maybe ok, this is an init! otherwise dont directly update
            self._current_ntp_time = now_ntp_time # after is offset
        
            sync_ok = False 
            nbr_no_connects = 0 # # of no connects
            
            isyncs = 2
            
            for i in range(isyncs):
                #print()
                print("Synchronization phase #",i+1," ",end='')
                #print()
             
                current_global_utc_time, delta_ntp, was_ntp_ok = self._get_new_ntp_time()
               
                if (was_ntp_ok == True):
                    
                    # adjust time
                    if self.debugIsOn(): 
                            #print()
                            #print("Current Delta")
                            #print()  
                            print("delta:",delta_ntp,"(fp)") #d
                                         
                    delta_adj = delta_ntp
                                
                    if self.debugIsOn():
                        #print()
                        print("Adjusting offset...") #= "#,self._ntp_time_offset)
                        #print()
                        print("previous offset:",self._ntp_time_offset)
                    
                    self._ntp_time_offset += delta_adj  
                    
                    if self.debugIsOn(): 
                            print("     new offset:",self._ntp_time_offset)
                            #print()
                            # AND UPDATE TIME STATE
                       
                    self._ntp_last_delta_adj = delta_adj
                    self._recalc_ntp_time()
                    sync_ok = True
                    self._init_done_ok = True #mk new 9/12
                    delay(250)
                    print("OK")
                    self.delay(1024)
                    
                else:
                    #dont set here could be a re-init
                    #sync_ok = False
                    #self._init_done_ok = False
                    nbr_no_connects +=1
                    print("No NTP connection!")
                # out of the loop
                # did either phase ok
                
            if sync_ok:
                #this is the last phase i+1
                
                #skip the verbage?
                #print("Current WorldClock NTP (UTC) time:", \
                # datetime.utcfromtimestamp(self._getTimeNow()))
                #print();
                self.delay(500)
                #print()
                print("Synchronization phase #",isyncs+1)
                #print()
                #print("Initiating Resync....")
                #print()
                
                # attemp resync to get better result
                self.resync()
                #print() # put below in resync
                #print("Current WorldClock NTP (UTC) time:", \
                # datetime.utcfromtimestamp(self._getTimeNow()))       
       
            
            if (sync_ok == True and nbr_no_connects == 0):
              print("Initialization done!")
            else: 
              print("Initialization done (incomplete)")
          
         
        print()
        return
      
    
    def initialize(self):
        # can call repeatedly
        # does 3 stage sync using current UTC stored
        self._init_ntp_clock()
    
    
    def init(self):
        self.initialize()
    
    
    def reset(self):
        # reset UTC to unix epoch start
        # changed for now, dont init
        # then init, does not reset uptime!!
        self._start_epoch_time = 0.0 # UTC reads this as 1970-01-01....
        self._init_ntp_time = 0.0 # will be initialized in UTC
        self._current_ntp_time = 0.0
        self._ntp_time_offset = 0.0 # is delta from current
        # would start init from scratch also
        self._init_done_ok = False
        #self._init_ntp_clock()
        return
        
    
    def resync(self,show=True):
        # resync to global ntp/utc servers
        # can be called frequently
        if self._init_done_ok == False:
        #if self._current_ntp_time == 0:
          print("Never initialized. Not resyncing!")
          return
        #else:
        #    print("Re-initializing..")
            
        #FUTURE show=? output progress or not
        
        self._adjust_ntp_time()
        # self._update_ntp_time()
        self._recalc_ntp_time() # just to make sure
        print("Current WorldClock NTP (UTC) time:", \
                datetime.utcfromtimestamp(self._getTimeNow()))   
        return
    
    def getDeltaThreshold(self):
        return self._ntp_delta_threshold
    
    def setDeltaThreshold(self,delta):
        # delta is in milliseconds
        delta = abs(delta) # just fix it 
        delta = delta/1000 #in milliseconds
        
        if delta > 0:
         self._ntp_delta_threshold = delta
        else:
         print("Delta threshold needs to be > 0")
         
    def getDelta(self):
        #shortfome
        return self.getDeltaThreshold()
    
    def setDelta(self,delta):
        #shortform
        self.setDeltaThreshold(delta)
        
    ## base class Clock overrides ##
    
    #*here
    #Worldclock
    def _updateCal(self):
      #WorldClock override this is
      #mk recked this, is ok 2023-09-10
      #as of dev v0.09 dont access time directly 
      #self._update_ntp_time()
      #now_ntp = self._current_ntp_time 
      
      #if 
      # this is the fpoint time
      # from THIS WorldClock private function
      
      now_ntp = self._getTimeNow()
      
      dt=datetime.utcfromtimestamp(now_ntp)
      
      # or datetime.datetime.utcnow()
      # NO! from WorldClock own representation 
      # of unix time starting at beginning of epoch
      #HET, fp_utc_now=datetime.now(timezone.utc).timestamp()
      
      tt = dt.timetuple()
      # numerics
      weekday=tt[6] # is weekday offset from zero? yes.
      day_in_year = tt[7]  
    
      # timezone - worldclock set at init never changes
      
      # last but now least
      self._cal_leapyear = self.isLeapYear(dt.year)
      #TEST, OK 2022-12-18 dev V0.06
      #self._cal_leapyear = self.isLeapYear(2020)
      
      if (self._cal_leapyear==True):  
          self._cal_days_in_year = 366
      else:
           self._cal_days_in_year = 365
      
      # update days in current month
      self._cal_days_in_month= calendar.monthrange(dt.year, dt.month)[1]

      # is init-ed but set anyway
      self._cal_dst = False
     
      self._cal_year = dt.year
      self._cal_month = dt.month   
      self._cal_day= dt.day
      self._cal_day_in_year = day_in_year
      #self._cal_week = 
      self._cal_day_of_week = weekday
     
      ## could use previous algo also if better
      
      self._cal_hours = dt.hour
      self._cal_min =  dt.minute
      self._cal_sec = dt.second
      
      # want to parse these out from
      # floating point current ntp time
      
      # calculate this way 
      f,n = math.modf(now_ntp)
      int_milli=f*1000
      rem_int_milli =int(int_milli)
    
      #f,n = math.modf(now_ntp)
      int_micro=f*1000000
      rem_int_micro =int(int_micro)
        
      self._cal_microsec = rem_int_micro
      self._cal_millisec = rem_int_milli ##int(dt.microsecond/1000) #chop fp not round
      
      # for additional formatting 
      # return fp nowtime from THIS current update to keep in sync
      return now_ntp
    
    
    def isLeapYear(self,year):
        #dev-v0.18 WORKS
        leap = False
        if year%4 ==0:
            if year%100 != 0:
                leap = True
            else:
                if year%400 == 0:
                    leap = True
        else:
            leap = False
        return leap
    
    
    def getTimestamp(self):
      
      # override Clock function
      # starts here
      # the other timestamp functions call this one
      # y,mo,dy,h,m,s,res= self.getTimestamp()
      # based on system settings
      
      self._updateCal() #  get date/time state
      
      # these are from Clock uptime  
      #micros = self._up_microsec
      #millis = self._up_millisec
      
      # WorldClock uses the res attached to read of 
      # date/time with calendar attributes
      micros = self._cal_microsec
      millis = self._cal_millisec
        
      if (self._timestamp_res == 'micro'):
            res = micros
      elif (self._timestamp_res == 'milli'):
            res = millis
      else:
            res = 0 # since numeric zero if no resolution

      yr = self._cal_year #= dt.year
      mo = self._cal_month# = dt.month   
      dy = self._cal_day#= dt.day
     
     
      h = self._cal_hours #= dt.hour
      m = self._cal_min #=  dt.minute
      s = self._cal_sec# = dt.second
   
      return (yr,mo,dy,h,m,s,res)
  
    
  
    def getTimestampFp(self):
        
       #self._update_ntp_time()
       #return self._current_ntp_time
       return (self._getTimeNow())

    
    def epoch(self):
         #print("NTP epoch start        (UTC):", \
         # UTC starts counting at ZERO, that is UTC 1970-01-01...
         print(datetime.utcfromtimestamp(self._start_epoch_time))
     
    
    def time(self):
        # time in the currend day
        # HH:MM:SS
        (yr,mo,dy,h,m,s,res)=self.getTimestamp()
        
        hh = str(h).zfill(2)
        mm = str(m).zfill(2)
        ss = str(s).zfill(2)
        tm = hh+":"+mm+":"+ss
        print(tm)
        return 
    
   
    def date(self):
        # current year up
        # YYYY-DD-MM
        ts = self.getTimestamp()
        yyyy=str(ts[0]).zfill(4)
        mm = str(ts[1]).zfill(2)
        dd = str(ts[2]).zfill(2)
        d=yyyy+"-"+mm+"-"+dd
        print(d)
        return

     
    def now(self):
        
        ntp_now = self._getTimeNow()
        
        now = datetime.utcfromtimestamp(ntp_now ).\
               replace(microsecond=0).isoformat(' ')

        now = now + " " + self._cal_timezone
        
        # print( datetime.utcfromtimestamp(self._current_ntp_time ).\
        #       replace(microsecond=0).isoformat(' '))
        print(now)
       
        
    def today(self):
        
        # self._getTimeNow() # returns fp
        fpnow=self._updateCal()
        
        # numerics here are from the
        # tt struct ie. tt = dt.timetuple() 
        yyyy=str(self._cal_year).zfill(4)
        mo = str(self._cal_month).zfill(2)
        dd = str(self._cal_day).zfill(2)
        
        hh = str(self._cal_hours).zfill(2)  #str(up[2]).zfill(2)
        mm = str(self._cal_min).zfill(2)
        sc = str(self._cal_sec).zfill(2)  #str(up[4]).zfill(2)
        tm = hh+":"+mm+":"+sc
        
        # world clock has only ONE timezone
        # use SystemClock for locale & UTC both
        
        dt=datetime.utcfromtimestamp(fpnow)
        ts = dt.timetuple()
        # now stored cal info so  easiest way to string format
        # ISO-8601
        iso_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', ts)
        iso_utc_short=utc=time.strftime('%Y%m%dT%H%M%SZ', ts)
        
        #s = time.strftime("%a, %d %b %Y %H:%M:%S", gmtime())
        
        day_name = time.strftime("%A",ts)
        day_name_short = time.strftime("%a",ts)
        month_name=time.strftime("%B",ts) # long name
        month_name_short = time.strftime("%b",ts)
       
        tzone = "UTC"

        # day_name = now.strftime("%A")
        # day_name_short = now.strftime("%a")
        # month_name=now.strftime("%B") # long name
        # month_name_short = now.strftime("%b")
        
        tdsz = day_name_short +" "+ month_name_short+\
            " " +dd+" "+yyyy+" "+ tm + " "+ tzone
                    
        print(tdsz)
        return
    
    
    #*here
    def getTimestampStr(self):
       
        #WorldClock override from Clock 
        #mk 9/14,15
        
        # easy, work right from tuple
        y,mo,dy,h,m,s,res= self.getTimestamp()
        
        ys = str(y).zfill(4)
        #ds = str(d).zfill(2) # total days into year from uptime
        hs = str(h).zfill(2)
        ms = str(m).zfill(2)
        sc = str(s).zfill(2)
        
        mostr=  str(mo).zfill(2)
        dystr  = str(dy).zfill(2)

        # micros = str(self._up_microsec).zfill(6)
        # millis = str(self._up_millisec).zfill(3)

        ddsep = self._timestamp_date_sep # date digit sep
        dtsep = self._timestamp_dt_sep
        tmsep = self._timestamp_time_sep #mk NEW 9/10
        resep = self._timestamp_res_sep
        
        # current resolution on tail end if any is used
        if (self._timestamp_res == 'micro'):
            resz = str(res).zfill(6)
        elif (self._timestamp_res == 'milli'):
            resz = str(res).zfill(3)
        elif (self._timestamp_res == 'none'):
            resz = ""
            #v0.23
            resep = ""
        else:
            resz = ""
            #0.23
            resep = ""
        

        if ( self._timestamp_format == 'iso-local'):

            #mk iime sep char
            tsz =  ys + ddsep + mostr + ddsep + dystr + dtsep + \
                      hs + tmsep + ms + tmsep + sc + resep + resz #+ uoffset
                      
        elif (self._timestamp_format == 'iso-utc'):
                 
      
                  if (self._timestamp_use_ztail == True):
                   
                    #mk new tmsep
                    # compressed leave same ending
                    tsz =  ys + ddsep + mostr + ddsep + dystr + dtsep + \
                        hs + tmsep + ms + tmsep + sc + resep + resz + "Z" 
                        
                  else:
                      #9/15 compressed update
                      tzend = "+00:00"
                      if self._timestamp_compressed == True:
                          tzend = "0000"
                      #mk new tmsep
                      tsz =  ys + ddsep + mostr + ddsep + dystr + dtsep + \
                          hs + tmsep + ms + tmsep + sc + resep + resz + tzend #"+00:00"
      
        else:
        #mk new tmsep
           tsz =  ys + ddsep + mostr + ddsep + dystr + dtsep + \
                      hs + tmsep + ms + tmsep + sc + resep + resz 

        return tsz
    
    

#/**********************************************/
  

class SyncClock(Clock):
    # for sync clock in robots, sensors etc
    def __init__(self):
        
        self._name = "Sync Clock"
        self._vers = "v0.01.02"
        self._desc = "Sync Clock"
        
        self._init_datetime = datetime.now()#time.time()# time.clock()
        self._init_monotime = self.getMonotime()  # init base time as monotonic
        self._init_time = time.time() # init times  NEVER changes
        self._init_time_offset = 0 # offset to sync w/ external clock
        #self._init_monotime_offset = 0 # same for monotonic time
        
        self._start_epoch_time = time.gmtime(0)
         
        self._current_datetime = self._init_datetime
                
        self._up_monotime = 0
        self._up_days = 0
        self._up_hours = 0
        self._up_minutes = 0
        self._up_seconds = 0
        self._up_millisec = 0
        self._up_microsec = 0


#/**********************************************/
  
class SyncMasterClock(Clock):
    # or MasterSyncClock?
    # for sync clock in robots, sensors etc
    def __init__(self):
        
        self._name = "Master Sync Clock"
        self._vers = "v0.01.02"
        self._desc = "Master Sync Clock"
        
        self._init_datetime = datetime.datetime.now()#time.time()# time.clock()
        self._init_monotime = self.getMonotime()  # init base time as monotonic
        self._init_time = time.time() # init times  NEVER changes
        self._init_time_offset = 0 # offset to sync w/ external clock
        #self._init_monotime_offset = 0 # same for monotonic time
        
        self._start_epoch_time = time.gmtime(0)
         
        self._current_datetime = self._init_datetime
                
        self._up_monotime = 0
        self._up_days = 0
        self._up_hours = 0
        self._up_minutes = 0
        self._up_seconds = 0
        self._up_millisec = 0
        self._up_microsec = 0


#/**********************************************/
        
class SyncSlaveClock(Clock):
    # for sync clock in robots, sensors etc
    def __init__(self):
        
        self._name = "Slave Sync Clock"
        self._vers = "v0.01.02"
        self._desc = "Slave Sync Clock"
        
        self._init_datetime = datetime.datetime.now()#time.time()# time.clock()
        self._init_monotime = self.getMonotime()  # init base time as monotonic
        self._init_time = time.time() # init times  NEVER changes
        self._init_time_offset = 0 # offset to sync w/ external clock
        #self._init_monotime_offset = 0 # same for monotonic time
        
        self._current_datetime = self._init_datetime
                
        self._up_monotime = 0
        self._up_days = 0
        self._up_hours = 0
        self._up_minutes = 0
        self._up_seconds = 0
        self._up_millisec = 0
        self._up_microsec = 0


#/**********************************************/


##############
# SCRAP HEAP #
##############
