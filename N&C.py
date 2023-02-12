import tkinter as tk
from tkinter import messagebox
import random

#Defining All Variables

Clicked = True
Count = 0
RandomBotBegun = False
DefensiveBotBegun = False
AggressiveBotBegun = False
IsDraw = False
RobotGoesFirst = False
WonYet = False

#Allows For Quick Enabling Of Buttons

def EnableButtons():
    b1["state"] = 'normal'
    b2["state"] = 'normal'
    b3["state"] = 'normal'
    b4["state"] = 'normal'
    b5["state"] = 'normal'
    b6["state"] = 'normal'
    b7["state"] = 'normal'
    b8["state"] = 'normal'
    b9["state"] = 'normal'

#Defines Who Goes First, If The Robot Goes First It Robot Move Is Called.

def WhoGoesFirst():
    global WhoFirst, RobotGoesFirst
    WhoFirst = random.randint(1, 2)
    if WhoFirst == 1:
        RobotGoesFirst = True
        AggressiveRobot()
    elif WhoFirst == 2:
        RobotGoesFirst = False
    else:
        pass

#Begins The Random Robot

def RandomBotBegin():
    global RandomBotBegun
    RandomBotBegun = True
    Reset()

#Begins The Defensive Robot

def DefensiveBotBegin():
    global DefensiveBotBegun
    RandomBotBegin()
    DefensiveBotBegun = True
    Reset()

#Begins The Aggressive Robot

def AggressiveBotBegin():
    global AggressiveBotBegun
    DefensiveBotBegin()
    AggressiveBotBegun = True
    Reset()

#Begins The Next Level

def NextLevel():
    global RandomBotBegun, DefensiveBotBegun, AggressiveBotBegun
    if RandomBotBegun == False:
        RandomBotBegin()
        level["text"] = "Level:\nRandom Robot"
    elif DefensiveBotBegun == False:
        DefensiveBotBegin()
        level["text"] = "Level:\n Defensive Robot"
    elif AggressiveBotBegun == False:
        AggressiveBotBegin()
        level["text"] = "Level: \nAggressive Robot"
    else:
        pass

#Resets The Board

def Reset():
    global Count, Clicked
    b1["text"] = " "
    b2["text"] = " "
    b3["text"] = " "
    b4["text"] = " "
    b5["text"] = " "
    b6["text"] = " "
    b7["text"] = " "
    b8["text"] = " "
    b9["text"] = " "
    Count = 0
    Clicked = True
    WhoGoesFirst()
    EnableButtons()

#Resets The Variables So That You Can Go Back Through Levels

def PvPRestart():
    global RandomBotBegun, DefensiveBotBegun, AggressiveBotBegun
    RandomBotBegun = False
    DefensiveBotBegun = False
    AggressiveBotBegun = False
    level["text"] = "Level: \nPlayer V. Player"
    Reset()

#For Shorthand

def ShortBot():
    global Clicked, Count, WonYet, RobotGoesFirst
    EnableButtons()
    if RobotGoesFirst == True:
        Clicked = False
    elif RobotGoesFirst == False:
        Clicked = True
    else:
        pass
    Count += 1
    if WonYet == False:
        CheckIfWon()
    else:
        DisableButtons()

#Determines Whether Or Not A Draw Has Occured

def DrawOrNot():
    global IsDraw
    if b1["text"] != " " and b2["text"] != " " and b3["text"] != " " and b4[
            "text"] != " " and b5["text"] != " " and b6["text"] != " " and b7[
                "text"] != " " and b8["text"] != " " and b9["text"] != " ":
        IsDraw = True
    else:
        pass

#Picks Number Between 1-9 And If Empty, Fills The Space, Otherwise It Chooses Another Number

