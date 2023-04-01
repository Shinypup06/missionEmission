import variables

name = input(

    """
    Welcome to CarbonGame!
    Please enter your name below:
    """
)
variable = variables.variableClass(name, 100, 412000, 50)

year = 2023
months = 1

while True:
    option = input(
        f"""
        {str(variable)}
        Welcome to Home. The year is Year {year}, Month {months*6+1}. Please choose one of the following:
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
        if months == 1:
            months = 0
            print(months)
            year += 1
        elif months == 0:
            months += 1
    else:
        input("error, please try again")
