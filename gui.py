import tkinter.filedialog as filedialog
from tkinter import*
from tkinter import font
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
menu=Menu(window)
window.config(menu=menu)
selectLocation=Menu(menu,tearoff=0)
menu.add_cascade(font=mainMenuFont,label="Select Location", menu=selectLocation)

australia=Menu(selectLocation,tearoff=0)
selectLocation.add_cascade(font=mainMenuFont,label="Australia", menu=australia)
australia.add_command(label="Adelaide", command=doNothing)
australia.add_command(label="Brisbane", command=doNothing)
australia.add_command(label="Canberra", command=doNothing)
australia.add_command(label="Melbourne", command=doNothing)
australia.add_command(label="Perth", command=doNothing)
australia.add_command(label="Sydney", command=doNothing)

india=Menu(selectLocation,tearoff=0)
selectLocation.add_cascade(font=mainMenuFont,label="INDIA", menu=india)
india.add_command(label="Ahmedabad", command=doNothing)
india.add_command(label="Bangalore", command=doNothing)
india.add_command(label="Bhopal", command=doNothing)
india.add_command(label="Chennai", command=doNothing)
india.add_command(label="Hyderabad", command=doNothing)
india.add_command(label="Indore", command=doNothing)
india.add_command(label="Kolkata", command=doNothing)
india.add_command(label="Lucknow", command=doNothing)
india.add_command(label="Mumbai", command=doNothing)
india.add_command(label="Nagpur", command=doNothing)
india.add_command(label="Patna", command=doNothing)
india.add_command(label="Srinagar", command=doNothing)

window.mainloop()