def RandRobotMove():
    if RandomBotBegun == True:
        global RandomRobotMove, Count, Clicked
        b1["state"] = 'disabled'
        b2["state"] = 'disabled'
        b3["state"] = 'disabled'
        b4["state"] = 'disabled'
        b5["state"] = 'disabled'
        b6["state"] = 'disabled'
        b7["state"] = 'disabled'
        b8["state"] = 'disabled'
        b9["state"] = 'disabled'
        RandomRobotMove = random.randint(1, 9)
        if RandomRobotMove == 1 and b1["text"] == " ":
            if RobotGoesFirst == True:
                b1["text"] = "X"
            elif RobotGoesFirst == False:
                b1["text"] = "O"
            ShortBot()
        elif RandomRobotMove == 2 and b2["text"] == " ":
            if RobotGoesFirst == True:
                b2["text"] = "X"
            elif RobotGoesFirst == False:
                b2["text"] = "O"
            ShortBot()
        elif RandomRobotMove == 3 and b3["text"] == " ":
            if RobotGoesFirst == True:
                b3["text"] = "X"
            elif RobotGoesFirst == False:
                b3["text"] = "O"
            ShortBot()
        elif RandomRobotMove == 4 and b4["text"] == " ":
            if RobotGoesFirst == True:
                b4["text"] = "X"
            elif RobotGoesFirst == False:
                b4["text"] = "O"
            ShortBot()
        elif RandomRobotMove == 5 and b5["text"] == " ":
            if RobotGoesFirst == True:
                b5["text"] = "X"
            elif RobotGoesFirst == False:
                b5["text"] = "O"
            ShortBot()
        elif RandomRobotMove == 6 and b6["text"] == " ":
            if RobotGoesFirst == True:
                b6["text"] = "X"
            elif RobotGoesFirst == False:
                b6["text"] = "O"
            ShortBot()
        elif RandomRobotMove == 7 and b7["text"] == " ":
            if RobotGoesFirst == True:
                b7["text"] = "X"
            elif RobotGoesFirst == False:
                b7["text"] = "O"
            ShortBot()
        elif RandomRobotMove == 8 and b8["text"] == " ":
            if RobotGoesFirst == True:
                b8["text"] = "X"
            elif RobotGoesFirst == False:
                b8["text"] = "O"
            ShortBot()
        elif RandomRobotMove == 9 and b9["text"] == " ":
            if RobotGoesFirst == True:
                b9["text"] = "X"
            elif RobotGoesFirst == False:
                b9["text"] = "O"
            ShortBot()
        else:
            RandRobotMove()
    else:
        pass

#If Two Of The Same Symbol Are Next To Eachother, Place A Symbol. This Allows For Both Blocking And Attacking.

