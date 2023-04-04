import tkinter as tk
from PIL import ImageTk, Image
import random
import Situations
import os
import sys

HEIGHT = 700
WIDTH = 1200

name = " "
money = 100
carbon = 412
happiness = 0.6

year = 2023
allottedPredictions = 0
usedPredictions = 0

treeNumber = 6
utilityUsage = 5
factoryNumber = 4

tutorialStep=1

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def updateResourceLabels():
    approvalBarValue.place(relx=0.203, rely = 0.206, relheight= 0.088, relwidth=0.594 * happiness)
    approvalValue["text"] = f"{round(happiness*100, 3)}%" 
    if (money/100)*0.5 > 1:
        moneyBarValue.place(relx=0.203, rely = 0.456, relheight= 0.088, relwidth=0.594)
    else:
        moneyBarValue.place(relx=0.203, rely = 0.456, relheight= 0.088, relwidth=0.594 * (money/100) * 0.5)
    moneyValue["text"] = f"{round(money, 1)}"

    if ((carbon/412) * 0.75 > 549):
        carbonBarValue.place(relx=0.203, rely = 0.706, relheight= 0.088, relwidth=0.594)
    else:
        carbonBarValue.place(relx=0.203, rely = 0.706, relheight= 0.088, relwidth=0.594 * (carbon/412) * 0.75)
    if(carbon > 475):
        carbonBarValue["bg"]="#bc4c4c"
    elif(carbon < 270):
        carbonBarValue["bg"]="#73ba77"
    else:
        carbonBarValue["bg"]="#e5e0d2"
    carbonValue["text"] = f"{round(carbon,1)}"
    currentCO2["text"] = f"{round(carbon,1)} ppm"

def addTrees():
    global treeNumber
    if(treeNumber < 10):
        treeNumber += 1
    else:
        errorMessage["text"]= "Your city does not have\nenough space for more trees!"
    treesnum["text"]= str(treeNumber * 10)

def subtractTrees():
    global treeNumber
    if(treeNumber > 0):
        treeNumber -= 1
    else:
        errorMessage["text"]= "You can't cut down trees if there are none!"
    treesnum["text"]= str(treeNumber * 10)

def addUtility():
    global utilityUsage
    if(utilityUsage < 10):
        utilityUsage += 1
    else:
        errorMessage["text"]= "There are not enough people in\nyour city to build more utilities!"
    utilitiesnum["text"]= str(utilityUsage)

def subtractUtility():
    global utilityUsage
    if(utilityUsage > 0):
        utilityUsage -= 1
    else:
        errorMessage["text"]= "There are no utility facilities to destroy!"
    utilitiesnum["text"]= str(utilityUsage)

def addFactory():
    global factoryNumber
    if(factoryNumber < 10):
        factoryNumber += 1
    else:
        errorMessage["text"]= "There are not enough people\nwilling to work in factories!"
    factoriesnum["text"]= str(factoryNumber)

def subtractFactory():
    global factoryNumber
    if(factoryNumber > 0):
        factoryNumber -= 1
    else:
        errorMessage["text"]= "There are no more factories to destroy!"
    factoriesnum["text"]= str(factoryNumber)

def getProjections():
    global treeNumber
    global utilityUsage
    global factoryNumber
    global allottedPredictions
    global usedPredictions

    if(usedPredictions < allottedPredictions):

        if(round(utilityUsage*0.004 - factoryNumber*0.011 + outcomestats[2] - 0.001, 3) > 0):
            approvalPrediction["text"]="Projected Change in Approval: +"
        elif (round(utilityUsage*0.004 - factoryNumber*0.011 + outcomestats[2] - 0.001, 3) < 0):
            approvalPrediction["text"]="Projected Change in Approval: -"
        else:
            approvalPrediction["text"]="Projected Change in Approval: 0"

        if(round(utilityUsage*5 + factoryNumber*10 - treeNumber*9 + outcomestats[0], 3) > 0):
            budgetPrediction["text"]="Projected Change in Budget: +"
        elif (round(utilityUsage*5 + factoryNumber*10 - treeNumber*9 + outcomestats[0], 3) < 0):
            budgetPrediction["text"]="Projected Change in Budget: -"
        else:
            budgetPrediction["text"]="Projected Change in Budget: 0"

        if(round(utilityUsage*3 + factoryNumber*6 - treeNumber*6.5 + outcomestats[1], 3) > 0):
            co2Prediction["text"]="Projected Change in Carbon Levels: +"
        elif (round(utilityUsage*3 + factoryNumber*6 - treeNumber*6 + outcomestats[1], 3) < 0):
            co2Prediction["text"]="Projected Change in Carbon Levels: -"
        else:
            co2Prediction["text"]="Projected Change in Carbon Levels: 0"
        usedPredictions += 1

    elif (usedPredictions == 0):
        approvalPrediction["text"]= "Your analytics team was unable to gather any projections for this year."
        budgetPrediction["text"]= "There is nothing much you can do about it."
        co2Prediction["text"]= "They say they may have data for you next year."

    else:
        approvalPrediction["text"]= "Your analytics team is tired of you asking for more projections."
        budgetPrediction["text"]= "They tell you that time does not grow on trees."
        co2Prediction["text"]= "Maybe they will be ready for you next year..."


    projectionFrame.lift()

