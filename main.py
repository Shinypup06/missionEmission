import variables
import Situations

name = input(

    """
    Welcome to Mission: Emission!
    Please enter your name below:
    """
)

money = 100
carbon = 412
happiness = 0.5

year = 2023
months = 1

treeNumber = 6
utilityUsage = 5
factoryNumber = 4



while True:
    deltaCO2 = utilityUsage*3 + factoryNumber*6 - treeNumber*5
    deltaMoney = utilityUsage*5 + factoryNumber*10 - treeNumber*10
    deltaHappiness = utilityUsage*0.05 + treeNumber*0.01 - factoryNumber*0.02 - 0.01
    option = input(
        f"""
        Money: ${money}\tCO2 Levels: {carbon} ppm\tApproval Rating: {happiness*10}%
        Welcome to Home. The year is Year {year}, Month {months*6+1}. 
        Projected change in CO2: {deltaCO2}
        Projected change in money: {deltaMoney}
        Projected change in approval: {deltaHappiness}
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
    elif int(option) == 6:
        yn = input("""
        Are you sure you want to exit? (Y/N):
        """) 
        if yn == "Yes" or yn == "Y" or yn == "YES" or yn == "yes":
            break
    elif int(option) == 0:
        yn = input("""
        Are you sure you want to go on to the next turn? (Y/N):
        """) 
        
        if yn == "Yes" or yn == "Y" or yn == "YES" or yn == "yes":
            if months == 1:
                months = 0
                print(months)
                year += 1
            elif months == 0:
                months += 1

            money += deltaMoney
            carbon += deltaCO2
            happiness += deltaHappiness
    elif int(option) == 2:
        
        while True:
            choice = input(f"""
            Trees Planted per turn: {treeNumber}
            Utility Usage per turn: {utilityUsage}
            Factories in Operation: {factoryNumber}

            Current Effects that will apply Next Turn:
            Projected change in CO2: {deltaCO2}
            Projected change in money: {deltaMoney}
            Projected change in approval: {deltaHappiness}

            What would you like to do? 
            1 - change Trees Planted (decreases CO2 and increases approval but costs money)
            2 - change Utility usage (increases CO2 and increases money from tax revenue, but decreasing utility usage will cause citizens' approval to go way down however)
            3 - change Factories (decreases citizens' approval and increases CO2 and makes a high amount of tax revenue)
            4 - return to Menu
            """)

            if int(choice) == 1:
                treeNumber += 1
                print("Number of trees planted per turn increased.")
                increased = True
            elif int(choice) == 2:
                treeNumber += 1
                print("Number of trees planted per turn increased.")
                increased = True
            elif int(choice) == 3:
                treeNumber += 1
                print("Number of trees planted per turn increased.")
                increased = True
            elif int(choice) == 4:
                break
    else:
        input("error, please try again")
