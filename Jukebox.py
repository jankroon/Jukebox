# Class
class Jukebox(object):
    "Python Class that can play popular tunes"

    def __init__(self, name): # This is called a constructor method
        self.name = name
        self.coins = 0
        self.credits = 0
        self.tunes = []

    def insertCoins(self, n):
        self.coins = self.coins + n
        self.credits = self.credits + n

    def playSinatraTune(self):
        if self.credits > 0:
            self.credits = self.credits - 1
            print("doobie doobie doo")
        else:
            print("First insert coins, please!")

    def playHappyBirthDay(self, birthDayGirl):
        if self.credits > 0:
            self.credits = self.credits - 1
            print("Happy Birthday to you")
            print("Happy Birthday to you")
            print("Happy Birthday dear " + birthDayGirl)
            print("Happy Birthday to you!")
        else:
            print("First insert coins, please!")

jb = Jukebox("Wurlitzer")

            
        
