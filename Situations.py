descriptions = {
        0: "A wildfire caused 1.5 acres of redwood trees to burn down.",
        1: "A massive flood has displaced carbon in the water and soil",
        2: "An earthquake caused carbon to release through faults below the ground",
    3: "A volcanic eruption caused massive amounts of CO2 gas to be released through magma, volcanic lakes, and hot springs",
    4: "A foreign nation has passed a bill to generate 3x more electrical component factories. Your country cannot compete",
    5: "Your opponent in the upcoming election has vowed to reduce carbon emission by 10%",
    6: "Competitive pricing in electric vehicles has influenced massive surges in cobalt mines",
    7: "15 million barrels of oil has spilled into a drinkable water source",
    8: "Elon Musk’s chemical plant is releasing toxic fumes near a rural farming village",
    9: "A new energy source that is 10x more efficient than fossil fuels has been found hundreds of meters in the ground requires use of heavy machinery to mine",
    10: "A new cryptocurrency KESHcoin has sparked thousands of cryptomining farms",
    11: "A new bill allows oil drilling in 30 new territories",
    12: "BOEING has built a record 500 737s in one year",
    13: "New research in alternative fuel sources has shown that it produces 3x more carbon emission than common fossil fuels",
    14: "UPS is manufacturing 30,000 new trucks",
    15: "NASA is partnering with spaceX to test 50 new passenger space vehicles",
    16: "A foreign country is building a nuclear arsenal with an unknown amount of weapons",
    17: "New trends surge consumption of “fast fashion” goods. Waste is being produced in mass and use of coal fueled factories",
    18: "Production of fracking machines has increased due to demand for energy",
    19: "Nuclear waste spill has affected sea life in a nearby pond",
    20: "The president has passed a bill allowing the use of mass fracking",
    21: "International Paper has cut down trees in 20 acres of forest",
    22: "An increase of coal use due to extreme cold temperatures caused smog to cover a major city",
    23: "A factory near a major port city leaked mercury contaminated water causing many birth defects and disorders",
    24: "Many citizens are getting sick because of factories releasing toxic gasses into the air",
    25: "40,000 refugees from a foreign war want to enter your country",
    26: "An oil rig has caught on fire and is releasing CO2"
    }

deltaMoney = 1
deltaCO2 = 1
deltaHappiness = 1

outcome1s = {
    0: ("Send firefighters to reduce the blaze", -10, 5, .05),
1: ("Evacuate the area", -15, 10, .05),
2: ("Aid those who were affected", -8, 5, .05),
3: ("Evacuate the area near the volcano", -15, 5, .05),
4: ("Publicly condemn mass use of factories", 0, 0, .02),
5: ("Promise to decrease carbon emissions by even more", -5, 0, .03),
6: ("Reduce ", dM, dC, dH),
7: ("desc here", dM, dC, dH),
8: ("desc here", dM, dC, dH),
9: ("desc here", dM, dC, dH),
10: ("desc here", dM, dC, dH),
11: ("desc here", dM, dC, dH),
12: ("desc here", dM, dC, dH),
13: ("desc here", dM, dC, dH),
14: ("desc here", dM, dC, dH),
15: ("desc here", dM, dC, dH),
16: ("desc here", dM, dC, dH),
17: ("desc here", dM, dC, dH),
18: ("desc here", dM, dC, dH),
19: ("desc here", dM, dC, dH),
20: ("desc here", dM, dC, dH),
21: ("desc here", dM, dC, dH),
22: ("desc here", dM, dC, dH),
23: ("desc here", dM, dC, dH),
24: ("desc here", dM, dC, dH),
25: ("desc here", dM, dC, dH),
26: ("desc here", dM, dC, dH)
}

outcome2s = {
    0: ("Let the blaze die naturally", 0, 15, -.08),
1: ("Leave the area alone and wait for it to naturally go away", 0, 15, -.08),
2: ("Let the situation resolve itself naturally", 0, 10, -.08),
3: ("Let the eruption calm down", 0, 10, -.09),
4: ("Don't acknowledge the competition", -5, 0, -5),
5: ("Don't acknowledge the campaign", 0, 0, -.03),
6: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
7: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
8: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
9: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
10: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
11: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
12: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
13: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
14: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
15: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
16: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
17: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
18: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
19: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
20: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
21: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
22: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
23: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
24: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
25: ("desc here", deltaMoney, deltaCO2, deltaHappiness),
26: ("desc here", deltaMoney, deltaCO2, deltaHappiness)
}
def createSituation(num):
    print(descriptions[num])
    print("What will you do?")
    print("1 - " + outcome1s[num])
    print("2 - " + outcome2s[num])