def closeProjections():
    projectionFrame.lower()

def closeTutorial():
    global tutorialStep
    if(tutorialStep == 1):

        tutorialOK["text"]="OK, LET'S PLAY!"
        tutorialText["text"]="Use the + and - buttons on the bottom right to control the number of \ntrees, factories and utility facilities in your city. \n\nEach has its ups and downs: \nPlanting trees costs money, but reduces carbon. \nFactories make money, but produce carbon and cause popular discontent.\n Utilities will make people happy and generate some income but also produce carbon. \n\nYou will also have to deal with random situations that pop up at times. \n\nAre you ready to save the planet?"
        tutorialStep += 1
    else:
        tutorialOK["text"]="NEXT"
        tutorialText["text"]="You have been elected as Mayor of Hackerstown! \n The goal of the game is to reduce CO2 emissions to 270ppm, the pre-industrial level. \nCurrently, it is at 412ppm. \n\n Each action will affect your approval, economy or carbon footprint. \n\n If your approval rating goes below 20%, you will be fired. \n\n If your money runs below 0, your city goes bankrupt. \n\n To win, fulfill all CO2 objectives while managing money and approval until 2050."
        tutorialStep = 1
        enableButtons()
        tutorialFrame.lower()

def openTutorial():
    tutorialFrame.lift() 
    disableButtons()

def selectMChar(entry):
    global name
    character["image"] = mchar
    name = entry
    if(len(name) > 0):
        nameDisplay["text"] = "Welcome, " + name + "!"
        situationTitle["text"] = "Important Message for Mayor " + name + "!"
        charSelectFrame.lower()
    else:
        nameMsg["text"]="Please enter a name!"

def selectFChar(entry):
    global name
    character["image"] = fchar
    name = entry
    if(len(name) > 0):
        nameDisplay["text"] = "Welcome, " + name + "!"
        situationTitle["text"] = "Important Message for Mayor " + name + "!"
        charSelectFrame.lower()
    else:
        nameMsg["text"]="Please enter a name!"

usedSituations = []
outcomestats = (0, 0, 0)

def generateSituation():
    global randnum
    randnum = random.randint(0, 27)
    while True:
        if randnum in usedSituations:
            randnum = random.randint(0, 27)
        else:
            usedSituations.append(randnum)
            break
    situationText["text"] = Situations.descriptions[randnum] + Situations.outcome1s[randnum][0] + Situations.outcome2s[randnum][0]
    situationFrame.lift()

def enableButtons():
    endTurnButton["state"]="normal"
    projectionsButton["state"]="normal"
    addTreesButton["state"]="normal"
    subtractTreesButton["state"]="normal"
    addFactories["state"]="normal"
    subtractFactories["state"]="normal"
    addUtilities["state"]="normal"
    subtractUtilities["state"]="normal"
    restartButton["state"]="normal"
    showTutorial["state"]="normal"

def disableButtons():
    endTurnButton["state"]="disabled"
    projectionsButton["state"]="disabled"
    addTreesButton["state"]="disabled"
    subtractTreesButton["state"]="disabled"
    addFactories["state"]="disabled"
    subtractFactories["state"]="disabled"
    addUtilities["state"]="disabled"
    subtractUtilities["state"]="disabled"
    restartButton["state"]="disabled"
    showTutorial["state"]="disabled"

def executeSituation(num):
    global outcomestats
    if(num == 1):
        outcomestats = Situations.outcome1s[randnum][1:4]
    if(num == 2):
        outcomestats = Situations.outcome2s[randnum][1:4]

    enableButtons()
    situationFrame.lower()

