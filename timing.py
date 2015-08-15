days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
open = [900,1000,1000,1000,2700,1200,800]
close = [1700,1600,1600,1600,1600,1200,800]
timings = []
i = 0
while i < 7:
#for i in range(0,7):
    if(open[i] < close[i]):
        j = i
        while(open[i] == open[i+1] and close[i] == close[i+1]):
            i+=1
        if(j == i and i!= 6):
            timings.append(days[i] + ": " + str(open[i]) + "-" + str(close[i]))
        else:
            timings.append(days[j] + '-' + days[i] + ": " + str(open[i]) + "-" + str(close[i]))
    elif(open[i] > 2400):
        timings.append(days[i] + ": Closed")
    elif(open[i] == close[i]):
        j = i
        while(i < 6 and open[i] == close[i] and open[i+1] == close[i+1]):
            i+=1
        if(j == i and i < 6):
            timings.append(days[i] + ": Open 24 Hours")
        elif(j < i):
            timings.append(days[j] + '-' + days[i] + ": Open 24 Hours")
    if(i < 7):
        i+=1

for i in range(len(timings)):
    print timings[i]
