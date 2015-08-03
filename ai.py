# Copyright (c) 2015 Jackson Isaac <jacksonisaac2008@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of The MacPorts Project nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

from datetime import datetime, timedelta

## Time class to store the time.
class Time(object):
    def __init__(self):
        self.hours = int(datetime.now().strftime("%H"))
        self.minutes = int(datetime.now().strftime("%M"))
        self.year = int(datetime.now().strftime("%Y"))
        self.month = datetime.now().strftime("%B")
        self.imonth = int(datetime.now().strftime("%m"))
        self.day = datetime.now().strftime("%A")
        self.date = datetime.now().strftime("%d")
    def update_hours(self, hrs):
        self.hours += hrs
        if(self.hours >= 24):
            self.hours -= 24
        time_temp = datetime.now() + timedelta(days=1)
        self.set_date(time_temp.strftime("%d"))
        self.update_day(time_temp)

    def inc_date(self):
        self.date = int(self.date) + 1
        new_time = datetime(self.get_iyear(), self.get_imonth(), self.get_date() + 1)
        self.update_day(new_time)

    def update_min(self, min):
        self.minutes += min
        if(self.minutes >= 60):
            self.minutes -= 60
            self.update_hours(1)
    
    def update_day(self, time):
        self.day = time.strftime("%A")

    def set_hours(self, inp):
        self.hours = inp
    def set_min(self, inp):
        self.minutes = inp
    def set_year(self, inp):
        self.year = inp
    def set_month(self, inp):
        self.month = inp
    def set_day(self, inp):
        self.day = inp
    def set_date(self, inp):
        self.date = inp

    def get_hours(self):
        if(self.hours >= 0 and self.hours <= 9):
            return '0' + str(self.hours)
        else:
            return str(self.hours)
    def get_ihours(self):
        return self.hours
    def get_min(self):
        if(self.minutes >= 0 and self.minutes <=9):
            return '0' + str(self.minutes)
        return str(self.minutes)
    def get_imin(self):
        return self.minutes
    def get_imonth(self):
        return self.imonth
    def get_year(self):
        return str(self.year)
    def get_iyear(self):
        return self.year
    def get_month(self):
        return self.month
    def get_day(self):
        return self.day
    def get_date(self):
        return self.date
    def get_sdate(self):
        return str(self.date)

## Reference from: http://stackoverflow.com/a/493788
## Convert string numbers to integers.
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current


def parse_token(inp):
    time = Time()
    op = 0
    trange = 0
    reminder = 0
    future = 0
    pm = 0
    for pos in inp:
        val = pos[0]
        key = pos[1]
        if(key == 'NN' and val == 'timer'):
            reminder = 1
        if(key == 'IN'):
            if(val == 'for'):
                trange = 1
            if(val == 'Before'):
                reminder = 1
            if(val == 'from' or val == 'after'):
                op = 1
        if(key == 'NN'):
            if(val == 'tomorrow'):
                time.inc_date()
                time.inc_date()
                future = 1
            if(val == 'evening'):
                pm = 1
        if(key == 'RB' and val == 'now'):
            curr_time = datetime.now() 
        if(key == 'CD'):
            if(val.isdigit()):
                tval = val
            else:
                tval = text2int(val)
    if(future == 1):
        if(pm == 1 and int(tval) < 12):
            tval = int(tval) + 12
        time.set_hours(tval)
        time.set_min(0)
        return time.get_hours() + time.get_min() + " hours, " + time.get_day() + ", " + time.get_sdate() + " " + time.get_month() + ", " + time.get_year()
    if(reminder == 1):
        if(time.get_ihours() < int(tval)):
            print time.get_ihours(), int(tval)
            time.set_hours(tval)
            time.set_min(0)
        else:
            print "Incrementing date"
            time.inc_date()
            time.set_hours(tval)
            time.set_min(0)
        return "start: " + datetime.now().strftime("%H%M, %B %d, %Y") + " : end: " + time.get_hours() + time.get_min() + " hours, " + time.get_day() + ", " + time.get_sdate() + " " + time.get_month() + ", " + time.get_year()
    if(op == 0):
        time.update_min(-int(tval))
    else:
        time.update_min(int(tval))
    if(trange == 1):
        return str(time.get_iyear() - tval) + " - " + time.get_year()
    return time.get_hours() + time.get_min() + " hours, " + time.get_day() + ", " + time.get_date() + " " + time.get_month() + ", " + time.get_year()


print ("Loading AI")
import nltk

## Uncomment this to download nltk packages
#nltk.download("book")

#input = raw_input("What do you want to do?\n")
input = "Looking to a make reservation for two people day after tomorrow at seven in the evening"
#input = "I was working in san francisco for last two years"
#input = "Any timer after 15 is fine"
#input = "Before 1 is good"
tokens = nltk.sent_tokenize(input)

for token in tokens:
    tok = nltk.word_tokenize(token)
    t =  nltk.pos_tag(tok)
    print t
    res = parse_token(t)
    print res
