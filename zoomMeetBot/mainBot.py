'''
    Author : Sukarna Jana
    Date   : 03/05/2021
    Title  : i will be controlling the whole zoom
             be chill ;)
'''

import pyautogui
import time
import os

def openZoomMeet():
    os.system("zoom")
    time.sleep(4)

def joinMeet(meetid,passwd,username):
    while True:
        joinMeeting = pyautogui.locateOnScreen("./imgOfMeet/joinZoomMeet.png")
        print("ready to join...")
        if(joinMeeting != None):
            pyautogui.click(joinMeeting)
            time.sleep(2)
            break
    while True:
        meetingID = pyautogui.locateOnScreen("./imgOfMeet/enterMeetID.png")
        if(meetingID != None):
            pyautogui.click(meetingID)
            time.sleep(1)
            pyautogui.typewrite(meetid)
            time.sleep(1)
            break
        print("finding...")
    print("inserted Meeting ID")
    count = 0
    while count <= 5:
        meetingName = pyautogui.locateOnScreen("./imgOfMeet/enterName.png")
        if(meetingName != None):
            pyautogui.click(meetingpasswd)
            time.sleep(1)
            pyautogui.typewrite(username)
            time.sleep(1)
            break
        else:
            count += 1
        time.sleep(1)
    print("Name has been given")
    clk1TurnOffVideo = pyautogui.locateOnScreen("./imgOfMeet/turnOffVideo.png")
    if(clk1TurnOffVideo != None):
        pyautogui.click(clk1TurnOffVideo)
    elif(pyautogui.locateOnScreen("./imgOfMeet/videoIsOff.png") != None):
        pass
    else:
        pass
    print("while entering video is off...")
    while True:
        join = pyautogui.locateOnScreen("./imgOfMeet/joinMeet.png")
        if(join != None):
            pyautogui.click(join)
            break
    time.sleep(3)
    count = 0
    while count <= 5:
        meetingpasswd = pyautogui.locateOnScreen("./imgOfMeet/enterPasswd.png")
        if(meetingpasswd != None):
            pyautogui.click(meetingpasswd)
            time.sleep(1)
            pyautogui.typewrite(passwd)
            time.sleep(1)
            finalMeetIn = pyautogui.locateOnScreen("./imgOfMeet/joinMeetfinal.png") 
            time.sleep(1)
            pyautogui.click(finalMeetIn)
            time.sleep(5)
            break
        else:
            count += 1
    print("inserted Meeting Password")

def checkConnection():
    count = 0
    while count <= 5:
        shake = pyautogui.locateOnScreen("./imgOfMeet/justToPopupBtn.png")
        pyautogui.moveTo(shake)
        audioConnected = pyautogui.locateOnScreen("./imgOfMeet/joinAudio.png")
        if(audioConnected != None):
            pyautogui.click(audioConnected)
            time.sleep(1)
            while True:
                audioConnectedFinal = pyautogui.locateOnScreen("./imgOfMeet/joinwithPCaudio.png")
                if(audioConnectedFinal != None):
                    pyautogui.click(audioConnectedFinal)
                    time.sleep(1)
                    break
            break
        else:
            count += 1
        time.sleep(1)
    print("Audio is connceted")
    while True:
        shake = pyautogui.locateOnScreen("./imgOfMeet/justToPopupBtn.png")
        pyautogui.moveTo(shake)
        micmute = pyautogui.locateOnScreen("./imgOfMeet/unmute.png")
        micunmute = pyautogui.locateOnScreen("./imgOfMeet/mute.png")
        if(micmute != None):
            break
        elif(micunmute != None):
            pyautogui.click(micunmute)
            time.sleep(1)
    print("Mic Checked")
    count = 0
    while count <= 5:
        shake = pyautogui.locateOnScreen("./imgOfMeet/justToPopupBtn.png")
        pyautogui.moveTo(shake)
        if(pyautogui.locateOnScreen("./imgOfMeet/offvideo.png") == None):
            print("Video is not supported")
            time.sleep(1)
            count += 1
        videoOn = pyautogui.locateOnScreen("./imgOfMeet/offVideoFeed.png")
        if(videoOn != None):
            time.sleep(1)
            pyautogui.click(videoOn)
            print("video was no but now it's off")
            break
        elif(pyautogui.locateOnScreen("./imgOfMeet/offvideo.png") != None):
            print("video offed")
            break
    print("Video Checked")
    print("Your Meeting is running now have a great fun...")

def leaveMeet():
    while True:
        shake = pyautogui.locateOnScreen("./imgOfMeet/justToPopupBtn.png")
        pyautogui.moveTo(shake)
        time.sleep(1)
        clickLeave = pyautogui.locateOnScreen("./imgOfMeet/leaveMeet.png")
        if(clickLeave != None):
            print("Ready to leave")
            pyautogui.click(clickLeave)
            time.sleep(1)
            while True:
                finalToLeave = pyautogui.locateOnScreen("./imgOfMeet/finalLeaveMeet.png")
                if(finalToLeave != None):
                    pyautogui.click(finalToLeave)
                    print("Exited from meeting successfully...")
                    break
            break 