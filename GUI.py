import tkinter as tk
from PIL import ImageTk, Image

HEIGHT = 700
WIDTH = 1200

global money
global carbon
global happiness
global year

global treeNumber
global utilityUsage
global factoryNumber

global deltaCO2
global deltaMoney
global deltaHappiness

money = 100
carbon = 412
happiness = 0.6

year = 2023

treeNumber = 6
utilityUsage = 5
factoryNumber = 4


def closeTutorial():
    tutorialFrame.lower()

def selectMChar():
    character["image"] = mchar
    charSelectFrame.lower()

def selectFChar():
    character["image"] = fchar
    charSelectFrame.lower()

#TODO: write this
def endturn():
    print("temp")

root = tk.Tk()


#images
mchar = tk.PhotoImage(file="mChar.png")
fchar = tk.PhotoImage(file="fChar.png")
nochar = tk.PhotoImage(file="nochar.png")
smallmchar = ImageTk.PhotoImage(Image.open("mChar.png").resize((200, 200), Image.ANTIALIAS))
smallfchar = ImageTk.PhotoImage(Image.open("fChar.png").resize((200, 200), Image.ANTIALIAS))

#this is just here to reserve the space on the gui
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()



mainFrame = tk.Frame(root, bg="white")
mainFrame.place(relheight = 1, relwidth=1, relx=0, rely=0)


charFrame = tk.Frame(mainFrame, bg="white")
charFrame.place(relx=0.3, rely=0, relheight=0.55, relwidth=0.7)
character = tk.Label(charFrame, image=nochar, bg="white")
character.place(relx = 0.2, rely=0.15, relwidth=0.6, relheight=0.8)

