import Situations
import random

global money
global carbon
global happiness
global year
global months

name = input(

    """
    Welcome to Mission: Emission!
    Please enter your name below:
    """
)

money = 100
carbon = 412
happiness = 0.6

year = 2023

# global treeNumber
# global utilityUsage
# global factoryNumber

treeNumber = 6
utilityUsage = 5
factoryNumber = 4

finalobj = 270



deltaCO2 = utilityUsage*3 + factoryNumber*6 - treeNumber*5
deltaMoney = utilityUsage*5 + factoryNumber*10 - treeNumber*10
deltaHappiness = round(utilityUsage*0.005 + treeNumber*0.001 - factoryNumber*0.002 - 0.001, 3)

usedSituations = []





def updateResourceLabels():
    approvalBarValue["relwidth"] = 0.594 * happiness
    approval["text"] = f"{round(happiness*100, 3)}%"
    moneyBarValue["relwidth"] = 0.594 * (money/100) * 0.5
    if (money/100)*0.5 > 1:
        moneyBarValue["relwidth"] = 0.594
    money["text"] = f"{money}"
    carbonBarValue["relwidth"] = 0.594 * (carbon/412) * 0.75
    carbon["text"] = f"{carbon}"

def endTurn():
    year += 1
    money += deltaMoney
    carbon += deltaCO2
    happiness += deltaHappiness
    updateResourceLabels()

def addTrees():
    treeNumber += 1

def subtractTrees():
    treeNumber -= 1

def addUtility():
    utilityUsage += 1

def subtractUtility():
    utilityUsage -= 1

def addFactory():
    factoryNumber += 1

def subtractFactory():
    factoryNumber -= 1

def calcDeltas(stats):
    global deltaCO2
    global deltaMoney
    global deltaHappiness

    deltaCO2 = utilityUsage*3 + factoryNumber*6 - treeNumber*5 + stats[1]
    deltaMoney = utilityUsage*5 + factoryNumber*10 - treeNumber*10 + stats[0]
    deltaHappiness = round(utilityUsage*0.005 + treeNumber*0.001 - factoryNumber*0.002 + stats[2] - 0.001, 3)
    

def executeSituation():
    randnum = random.randint(0, 27)
    while True:
        if randnum in usedSituations:
            randnum = random.randint(0, 27)
        else:
            usedSituations.append(randnum)
            break
    desc = Situations.descriptions[randnum]
    outcome1desc = Situations.outcome1s[randnum][0]
    outcome2desc = Situations.outcome2s[randnum][0]
    outcome1stats = Situations.outcome1s[randnum][1:3]
    outcome2stats = Situations.outcome2s[randnum][1:3]

def endturn():
    calcDeltas(outcomeStats)
    money += deltaMoney
    carbon += deltaCO2
    happiness += deltaHappiness
    updateResourceLabels()
    situationFrame.lift()

def losing():
    if money < 0:
        loseScreen["text"] = "You went bankrupt and your department has been disbanded."
    elif carbon > 549:
        loseScreen["text"] = "You went above the carbon emissions limit and you have been fired for failing to prevent carbon emission rates from skyrocketing"
    elif happiness < 20:
        loseScreen["text"] = "You were too unpopular and you have been fired due to popular discontent"
    elif year == 2050 and carbon > 270:
        loseScreen["text"] = "You were unable to reach the 2050 carbon emission target, despite your impressive money and approval management skills."
        
        










while True:
    if random.randint(0, 1) == 1:
        situationNumber = random.randint(0, 26)
        while True:
            if (usedSituations.count(situationNumber) > 0):
                situationNumber = random.randint(0, 26)
            else:
                break
        Situations.createSituation(situationNumber)

    deltaCO2 = utilityUsage*3 + factoryNumber*6 - treeNumber*5
    deltaMoney = utilityUsage*5 + factoryNumber*10 - treeNumber*10
    deltaHappiness = round(utilityUsage*0.005 + treeNumber*0.001 - factoryNumber*0.002 - 0.001, 3)
    option = input(
        f"""
        Money: ${money}\tCO2 Levels: {carbon} ppm\tApproval Rating: {happiness*100}%
        Welcome to Home. The year is Year {year}. 
        Projected change in CO2: {deltaCO2}
        Projected change in money: {deltaMoney}
        Projected change in approval: {round(deltaHappiness*100, 3)}%
        Please choose one of the following:
        0 - Next Turn
        1 - View Bills
        2 - View Policies
        3 - View Situations
        4 - View Objectives
        5 - Instructions/Credits
        6 - Exit (note: your data will not be saved for now)
        Please enter your choice: 
        """
    )

    if int(option) == 5:
        input("""
        Credits: Shining Wang, Keshav Gollamudi, Lelun Li
        You have been hired as the Secretary of the Environmental Regulation Agency in the Glorious State of Gilead!
        The goal of the game is to fulfil CO2 emission objectives. If you go above them for more than 3 turns, you will be fired.
        To win, fulfill all CO2 objectives while managing money and civilian happiness in 2050.
        Good luck!
        """)
    
    elif int(option) == 2:
        while True:
            deltaCO2 = utilityUsage*3 + factoryNumber*6 - treeNumber*5
            deltaMoney = utilityUsage*5 + factoryNumber*10 - treeNumber*10
            deltaHappiness = round(utilityUsage*0.005 + treeNumber*0.001 - factoryNumber*0.002 - 0.001, 3)
            choice = input(f"""
            Trees Planted per turn: {treeNumber}
            Utility Usage per turn: {utilityUsage}
            Factories in Operation: {factoryNumber}

            Current Effects that will apply Next Turn:
            Projected change in CO2: {deltaCO2}
            Projected change in money: {deltaMoney}
            Projected change in approval: {round(deltaHappiness*100, 3)}%

            What would you like to do? 
            1 - change Trees Planted (decreases CO2 and increases approval but costs money)
            2 - change Utility usage (increases CO2 and increases money from tax revenue, but decreasing utility usage will cause citizens' approval to go way down)
            3 - change Factories (decreases citizens' approval and increases CO2 and makes a high amount of tax revenue)
            4 - return to Menu
            """)

            if int(choice) == 1:
                treeNumber += 1
                print("Number of trees planted per turn increased.")
            elif int(choice) == 2:
                utilityUsage += 1
                print("Utility usage increased.")
            elif int(choice) == 3:
                factoryNumber += 1
                print("Number of factories in operation increased.")
            elif int(choice) == 4:
                break
    else:
        input("error, please try again")
