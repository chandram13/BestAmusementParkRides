# Author: Marvish Chandra

'''This program is intended to help a person or family choose the best rides at the most popular amusement parks of their choosing
in California.'''

class AmusementParks:

def veryPopular(amusementParks):
    amusementParks = ["Disneyland California Adventure","Six Flags Magic Mountain","Knott's Berry Farm","Universal Studios Hollywood",]
    print(amusementParks)
    choiceAmusement = input("What did you or your family choose to go?")
    print("The choice was" + choiceAmusement + ".")

def disneylandCali(bestrides1,bestrides2):
    bestrides1 = ["Guardians of the Galaxy-Mission: BREAKOUT!","The Incredicoaster","Radiator Springs Racers","Soarin' Over California","Toy Story Midway Mania"]
    print(bestrides1)
    choicerides1 = input("Which of the first five rides do you want to go to first?")
    bestrides2 = ["Grizzly River Run","Goofy's Sky School","The Ferris Wheel","The Little Mermaid","Mater's Junkyard Jamboree"]
    print(bestrides2)
    choicerides2 = input("Which of the last five rides do you want to go to first?")
    print("Our initial choice of rides are:" + choicerides1 + "and" + choicerides2 + ".")

def sixflags(magicrides1,magicrides2):
    magicrides1 = ["Goliath","X Flight","Justice League: Battle for Metropolis","Maxx Force","Vertical Velocity","Superman: Ultimate Flight"]
    print(magicrides1)
    choicemagic1 = input("Which of the first six rides do you want to go to first?")
    magicrides2 = ["Batman: The Ride","Raging Bull","The Joker Free Fly Coaster","Tsunami Surge","Whizzer","Little Dipper","Viper"]
    print(magicrides2)
    choicemagic2 = input("Which of the last seven rides do you want to go to first")
    print("Our initial choice of rides are:" + choicemagic1 + "and" + choicemagic2 + ".")

def knotts(berryrides1,berryrides2):
    berryrides1 = ["Calico Mine Ride","Xcelerator","Timber Mountain Log Ride","GhostRider","HangTime"]
    print(berryrides1)
    choiceberry1 = input("Which of the first five rides do you want to go to first?")
    berryrides2 = ["Knott's Bear-y Tales: Return to the Fair","Silver Bullet","Supreme Scream","Calico River Rapids","Calico Railroad"]
    print(berryrides2)
    choiceberry2 = input("Which of the last five rides do you want to go to first?")
    print("Our initial choice of rides are" + choiceberry1 + "and" + choiceberry2 + ".")

def universalStudios(Hollywoodrides1,Hollywoodrides2):
    Hollywoodrides1 = ["Harry Potter and the Forbidden Journey","Studio Tour","Transformers: The Ride 3D","King Kong 360 3D","Despicable Me Minion Mayhem"]
    print(Hollywoodrides1)
    choiceHR1 = input("Which of the first five rides do you want to go to first?")
    Hollywoodrides2 = ["Jurassic World: The Ride","Revenge of the Mummy: The Ride","The Secret Life of Pets: Off the Leash","The Simpsons Ride","WaterWorld"]
    choiceHR2 = input("Which of the last five rides do you want to go to first?")
    print(Hollywoodrides2)
    print("Our initial choice of rides are" + choiceHR1 + "and" + choiceHR2 + ".")




