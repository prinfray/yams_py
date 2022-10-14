import random


class Main:
    game = None

    def __init__(self):
        self.game = Game()


class Game:
    score = None
    game_on = None
    round = None
    dices = None

    def __init__(self):
        self.game_on = True
        self.dices = Dices()
        self.score = Score()

        while self.game_on == True:
            self.doRound()

    def endGame(self):
        self.game_on = False
        self.score.finalScore()

    def doRound(self):

        self.round = Round(self.score, self.dices)
        self.dices.throw_count = 0
        self.dices.round_is_end = False
        while self.dices.round_is_end == False:
            self.dices.rollAll()
            self.dices.getDices()
            self.dices.nextThrow()
        response = self.round.detectFigure()
        if len(response) == 0:
            result = self.round.checkRemainingFigures(self.score)
            if result == 'no possibility':
                self.endGame()
            self.dices.round_is_end = True
            return
        choice = self.round.chooseCombination()
        self.score.setScore(choice)
        self.score.getScore()


class Round:

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

    def __init__(self, score, dices):
        self.score = score
        self.dices = dices
        self.combinations = {}

    def chooseCombination(self):
        print("choisir la combinaison", self.combinations)
        choice = input()
        value = self.combinations.get(choice)
        combination = []
        combination.append(choice)
        combination.append(value)
        return combination

    def detectFigure(self):
        # Tri des dés par ordre croissant
        (self.dices.result).sort()
        # On parcour chaque valeur unitairement
        for i in range(len(self.dices.result)):
            current_val = self.dices.result[i]
            self.detectNumber(current_val)
            self.countSuit(i, current_val)
        self.detectBrelan()
        self.detectSquare()
        self.detectFull()
        self.detectSuit()
        self.detectYams()
        self.setPossiblesCombis()
        return self.combinations

    def setCombiOne(self):
        if 'one' in self.score.score_possible:
            value = self.one * 1
            self.combinations["one"] = value

    def setCombiTwo(self):
        if 'two' in self.score.score_possible:
            value = self.two * 2
            self.combinations["two"] = value

    def setCombiThree(self):
        if 'three' in self.score.score_possible:
            value = self.three * 3
            self.combinations["three"] = value

    def setCombiFour(self):
        if 'four' in self.score.score_possible:
            value = self.four * 4
            self.combinations["four"] = value

    def setCombiFive(self):
        if 'five' in self.score.score_possible:
            value = self.five * 5
            self.combinations["five"] = value

    def setCombiSix(self):
        if 'six' in self.score.score_possible:
            value = self.six * 6
            self.combinations["six"] = value
            # print("six : ", value)

    def setCombiBrelan(self):
        if 'brelan' in self.score.score_possible:
            value = self.dices.getSum()
            self.combinations["brelan"] = value

    def setCombiSquare(self):
        if 'square' in self.score.score_possible:
            value = self.dices.getSum()
            self.combinations["square"] = value

    def setCombiFull(self):
        if 'full' in self.score.score_possible:
            self.combinations["full"] = 25

    def setCombiSmallSuit(self):
        if 'small suit' in self.score.score_possible:
            self.combinations["small suit"] = 25

    def setCombiBigSuit(self):
        if 'big suit' in self.score.score_possible:
            self.combinations["big suit"] = 25

    def setCombiYams(self):
        if 'yams' in self.score.score_possible:
            value = 50
            self.combinations["chance"] = value

    def detectNumber(self, current_val):
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

    def countSuit(self, i, current_val):
        if current_val == self.dices.result[i-1] + 1:
            self.counterSuit += 1
        if current_val > self.dices.result[i-1] + 1:
            self.counterSuit -= 1

    def detectBrelan(self):
        if self.one == 3 or self.two == 3 or self.three == 3 or self.four == 3 or self.five == 3 or self.six == 3:
            self.brelan += 1

    def detectSquare(self):
        if self.one == 4 or self.two == 4 or self.three == 4 or self.four == 4 or self.five == 4 or self.six == 4:
            self.square += 1

    def detectFull(self):
        if (self.one == 3 or self.two == 3 or self.three == 3 or self.four == 3 or self.five == 3 or self.six == 3) and (self.one == 2 or self.two == 2 or self.three == 2 or self.four == 2 or self.five == 2 or self.six == 2):
            self.full += 1

    def detectSuit(self):
        if self.counterSuit == 3:
            self.small_suit += 1
        if self.counterSuit == 4:
            self.big_suit += 1

    def detectYams(self):
        if self.one == 5 or self.two == 5 or self.three == 5 or self.four == 5 or self.five == 5 or self.six == 5:
            self.yams += 1

    def setPossiblesCombis(self):
        if self.one > 0:
            self.setCombiOne()
        if self.two > 0:
            self.setCombiTwo()
        if self.three > 0:
            self.setCombiThree()
        if self.four > 0:
            self.setCombiFour()
        if self.five > 0:
            self.setCombiFive()
        if self.six > 0:
            self.setCombiSix()
        if self.brelan > 0:
            self.setCombiBrelan()
        if self.square > 0:
            self.setCombiSquare()
        if self.full > 0:
            self.setCombiFull()
        if self.small_suit > 0:
            self.setCombiSmallSuit()
        if self.big_suit > 0:
            self.setCombiBigSuit()
        if self.yams > 0:
            self.setCombiYams()
        if 'chance' in self.score.score_possible:
            value = self.dices.getSum()
            self.combinations["chance"] = value


    def checkRemainingFigures(self, score):
        if len(score.score_possible) == 0:
            return "no possibility"
        print("Choisir une figure à sacrifier :", score.score_possible)
        combi_to_delete = input()
        self.score.score_possible.remove(combi_to_delete)
        return "success"


class Dice:
    nb_faces = 6
    value = None

    def roll(self):
        self.value = random.randint(1, self.nb_faces)


class Dices:
    dices = []
    result = []
    throw_count = 0
    round_is_end = False

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
        self.rollIndex(changes)
        self.getDices()
        self.nextThrow()

    def nextThrow(self):
        while self.throw_count < 3:
            print("voulez vous reroll ? y/n")
            response = input()
            if response == "y":
                self.throw_count += 1
                self.reRoll()
            if response == "n":
                self.throw_count = 4
        self.round_is_end = True

    def getSum(self):
        value = 0
        for i in range(len(self.result)):
            current_val = self.result[i]
            value = value + current_val
        return value


class Score:
    sum_points = 0
    bonus_part_1 = False
    score_possible = ['one', 'two', 'three', 'four', 'five',
                      'six', 'brelan', 'square', 'full', 'chance', 'yams']

    def __init__(self):
        print("INITIALISATION DU SCORE")

    def setScore(self, result):
        combination = result
        combinations_choosed = {}
        combinations_choosed[combination[0]] = combination[1]
        print(combinations_choosed)
        self.score_possible.remove(combination[0])
        self.sum_points += combination[1]

    def getScore(self):
        print("somme des points: ", self.sum_points)

    def finalScore(self):
        if self.sum_points > 63:
            print("BONUS DE POINTS !!!")
            self.sum_points += 35
        print("SCORE FINAL:", self.sum_points)


Game()
