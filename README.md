# Mission: Emission

Welcome to Mission: Emission, a game that we made to simulate the difficulties of managing carbon emissions while balancing a budget and public approval.

In the game, you’re a government official who is able to see what level your budget, approval ratings, and emissions are at. You can change the number of trees you plant per year, as well as global utility usage and factories.

Planting trees costs money but increases approval and decreases CO2. Utility usage such as lights and electricity usage increases approval and makes tax revenue but slightly increases CO2. Factories decrease public approval and greatly increase CO2 but you gain lots of tax revenue.

In addition, every couple of years, random situations appear which force you to make a decision which will impact approval, budget, and carbon emissions. The goal of the game is to reach 270 parts per million of CO2, which is the pre-industrial CO2 level.

Moving onto the code behind all of this, we used Tkinter to create a functioning GUI for the game instead of doing it completely in terminal or text-based, so that we can appeal to a more expansive audience. We divided up the jobs, such as creating all of the GUI, writing situations, and integrating everything between ourselves in order to streamline work.

We hard coded various scenarios and situations as well as options into a separate python file, and then imported that into the main file. This helps with code readability. We also used a random number generator to randomly pop out situations at a varying rate to make the game more unpredictable, and also to improve player engagement.

The inspiration behind this project was our previous experiences with text-based games where you are in control of a larger institution and our passion for educating the youth. But we also wanted to add some flair so we use a GUI instead of terminal based.

Thank you for reading, and we hope you enjoy our game!
Shiny, Kesh and Alan
