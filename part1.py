'''
    Programming Assignment 1 - Part1
    Submitted by Balaji Senthilkumar
'''
#The funtion to load the board (.txt to 2Dlist/array)
def loadBoard(board):
    inputFile = open(board, 'r')
    myBoard = []
    for row in inputFile:
        myBoard.append(row.split())
    return myBoard


#THE FUNCTION TO PRINT 'myBoard'
def printBoard(myBoard): 
    for row in myBoard:
        print (" ".join(map(str,row)))
    # print('****'+myBoard[2][3])
   
    
def possibleMoves(currentPosition,myBoard):
    #So here I have used a graph based approach, for figuring out the solution,
    #  using x_co_ordinates and y_co_oridinates as the positional arguments.
    
    x_co_ordinate,y_co_ordinate = currentPosition #spreading operation 
    
    possibleMovesArray=[]
    
    limit=len(myBoard) # ensuring that the program does not cause an outOfBounds or any negative array positioning
    
    if(x_co_ordinate+1<limit and y_co_ordinate<limit): #left to right
        possibleMovesArray.append((x_co_ordinate+1,y_co_ordinate))
    
    if(x_co_ordinate<limit and y_co_ordinate+1<limit): #Top-Bottom
        possibleMovesArray.append((x_co_ordinate,y_co_ordinate+1))
    
    if(x_co_ordinate+1<limit and y_co_ordinate+1<limit): #diagonal 1
        possibleMovesArray.append((x_co_ordinate+1,y_co_ordinate+1))
    
    if(x_co_ordinate+1<limit and ((y_co_ordinate-1<limit)and y_co_ordinate-1>=0)): #diagonal 2
        possibleMovesArray.append((x_co_ordinate+1,y_co_ordinate-1))
    
    if(((x_co_ordinate-1<limit)and x_co_ordinate-1>=0) and ((y_co_ordinate-1<limit)and y_co_ordinate-1>=0)): #diagonal 3
        possibleMovesArray.append((x_co_ordinate-1,y_co_ordinate-1))
    
    if(((x_co_ordinate-1<limit)and x_co_ordinate-1>=0) and (y_co_ordinate+1<limit)): #diagonal 4
        possibleMovesArray.append((x_co_ordinate-1,y_co_ordinate+1))
    
    if(((x_co_ordinate-1<limit)and x_co_ordinate-1>=0) and y_co_ordinate<limit): #right to left
        possibleMovesArray.append((x_co_ordinate-1,y_co_ordinate))
    
    if(x_co_ordinate<limit and ((y_co_ordinate-1<limit)and y_co_ordinate-1>=0)): #Bottom Up
        possibleMovesArray.append((x_co_ordinate,y_co_ordinate-1))
    
    return set(possibleMovesArray)


def legalMoves(possibleMovesArg,pathArg):
    legalMovesArray=[]          #creating a list to store the legal moving positions(co_ordinates)
    for pos in possibleMovesArg:    
        if pos not in legalMovesArray:  #checking for non-repetion of positions, to comply the rules of the game
            legalMovesArray.append(pos) 
    return set(legalMovesArray)
   

def examineState(myBoard,currentPosition,path,myDict):
    wordList = []
    for i in path:
        x_co_ordinate, y_co_ordinate = i    #spreading x_co_ordinate and y_co_ordinate out of the path 
        wordList.append(myBoard[x_co_ordinate][y_co_ordinate])
    x_co_ordinate, y_co_ordinate = currentPosition 
    wordList.append(myBoard[x_co_ordinate][y_co_ordinate])
    finalList = ''.join([str(i) for i in wordList])
    # print(finalList)
    if finalList.lower() in myDict: #Checking whether the word is in the given dicionary
        return (finalList.lower(),'Yes')
    else:
        return(finalList.lower(),'No')



    
#testing output of part1

myBoard=loadBoard('board.txt')
printBoard(myBoard)
# pos=(2,2)#get user input
# pm=possibleMoves(pos,myBoard)
#print(pm)
# pathArg=((0,0),(1,1),(2,2),(3,3))
# print(legalMoves((possibleMoves(pos,myBoard)),pathArg))
# print(legalMoves( possibleMoves((2,2), myBoard), ( (1,1),(1,2),(1,3),(2,3),(3,2) ) ))
# mainDictionary=open('dictionary.txt').read()
#         for word in mainDictionary:
#             word.lower
# print(examineState(myBoard,pos,((1,1),(1,0)),mainDictionary))
# myDict = open('twl06.txt').read()
print(possibleMoves((3,3),myBoard))
print(legalMoves( possibleMoves((1,2), myBoard), ( (1,0),(2,0),(2,1),(2,2) )))
myDict = frozenset(word.strip() for word in open("twl06.txt"))
print(examineState(myBoard,(0,0),((1,1),(1,0)), myDict))#- max,yes
# print(examineState(myBoard,(3,1),((0,1),(1,0),(1,1),(2,1)), myDict)) - ocmfg,no
print(examineState(myBoard,(0,3),( (1,1), (0,1),(0,2) ) ,myDict)) #- mopy,yes
# print(examineState(myBoard,(0,0),( (3,3), (2,2), (1,1) ) ,myDict)) #uemj, no
# print(examineState(myBoard,(3,3),( (2,2),(2,1),(2,0),(3,0),(3,1),(3,2) ) ,myDict)) #efxpgvu,No






