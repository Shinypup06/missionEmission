descriptions = {
        0: "A wildfire caused 1.5 acres of redwood trees to burn down.",
        1: "A massive flood has displaced carbon in the water and soil",
        2: "An earthquake caused carbon to release through faults below the ground",
    3: "A volcanic eruption caused massive amounts of CO2 gas to be released \nthrough magma, volcanic lakes, and hot springs",
    4: "A foreign nation has passed a bill to generate 3x more electrical component factories.\nYour country cannot compete",
    5: "Your opponent in the upcoming election has vowed to reduce carbon emission by 10%",
    6: "Competitive pricing in electric vehicles has influenced massive surges in cobalt mines",
    7: "15 million barrels of oil has spilled into a drinkable water source",
    8: "Elon Musk’s chemical plant is releasing toxic fumes near a rural farming village",
    9: "A new energy source that is 10x more efficient than fossil fuels has been found \nhundreds of meters in the ground requires use of heavy machinery to mine",
    10: "A new cryptocurrency KESHcoin has sparked thousands of cryptomining farms",
    11: "A new bill allows oil drilling in 30 new territories",
    12: "BOEING has built a record 500 737s in one year",
    13: "New research in alternative fuel sources has shown that \nit produces 3x more carbon emission than common fossil fuels",
    14: "UPS is manufacturing 30,000 new trucks",
    15: "NASA is partnering with spaceX to test 50 new passenger space vehicles",
    16: "A foreign country is building a nuclear arsenal with an unknown amount of weapons",
    17: "New trends surge consumption of “fast fashion” goods. \nWaste is being produced in mass and use of coal fueled factories",
    18: "Production of fracking machines has increased due to demand for energy",
    19: "Nuclear waste spill has affected sea life in a nearby pond",
    20: "The president has passed a bill allowing the use of mass fracking",
    21: "International Paper has cut down trees in 20 acres of forest",
    22: "An increase of coal use due to extreme cold temperatures caused smog to cover a major city",
    23: "A factory near a major port city leaked mercury contaminated water \ncausing many birth defects and disorders",
    24: "Many citizens are getting sick because of factories releasing toxic gasses into the air",
    25: "40,000 refugees from a foreign war want to enter your country",
    26: "An oil rig has caught on fire and is releasing CO2"
    }

deltaMoney = 1
deltaCO2 = 1
deltaHappiness = 1

outcome1s = {
    0: ("\nSend firefighters to reduce the blaze", -10, 5, .05),
1: ("\nEvacuate the area", -15, 10, .05),
2: ("\nAid those who were affected", -8, 5, .05),
3: ("\nEvacuate the area near the volcano", -15, 5, .05),
4: ("\nPublicly condemn mass use of factories", 0, 0, .02),
5: ("\nPromise to decrease carbon emissions by even more", -5, 0, .03),
6: ("\nReduce number of mines accessible to companies", -8, -3, .01),
7: ("\nMake efforts to decrease oil in the water source", -15, -3, .08),
8: ("\nReprimand Mr. Musk and shut down the chemical plant immediately", -7, -.08, .05),
9: ("\ndesc here", dM, dC, dH),
10: ("\ndesc here", dM, dC, dH),
11: ("\ndesc here", dM, dC, dH),
12: ("\ndesc here", dM, dC, dH),
13: ("\ndesc here", dM, dC, dH),
14: ("\ndesc here", dM, dC, dH),
15: ("\ndesc here", dM, dC, dH),
16: ("\ndesc here", dM, dC, dH),
17: ("\ndesc here", dM, dC, dH),
18: ("\ndesc here", dM, dC, dH),
19: ("\ndesc here", dM, dC, dH),
20: ("\ndesc here", dM, dC, dH),
21: ("\ndesc here", dM, dC, dH),
22: ("\ndesc here", dM, dC, dH),
23: ("\ndesc here", dM, dC, dH),
24: ("\ndesc here", dM, dC, dH),
25: ("\ndesc here", dM, dC, dH),
26: ("\ndesc here", dM, dC, dH)
}

outcome2s = {
    0: ("Let the blaze die naturally", 0, 15, -.08),
1: ("\nLeave the area alone and wait for it to naturally go away", 0, 15, -.08),
2: ("\nLet the situation resolve itself naturally", 0, 10, -.08),
3: ("\nLet the eruption calm down", 0, 10, -.09),
4: ("\nDon't acknowledge the competition", 0, 0, -5),
5: ("\nDon't acknowledge the campaign", 0, 0, -.03),
6: ("\nLet the companies mine cobalt", 0, 8, -.03),
7: ("\nKeep using the water source as a dump for oil", 20, -30, -.25),
8: ("\nSubsidize Mr. Musk's exploitation program", 20, deltaCO2, deltaHappiness),
9: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
10: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
11: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
12: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
13: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
14: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
15: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
16: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
17: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
18: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
19: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
20: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
21: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
22: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
23: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
24: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
25: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness),
26: ("\ndesc here", deltaMoney, deltaCO2, deltaHappiness)
}
def createSituation(num):
    print(descriptions[num])
    print("What will you do?")
    print("1 - " + outcome1s[num])
    print("2 - " + outcome2s[num])