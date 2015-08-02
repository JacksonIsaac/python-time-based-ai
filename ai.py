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

from datetime import datetime

class Time(object):
    hours = 0.0
    minutes = 0.0
    year = 0000
    month = 00
    day = 00

def parse_token(inp):
    for pos in inp:
        if(pos[1] == 'RB' and pos[0] == 'now'):
            curr_time =  datetime.now()
            Time.hours = curr_time.strftime("%H")
            Time.minutes = curr_time.strftime("%M")
            Time.year = curr_time.strftime("%Y")
            Time.month = curr_time.strftime("%m")
            Time.day = curr_time.strftime("%d")
            return Time.hours + ":" + Time.minutes + " hours, " + curr_time.strftime("%A") + ", " + Time.year 


print ("Loading AI")
import nltk

## Uncomment this to download nltk packages
#nltk.download("book")

input = raw_input("What do you want to do?\n")
tokens = nltk.sent_tokenize(input)

for token in tokens:
    tok = nltk.word_tokenize(token)
    t =  nltk.pos_tag(tok)
    res = parse_token(t)
    print res
