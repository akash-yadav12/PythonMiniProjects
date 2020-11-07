def isSpaceFree(pos):
    return board[pos] == ' '

def insertLetter(letter,pos):
    board[pos] = letter

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] +' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('============')
    print('   |   |   ')
    print(' ' + board[4] +' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('============')
    print('   |   |   ')
    print(' ' + board[7] +' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    return True

def checkWinner(b,le):
     return ((b[1] == le and b[2] == le and b[3] == le) or
     (b[4] == le and b[5] == le and b[6] == le) or
     (b[7] == le and b[8] == le and b[9] == le) or
     (b[1] == le and b[4] == le and b[7] == le) or 
     (b[2] == le and b[5] == le and b[8] == le) or
     (b[3] == le and b[6] == le and b[9] == le) or
     (b[1] == le and b[5] == le and b[9] == le) or 
     (b[3] == le and b[5] == le and b[7] == le))

def playerMove():
    run = True
    while run:
        move = input('please select the position of x from 1 to 9: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isSpaceFree(move):
                    run = False
                    insertLetter('X',move)
                else:
                    print('Sorry this position is occupied')
            else:
                print('please enter a valid input i.e between 1 to 9')
        except:
            print('Please type a number')
    # computerMove()

def selectRand(ar):
    import random
    return ar[random.randrange(0,len(ar))]


def computerMove():
    possibleMoves = [x for x,le in enumerate(board) if le == ' ' and x!=0]
    move = 0
    if isBoardFull(board):
        return 0
    for le in ['0','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = le
            if checkWinner(boardCopy, le):
                move = i
                return move
    #for corner elemments
    cornerOpt = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornerOpt.append(i)
    if len(cornerOpt)> 0:
        move = selectRand(cornerOpt)
        return move
    
    #check if center position is availble
    if 5 in possibleMoves:
        move = 5
        return move
    
    #edge elements check
    edgesopt = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesopt.append(i)
    if len(edgesopt) > 0:
        move = selectRand(edgesopt)
        return move

def main():
    print('Welcome to the game')
    printBoard(board)

    while not isBoardFull(board):
        if not(checkWinner(board,'0')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, You lose :/')
            break
        if not(checkWinner(board,'X')):
            move = computerMove()
            if move == 0:
                print('Tie Game')
            else:
                insertLetter('0',move)
                print('Computer placed an 0 in position',move)
                printBoard(board)
        else:
            print('You win')
            break

    if isBoardFull(board):
        print('Tie Game')

while(True):
    s = input('Do you want to Play again (y/n)?')
    if s.lower() == 'y':
        board = [' ' for x in range(10)]
        print('======================')
        main()
    else:
        break