#prints the game board to the screen
def printBoard(gameBoard):
	print(gameBoard['TL'] + ' | ' + gameBoard['TM'] + ' | ' + gameBoard['TR'])
	print('--+---+--')
	print(gameBoard['ML'] + ' | ' + gameBoard['MM'] + ' | ' + gameBoard['MR'])
	print('--+---+--')
	print(gameBoard['BL'] + ' | ' + gameBoard['BM'] + ' | ' + gameBoard['BR'])

#assigns a player move to the gameboard
def makeMove(gameBoard, move, turn):
	if turn % 2 == 0:
		gameBoard[move] = 'X'
	else:
		gameBoard[move] = 'O'

#checks to see if the most recent move has resulted in a win for either player
def winCondition(gameBoard):
	return checkRow(gameBoard) or checkColumn(gameBoard) or checkDiagonal(gameBoard)

#checks each row for a win condition
def checkRow(gameBoard):
	rowWin = False
	topRowValue = gameBoard['TL'] + gameBoard['TM'] + gameBoard['TR']
	middleRowValue = gameBoard['ML'] + gameBoard['MM'] + gameBoard['MR']
	bottomRowValue = gameBoard['BL'] + gameBoard['BM'] + gameBoard['BR']

	if 'X'*3 in (topRowValue, middleRowValue, bottomRowValue):
		rowWin = True
	elif 'O'*3 in (topRowValue, middleRowValue, bottomRowValue):
		rowWin = True

	return rowWin

#checks each column for a win condition
def checkColumn(gameBoard):
	columnWin = False
	leftColumnValue = gameBoard['TL'] + gameBoard['ML'] + gameBoard['BL']
	middleColumnValue = gameBoard['TM'] + gameBoard['MM'] + gameBoard['BM']
	rightColumnValue = gameBoard['TR'] + gameBoard['MR'] + gameBoard['BR']

	if 'X'*3 in (leftColumnValue, middleColumnValue, rightColumnValue):
		columnWin = True
	elif 'O'*3 in (leftColumnValue, middleColumnValue, rightColumnValue):
		columnWin = True

	return columnWin

#checks the diagonals
def checkDiagonal(gameBoard):
	diagonalWin = False
	leftDiagonal = gameBoard['TL'] + gameBoard['MM'] + gameBoard['BR']
	rightDiagonal = gameBoard['BL'] + gameBoard['MM'] + gameBoard['TR']

	if 'X'*3 in (leftDiagonal, rightDiagonal):
		diagonalWin = True
	elif 'O'*3 in (leftDiagonal, rightDiagonal):
		diagonalWin = True

	return diagonalWin

#the main function I guess

#initialize the gameboard
gameBoard = { 'TL' : ' ', 'TM' : ' ', 'TR' : ' ',
			'ML' : ' ', 'MM' : ' ', 'MR' : ' ',
			'BL' : ' ', 'BM' : ' ', 'BR' : ' '}

printBoard(gameBoard)

for turn in range(0, 9):
	print('Make a move: ')
	playerMove = input()
	
	makeMove(gameBoard, playerMove, turn)

	printBoard(gameBoard)

	if winCondition(gameBoard):
		break