def checkWinLoss():
    if money < 0:
        reason["text"] = "You went bankrupt and your department has been disbanded."
        disableButtons()
        loseFrame.lift()
    elif carbon > 549:
        reason["text"] = "You went above the carbon emissions limit and you have \nbeen fired for failing to prevent carbon emission rates from skyrocketing."
        disableButtons()
        loseFrame.lift()
    elif happiness < 0.2:
        reason["text"] = "You were too unpopular and you have been fired \ndue to popular discontent. Better luck next time!"
        disableButtons()
        loseFrame.lift()
    elif year == 2050 and carbon > 270:
        reason["text"] = "You were unable to reach the 2050 carbon emission target, despite your impressive money and approval management skills."
        disableButtons()
        loseFrame.lift()
    elif year == 2050 and carbon <=270:
        successMsg["text"] = "Congrats, You were able to reach the 2050 carbon emission target!"
        disableButtons()
        winFrame.lift()

def endturn():
    
    global outcomestats
    global year
    global money
    global carbon
    global happiness
    
    global deltaCO2
    global deltaMoney
    global deltaHappiness

    global allottedPredictions
    global usedPredictions

    print(outcomestats)

    errorMessage["text"]= " "

    deltaCO2 = round(utilityUsage*3 + factoryNumber*6 - treeNumber*6.5 + outcomestats[1], 3)
    deltaMoney = round(utilityUsage*5 + factoryNumber*10 - treeNumber*9 + outcomestats[0], 3)
    deltaHappiness = round(utilityUsage*0.004 - factoryNumber*0.011 + outcomestats[2] - 0.001, 3)




    year += 1
    yearDisplay["text"] = str(year)
    money += deltaMoney
    carbon += deltaCO2
    if (happiness + deltaHappiness > 1):
        happiness = 1
    else:
        happiness += deltaHappiness
    updateResourceLabels()

    allottedPredictions = random.randint(0, 3)
    usedPredictions = 0

    checkWinLoss()

    if (random.randint(1,2) == 1):
        generateSituation()
        disableButtons()
    else:
        outcomestats = (0, 0, 0)   

def playAgain():
    global usedSituations
    global outcomestats
    global year
    global money
    global carbon
    global happiness
    global treeNumber
    global factoryNumber
    global utilityUsage
    global name
    global tutorialStep
    global nameEntry

    global allottedPredictions
    global usedPredictions
    
    money = 100
    carbon = 412
    happiness = 0.6

    tutorialStep=1

    year = 2023
    allottedPredictions = 0
    usedPredictions = 0

    treeNumber = 6
    utilityUsage = 5
    factoryNumber = 4

    usedSituations = []
    outcomestats = (0, 0, 0)   
    name = " "

    treesnum["text"]= str(treeNumber * 10)
    utilitiesnum["text"]= str(utilityUsage)
    factoriesnum["text"]= str(factoryNumber)
    yearDisplay["text"]=str(year)
    nameDisplay["text"]=" "
    nameMsg["text"]=" "
    nameEntry.delete(0, 'end')

    updateResourceLabels()
    disableButtons()

    mainFrame.lift()

    tutorialFrame.lift() 
    charSelectFrame.lift()

root = tk.Tk()

#images
mchar = tk.PhotoImage(file=resource_path("images/mChar.png"))
fchar = tk.PhotoImage(file=resource_path("images/fChar.png"))
nochar = tk.PhotoImage(file=resource_path("images/nochar.png"))
smallmchar = ImageTk.PhotoImage(Image.open(resource_path("images/mChar.png")).resize((175, 175), Image.ANTIALIAS))
smallfchar = ImageTk.PhotoImage(Image.open(resource_path("images/fChar.png")).resize((175, 175), Image.ANTIALIAS))

#this is just here to reserve the space on the gui
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#projected changes
projectionFrame = tk.Frame(root, bg="white", bd=2, highlightbackground="#6b644e", highlightthickness=2)
projectionFrame.place(relx = 0.2, rely = 0.2, relheight=0.6, relwidth=0.6)

projectionTitle = tk.Label(projectionFrame, font = ("Cambria", 16, "bold"), text= "Predicted Changes for Next Year", bg="white")
projectionTitle.place(relx = 0.1, rely=0.15, relheight=0.1, relwidth=0.8)

approvalPrediction = tk.Label(projectionFrame, font = ("Cambria", 14), text= "Projected Approval: ", bg="white")
approvalPrediction.place(relx=0.1, rely=0.25, relheight=0.15, relwidth=0.8)

