'''
    Author : Sukarna Jana
    Date   : 03/05/2021
    Title  : this file will say the main 
             bot when to join and when to 
             exit meetings
'''

import mainBot
import datetime

print("Bot is ready to start...")
print("Featching Data From scheduleTiming.txt")

scheduleFile = open("scheduleTimings.txt",'r')
fetchData = scheduleFile.readlines()
fetchData = [data for data in fetchData if data[0] != "#"]
scheduleTime = {}
for i in range(len(fetchData)):
    data = fetchData[i]
    data = data.rstrip("\n")
    data = data.split(',')
    if(len(data)==5):
        scheduleTime[f"Meeting Num:{i+1}"] = data
    else:
        print("Insaficient Data input in ScheduleTimings.txt pleace check")
scheduleFile.close()

mainBot.openZoomMeet()

print("Bot has started his work...")
while True:
    currentTimeData = datetime.datetime.now()
    currentTimeData = (currentTimeData.strftime("%H:%M"))
    print("Meetings Timing")
    for i in scheduleTime:    
        print(i)
    for i in scheduleTime:
        if(scheduleTime[i][0] == currentTimeData):
            meetid = scheduleTime[i][-2]
            name = scheduleTime[i][2]
            passwd = scheduleTime[i][-1]
            print("Ready to enter meeting")
            mainBot.joinMeet(str(meetid),str(passwd),str(name))
            mainBot.checkConnection()
            while True:
                currentTimeData = datetime.datetime.now()
                currentTimeData = (currentTimeData.strftime("%H:%M"))
                if(scheduleTime[i][1] == currentTimeData):
                    mainBot.leaveMeet()
                    print(f"{i} : Meeting has completed")
                    break
    print("Ready for attending Upcomming Meeting...")
    print(f"It's Time : {currentTimeData}")