endTurnButton = tk.Button(charFrame, text= "End Turn", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", command=endturn)
endTurnButton.place(relx=0.7, rely=0.4, relheight=0.2, relwidth=0.2)


#statistics - bottom right
statsFrame = tk.Frame(mainFrame, bg="#f8f6f2")
statsFrame.place(relheight=0.45, relwidth=0.7, relx = 0.3, rely=0.55)

approvalBar = tk.Frame(statsFrame, bg="white", highlightbackground="#a69d80", highlightthickness=2)
approvalBar.place(relx=0.2, rely = 0.2, relheight= 0.1, relwidth=0.6)

#TODO: approvalbarvalue changes with approval rating. need to update
approvalBarValue = tk.Frame(statsFrame, bg="#e5e0d2")
approvalBarValue.place(relx=0.203, rely = 0.206, relheight= 0.088, relwidth=0.594 * 0.6)
approvalLabel = tk.Label(statsFrame, text="Approval (%): ", font=("Cambria", 12),  bg="#f8f6f2", justify="left")
approvalLabel.place(relx=0.06, rely=0.206, relheight=0.088, relwidth=0.14)

#TODO: this is the number changed when approval rating changes.
approvalValue = tk.Label(statsFrame, text="60", font=("Cambria", 12),  bg="#f8f6f2", justify="left")
approvalValue.place(relx=0.8, rely=0.206, relheight=0.088, relwidth=0.05)


moneyBar = tk.Frame(statsFrame, bg="white", highlightbackground="#a69d80", highlightthickness=2)
moneyBar.place(relx=0.2, rely = 0.45, relheight= 0.1, relwidth=0.6)
moneyBarValue = tk.Frame(statsFrame, bg="#e5e0d2")
moneyBarValue.place(relx=0.203, rely = 0.456, relheight= 0.088, relwidth=0.594 * 0.5)
moneyLabel = tk.Label(statsFrame, text="Budget ($k): ", font=("Cambria", 12),  bg="#f8f6f2", justify="left")
moneyLabel.place(relx=0.06, rely = 0.456, relheight= 0.088, relwidth=0.14)

moneyValue = tk.Label(statsFrame, text="100", font=("Cambria", 12),  bg="#f8f6f2", justify="left")
moneyValue.place(relx=0.8, rely=0.456, relheight=0.088, relwidth=0.05)

carbonBar = tk.Frame(statsFrame, bg="white", highlightbackground="#a69d80", highlightthickness=2)
carbonBar.place(relx=0.2, rely = 0.7, relheight= 0.1, relwidth=0.6)
carbonBarValue = tk.Frame(statsFrame, bg="#e5e0d2")
carbonBarValue.place(relx=0.203, rely = 0.706, relheight= 0.088, relwidth=0.594 * 0.75)
carbonLabel = tk.Label(statsFrame, text="Carbon (ppm): ", font=("Cambria", 12),  bg="#f8f6f2", justify="left")
carbonLabel.place(relx=0.06, rely = 0.706, relheight= 0.088, relwidth=0.14)

carbonValue = tk.Label(statsFrame, text="412", font=("Cambria", 12),  bg="#f8f6f2", justify="left")
carbonValue.place(relx=0.8, rely=0.706, relheight=0.088, relwidth=0.05)


actionBar = tk.Frame(mainFrame, bg="#d6cfb7")
actionBar.place(relheight=1, relwidth=0.3, relx=0, rely=0)

actionBarTitle = tk.Label(actionBar, text="Your Current Actions", font=("Cambria", 15, "bold"), bg="#f3efe1")
actionBarTitle.place(relx = 0.05, rely = 0.05, relheight=0.06, relwidth=0.9)

#TODO: ADD COMMAND FOR CHANGE TREES
addTrees = tk.Button(actionBar, text= "+", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1")
subtractTrees = tk.Button(actionBar, text= "-", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1")
addTrees.place(relwidth=0.15, relheight=0.05, relx = 0.05, rely = 0.7)
subtractTrees.place(relwidth=0.15, relheight=0.05, relx = 0.8, rely = 0.7)

treesLabel = tk.Label(actionBar, text="Amount of trees: ", font=("Cambria", 11),  bg="#d6cfb7", justify="left")
treesLabel.place(relwidth=0.35, relheight=0.05, relx = 0.28, rely = 0.7)

#TODO: REPLACE NUM OF TREES WITH UPDATED VALUE IN FUNCTION
treesnum = tk.Label(actionBar, text="6", font=("Cambria", 12),  bg="#d6cfb7", justify="left")
treesnum.place(relwidth=0.1, relheight=0.05, relx = 0.64, rely = 0.7)


addFactories = tk.Button(actionBar, text= "+", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1")
subtractFactories = tk.Button(actionBar, text= "-", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1")
addFactories.place(relwidth=0.15, relheight=0.05, relx = 0.05, rely = 0.8)
subtractFactories.place(relwidth=0.15, relheight=0.05, relx = 0.8, rely = 0.8)

factoriesLabel = tk.Label(actionBar, text="Amount of Factories: ", font=("Cambria", 11),  bg="#d6cfb7", justify="left")
factoriesLabel.place(relwidth=0.36, relheight=0.05, relx = 0.27, rely = 0.8)

#TODO: REPLACE NUM OF FACTORIES WITH UPDATED VALUE IN FUNCTION
factoriesnum = tk.Label(actionBar, text="4", font=("Cambria", 12),  bg="#d6cfb7", justify="left")
factoriesnum.place(relwidth=0.1, relheight=0.05, relx = 0.64, rely = 0.8)


addUtilities = tk.Button(actionBar, text= "+", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1")
subtractUtilities = tk.Button(actionBar, text= "-", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1")
addUtilities.place(relwidth=0.15, relheight=0.05, relx = 0.05, rely = 0.9)
subtractUtilities.place(relwidth=0.15, relheight=0.05, relx = 0.8, rely = 0.9)

utilitiesLabel = tk.Label(actionBar, text="Amount of Utilities: ", font=("Cambria", 11),  bg="#d6cfb7", justify="left")
utilitiesLabel.place(relwidth=0.36, relheight=0.05, relx = 0.27, rely = 0.9)

#TODO: REPLACE NUM OF FACTORIES WITH UPDATED VALUE IN FUNCTION
utilitiesnum = tk.Label(actionBar, text="5", font=("Cambria", 12),  bg="#d6cfb7", justify="left")
utilitiesnum.place(relwidth=0.1, relheight=0.05, relx = 0.64, rely = 0.9)

situationFrame = tk.Frame(actionBar, bg="#f3efe1")
situationFrame.place(relwidth= 0.9, relheight= 0.5, relx = 0.05, rely = 0.15)


#tutorial stuff

tutorialFrame = tk.Frame(root, bg="white", bd=2, highlightbackground="#6b644e", highlightthickness=2)
tutorialFrame.place(relx = 0.2, rely = 0.2, relheight=0.6, relwidth=0.6)

tutorialTitle = tk.Label(tutorialFrame, font = ("Cambria", 16, "bold"), text= "Welcome to the Mission: Emission!", bg="white")
tutorialTitle.place(relx = 0.1, rely=0.15, relheight=0.1, relwidth=0.8)

tutorialText = tk.Label(tutorialFrame, font= ("Cambria", 12), bg="white", text="You have been elected as Mayor of Hackerstown! \n The goal of the game is to reduce CO2 emissions to 270ppm. \n Currently, it is at 412ppm. \n Each action will affect your approval, economy and carbon footprint. \n If your approval goes below 30%, you will be fired. \n If your money runs below 0, your city goes bankrupt. \n To win, fulfill all CO2 objectives while managing money and approval until 2050.")
tutorialText.place(relx=0.1, rely=0.25, relheight=0.45, relwidth=0.8)

tutorialOK=tk.Button(tutorialFrame, text= "Ok, let's play!", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", command=closeTutorial)
tutorialOK.place(relx=0.3, rely=0.8, relheight=0.15, relwidth=0.4)

#character select
charSelectFrame =tk.Frame(root, bg="white", bd=2, highlightbackground="#6b644e", highlightthickness=2)
charSelectFrame.place(relx = 0.2, rely = 0.2, relheight=0.6, relwidth=0.6)

charSelectTitle = tk.Label(charSelectFrame, font = ("Cambria", 16, "bold"), text= "Select Character", bg="white")
charSelectTitle.place(relx = 0.1, rely=0.15, relheight=0.1, relwidth=0.8)

mCharButton = tk.Button(charSelectFrame, image=smallmchar, command=selectMChar, bg="white")
mCharButton.place(relx=0.15, rely= 0.3, relheight= 0.6, relwidth= 0.3)

fCharButton = tk.Button(charSelectFrame, image=smallfchar, command=selectFChar, bg="white")
fCharButton.place(relx=0.55, rely= 0.3, relheight= 0.6, relwidth= 0.3)

root.title("Mission: Emission")
root.mainloop()