budgetPrediction = tk.Label(projectionFrame, font = ("Cambria", 14), text= "Projected Money: ", bg="white")
budgetPrediction.place(relx=0.1, rely=0.4, relheight=0.15, relwidth=0.8)

co2Prediction = tk.Label(projectionFrame, font = ("Cambria", 14), text= "Projected Carbon Levels: ", bg="white")
co2Prediction.place(relx=0.1, rely=0.55, relheight=0.15, relwidth=0.8)

projectionOK = tk.Button(projectionFrame, text= "OK", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", command=lambda: closeProjections())
projectionOK.place(relwidth=0.4, relheight=0.2, relx = 0.3, rely = 0.7)

#Lose case
loseFrame = tk.Frame(root, bg="white", bd=2, highlightbackground="#6b644e", highlightthickness=2)
loseFrame.place(relx = 0.2, rely = 0.2, relheight=0.6, relwidth=0.6)

loseTitle = tk.Label(loseFrame, font = ("Cambria", 16, "bold"), text= "You Lost!", bg="white")
loseTitle.place(relx = 0.1, rely=0.15, relheight=0.1, relwidth=0.8)

reason = tk.Label(loseFrame, font= ("Cambria", 12), bg="white", text="temp")
reason.place(relx=0.1, rely=0.25, relheight=0.45, relwidth=0.8)

loseButton = tk.Button(loseFrame, text= "Play Again", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", command = lambda: playAgain())
loseButton.place(relwidth=0.4, relheight=0.2, relx = 0.3, rely = 0.7)

#Win case
winFrame = tk.Frame(root, bg="white", bd=2, highlightbackground="#6b644e", highlightthickness=2)
winFrame.place(relx = 0.2, rely = 0.2, relheight=0.6, relwidth=0.6)

winTitle = tk.Label(winFrame, font = ("Cambria", 16, "bold"), text= "You won!", bg="white")
winTitle.place(relx = 0.1, rely=0.15, relheight=0.1, relwidth=0.8)

successMsg = tk.Label(winFrame, font= ("Cambria", 12), bg="white", text="temp")
successMsg.place(relx=0.1, rely=0.25, relheight=0.45, relwidth=0.8)

winButton = tk.Button(winFrame, text= "Play Again", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", command= lambda: playAgain())
winButton.place(relwidth=0.4, relheight=0.2, relx = 0.3, rely = 0.7)


#The frame with the situation in it that pops up and disappears when you resolve it
situationFrame = tk.Frame(root, bg="white", bd=2, highlightbackground="#6b644e", highlightthickness=2)
situationFrame.place(relx = 0.2, rely = 0.2, relheight=0.6, relwidth=0.6)

situationTitle = tk.Label(situationFrame, font = ("Cambria", 16, "bold"), text= "Important Message!", bg="white")
situationTitle.place(relx = 0.1, rely=0.15, relheight=0.1, relwidth=0.8)


situationText = tk.Label(situationFrame, font= ("Cambria", 12), bg="white", text="temp")
situationText.place(relx=0.1, rely=0.25, relheight=0.45, relwidth=0.8)

situation1 = tk.Button(situationFrame, text= "1", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", command= lambda: executeSituation(1))
situation2 = tk.Button(situationFrame, text= "2", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", command= lambda: executeSituation(2))

situation1.place(relwidth=0.3, relheight=0.1, relx = 0.15, rely = 0.7)
situation2.place(relwidth=0.3, relheight=0.1, relx = 0.55, rely = 0.7)

mainFrame = tk.Frame(root, bg="white")
mainFrame.place(relheight = 1, relwidth=1, relx=0, rely=0)


#the frame with the character in it
charFrame = tk.Frame(mainFrame, bg="white")
charFrame.place(relx=0.3, rely=0, relheight=0.55, relwidth=0.7)
character = tk.Label(charFrame, image=nochar, bg="white")
character.place(relx = 0.2, rely=0.15, relwidth=0.6, relheight=0.8)
nameDisplay = tk.Label(charFrame, text= " ", font=("Cambria", 16, "bold"), bg="white")
nameDisplay.place(relx = 0.09, rely=0.1, relheight=0.1, relwidth=0.8 ) 

endTurnButton = tk.Button(charFrame, text= "End Turn", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", state="disabled", command=endturn)
endTurnButton.place(relx=0.7, rely=0.4, relheight=0.2, relwidth=0.2)

projectionsButton = tk.Button(charFrame, text= "Get \nProjections", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", state="disabled", command=getProjections)
projectionsButton.place(relx=0.1, rely=0.4, relheight=0.2, relwidth=0.2)

restartButton = tk.Button(charFrame, text= "↻", background="white", font=("Cambria",16), activebackground="#fdfaf1", state="disabled", command=playAgain)
restartButton.place(relx=0.92, rely=0.03, relheight=0.1, relwidth=0.05)

showTutorial = tk.Button(charFrame, text= "?", background="white", font=("Cambria",16), activebackground="#fdfaf1", state="disabled", command=lambda: openTutorial())
showTutorial.place(relx=0.86, rely=0.03, relheight=0.1, relwidth=0.05)


#statistics - bottom right
statsFrame = tk.Frame(mainFrame, bg="#f8f6f2")
statsFrame.place(relheight=0.45, relwidth=0.7, relx = 0.3, rely=0.55)

approvalBar = tk.Frame(statsFrame, bg="white", highlightbackground="#a69d80", highlightthickness=2)
approvalBar.place(relx=0.2, rely = 0.2, relheight= 0.1, relwidth=0.6)


approvalBarValue = tk.Frame(statsFrame, bg="#e5e0d2")
approvalBarValue.place(relx=0.203, rely = 0.206, relheight= 0.088, relwidth=0.594 * 0.6)
approvalLabel = tk.Label(statsFrame, text="Approval (%): ", font=("Cambria", 12),  bg="#f8f6f2", justify="left")
approvalLabel.place(relx=0.06, rely=0.206, relheight=0.088, relwidth=0.14)


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

actionBarTitle = tk.Label(actionBar, text="Your Options", font=("Cambria", 15, "bold"), bg="#f3efe1")
actionBarTitle.place(relx = 0.05, rely = 0.05, relheight=0.06, relwidth=0.9)

yearlabelDisplay = tk.Label(actionBar, text="Current year:", font=("Cambria", 20), bg="#d6cfb7")
yearlabelDisplay.place(relx = 0.05, rely = 0.15, relheight=0.05, relwidth=0.9)
yearDisplay = tk.Label(actionBar, text="2023", font=("Cambria", 30, "bold"), bg="#d6cfb7")
yearDisplay.place(relx = 0.05, rely = 0.2, relheight=0.06, relwidth=0.9)

objective = tk.Label(actionBar, text="Your objective: \n reduce carbon levels to \n below 270 ppm by 2050.", font=("Cambria", 14), bg="#d6cfb7")
objective.place(relx = 0.05, rely = 0.29, relheight=0.1, relwidth=0.9)

currentCO2label = tk.Label(actionBar, text="Current carbon levels:", font=("Cambria", 14), bg="#d6cfb7")
currentCO2label.place(relx = 0.05, rely = 0.42, relheight=0.1, relwidth=0.9)

currentCO2 = tk.Label(actionBar, text="412 ppm", font=("Cambria", 18, "bold"), bg="#d6cfb7")
currentCO2.place(relx = 0.05, rely = 0.48, relheight=0.08, relwidth=0.9)




addTreesButton = tk.Button(actionBar, text= "+", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", state="disabled", command=addTrees)
subtractTreesButton = tk.Button(actionBar, text= "-", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", state="disabled", command=subtractTrees)
addTreesButton.place(relwidth=0.15, relheight=0.05, relx = 0.05, rely = 0.7)
subtractTreesButton.place(relwidth=0.15, relheight=0.05, relx = 0.8, rely = 0.7)

treesLabel = tk.Label(actionBar, text="Amount of trees: ", font=("Cambria", 11),  bg="#d6cfb7", justify="left")
treesLabel.place(relwidth=0.35, relheight=0.05, relx = 0.28, rely = 0.7)


treesnum = tk.Label(actionBar, text="60", font=("Cambria", 12),  bg="#d6cfb7", justify="left")
treesnum.place(relwidth=0.1, relheight=0.05, relx = 0.64, rely = 0.7)


addFactories = tk.Button(actionBar, text= "+", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", state="disabled", command=addFactory)
subtractFactories = tk.Button(actionBar, text= "-", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", state="disabled", command=subtractFactory)
addFactories.place(relwidth=0.15, relheight=0.05, relx = 0.05, rely = 0.8)
subtractFactories.place(relwidth=0.15, relheight=0.05, relx = 0.8, rely = 0.8)

factoriesLabel = tk.Label(actionBar, text="Amount of Factories: ", font=("Cambria", 11),  bg="#d6cfb7", justify="left")
factoriesLabel.place(relwidth=0.36, relheight=0.05, relx = 0.27, rely = 0.8)


factoriesnum = tk.Label(actionBar, text="4", font=("Cambria", 12),  bg="#d6cfb7", justify="left")
factoriesnum.place(relwidth=0.1, relheight=0.05, relx = 0.64, rely = 0.8)


addUtilities = tk.Button(actionBar, text= "+", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", state="disabled", command=addUtility)
subtractUtilities = tk.Button(actionBar, text= "-", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", state="disabled", command=subtractUtility)
addUtilities.place(relwidth=0.15, relheight=0.05, relx = 0.05, rely = 0.9)
subtractUtilities.place(relwidth=0.15, relheight=0.05, relx = 0.8, rely = 0.9)

utilitiesLabel = tk.Label(actionBar, text="Amount of Utilities: ", font=("Cambria", 11),  bg="#d6cfb7", justify="left")
utilitiesLabel.place(relwidth=0.36, relheight=0.05, relx = 0.27, rely = 0.9)


utilitiesnum = tk.Label(actionBar, text="5", font=("Cambria", 12),  bg="#d6cfb7", justify="left")
utilitiesnum.place(relwidth=0.1, relheight=0.05, relx = 0.64, rely = 0.9)

errorMessage = tk.Label(actionBar, text=" ", font=("Cambria", 12, "italic"),  bg="#d6cfb7")
errorMessage.place(rely=0.6, relheight=0.08, relx=0.05, relwidth=0.9)

#tutorial stuff

tutorialFrame = tk.Frame(root, bg="white", bd=2, highlightbackground="#6b644e", highlightthickness=2)
tutorialFrame.place(relx = 0.15, rely = 0.15, relheight=0.7, relwidth=0.7)

tutorialTitle = tk.Label(tutorialFrame, font = ("Cambria", 16, "bold"), text= "Welcome to Mission: Emission!", bg="white")
tutorialTitle.place(relx = 0.1, rely=0.15, relheight=0.1, relwidth=0.8)

tutorialText = tk.Label(tutorialFrame, font= ("Cambria", 12), bg="white", text="You have been elected as Mayor of Hackerstown! \n The goal of the game is to reduce CO2 emissions to 270ppm, the pre-industrial level. \nCurrently, it is at 412ppm. \n\n Each action will affect your approval, economy or carbon footprint. \n\n If your approval rating goes below 20%, you will be fired. \n\n If your money runs below 0, your city goes bankrupt. \n\n To win, fulfill all CO2 objectives while managing money and approval until 2050.")
tutorialText.place(relx=0.1, rely=0.25, relheight=0.45, relwidth=0.8)

tutorialOK=tk.Button(tutorialFrame, text= "NEXT", background="#f3efe1", font=("Cambria",16), activebackground="#fdfaf1", command=closeTutorial)
tutorialOK.place(relx=0.3, rely=0.8, relheight=0.15, relwidth=0.4)

#character select
charSelectFrame =tk.Frame(root, bg="white", bd=2, highlightbackground="#6b644e", highlightthickness=2)
charSelectFrame.place(relx = 0.15, rely = 0.15, relheight=0.7, relwidth=0.7)

charSelectTitle = tk.Label(charSelectFrame, font = ("Cambria", 16, "bold"), text= "Select Character", bg="white")
charSelectTitle.place(relx = 0.1, rely=0.1, relheight=0.1, relwidth=0.8)

nameQ = tk.Label(charSelectFrame, text="Name: ", font = ("Cambria", 16, "bold"), bg="white")
nameQ.place(relx=0.1, rely=0.25, relheight=0.1, relwidth=0.2)

nameEntry = tk.Entry(charSelectFrame, font= ("Cambria",16))
nameEntry.place(relx = 0.3, rely=0.25, relheight=0.1, relwidth=0.5)

mCharButton = tk.Button(charSelectFrame, image=smallmchar, command=lambda: selectMChar(nameEntry.get()), bg="white")
mCharButton.place(relx=0.2, rely= 0.4, relheight= 0.45, relwidth= 0.25)

fCharButton = tk.Button(charSelectFrame, image=smallfchar, command=lambda: selectFChar(nameEntry.get()), bg="white")
fCharButton.place(relx=0.55, rely= 0.4, relheight= 0.45, relwidth= 0.25)

nameMsg = tk.Label(charSelectFrame, text=" ", font = ("Cambria", 12), bg="white")
nameMsg.place(relx=0.1, rely=0.9, relheight=0.05, relwidth=0.8)

root.title("Mission: Emission")
root.mainloop()