def AggressiveRobot():
    global Count, Clicked, AggressiveBotBegun
    if AggressiveBotBegun == True:
        if b1["text"] == b2["text"] and b3["text"] == " " and b1["text"] != " ":
            if RobotGoesFirst == True:
                b3["text"] = "X"
            elif RobotGoesFirst == False:
                b3["text"] = "O"
            ShortBot()
        elif b2["text"] == b3["text"] and b1[
                "text"] == " " and b2["text"] != " ":
            if RobotGoesFirst == True:
                b1["text"] = "X"
            elif RobotGoesFirst == False:
                b1["text"] = "O"
            ShortBot()
        elif b3["text"] == b1["text"] and b2[
                "text"] == " " and b1["text"] != " ":
            if RobotGoesFirst == True:
                b2["text"] = "X"
            elif RobotGoesFirst == False:
                b2["text"] = "O"
            ShortBot()
        elif b5["text"] == b4["text"] and b6[
                "text"] == " " and b5["text"] != " ":
            if RobotGoesFirst == True:
                b6["text"] = "X"
            elif RobotGoesFirst == False:
                b6["text"] = "O"
            ShortBot()
        elif b6["text"] == b5["text"] and b4[
                "text"] == " " and b6["text"] != " ":
            if RobotGoesFirst == True:
                b4["text"] = "X"
            elif RobotGoesFirst == False:
                b4["text"] = "O"
            ShortBot()
        elif b6["text"] == b4["text"] and b5[
                "text"] == " " and b6["text"] != " ":
            b5["text"] = "O"
            ShortBot()
        elif b8["text"] == b7["text"] and b9[
                "text"] == " " and b8["text"] != " ":
            b9["text"] = "O"
            ShortBot()
        elif b9["text"] == b8["text"] and b7[
                "text"] == " " and b9["text"] != " ":
            if RobotGoesFirst == True:
                b7["text"] = "X"
            elif RobotGoesFirst == False:
                b7["text"] = "O"
            ShortBot()
        elif b9["text"] == b7["text"] and b8[
                "text"] == " " and b9["text"] != " ":
            if RobotGoesFirst == True:
                b8["text"] = "X"
            elif RobotGoesFirst == False:
                b8["text"] = "O"
            ShortBot()
        elif b4["text"] == b1["text"] and b7[
                "text"] == " " and b1["text"] != " ":
            if RobotGoesFirst == True:
                b7["text"] = "X"
            elif RobotGoesFirst == False:
                b7["text"] = "O"
            ShortBot()
        elif b7["text"] == b4["text"] and b1[
                "text"] == " " and b7["text"] != " ":
            if RobotGoesFirst == True:
                b1["text"] = "X"
            elif RobotGoesFirst == False:
                b1["text"] = "O"
            ShortBot()
        elif b7["text"] == b1["text"] and b4[
                "text"] == " " and b1["text"] != " ":
            if RobotGoesFirst == True:
                b4["text"] = "X"
            elif RobotGoesFirst == False:
                b4["text"] = "O"
            ShortBot()
        elif b5["text"] == b2["text"] and b8[
                "text"] == " " and b2["text"] != " ":
            if RobotGoesFirst == True:
                b8["text"] = "X"
            elif RobotGoesFirst == False:
                b8["text"] = "O"
            ShortBot()
        elif b8["text"] == b5["text"] and b2[
                "text"] == " " and b8["text"] != " ":
            if RobotGoesFirst == True:
                b2["text"] = "X"
            elif RobotGoesFirst == False:
                b2["text"] = "O"
            ShortBot()
        elif b8["text"] == b2["text"] and b5[
                "text"] == " " and b2["text"] != " ":
            if RobotGoesFirst == True:
                b5["text"] = "X"
            elif RobotGoesFirst == False:
                b5["text"] = "O"
            ShortBot()
        elif b6["text"] == b3["text"] and b9[
                "text"] == " " and b6["text"] != " ":
            if RobotGoesFirst == True:
                b9["text"] = "X"
            elif RobotGoesFirst == False:
                b1["text"] = "O"
            ShortBot()
        elif b9["text"] == b6["text"] and b3[
                "text"] == " " and b9["text"] != " ":
            if RobotGoesFirst == True:
                b3["text"] = "X"
            elif RobotGoesFirst == False:
                b3["text"] = "O"
            ShortBot()
        elif b9["text"] == b3["text"] and b6[
                "text"] == " " and b9["text"] != " ":
            if RobotGoesFirst == True:
                b6["text"] = "X"
            elif RobotGoesFirst == False:
                b6["text"] = "O"
            ShortBot()
        elif b5["text"] == b1["text"] and b9[
                "text"] == " " and b1["text"] != " ":
            if RobotGoesFirst == True:
                b9["text"] = "X"
            elif RobotGoesFirst == False:
                b9["text"] = "O"
            ShortBot()
        elif b9["text"] == b5["text"] and b1[
                "text"] == " " and b9["text"] != " ":
            if RobotGoesFirst == True:
                b1["text"] = "X"
            elif RobotGoesFirst == False:
                b1["text"] = "O"
            ShortBot()
        elif b9["text"] == b1["text"] and b5[
                "text"] == " " and b1["text"] != " ":
            if RobotGoesFirst == True:
                b5["text"] = "X"
            elif RobotGoesFirst == False:
                b5["text"] = "O"
            ShortBot()
        elif b5["text"] == b3["text"] and b7[
                "text"] == " " and b5["text"] != " ":
            if RobotGoesFirst == True:
                b7["text"] = "X"
            elif RobotGoesFirst == False:
                b7["text"] = "O"
            ShortBot()
        elif b5["text"] == b7["text"] and b3[
                "text"] == " " and b5["text"] != " ":
            if RobotGoesFirst == True:
                b3["text"] = "X"
            elif RobotGoesFirst == False:
                b3["text"] = "O"
            ShortBot()
        elif b7["text"] == b3["text"] and b5[
                "text"] == " " and b7["text"] != " ":
            if RobotGoesFirst == True:
                b5["text"] = "X"
            elif RobotGoesFirst == False:
                b5["text"] = "O"
            ShortBot()
        else:
            DefensiveRobot()
    else:
        DefensiveRobot()

#Good luck winning 

'''def GeniusRobot():
  if Count == 0:
    b1["text"] = "X"
  elif Count == 1:
    if b5["text"] == " ":
      b5["text"] = "O"
    elif b5["text"] == "X":
      b1["text"] = "O"
  elif Count == 2:
    if b1["text"] == "O" or b7["text"] == "O" or b9["text"] == "O" or b3["text"] == "O":
      if b3["text"] == " ":
        b3["text"] = "X"
      else:
        b7["text"] = "X"
    elif b5["text"] == "O":
      if b9["text"] == " ":
        b9["text"] = "X"
      elif b9["text"] == "O":
        b1["text"] = "O"
    elif b2["text"] == "O":
      b7["text"]="X"
    else:
      if b3["text"] == " ":
        b3["text"] = "X"
      elif b3["text"] == "O":
        b7["text"]= "X"
  elif Count == 3:
    '''

