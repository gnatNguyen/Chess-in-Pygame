import pygame
import time
import Pieces as cp

BOARD_SIZE = 8
HEIGHT = 640
WHITE = (255,255,255)
BLACK = (0,0,0)
BROWN = (222,184,135)
MOVE_LOG = []

class WhitePiecePlayer():
	def __init__(self): 

		self.whiteTurn = True
		self.win = False
		self.capturedPieces = []

class BlackPiecePlayer():
	def __init__(self): 

		self.blackTurn = False
		self.win = False
		self.capturedPieces = []

wPlayer = WhitePiecePlayer()
bPlayer = BlackPiecePlayer()

def main():


	wPawn1 = cp.whitePawn("wP1", 10, 490)
	wPawn2 = cp.whitePawn("wP2", 90, 490)
	wPawn3 = cp.whitePawn("wP3", 170, 490)
	wPawn4 = cp.whitePawn("wP4", 250, 490)
	wPawn5 = cp.whitePawn("wP5", 330, 490)
	wPawn6 = cp.whitePawn("wP6", 410, 490)
	wPawn7 = cp.whitePawn("wP7", 490, 490)
	wPawn8 = cp.whitePawn("wP8", 570, 490)

	wKing = cp.whiteKing()
	wQueen = cp.whiteQueen()
	wBishop1 = cp.whiteBishop("wB1", 170, 570)
	wBishop2 = cp.whiteBishop("wB2", 410, 570)
	wKnight1 = cp.whiteKnight("wK1", 90, 570)
	wKnight2 = cp.whiteKnight("wK2", 490, 570)
	wRook1 = cp.whiteRook("wR1", 10, 570)
	wRook2 = cp.whiteRook("wR2", 570, 570)

	bPawn1 = cp.blackPawn("bP1", 10, 90)
	bPawn2 = cp.blackPawn("bP2", 90, 90)
	bPawn3 = cp.blackPawn("bP3", 170, 90)
	bPawn4 = cp.blackPawn("bP4", 250, 90)
	bPawn5 = cp.blackPawn("bP5", 330, 90)
	bPawn6 = cp.blackPawn("bP6", 410, 90)
	bPawn7 = cp.blackPawn("bP7", 490, 90)
	bPawn8 = cp.blackPawn("bP8", 570, 90)

	bKing = cp.blackKing()
	bQueen = cp.blackQueen()
	bBishop1 = cp.blackBishop("bB1", 170, 10)
	bBishop2 = cp.blackBishop("bB2", 410, 10)
	bKnight1 = cp.blackKnight("bK1", 90, 10)
	bKnight2 = cp.blackKnight("bK2", 490, 10)
	bRook1 = cp.blackRook("bR1", 10, 10)
	bRook2 = cp.blackRook("bR2", 570, 10)

	whitePiecesList = [wKing, wQueen, wPawn1, wPawn2, wPawn3, wPawn4, 
				wPawn5, wPawn6, wPawn7, wPawn8, wBishop1, wBishop2,
				wKnight1, wKnight2, wRook1, wRook2]

	blackPiecesList = [bKing, bQueen, bPawn1, bPawn2, bPawn3, bPawn4, 
				bPawn5, bPawn6, bPawn7, bPawn8, bBishop1, bBishop2,
				bKnight1, bKnight2, bRook1, bRook2]

	pygame.init()
	screen = pygame.display.set_mode((HEIGHT, HEIGHT))
	screen.fill(WHITE)
	pygame.display.set_caption("EPIC CHESS")
	clock = pygame.time.Clock()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			elif event.type == pygame.MOUSEBUTTONDOWN:
				trunc_x, trunc_y = getClickPosition()

				chose_a_piece, selected_piece = findPiece(whitePiecesList, blackPiecesList, trunc_x, trunc_y)

				if chose_a_piece:
					showPossibleMoves(screen, whitePiecesList, blackPiecesList, selected_piece)

					moveToX, moveToY, invalid_move = selectNewTile(whitePiecesList, blackPiecesList, selected_piece)
					
					if invalid_move:
						print("Cannot capture own pieces")
					elif not invalid_move:
						movePiece(selected_piece, moveToX, moveToY)
						

		if bKing in wPlayer.capturedPieces:
			print("White Player Wins")
			running = False

		elif wKing in bPlayer.capturedPieces:
			print("Black Player Wins")
			running = False

		drawBoard(screen)
		drawPieces(screen, whitePiecesList, blackPiecesList)
		pygame.display.flip()

		clock.tick(60)


def drawBoard(screen):
	x = 0
	y = 0
	for col in range(BOARD_SIZE):
		for row in range(BOARD_SIZE):
			if (col+1) % 2 != 0: # if currently on an odd row
				if (row+1) % 2 == 0: # if the square is an even square, it is brown
					square_color = BROWN
				else:
					square_color = WHITE
			elif (col+1) % 2 == 0: # if currently on an even row
				if (row+1) % 2 != 0: # if the square is an odd square, it is brown
					square_color = BROWN
				else:
					square_color = WHITE
			
			pygame.draw.rect(screen, square_color, (x, y, 80, 80))
			x += 80

		y += 80
		x = 0


