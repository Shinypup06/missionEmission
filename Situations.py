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
    10: "A new cryptocurrency KESHcoin has sparked thousands of crypto mining farms",
    11: "A new bill allows oil drilling in 30 new territories",
    12: "Boeing has built a record 500 737s in one year",
    13: "New research in alternative fuel sources has shown that \nit produces 3x more carbon emission than common fossil fuels",
    14: "UPS is manufacturing 30,000 new trucks",
    15: "NASA is partnering with spaceX to test 50 new passenger space vehicles",
    16: "A foreign country is building a nuclear arsenal with an unknown amount of weapons",
    17: "New trends surge consumption of 'fast fashion' goods. \nWaste is being produced in mass and use of coal fueled factories",
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
9: ("\nReject new energy source and push for renewable energy", -8, -9, .07),
10: ("\nReduce the number of crypto mining farms", -9, -7, .04),
11: ("\nCondemn the new bill and make efforts to remove it", -6, -5, -.03),
12: ("\nPass a bill to reduce the maximum number of planes manufactured", -7, -7, -.04),
13: ("\nRefuse use of the new energy source", -2, -7, -.1),
14: ("\nReduce number of trucks manufactured", -5, -5, -.02),
15: ("\nFund the passenger space vehicle program", -15, 30, .2),
16: ("\nCut ties with foreign nation", 0, 0, -.1),
17: ("\nPut out statement addressing the issue and condemning 'fast fashion'", -8, 8, -.06),
18: ("\nPlace regulations on fracking", -7, -5, -.04),
19: ("\nLockdown affected areas", -8, -6, .03),
20: ("\nProtest the bill", 0, 0, .04),
21: ("\nConvert the forest into a national park", -20, -25, .2),
22: ("\nClear out the smog", -8, -10, .07),
23: ("\nGive medical aid to those effected", -10, 0, .13),
24: ("\nMake a statement assuring everyone that there is no need to worry", 0, 0, -.05),
25: ("\nAccept the refugees", -10, 0, .06),
26: ("\nSpend money to immediately douse the fire", -.04, -.03, .04)
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
8: ("\nSubsidize Mr. Musk's exploitation program", 20, 30, -.25),
9: ("\nEmbrace new energy source and reject renewable energy", 30, 15, -.13),
10: ("\nSupport crypto mining and the pursuit of capitalism", 10, 11, .01),
11: ("\nSupport the bill", 10, -9, -.1),
12: ("\nFund Boeing to create more planes and increase transportation rates", -3, 10, .25),
13: ("\nUse the new energy source in mass", 9, 20, .08),
14: ("\nDo nothing", 0, 20, .04),
15: ("\nDefund NASA", 15, -18, -.2),
16: ("\nDo nothing", 0, 0, -.12),
17: ("\nSupport 'fast fashion' and its usefulness to the economy", 9, 18, .09),
18: ("\nAdvocate for fracking because of its efficiency", 6, 11, .05),
19: ("\nattempt to help the animals", -12, -3, .09),
20: ("\nAdvocate for the bill", 6, 3, -.1),
21: ("\nDo nothing", 0, 30, -.15),
22: ("\nEvacuate the city", -5, 0, .03),
23: ("\nClear the mercury out of the water", -12, -.07, .15),
24: ("\nProvide medical care to those who are sick", -15, 0, .15),
25: ("\nReject the refugees", 0, 0, -.14),
26: ("\nWait for the fire to go out eventually", 0, 9, -.04)
}
def createSituation(num):
    print(descriptions[num])
    print("What will you do?")
    print("1 - " + outcome1s[num])
    print("2 - " + outcome2s[num])