#If Two Symbols Next To Eachother THAT ARENT THE ROBOT'S SYMBOL, It Will Put A Symbol In The Final Spot In A Row.

def DefensiveRobot():
    global Count, Clicked, DefensiveBotBegun
    if DefensiveBotBegun == True:
        if RobotGoesFirst == False:
            if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == " ":
                b3["text"] = "O"
                ShortBot()
            elif b2["text"] == "X" and b3["text"] == "X" and b1["text"] == " ":
                b1["text"] = "O"
                ShortBot()
            elif b3["text"] == "X" and b1["text"] == "X" and b2["text"] == " ":
                b2["text"] = "O"
                ShortBot()
            elif b5["text"] == "X" and b4["text"] == "X" and b6["text"] == " ":
                b6["text"] = "O"
                ShortBot()
            elif b6["text"] == "X" and b5["text"] == "X" and b4["text"] == " ":
                b4["text"] = "O"
                ShortBot()
            elif b6["text"] == "X" and b4["text"] == "X" and b5["text"] == " ":
                b5["text"] = "O"
                ShortBot()
            elif b8["text"] == "X" and b7["text"] == "X" and b9["text"] == " ":
                b9["text"] = "O"
                ShortBot()
            elif b9["text"] == "X" and b8["text"] == "X" and b7["text"] == " ":
                b7["text"] = "O"
                ShortBot()
            elif b9["text"] == "X" and b7["text"] == "X" and b8["text"] == " ":
                b8["text"] = "O"
                ShortBot()
            elif b4["text"] == "X" and b1["text"] == "X" and b7["text"] == " ":
                b7["text"] = "O"
                ShortBot()
            elif b7["text"] == "X" and b4["text"] == "X" and b1["text"] == " ":
                b1["text"] = "O"
                ShortBot()
            elif b7["text"] == "X" and b1["text"] == "X" and b4["text"] == " ":
                b4["text"] = "O"
                ShortBot()
            elif b5["text"] == "X" and b2["text"] == "X" and b8["text"] == " ":
                b8["text"] = "O"
                ShortBot()
            elif b8["text"] == "X" and b5["text"] == "X" and b2["text"] == " ":
                b2["text"] = "O"
                ShortBot()
            elif b8["text"] == "X" and b2["text"] == "X" and b5["text"] == " ":
                b5["text"] = "O"
                ShortBot()
            elif b6["text"] == "X" and b3["text"] == "X" and b9["text"] == " ":
                b9["text"] = "O"
                ShortBot()
            elif b9["text"] == "X" and b6["text"] == "X" and b3["text"] == " ":
                b3["text"] = "O"
                ShortBot()
            elif b9["text"] == "X" and b3["text"] == "X" and b6["text"] == " ":
                b6["text"] = "O"
                ShortBot()
            elif b5["text"] == "X" and b1["text"] == "X" and b9["text"] == " ":
                b9["text"] = "O"
                ShortBot()
            elif b9["text"] == "X" and b5["text"] == "X" and b1["text"] == " ":
                b1["text"] = "O"
                ShortBot()
            elif b9["text"] == "X" and b1["text"] == "X" and b5["text"] == " ":
                b5["text"] = "O"
                ShortBot()
            elif b5["text"] == "X" and b3["text"] == "X" and b7["text"] == " ":
                b7["text"] = "O"
                ShortBot()
            elif b5["text"] == "X" and b7["text"] == "X" and b3["text"] == " ":
                b3["text"] = "O"
                ShortBot()
            elif b7["text"] == "X" and b3["text"] == "X" and b5["text"] == " ":
                b5["text"] = "O"
                ShortBot()
            else:
                RandRobotMove()
        elif RobotGoesFirst == True:
            if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == " ":
                b3["text"] = "X"
                ShortBot()
            elif b2["text"] == "O" and b3["text"] == "O" and b1["text"] == " ":
                b1["text"] = "X"
                ShortBot()
            elif b3["text"] == "O" and b1["text"] == "O" and b2["text"] == " ":
                b2["text"] = "X"
                ShortBot()
            elif b5["text"] == "O" and b4["text"] == "O" and b6["text"] == " ":
                b6["text"] = "X"
                ShortBot()
            elif b6["text"] == "O" and b5["text"] == "O" and b4["text"] == " ":
                b4["text"] = "X"
                ShortBot()
            elif b6["text"] == "O" and b4["text"] == "O" and b5["text"] == " ":
                b5["text"] = "X"
                ShortBot()
            elif b8["text"] == "O" and b7["text"] == "O" and b9["text"] == " ":
                b9["text"] = "X"
                ShortBot()
            elif b9["text"] == "O" and b8["text"] == "O" and b7["text"] == " ":
                b7["text"] = "X"
                ShortBot()
            elif b9["text"] == "O" and b7["text"] == "O" and b8["text"] == " ":
                b8["text"] = "X"
                ShortBot()
            elif b4["text"] == "O" and b1["text"] == "O" and b7["text"] == " ":
                b7["text"] = "X"
                ShortBot()
            elif b7["text"] == "O" and b4["text"] == "O" and b1["text"] == " ":
                b1["text"] = "X"
                ShortBot()
            elif b7["text"] == "O" and b1["text"] == "O" and b4["text"] == " ":
                b4["text"] = "X"
                ShortBot()
            elif b5["text"] == "O" and b2["text"] == "O" and b8["text"] == " ":
                b8["text"] = "X"
                ShortBot()
            elif b8["text"] == "O" and b5["text"] == "O" and b2["text"] == " ":
                b2["text"] = "X"
                ShortBot()
            elif b8["text"] == "O" and b2["text"] == "O" and b5["text"] == " ":
                b5["text"] = "X"
                ShortBot()
            elif b6["text"] == "O" and b3["text"] == "O" and b9["text"] == " ":
                b9["text"] = "X"
                ShortBot()
            elif b9["text"] == "O" and b6["text"] == "O" and b3["text"] == " ":
                b3["text"] = "X"
                ShortBot()
            elif b9["text"] == "O" and b3["text"] == "O" and b6["text"] == " ":
                b6["text"] = "X"
                ShortBot()
            elif b5["text"] == "O" and b1["text"] == "O" and b5["text"] == " ":
                b9["text"] = "X"
                ShortBot()
            elif b9["text"] == "O" and b5["text"] == "O" and b1["text"] == " ":
                b1["text"] = "X"
                ShortBot()
            elif b9["text"] == "O" and b1["text"] == "O" and b5["text"] == " ":
                b5["text"] = "X"
                ShortBot()
            elif b5["text"] == "O" and b3["text"] == "O" and b7["text"] == " ":
                b7["text"] = "X"
                ShortBot()
            elif b5["text"] == "O" and b5["text"] == "O" and b3["text"] == " ":
                b3["text"] = "X"
                ShortBot()
            elif b7["text"] == "O" and b3["text"] == "O" and b5["text"] == " ":
                b5["text"] = "X"
                ShortBot()
            else:
                RandRobotMove()
        else:
            pass
    else:
        RandRobotMove()

