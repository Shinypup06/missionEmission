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
    print(descriptions[num])
    print("What will you do?")
    print("1 - " + outcome1s[num])
    print("2 - " + outcome2s[num])
    print("3 - " + outcome3s[num])
