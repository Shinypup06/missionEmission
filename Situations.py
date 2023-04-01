descriptions = {
    0: "A wildfire caused 1.5 acres of redwood trees to burn down.",
    1: "A massive flood has displaced carbon in the water and soil.",
    2: "An earthquake caused carbon to release through faults below the ground.",
    3: "A volcanic eruption caused massive amounts of CO2 gas to be released \nthrough magma, volcanic lakes, and hot springs.",
    4: "A foreign nation has passed a bill to generate 3x more electrical \n component factories.\nYour country cannot compete.",
    5: "Your opponent in the upcoming election has \nvowed to reduce carbon emission by 10%.",
    6: "Competitive pricing in electric vehicles has \ninfluenced massive surges in cobalt mines.",
    7: "15 million barrels of oil has spilled into a drinkable water source.",
    8: "Elon Musk’s chemical plant is releasing \ntoxic fumes near a rural farming village.",
    9: "A new energy source that is 10x more efficient than fossil fuels has been found \nhundreds of meters in the ground, but requires use of heavy machinery to mine.",
    10: "A new cryptocurrency KESHcoin has sparked thousands of crypto mining farms.",
    11: "A new bill allows oil drilling in 30 new territories.",
    12: "Boeing has built a record 500 737s in one year.",
    13: "New research in alternative fuel sources has shown that \nit produces 3x more carbon emission than common fossil fuels.",
    14: "UPS is manufacturing 30,000 new trucks.",
    15: "NASA is partnering with spaceX to test 50 new passenger space vehicles.",
    16: "A foreign country is building a nuclear arsenal with \nan unknown amount of weapons.",
    17: "New trends surge consumption of 'fast fashion' goods. \nWaste is being produced in mass and use of coal fueled factories.",
    18: "Production of fracking machines has increased due to demand for energy.",
    19: "Nuclear waste spill has affected sea life in a nearby pond.",
    20: "The president has passed a bill allowing the use of mass fracking.",
    21: "International Paper has cut down trees in 20 acres of forest.",
    22: "An increase of coal use due to extreme cold \ntemperatures caused smog to cover a major city.",
    23: "A factory near a major port city leaked mercury contaminated water \ncausing many birth defects and disorders.",
    24: "Many citizens are getting sick because of factories releasing toxic gasses into the air.",
    25: "40,000 refugees from a foreign war want to enter your city.",
    26: "An oil rig has caught on fire and is releasing CO2."
    }

deltaMoney = 1
deltaCO2 = 1
deltaHappiness = 1

outcome1s = {
    0: ("\n\n1. Spend money to send firefighters to reduce the blaze", -20, 10, .1),
    1: ("\n\n1. Spend money to evacuate the area", -25, 18, .1),
    2: ("\n\n1. Fund aid for those who were affected", -16, 10, .1),
    3: ("\n\n1. Spend money to evacuate the area near the volcano", -30, 10, .1),
    4: ("\n\n1. Publicly condemn mass use of factories", 0, 0, .04),
    5: ("\n\n1. Promise to decrease carbon emissions by even more", -10, 0, .06),
    6: ("\n\n1. Fund incentives to encourage companies to stop using mines", -16, -6, .02),
    7: ("\n\n1. Fund incentives to decrease oil in the water source", -30, -6, .16),
    8: ("\n\n1. Reprimand Mr. Musk and spend money to shut down the chemical plant", -14, -.16, .1),
    9: ("\n\n1. Spend money lobbying to reject the new energy source and push for renewable energy", -16, -18, .14),
    10: ("\n\n1. Create an enforcement agency to reduce the number of crypto mining farms", -9, -7, .04),
    11: ("\n\n1. Condemn the new bill and create monetary incentives to remove it", -6, -5, -.03),
    12: ("\n\n1. Pass a bill to reduce the maximum number of planes manufactured", -7, -7, -.04),
    13: ("\n\n1. Refuse to use the new energy source and lobby for its illegality", -2, -7, -.1),
    14: ("\n\n1. Pass monetary incentives to reduce number of trucks manufactured", -5, -5, -.02),
    15: ("\n\n1. Fund the passenger space vehicle program", -15, 30, .2),
    16: ("\n\n1. Cut ties with foreign nation", 0, 0, -.1),
    17: ("\n\n1. Put out statement addressing the issue and condemning 'fast fashion'", -8, 8, -.06),
    18: ("\n\n1. Place regulations on fracking", -7, -5, -.04),
    19: ("\n\n1. Spend money to lockdown affected areas", -8, -6, .03),
    20: ("\n\n1. Protest the bill", 0, 0, .04),
    21: ("\n\n1. Spend money to convert the forest into a national park", -20, -25, .2),
    22: ("\n\n1. Hire an advanced team to clear out the smog", -8, -10, .07),
    23: ("\n\n1. Fund medical aid to those affected", -10, 0, .13),
    24: ("\n\n1. Make a statement assuring everyone that there is no need to worry", 0, 0, -.05),
    25: ("\n\n1. Accept the refugees", -10, 0, .06),
    26: ("\n\n1. Spend money to immediately douse the fire", -.04, -.03, .04)
}

outcome2s = {
    0: ("\n2. Let the blaze die naturally", 0, 30, -.16),
    1: ("\n2. Leave the area alone and wait for it to naturally go away", 0, 30, -.16),
    2: ("\n2. Let the situation resolve itself naturally", 0, 20, -.16),
    3: ("\n2. Let the eruption calm down by itself", 0, 20, -.18),
    4: ("\n2. Refuse to acknowledge the competition", 0, 0, -10),
    5: ("\n2. Refuse to acknowledge the campaign", 0, 0, -.06),
    6: ("\n2. Let the companies mine cobalt", 0, 8, -.06),
    7: ("\n2. Keep using the water source as a dump for oil", 40, -60, -.5),
    8: ("\n2. Loan money (with high interest) to Mr. Musk for exploitation program", 40, .06, -.5),
    9: ("\n2. Embrace new energy source and reject renewable energy", 60, 30, -.26),
    10: ("\n2. Support crypto mining and the pursuit of capitalism", 20, 2, .02),
    11: ("\n2. Support the bill in exchange for monetary incentive", 10, -9, -.1),
    12: ("\n2. Fund Boeing to create more planes and increase transportation rates", -3, 10, .25),
    13: ("\n2. Use the new energy source en masse, saving money on energy production", 9, 20, .08),
    14: ("\n2. Do nothing", 0, 20, .04),
    15: ("\n2. Defund NASA", 15, -18, -.2),
    16: ("\n2. Do nothing", 0, 0, -.12),
    17: ("\n2. Support 'fast fashion' and benefit from its usefulness to the economy", 9, 18, .09),
    18: ("\n2. Advocate for fracking because of its cost-efficiency", 6, 11, .05),
    19: ("\n2. Fund a rescue team to help the animals", -12, -3, .09),
    20: ("\n2. Advocate for the bill, and receive monetary incentives from the president.", 6, 3, -.1),
    21: ("\n2. Do nothing", 0, 30, -.15),
    22: ("\n2. Spend money to evacuate the city", -5, 0, .03),
    23: ("\n2. Hire an extraction team to clear the mercury out of the water", -12, -.07, .15),
    24: ("\n2. Fund medical care for those who are sick", -15, 0, .15),
    25: ("\n2. Reject the refugees", 0, 0, -.14),
    26: ("\n2. Wait for the fire to go out eventually", 0, 9, -.04)
}
def createSituation(num):
    print(descriptions[num])
    print("What will you do?")
    print("1 - " + outcome1s[num])
    print("2 - " + outcome2s[num])