#Changes The Symbol In A Space If It's Empty And Has Been Clicked

def B_Click(b):
  try:
      global Clicked, Count
      if RandomBotBegun == False or RandomBotBegun == True and RobotGoesFirst == False:
          if b["text"] == " " and Clicked == True:
              b["text"] = "X"
              Clicked = False
              Count += 1
              CheckIfWon()
              AggressiveRobot()
          elif b["text"] == " " and Clicked == False:
              b["text"] = "O"
              Clicked = True
              Count += 1
              CheckIfWon()
              AggressiveRobot()
          else:
              tk.messagebox.showwarning("Noughts and Crosses",
                                        "That box has already been filled")
      elif RandomBotBegun == True and RobotGoesFirst == True:
          if b["text"] == " " and Clicked == True:
              b["text"] = "X"
              Clicked = False
              Count += 1
              CheckIfWon()
              AggressiveRobot()
          elif b["text"] == " " and Clicked == False:
              b["text"] = "O"
              Clicked = True
              Count += 1
              CheckIfWon()
              AggressiveRobot()
          else:
              tk.messagebox.showwarning("Noughts and Crosses",
                                        "That box has already been filled")
      else:
          if b["text"] == " " and Clicked == True:
              b["text"] = "X"
              Clicked = False
              Count += 1
              CheckIfWon()
              AggressiveRobot()
          elif b["text"] == " " and Clicked == False:
              b["text"] = "O"
              Clicked = True
              Count += 1
              CheckIfWon()
              AggressiveRobot()
          else:
              tk.messagebox.showwarning("Noughts and Crosses",
                                        "That box has already been filled")
  except RecursionError:
    print("lol bot tried move but no space bozo")
