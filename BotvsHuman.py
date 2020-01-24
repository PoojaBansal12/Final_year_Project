import tkinter.filedialog as filedialog
from tkinter import*
from tkinter import font
import tweepy
import os.path
import csv
from PIL import ImageTk, Image, ImageGrab
from tweepy.auth import OAuthHandler
import time
import datetime
import numpy as np
import smtplib
import analysis
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
isDataRetrived=0
botCount=0
humanCount=0
totalTweetData=0
def doNothing():
    print("BotvsHuman")
window=Tk()
window.title("Bot vs Human Detection")
window.geometry("1366x732+0+0")
window.resizable(width=False, height=False)
mainMenuFont = font.Font(family='Arial', size=8, weight=font.NORMAL)
fontOne = font.Font(family='helvetica', size=15, weight=font.BOLD)
fontTwo = font.Font(family='helvetica', size=15)
fontThree=font.Font(family='helvetica', size=14, weight=font.BOLD)
fontFour=font.Font(family='helvetica', size=12)
setTextFoneForTopTweetst=font.Font(family="helvetica", size=10)
setTextFoneForTopTrend=font.Font(family="helvetica", size=12)
setTextFoneForAllTweet=font.Font(family="helvetica", size=12, weight=font.NORMAL)
isSearchBarClick = True
isEmailId=True
isVarify=False
def isSearchEntered(event):       
    global isSearchBarClick
    if isSearchBarClick:
        isSearchBarClick = False
        search.delete(0, "end")       
def getAdelaideTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Adelaide Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(1099805)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getBrisbaneTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Brisbane Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(1100661)
    dataObtainedFromLocationId= tre[0]
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getCanberraTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Canberra Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(1100968)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getMelbourneTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Melbourne Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(1103816)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getPerthTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Perth Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(1098081)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getSydneyTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Sydney Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(1105779)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getAlgoma(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Algoma Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(56621452)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getOttawa(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Ottawa Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(91982014)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()    
def getVancouver(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Vancouver Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(12482814)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getWaterloo(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Waterloo Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(23396898)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()    
def getAhemdabadTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Ahemdabad Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(2295411)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getBangloreTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Banglore Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(2295420)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getBhopalTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Bhopal Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(2295407)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()  
def getChandigarhTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Chandigarh Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(2295391)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getChennaiTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Chennai Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(2295424)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getDelhiTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Delhi Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(2295019)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()  
def getHyderabadTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Hyderabad Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(2295414)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getIndoreTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Indore Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(2295408)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()    
def getKolkataTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Kolkata Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(2295386)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getLucknowTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Lucknow Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(2295377)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()     
def getMumbaiTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Mumbai Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(2295411) #MumbaiId
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getNagpurTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Nagpur Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(2282863)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getPatnaTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Patna Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(2295381)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()
def getSrinagarTrend(event=None):
    global windowRTT
    global twitterTrends
    global window
    windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowRBB.place(x=0, y=30, width=316, height=270)
    scrollbarTrends = Scrollbar(windowRBB)
    scrollbarTrends.pack( side = RIGHT, fill=Y )
    text = Text(windowRBB, yscrollcommand=scrollbarTrends.set,font=setTextFoneForTopTrend)
    text.delete('1.0', END)
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Srinagar Trends",font=fontThree, borderwidth=2, relief="groove")
    twitterTrends.place(x=0, y=0, width=314, height=30)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth)
    tre = api.trends_place(2295387)
    dataObtainedFromLocationId= tre[0] 
    currentTrending = dataObtainedFromLocationId['trends']
    nam = [trend['name'] for trend in currentTrending]
    topicName = '\n'.join(nam)
    topicName+="\n"
    text.insert(INSERT,topicName,'colo')
    scrollbarTrends.config(command=text.yview)
    text.pack()    
def onClickRetriveData(event=None):
    global search
    global window
    global windowMM
    global noOfTweets
    global isDataRetrived
    input =search.get()
    path="BotvsHumanData\\"+input+".csv"
    if os.path.exists(path):
        os.remove(path)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    enterQuery =input
    mT = 10000
    tPQ = 100
    sinceId = None
    mi = -1
    tc = 0
    counter=0;
    tex=""
    windowRB=Frame(window,borderwidth=2, relief="ridge",bg="#ffffff")
    windowRB["bg"] = "#ffffff"
    windowRB.place(x=0, y=330, width=316, height=400)
    scrollbarTopTweets = Scrollbar(windowRB)
    scrollbarTopTweets.pack( side = RIGHT, fill=Y )
    text = Text(windowRB, yscrollcommand=scrollbarTopTweets.set,font=setTextFoneForTopTweetst)
    text.delete('1.0', END)
    windowMMM=Frame(windowMM,borderwidth=2, relief="ridge",bg="#ffffff")
    windowMMM["bg"] = "#ffffff"
    windowMMM.place(x=0, y=0, width=1050, height=600)
    scrollbarAllTweetDetails = Scrollbar(windowMMM)
    scrollbarAllTweetDetails.pack( side = RIGHT, fill=Y )
    allTweetInfo=""
    allText = Text(windowMMM, yscrollcommand=scrollbarAllTweetDetails.set,font=setTextFoneForAllTweet,height=35,width=112)
    allText.delete('1.0', END)
    f = open(path, "a",newline='')
    fw = csv.writer(f)
    fw.writerow(['Tweet Id','User Name','Screen Name', 'Location','Profile Description', 'Followers Count', 'Friends Count','Listed Count','Tweet Created Time','Favorites Count','Verified Profile','Tweet Count','Language','Tweet','Default Profile','Default Profile Image'])
    f.close()
    f =path
    with open(f, 'a',newline='') as f:
        fw = csv.writer(f)
        while tc < mT:
            try:
                if (mi <= 0):
                    nT = api.search(q=enterQuery, count=tPQ,tweet_mode='extended')
                else:
                    nT = api.search(q=enterQuery, count=tPQ,max_id=str(mi-1),tweet_mode='extended')
                if not nT:
                    print("No Further Tweets Found")
                    break
                for tweet in nT:
                    if (not tweet.retweeted) and ('RT @' not in tweet.full_text) and tweet.lang == "en":
                        fw.writerow([str(int(float(tweet.id))),str(tweet.user.screen_name),str(tweet.user.name.encode('utf-8')),str((tweet.user.location).encode('unicode-escape').decode('utf-8')),str((tweet.user.description).encode('unicode-escape').decode('utf-8')),str(tweet.user.followers_count),str(tweet.user.friends_count),str(tweet.user.listed_count),str(tweet.created_at),str(tweet.favorite_count),str((tweet.user.verified)),str(tweet.user.statuses_count),'en',str(tweet.full_text.encode('utf-8')),str(tweet.user.default_profile),str(tweet.user.default_profile_image)])
                        
                        allTweetInfo+="Tweet Id: "+str(int(float(tweet.id)))+"\n\nUser Name: "+str(tweet.user.screen_name)+"\n\nScreen Name: "+str(tweet.user.name.encode('utf-8'))+"\n\nLocation: "+str((tweet.user.location).encode('unicode-escape').decode('utf-8'))+"\n\nProfile Description: "+str((tweet.user.description).encode('unicode-escape').decode('utf-8'))+"\n\nFollowers Count: "+str(tweet.user.followers_count)+"\n\nFriends Count: "+str(tweet.user.friends_count)+"\n\nListed Count: "+str(tweet.user.listed_count)+"\n\nTweet Created Time: "+str(tweet.created_at)+"\n\nFavorites Count: "+str(tweet.favorite_count)+"\n\nVerified Profile: "+str((tweet.user.verified))+"\n\nTweet Count: "+str(tweet.user.statuses_count)+"\n\nLanguage: English"+"\n\nTweet: "+str(tweet.full_text.encode('utf-8'))+"\n\nDefault Profile: "+str(tweet.user.default_profile)+"\n\nDefault Profile Image: "+str(tweet.user.default_profile_image)+"\n\n*******\n\n"
                    if(tweet.user.verified and ('RT @' not in tweet.full_text) and tweet.lang == "en"):
                        tex+=str(tweet.user.name.encode('utf-8'))+" Tweeted:\n"+" "+str(tweet.full_text.encode('utf-8'))+"\nReweetCount="+str(tweet.retweet_count)+"\n"+"********\n"
                    counter+=1
                tc += len(nT)
                print("Downloaded {0} Tweets".format(counter))
                mi = nT[-1].id
            except tweepy.TweepError as e:
                break
    f.close()
    print ("File Created Successfully")
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    text.insert(INSERT,tex,'colo')
    scrollbarTopTweets.config(command=text.yview)
    text.pack()
    text.config(state=DISABLED)
    
    allText.tag_config('colo', background="#ffffff", foreground="#000000")
    allText.insert(INSERT,allTweetInfo,'colo')
    scrollbarAllTweetDetails.config(command=allText.yview)
    allText.pack()
    allText.config(state=DISABLED)
    allText.place(x=0,y=0)
    isDataRetrived=1
def realTimeData(event=None):
    global search
    global window
    global windowMM
    global noOfTweets
    input =search.get()
    global isDataRetrived
    path="BotvsHumanData\\"+input+".csv"
    if os.path.exists(path):
        os.remove(path)
    c_key = "0i5s4gl3pqjBo9gEd8nBZQWLu"
    c_sec = "1YHtgjdBIq0wVRX6OfBtPGedGNPCTI04UsU8u8qmwUIvahvH9W"
    a_tok = "1112250983256489984-7cftG6tZ2iw4VZlNT7Nh3an9lUpfQs"
    a_sec = "ZUeeBoAjkz8ZpDlQYXMsfTL1BaV8sZDxtjoCP4TGn3uDu"
    auth = OAuthHandler(c_key, c_sec)
    auth.set_access_token(a_tok,a_sec)
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    enterQuery =input
    mT = 1000
    tPQ = 100
    sinceId = None
    mi = -1
    tc = 0
    counter=0;
    tex=""
    windowRB=Frame(window,borderwidth=2, relief="ridge",bg="#ffffff")
    windowRB["bg"] = "#ffffff"
    windowRB.place(x=0, y=330, width=316, height=400)
    scrollbarTopTweets = Scrollbar(windowRB)
    scrollbarTopTweets.pack( side = RIGHT, fill=Y )
    text = Text(windowRB, yscrollcommand=scrollbarTopTweets.set,font=setTextFoneForTopTweetst)
    text.delete('1.0', END)
    windowMMM=Frame(windowMM,borderwidth=2, relief="ridge",bg="#ffffff")
    windowMMM["bg"] = "#ffffff"
    windowMMM.place(x=0, y=0, width=1050, height=600)
    scrollbarAllTweetDetails = Scrollbar(windowMMM)
    scrollbarAllTweetDetails.pack( side = RIGHT, fill=Y )
    allTweetInfo=""
    allText = Text(windowMMM, yscrollcommand=scrollbarAllTweetDetails.set,font=setTextFoneForAllTweet,height=35,width=112)
    allText.delete('1.0', END)
    f = open(path, "a",newline='')
    fw = csv.writer(f)
    fw.writerow(['Tweet Id','User Name','Screen Name', 'Location','Profile Description', 'Followers Count', 'Friends Count','Listed Count','Tweet Created Time','Favorites Count','Verified Profile','Tweet Count','Language','Tweet','Default Profile','Default Profile Image'])
    f.close()
    f =path
    with open(f, 'a',newline='') as f:
        fw = csv.writer(f)
        while tc < mT:
            try:
                if (mi <= 0):
                    nT = api.search(q=enterQuery, count=tPQ,tweet_mode='extended')
                else:
                    nT = api.search(q=enterQuery, count=tPQ,max_id=str(mi-1),tweet_mode='extended')
                if not nT:
                    print("No Further Tweets Found")
                    break
                for tweet in nT:
                    if (not tweet.retweeted) and ('RT @' not in tweet.full_text) and tweet.lang == "en":
                        fw.writerow([str(int(float(tweet.id))),str(tweet.user.screen_name),str(tweet.user.name.encode('utf-8')),str((tweet.user.location).encode('unicode-escape').decode('utf-8')),str((tweet.user.description).encode('unicode-escape').decode('utf-8')),str(tweet.user.followers_count),str(tweet.user.friends_count),str(tweet.user.listed_count),str(tweet.created_at),str(tweet.favorite_count),str((tweet.user.verified)),str(tweet.user.statuses_count),'en',str(tweet.full_text.encode('utf-8')),str(tweet.user.default_profile),str(tweet.user.default_profile_image)])
                        
                        allTweetInfo+="Tweet Id: "+str(int(float(tweet.id)))+"\n\nUser Name: "+str(tweet.user.screen_name)+"\n\nScreen Name: "+str(tweet.user.name.encode('utf-8'))+"\n\nLocation: "+str((tweet.user.location).encode('unicode-escape').decode('utf-8'))+"\n\nProfile Description: "+str((tweet.user.description).encode('unicode-escape').decode('utf-8'))+"\n\nFollowers Count: "+str(tweet.user.followers_count)+"\n\nFriends Count: "+str(tweet.user.friends_count)+"\n\nListed Count: "+str(tweet.user.listed_count)+"\n\nTweet Created Time: "+str(tweet.created_at)+"\n\nFavorites Count: "+str(tweet.favorite_count)+"\n\nVerified Profile: "+str((tweet.user.verified))+"\n\nTweet Count: "+str(tweet.user.statuses_count)+"\n\nLanguage: English"+"\n\nTweet: "+str(tweet.full_text.encode('utf-8'))+"\n\nDefault Profile: "+str(tweet.user.default_profile)+"\n\nDefault Profile Image: "+str(tweet.user.default_profile_image)+"\n\n*******\n\n"
                    if(tweet.user.verified and ('RT @' not in tweet.full_text) and tweet.lang == "en"):
                        tex+=str(tweet.user.name.encode('utf-8'))+" Tweeted:\n"+" "+str(tweet.full_text.encode('utf-8'))+"\nReweetCount="+str(tweet.retweet_count)+"\n"+"********\n"
                    counter+=1
                tc += len(nT)
                print("Downloaded {0} Tweets".format(counter))
                mi = nT[-1].id
            except tweepy.TweepError as e:
                break
    f.close()
    print ("File Created Successfully")
    text.tag_config('colo', background="#ffffff", foreground="#000000")
    text.insert(INSERT,tex,'colo')
    scrollbarTopTweets.config(command=text.yview)
    text.pack()
    text.config(state=DISABLED)
    
    allText.tag_config('colo', background="#ffffff", foreground="#000000")
    allText.insert(INSERT,allTweetInfo,'colo')
    scrollbarAllTweetDetails.config(command=allText.yview)
    allText.pack()
    allText.config(state=DISABLED)
    allText.place(x=0,y=0)
    isDataRetrived=1
def startAnalysis(event=None):
    global search
    global isDataRetrived
    global botCount
    global humanCount
    global totalTweetData
    botCount=0
    humanCount=0
    totalTweetData=0
    windowMMM=Frame(windowMM,borderwidth=2, relief="ridge",bg="#ffffff")
    windowMMM["bg"] = "#ffffff"
    windowMMM.place(x=0, y=0, width=1050, height=600)
    scrollbarAllTweetDetails = Scrollbar(windowMMM)
    scrollbarAllTweetDetails.pack( side = RIGHT, fill=Y )
    allTweetInfo=""
    allText = Text(windowMMM, yscrollcommand=scrollbarAllTweetDetails.set,font=setTextFoneForAllTweet,height=35,width=112)
    allText.delete('1.0', END)
    if isDataRetrived==1:
        allText.tag_config('colo', background="#ffffff", foreground="#000000")
        allText.insert(INSERT,"Processing....",'colo')
        scrollbarAllTweetDetails.config(command=allText.yview)
        allText.pack()
        allText.config(state=DISABLED)
        allText.place(x=0,y=0)
        input =search.get()
        if os.path.exists("BotvsHumanData\\"+input+"_human.csv"):
            os.remove("BotvsHumanData\\"+input+"_human.csv")
        if os.path.exists("BotvsHumanData\\"+input+"_bot.csv"):
            os.remove("BotvsHumanData\\"+input+"_bot.csv")    
        path="BotvsHumanData\\"+input+".csv"
        csvFile = open(path)
        nlFilcontains = len(csvFile.readlines())
        reader = csv.reader(path)
        fileStroed=open(path, "r")
        reader = csv.reader(fileStroed)
        dataModel = list(reader)
        profileDetection=[]
        botAum="arse ass asshole bastard bitch bollocks frigger fuck damn goddamn godsdamn hell holy horseshit Jesus Christ Harold Christ Jesus wept Jesus Mary Joseph Judas Priest motherfucker nigga nigger prick shit ass shitass slut bot b0t cannabis tweet mishear follow me updates ever gorilla yes_ofc forget expos kill clit bbb butt fuck XXX sex truthe fake anony free virus funky RNA kuck jargon funk nerd swag jack bang bonsai chick prison paper pokem freak ffd dunia clone genie bbb ffd onlyman emoji joke troll droop free every wow cheese yeah bio magic wizard face more"
        result="Result Column One Indicates Twitter User Unique Id"+" "+"Column Two Indicates Twitter User Name\n"
        humanData="List Of Human Profile Are As Follows:\n"+""
        botData="List Of Bot Profile Are As Follows\n"        
        for x in range(2,int(nlFilcontains)):
            if(str(dataModel[x][10])=="False"):
                counter=0
                profileCounter=0
                pls=0
                words = (dataModel[x][13])
                for wordCloud in words:
                    if wordCloud in botAum and "#" not in wordCloud:
                        counter+=1
                    elif wordCloud not in botAum and "#" in wordCloud:
                        counter+=1
                if str(dataModel[x][1]) in botAum:
                    profileCounter=1
                if len(str(dataModel[x][3]))==0:
                    pls=1
                if int(str(dataModel[x][5]))==0 and int(str(dataModel[x][6]))!=0 and str(dataModel[x][14])=="False" and str(dataModel[x][15])=="False":
                    if dataModel[x][1] not in botData:
                        botData+=dataModel[x][0]+"    "+dataModel[x][1]+"\n"   
                        botCount=botCount+1
                        totalTweetData=totalTweetData+1
                else:
                    if int(str(dataModel[x][11]))>=6000 and str(dataModel[x][14])=="False" and str(dataModel[x][15])=="False":
                        if dataModel[x][1] not in botData:
                            botData+=dataModel[x][0]+"    "+dataModel[x][1]+"\n"   
                            botCount=botCount+1
                            totalTweetData=totalTweetData+1
                    else:
                        if counter>10 and profileCounter==1 and pls==1:
                            if dataModel[x][1] not in botData:
                                botData+=dataModel[x][0]+"    "+dataModel[x][1]+"\n"   
                                botCount=botCount+1
                                totalTweetData=totalTweetData+1
                        else:
                            if dataModel[x][1] not in humanData:
                                humanData+=dataModel[x][0]+"    "+dataModel[x][1]+"\n"   
                                humanCount=humanCount+1
                                totalTweetData=totalTweetData+1
            else:
                if dataModel[x][1] not in humanData:
                    humanData+=dataModel[x][0]+"    "+dataModel[x][1]+"\n"   
                    humanCount=humanCount+1
                    totalTweetData=totalTweetData+1
                
        prediction=result+"\n"+botData+"\n"+humanData
        allText.config(state="normal")
        allText.delete('1.0', END)
        allText.tag_config('colo', background="#ffffff", foreground="#000000")
        allText.insert(INSERT,prediction,'colo')
        scrollbarAllTweetDetails.config(command=allText.yview)
        allText.pack()
        allText.config(state=DISABLED)
        allText.place(x=0,y=0)    
        isDataRetrived=1
    else:
        print("Data Not Available To Analysis First You Need To Retrive Data From Twitter....")
        allText.tag_config('colo', background="#ffffff", foreground="#000000")
        allText.insert(INSERT,"Data Not Available To Analysis First You Need To Retrive Data From Twitter....",'colo')
        scrollbarAllTweetDetails.config(command=allText.yview)
        allText.pack()
        allText.config(state=DISABLED)
        allText.place(x=0,y=0)
        isDataRetrived=1
def visualHumanVsBot():
    global window, windowMM,imgHappy,imgBackground, botCount,humanCount,totalTweetData,search
    string="Bot vs Human Analysis On Query="
    inputData=search.get()
    windowMM.destroy()
    windowMM=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
    windowMM.place(x=318, y=60, width=1050, height=600)
    
    title = Label(windowMM, text=string+inputData+" "+"Total No Of Tweets="+str(totalTweetData),font=fontFour)
    title.place(x=80, y=20, width=900, height=30)
    canvasHappy = Canvas(windowMM, width =200, height =200)      
    canvasHappy.pack()      
    imgHappy = ImageTk.PhotoImage(Image.open("bot.png"))     
    canvasHappy.create_image(0,0, anchor=NW, image=imgHappy)
    canvasHappy.place(x=40,y=60)
    
    titleP = Label(windowMM, text="Number Of Bot Profile Detected On Twitter="+str(botCount),font=fontFour)
    titleP.place(x=260, y=80, width=600, height=30)
    
    canvasBackground = Canvas(windowMM, width =200, height =200)      
    canvasBackground.pack()      
    imgBackground = ImageTk.PhotoImage(Image.open("human.png"))     
    canvasBackground.create_image(0,0, anchor=NW, image=imgBackground)
    canvasBackground.place(x=40,y=300)
    
    titleN = Label(windowMM, text="Number Of Human Profile Detected On Twitter="+str(humanCount),font=fontFour)
    titleN.place(x=260, y=320, width=600, height=30)

def SendEmailFile(event=None):
    global windowMM
    global botCount
    global humanCount
    global totalTweetData
    global search
    im=ImageGrab.grab(bbox=(340,120,1360,600))
    fp = "C:\\Users\\User\\Desktop\\usinglstm\\analysis\\output.png"
    im.save(fp)
    def isEmailEntered(event):
        global isEmailId
        if isEmailId:
            isEmailId = False
            searchEmail.delete(0, "end")
    def sendEmailer():
        global isEmailId
        sender = "Botsvshuman@gmail.com"
        sender_password = "Admin@123"
        receivers=searchEmail.get()
        windowEmail.destroy()
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receivers
        msg['Subject'] = "Bot vs Human Detection Final Year Project"
        body ="PFA,\n\nResult For Bot vs Human Analaysis Is As Follows:\nSearch Query="+str(search.get())+"\nAnalysis On Total Number Of Tweets="+str(totalTweetData)+"\n"+"Total Number Of Bot Account Detected="+str(botCount)+"\nTotal Number Of Human Account Detected="+str(humanCount)+"\n\nThis Is Final Year Project Demo"
        msg.attach(MIMEText(body, 'plain'))
        attachment = open(fp, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename=output.png")
        msg.attach(part)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender, sender_password)
        text = msg.as_string()
        s.sendmail(sender, receivers, text)
        s.quit()
        isEmailId=True
    def scloseEmailPopup():
        windowEmail.destroy()
    windowEmail=Frame(window,borderwidth=2, relief="ridge",bg="#FFFFFF")
    windowEmail.place(x=533, y=250, width=300, height=135)
    searchEmail=Entry(windowEmail, font=fontFour,borderwidth=2,  relief="groove" )
    searchEmail.insert(0, 'Enter Email ID')
    searchEmail.bind('<FocusIn>',isEmailEntered)
    searchEmail.place(x=10, y=20, width=280, height=40)
    closeEmail=Button(windowEmail,text="Close",fg='#ffffff', bg="#1E88E5", font=fontTwo,borderwidth=2, relief="raised",command = scloseEmailPopup)
    closeEmail.place(x=55, y=80, width=80, height=30)
    buttonEmail=Button(windowEmail,text="OK",fg='#ffffff', bg="#1E88E5", font=fontTwo,borderwidth=2, relief="raised",command = sendEmailer)
    buttonEmail.place(x=165, y=80, width=80, height=30)


def saveImageFile(event=None):
    global windowMM
    im=ImageGrab.grab(bbox=(340,120,1360,600))
    fp = "C:\\Users\\User\\Desktop\\usinglstm\\analysis\\output.png"
    im.save(fp)
    
menu=Menu(window)
window.config(menu=menu)

selectLocation=Menu(menu,tearoff=0)
menu.add_cascade(font=mainMenuFont,label="Select Location", menu=selectLocation)

australia=Menu(selectLocation,tearoff=0)
selectLocation.add_cascade(font=mainMenuFont,label="Australia", menu=australia)
australia.add_command(label="Adelaide", command=getAdelaideTrend)
australia.add_command(label="Brisbane", command=getBrisbaneTrend)
australia.add_command(label="Canberra", command=getCanberraTrend)
australia.add_command(label="Melbourne", command=getMelbourneTrend)
australia.add_command(label="Perth", command=getPerthTrend)
australia.add_command(label="Sydney", command=getSydneyTrend)

india=Menu(selectLocation,tearoff=0)
selectLocation.add_cascade(font=mainMenuFont,label="INDIA", menu=india)

india.add_command(label="Bangalore", command=getBangloreTrend)
india.add_command(label="Bhopal", command=getBhopalTrend)
india.add_command(label="Chennai", command=getChennaiTrend)
india.add_command(label="Hyderabad", command=getHyderabadTrend)
india.add_command(label="Indore", command=getIndoreTrend)
india.add_command(label="Kolkata", command=getKolkataTrend)
india.add_command(label="Lucknow", command=getLucknowTrend)
india.add_command(label="Mumbai", command=getMumbaiTrend)
india.add_command(label="Nagpur", command=getNagpurTrend)
india.add_command(label="Patna", command=getPatnaTrend)
india.add_command(label="Srinagar", command=getSrinagarTrend)


rTD=Menu(menu,tearoff=0)
menu.add_cascade(label="Analysis On Real Time Data", menu=rTD)
rTD.add_command(label="Bot vs Human Analysis On Real Time Data", command=realTimeData)
analysis=Menu(menu,tearoff=0)
menu.add_cascade(font=mainMenuFont,label="Analysis", menu=analysis)
analysis.add_command(label="View Prediction", command=startAnalysis)
analysis.add_command(label="BotvsHuman Detection", command=visualHumanVsBot)

windowMT=Frame(window,borderwidth=2, relief="ridge",bg="#1E88E5")
windowMT.place(x=318, y=0, width=1050, height=60)
search=Entry(windowMT, font=fontTwo,borderwidth=2,  relief="groove" )
search.insert(0, 'Enter Search Query...')
search.bind('<FocusIn>',isSearchEntered)
search.place(x=150, y=20, width=550, height=25)
searchButton=Button(windowMT,text="Search",fg='#ffffff', bg="#424242", font=fontOne,borderwidth=2, relief="raised",  command=onClickRetriveData)
searchButton.place(x=710, y=17, width=100, height=30)
windowMM=Frame(window,borderwidth=2, relief="ridge",bg="#ffffff")
windowMM.place(x=318, y=60, width=1050, height=600)
windowRTC=Frame(window,borderwidth=2, relief="ridge",bg="#ffffff")
windowRTC.place(x=0, y=0, width=316, height=30)
twitterTrends = Label(windowRTC,background="#263238",foreground="#ffffff", text="Current Trends On Twitter",font=fontThree, borderwidth=2, relief="groove")
twitterTrends.place(x=0, y=0, width=314, height=30)
windowRTT=Frame(window,borderwidth=2, relief="ridge",bg="#ffffff")
windowRTT["bg"] = "#ffffff"
windowRTT.place(x=0, y=30, width=316, height=270)
scrollbarTrendss = Scrollbar(windowRTT)
scrollbarTrendss.pack( side = RIGHT, fill=Y )
windowRTCC=Frame(window,borderwidth=2, relief="ridge",bg="#ffffff")
windowRTCC.place(x=0, y=300, width=316, height=30)
twitterTrends = Label(windowRTCC, background="#263238",foreground="#ffffff", text="Verified User Tweets",font=fontThree, borderwidth=2, relief="groove")
twitterTrends.place(x=0, y=0, width=314, height=30)
windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="#ffffff")
windowRBB["bg"] = "#ffffff"
windowRBB.place(x=0, y=330, width=316, height=400)
scrollbarTopTweetss = Scrollbar(windowRBB)
scrollbarTopTweetss.pack( side = RIGHT, fill=Y )

shareEmi=Button(window,text="E-Mail",font=fontTwo,borderwidth=2, relief="raised",fg='#ffffff', bg="#1E88E5", command=SendEmailFile)
shareEmi.place(x=1050, y=680, width=100, height=30)

saveButton=Button(window,text="Save",font=fontTwo, borderwidth=2, relief="raised", fg='#ffffff', bg="#1E88E5", command=saveImageFile)
saveButton.place(x=1180, y=680, width=120, height=30)

window.mainloop()
