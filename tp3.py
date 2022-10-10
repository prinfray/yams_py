# from collections import Counter

from itertools import combinations
from math import comb
import random


class Main:
    game = None

    def __init__(self):
        self.game = Game()


class Game:
    score = None
    game_on = True
    def __init__(self):
        dices = Dices()
        score = Score()
        while self.game_on == True:

            result = self.doRound(dices, score)
            score.setScore(result)
            score.getScore()

    def endGame(self,game):
        self.finalScore()
        game.game_on = False
        
    def doRound(self,dices,score):
        while dices.round_is_end == False :
            dices.rollAll()
            dices.getDices()
            dices.nextThrow()
            dices.detectFigure(score)
            combination = dices.chooseCombination()
            return combination
            
            

# class Round :
    # 13 round max
    # def __init__(dices):


class Dice:
    nb_faces = 6
    value = None

    def roll(self):
        self.value = random.randint(1, self.nb_faces)


class Dices:
    dices = []
    result = []
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    brelan = 0
    square = 0
    full = 0
    small_suit = 0
    big_suit = 0
    yams = 0
    counterSuit = 0
    combinations = {}

    round_is_end = False
    throw_count = 0

    def __init__(self):
        for i in range(0, 5):
            self.dices.append(Dice())

    def rollAll(self):
        for i in range(5):
            self.dices[i].roll()
        self.throw_count += 1

    def getDices(self):
        index = 1
        self.result.clear()
        print("vos dés sont : ")
        for i in self.dices:
            print("dé", index, ":", i.value)
            self.result.append(i.value)
            index = index + 1

    def rollIndex(self, changes):
        for i in changes:
            i = i-1
            print(changes)
            self.dices[i].roll()

    def reRoll(self):
        print("Combien de dés souhaitez vous changer ? ")
        nbrChanges = input()
        nbrChanges = int(nbrChanges)
        changes = []
        x = 1
        for i in range(nbrChanges):
            print("choisissez un dé à changer:")
            change = input()
            change = int(change)
            changes.append(change)
            x += 1
        print(changes)
        self.rollIndex(changes)
        self.getDices()
        self.nextThrow()

    def chooseCombination(self):
        print("choisir la combinaison")
        print(self.combinations)
        choice = input()
        value = self.combinations.get(choice)
        combination = []
        combination.append(choice)
        combination.append(value)
        print (combination)
        self.round_is_end = True
        return combination

# brelan somme
# carre somme
# full 25

    def nextThrow(self):
        while self.throw_count < 3:
            print("voulez vous reroll ? y/n")
            response = input()
            if response == "y":
                self.throw_count += 1
                self.reRoll()
            if response == "n":
                self.throw_count = 4
        

    def getSum(self):
        value = 0
        for i in range(len(self.result)):
            current_val = self.result[i]
            value = value + current_val
        return value

    def detectFigure(self, score):

        print(self.result)
        (self.result).sort()
        print(self.result)
        for i in range(len(self.result)):
            current_val = self.result[i]
            print(current_val)
            if current_val == 1:
                self.one += 1
            if current_val == 2:
                self.two += 1
            if current_val == 3:
                self.three += 1
            if current_val == 4:
                self.four += 1
            if current_val == 5:
                self.five += 1
            if current_val == 6:
                self.six += 1

            if current_val == self.result[i-1] + 1:
                self.counterSuit += 1
            if current_val > self.result[i-1] + 1:
                self.counterSuit -= 1

        if self.one == 3 or self.two == 3 or self.three == 3 or self.four == 3 or self.five == 3 or self.six == 3:
            self.brelan += 1

        if self.one == 4 or self.two == 4 or self.three == 4 or self.four == 4 or self.five == 4 or self.six == 4:
            self.square += 1

        if (self.one == 3 or self.two == 3 or self.three == 3 or self.four == 3 or self.five == 3 or self.six == 3) and (self.one == 2 or self.two == 2 or self.three == 2 or self.four == 2 or self.five == 2 or self.six == 2):
            self.full += 1

        if self.counterSuit == 3:
            self.small_suit += 1
        if self.counterSuit == 4:
            self.big_suit += 1

        if self.one == 5 or self.two == 5 or self.three == 5 or self.four == 5 or self.five == 5 or self.six == 5:
            self.yams += 1

        if self.one > 0:
            if score.one == False:
                value = self.one
                value = value * 1
                self.combinations["one"] = value
                print("One : ", value)
        if self.two > 0:
            if score.two == False:
                value = self.two
                value = value * 2
                self.combinations["two"] = value
                print("two : ", value)
        if self.three > 0:
            if score.three == False:
                value = self.three
                value = value * 3
                self.combinations["three"] = value
                print("three : ", value)
        if self.four > 0:
            if score.four == False:
                value = self.four
                value = value * 4
                self.combinations["four"] = value
                print("four : ", value)
        if self.five > 0:
            if score.five == False:
                value = self.five
                value = value * 5
                self.combinations["five"] = value
                print("five : ", value)
        if self.six > 0:
            if score.six == False:
                value = self.six
                value = value * 6
                self.combinations["six"] = value
                print("six : ", value)

        if self.brelan > 0:
            if score.brelan == False:
                value = self.getSum()
                self.combinations["brelan"] = value
                print("BRELAN")
        if self.square > 0:
            if score.square == False:
                value = self.getSum()
                self.combinations["square"] = value
                print("SQUARE")
        if self.full > 0:
            if score.full == False:
                self.combinations["full"] = 25
                print("FULL")

        if self.small_suit > 0:
            if score.small_suit == False:
                self.combinations["small suit"] = 25
                print("small suit")

        if self.big_suit > 0:
            if score.big_suit == False:
                self.combinations["big suit"] = 25
                print("big suit")

        if score.chance == False:
            value = self.getSum()
            self.combinations["chance"] = value

        if self.yams > 0:
            if score.yams == False:
                value = 50
                self.combinations["chance"] = value

        if len(self.combinations) == 0:
            score.endGame()
        return self.combinations


class Score:

    sum_points = 0

    one = False
    two = False
    three = False
    four = False
    five = False
    six = False
    bonus_part_1 = False
    #  si score final > 63 , 35 points bonus sur le score final .
    brelan = False
    square = False
    full = False
    small_suit = False
    big_suit = False
    yams = False
    chance = False

    def setScore(self, result):
        combination = result
        print('COMBINAISON', combination)

        if combination[0] == "one":
            self.one = True
        if combination[0] == "two":
            self.two = True
        if combination[0] == "three":
            self.three = True
        if combination[0] == "four":
            self.four = True
        if combination[0] == "five":
            self.five = True
        if combination[0] == "six":
            self.six = True
        if combination[0] == "brelan":
            self.brelan = True
        if combination[0] == "square":
            self.square = True
        if combination[0] == "full":
            self.full = True
        if combination[0] == "chance":
            self.chance = True
        if combination[0] == "yams":
            self.yams = True
        self.sum_points += combination[1]

    def getScore(self):
        print("somme des points: ", self.sum_points)



    def finalScore(self):
        if self.sum_points > 63:
            print ("BONUS DE POINTS !!!")
            self.sum_points += 35
        print ("SCORE FINAL:" , self.sum_points)

Game()