#Quickly Disables All Buttons

def DisableButtons():
    b1["state"] = 'disabled'
    b2["state"] = 'disabled'
    b3["state"] = 'disabled'
    b4["state"] = 'disabled'
    b5["state"] = 'disabled'
    b6["state"] = 'disabled'
    b7["state"] = 'disabled'
    b8["state"] = 'disabled'
    b9["state"] = 'disabled'

#Checks Who Won

def WhoWon():
    global WonYet
    if Clicked == True:
        tk.messagebox.showinfo("Noughts and Crosses", "O Wins!")
        DisableButtons()
        WonYet = True
    elif Clicked == False:
        tk.messagebox.showinfo("Noughts and Crosses", "X Wins!")
        DisableButtons()
        WonYet = True

#Checks If Anyone Won

def CheckIfWon():
    global WonYet
    WonYet = False

    if b1["text"] == b2["text"] == b3["text"] and b1["text"] != " ":
        WhoWon()
    elif b4["text"] == b5["text"] == b6["text"] and b4["text"] != " ":
        WhoWon()
    elif b7["text"] == b8["text"] == b9["text"] and b7["text"] != " ":
        WhoWon()
    elif b1["text"] == b4["text"] == b7["text"] and b1["text"] != " ":
        WhoWon()
    elif b2["text"] == b5["text"] == b8["text"] and b2["text"] != " ":
        WhoWon()
    elif b3["text"] == b6["text"] == b9["text"] and b3["text"] != " ":
        WhoWon()
    elif b1["text"] == b5["text"] == b9["text"] and b1["text"] != " ":
        WhoWon()
    elif b3["text"] == b5["text"] == b7["text"] and b3["text"] != " ":
        WhoWon()
    else:
        DrawOrNot()
        if IsDraw == True and Count >= 9:
            tk.messagebox.showinfo("Noughts and Crosses", "DRAW!")
            DisableButtons()
        else:
            pass

#Creates The Grid

pvp = tk.Tk()
pvp.title("Noughts and Crosses")

b1 = tk.Button(pvp,
               text=' ',
               font=("Calibri", 20),
               height=3,
               width=6,
               command=lambda: B_Click(b1))
b2 = tk.Button(pvp,
               text=' ',
               font=("Calibri", 20),
               height=3,
               width=6,
               command=lambda: B_Click(b2))
b3 = tk.Button(pvp,
               text=' ',
               font=("Calibri", 20),
               height=3,
               width=6,
               command=lambda: B_Click(b3))

b4 = tk.Button(pvp,
               text=' ',
               font=("Calibri", 20),
               height=3,
               width=6,
               command=lambda: B_Click(b4))
b5 = tk.Button(pvp,
               text=' ',
               font=("Calibri", 20),
               height=3,
               width=6,
               command=lambda: B_Click(b5))
b6 = tk.Button(pvp,
               text=' ',
               font=("Calibri", 20),
               height=3,
               width=6,
               command=lambda: B_Click(b6))

b7 = tk.Button(pvp,
               text=' ',
               font=("Calibri", 20),
               height=3,
               width=6,
               command=lambda: B_Click(b7))
b8 = tk.Button(pvp,
               text=' ',
               font=("Calibri", 20),
               height=3,
               width=6,
               command=lambda: B_Click(b8))
b9 = tk.Button(pvp,
               text=' ',
               font=("Calibri", 20),
               height=3,
               width=6,
               command=lambda: B_Click(b9))
resetbutton = tk.Button(pvp,
                        text='Reset Game',
                        font=("Calibri", 8),
                        height=1,
                        width=12,
                        command=Reset)
nextlevelbutton = tk.Button(pvp,
                            text='Next Level',
                            font=("Calibri", 8),
                            height=1,
                            width=12,
                            command=NextLevel)
pvpbutton = tk.Button(pvp,
                      text='Player V. Player',
                      font=("Calibri", 8),
                      height=1,
                      width=12,
                      command=PvPRestart)
level = tk.Button(pvp,
                  text='Level: \nPlayer V. Player',
                  font=("Calibri", 8),
                  height=2,
                  width=12)
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

#Aligns The Extra Buttons
resetbutton.grid(row=3, column=1)
nextlevelbutton.grid(row=3, column=2)
pvpbutton.grid(row=3, column=0)
level.grid(row=4, column=1)
level["state"] = 'active'                    