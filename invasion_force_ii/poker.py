#!/usr/bin/env python3
import random
import math

class OpponentTypes:
    CARDCOUNTER = 0
    PLANT = 1
    BLUFF = 2
    WIS = 3

def main():
    numOpponents = 3
    isAnotherRound = True
    opponents = [OpponentTypes.BLUFF, OpponentTypes.WIS, OpponentTypes.PLANT]
    isRandomize = not getYnAsTf('Do you want to use the standard table of 3 (y/n)? ')

    if isRandomize:
        isInvalid = True
        numOpponents = input('How many opponents? ')
        while isInvalid:
            try:
                numOpponents = int(numOpponents)
                isInvalid = False
            except ValueError:
                numOpponents = input('Invalid number. How many opponents? ')

        possibleOpponents = [OpponentTypes.CARDCOUNTER, OpponentTypes.BLUFF, OpponentTypes.WIS, OpponentTypes.PLANT]
        onlyOneAllowed = [OpponentTypes.CARDCOUNTER, OpponentTypes.PLANT]
        opponents = []

        while len(opponents) < numOpponents:
            opponent = random.choice(possibleOpponents)
            opponents.append(opponent)
            if opponent in onlyOneAllowed:
                possibleOpponents.remove(opponent)

    print('Starting an Invasion Force II simulated poker game. Opponents are as follows:')
    i = 0
    while i < numOpponents:
        printOpponent(opponents[i], i, True, 0)
        i = i+1

    while isAnotherRound:
        numRound = 0
        tippedRounds = getTippedRounds()
        while numRound < 8:
            isTipped = numRound in tippedRounds
            print()
            print('----------------------------')
            print()
            print('Starting round ' + str(numRound + 1))

            if isTipped:
                print('The Plant is tipped this round!')

            i = 0
            input("Press Enter to continue...")
            print()

            while i < numOpponents:
                printOpponent(opponents[i], i, False, numRound, isTipped)
                i = i+1
            print(str(numRound + 1) + ' is complete.')
            numRound = numRound + 1
        isAnotherRound = getYnAsTf('Another Round (y/n)?')
    print('Ending game...')


def getYnAsTf(textPrompt):
    yn = ''

    while 'y' not in yn and 'n' not in yn:
        yn = input(textPrompt)
        yn = yn.lower()

    return('y' in yn)

def printOpponent(opponent, index, isPrintRules, numRound, isTipped=False):
    opponentNum = index + 1
    print('Opponent ' + str(opponentNum) + ':')
    roll = rollD20()
    bonus = 0

    match opponent:
        case OpponentTypes.CARDCOUNTER:
            print('Card Counter')
            if isPrintRules:
                print('Each round, roll d20 + Int (+2) + round counter (0-7)')
            else:
                print('Raw roll was ' + str(roll))
                bonus = 2 + numRound
        case OpponentTypes.PLANT:
            print('Church of Norebo Plant')
            if isPrintRules:
                print('Each round, roll d20 + 2. On two randomized rounds, however, gain hidden knowledge from dealer and get')
                print('additional +10 (total +12). Plant will know if they have been "tipped off" this round at the very start')
                print('of round. With DC18 Sense Motive, other contestants can gain +5 as well on a "tipped" round.')
            elif isTipped:
                bonus = 12
            else:
                bonus = 2
        case OpponentTypes.BLUFF:
            print("Charismatic Bluffer")
            if isPrintRules:
                print("Roll 1d20+5 (3 CHA 2 Bluff)")
            else:
                bonus = 5
        case OpponentTypes.WIS:
            print ("Motive Senser")
            if isPrintRules:
                print("Rolls d20+3 WIS + COUNTDOWN, where COUNTDOWN is a number that starts at +3 and decreases by 1 after every 2 rounds.")
            else:
                bonus = 3 + ((7 - numRound) // 2)
                print
        case _:
            print('Invalid Value')

    if not isPrintRules:
        print('Raw roll was ' + str(roll))
        print('Total check was ' + str(roll + bonus))
    print()

def rollD20():
    return(math.ceil(random.random() * 20))

def getTippedRounds():
    rounds = [0, 1, 2, 3, 4, 5, 6, 7]
    round1 = random.choice(rounds)
    rounds.remove(round1)
    round2 = random.choice(rounds)
    return([round1, round2])

if __name__ == "__main__":
    main()
