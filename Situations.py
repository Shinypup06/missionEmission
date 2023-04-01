descriptions = {
        0: "insert desc here",
        1: "insert desc here"
    }

deltaMoney = 1
deltaCO2 = 1
deltaHappiness = 1

outcome1s = {
    0: ("desc here", deltaMoney, deltaCO2, deltaHappiness)
}

outcome2s = {
    0: ("desc here", deltaMoney, deltaCO2, deltaHappiness)
}

outcome3s = {
    0: ("desc here", deltaMoney, deltaCO2, deltaHappiness)
}

def createSituation(num):
    hasOutcome3 = num in outcome3s.keys()
    print(descriptions[num])
    while True:
        print("What will you do?")
        print("1 - " + outcome1s[num][0])
        print("2 - " + outcome2s[num][0])
        if (hasOutcome3):
            print("3 - " + outcome3s[num][0])
        choice = input()
        if int(choice) == 1:
            return outcome1s[num][1:3]
        if int(choice) == 2:
            return outcome2s[num][1:3]
        if hasOutcome3 and int(choice) == 3:
            return outcome3s[num][1:3]
        

