import random
def hangman():
    word = random.choice(['akame','arima','tatsumi','shinra','subaru','rem','okabe','elpsycongro','kurisu','hashida','yagamilight'])
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turn = 10 
    guessMade = ''
    while len(word) > 0:
        main = ''
        for lt in word:
            if lt in guessMade:
                main += lt
            else:
                main = main + '_' + " "
        if main == word:
            print(main)
            print('You Win')
            break
        print('Guess The word:',main)
        guess = input()

        if guess in validletters:
            guessMade += guess
        else:
            print('enter a valid letter')
            guess = input()
        if guess not in word:
            turn -= 1
            if turn == 9:
                print('9 turns left')
                print('  ===========  ')
            elif turn == 8:
                print('8 turns left')
                print('  ===========  ')
                print('       0       ')
            elif turn == 7:
                print('7 turns left')
                print('  ===========  ')
                print('       0       ')
                print('       |       ')
            elif turn == 6:
                print('6 turns left')
                print('  ===========  ')
                print('       0       ')
                print('       |       ')
                print('      /        ')
            elif turn == 5:
                print('5 turns left')
                print('  ===========  ')
                print('       0       ')
                print('       |       ')
                print('      / \      ')
            elif turn == 4:
                print('4 turns left')
                print('  ===========  ')
                print('     \ 0       ')
                print('       |       ')
                print('      / \      ')
            elif turn == 3:
                print('3 turns left')
                print('  ===========  ')
                print('     \ 0 /     ')
                print('       |       ')
                print('      / \      ')
            elif turn == 2:
                print('2 turns left')
                print('  ===========  ')
                print('     \ 0 / |   ')
                print('       |       ')
                print('      / \      ')
            elif turn == 1:
                print('1 turns left')
                print('  ===========  ')
                print('     \ 0_|/    ')
                print('       |       ')
                print('      / \      ')
            elif turn == 0:
                print('You lose')
                print('You let a kind man die')
                print('  ===========  ')
                print('       0_|   ')
                print('     / | \     ')
                print('      / \      ')              
                break

        

name = input('enter your name:')
print('Welcome',name)
print('=======================')
print('Try to guess the word in less than 10 attempts')
hangman()
print()