def drawPieces(screen, whitePiecesList, blackPiecesList):
	for piece in whitePiecesList:
		screen.blit(piece.image, (piece.xPos, piece.yPos))

	for piece in blackPiecesList:
		screen.blit(piece.image, (piece.xPos, piece.yPos))


def getClickPosition():
	mouse_position = pygame.mouse.get_pos()
	trunc_x = int(mouse_position[0]/80) + 1
	trunc_y = int(mouse_position[1]/80) + 1

	return trunc_x, trunc_y


def findPiece(whitePiecesList, blackPiecesList, trunc_x, trunc_y):
	chose_a_piece = False

	for piece in whitePiecesList:
		trunc_piece_x = int(piece.xPos/80) + 1
		trunc_piece_y = int(piece.yPos/80) + 1

		if trunc_x == trunc_piece_x and trunc_y == trunc_piece_y:
			chose_a_piece = True
			return chose_a_piece, piece

	if chose_a_piece == False:
		for piece in blackPiecesList:
			trunc_piece_x = int(piece.xPos/80) + 1
			trunc_piece_y = int(piece.yPos/80) + 1

			if trunc_x == trunc_piece_x and trunc_y == trunc_piece_y:
				chose_a_piece = True
				return chose_a_piece, piece

	if chose_a_piece == False:
		return chose_a_piece, None


def selectNewTile(whitePiecesList, blackPiecesList, selected_piece):
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				noPieceHere = True
				somethingCaptured = False
				invalid_move = False
				captured_piece = ""
				trunc_x, trunc_y = getClickPosition()

				if selected_piece.pieceType == "pawn":
					if abs((int(selected_piece.yPos/80)+1) - trunc_y) == 2 and selected_piece.canMoveTwoSpaces == False:
						invalid_move = True
						return None, None, invalid_move

					if selected_piece in whitePiecesList:
						if int(selected_piece.yPos/80)+1 - trunc_y < 0:
							invalid_move = True
							return None, None, invalid_move

					elif selected_piece in blackPiecesList:
						if int(selected_piece.yPos/80)+1 - trunc_y > 0:
							invalid_move = True
							return None, None, invalid_move

				if selected_piece in blackPiecesList:
					for piece in whitePiecesList:
						trunc_piece_x = int(piece.xPos/80) + 1
						trunc_piece_y = int(piece.yPos/80) + 1
						if trunc_x == trunc_piece_x and trunc_y == trunc_piece_y:
							bPlayer.capturedPieces.append(piece)
							whitePiecesList.remove(piece)
							somethingCaptured = True
							noPieceHere = False
							captured_piece = piece.name
							break

					for piece in blackPiecesList:
						trunc_piece_x = int(piece.xPos/80) + 1
						trunc_piece_y = int(piece.yPos/80) + 1
						if trunc_x == trunc_piece_x and trunc_y == trunc_piece_y:
							invalid_move = True
							noPieceHere = False
							break
					
				elif selected_piece in whitePiecesList:
					for piece in blackPiecesList:
						trunc_piece_x = int(piece.xPos/80) + 1
						trunc_piece_y = int(piece.yPos/80) + 1
						if trunc_x == trunc_piece_x and trunc_y == trunc_piece_y:
							wPlayer.capturedPieces.append(piece)
							blackPiecesList.remove(piece)
							somethingCaptured = True
							noPieceHere = False
							captured_piece = piece.name
							break

					for piece in whitePiecesList:
						trunc_piece_x = int(piece.xPos/80) + 1
						trunc_piece_y = int(piece.yPos/80) + 1
						if trunc_x == trunc_piece_x and trunc_y == trunc_piece_y:
							invalid_move = True
							noPieceHere = False
							break

				if noPieceHere:
					running = False

				elif somethingCaptured:
					print(f'{selected_piece.name} captures {captured_piece}')
					running = False

				elif invalid_move:
					running = False

				return trunc_x, trunc_y, invalid_move


def movePiece(selected_piece, moveToX, moveToY):
	current_x = int(selected_piece.xPos/80) + 1
	current_y = int(selected_piece.yPos/80) + 1

	move_difference_x = moveToX - current_x
	move_difference_y = moveToY - current_y

	if move_difference_x > 0:
		selected_piece.xPos += 80*move_difference_x

	if move_difference_y > 0:
		selected_piece.yPos += 80*move_difference_y

	if move_difference_x < 0:
		selected_piece.xPos += 80*move_difference_x

	if move_difference_y < 0:
		selected_piece.yPos += 80*move_difference_y

	print(f'{selected_piece.name} moves to {moveToX}, {moveToY}')

def showPossibleMoves(screen, whitePiecesList, blackPiecesList, selected_piece):
	newYPos, doubleMoveYPos = selected_piece.showMoves()
	pygame.draw.circle(screen, BLACK, (selected_piece.xPos+30, newYPos+30), 15)
	if doubleMoveYPos != None:
		pygame.draw.circle(screen, BLACK, (selected_piece.xPos+30, doubleMoveYPos+30), 15)

	pygame.display.update()



main()
pygame.quit()