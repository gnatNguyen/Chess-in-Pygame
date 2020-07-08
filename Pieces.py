import pygame

# WHITE PIECES

class whitePawn():
	def __init__(self, name, x, y):
		self.image = pygame.image.load('Images/wpawn.png')
		self.pieceType = "pawn"
		self.name = name
		self.canMoveTwoSpaces = True

		self.startingX = x
		self.startingY = y

		self.xPos = x
		self.yPos = y

	def showMoves(self):
		self.newYPos = self.yPos - 80

		if self.startingX != self.xPos or self.startingY != self.yPos:
			print("cannot not move two anymore")
			self.canMoveTwoSpaces = False

		if self.canMoveTwoSpaces:
			self.doubleMoveYPos = self.yPos - 160
			return self.newYPos, self.doubleMoveYPos
			
		else:
			return self.newYPos, None

class whiteRook():
	def __init__(self, name, x, y):
		self.image = pygame.image.load('Images/wrook.png')
		self.pieceType = "rook"
		self.name = name
		self.xPos = x
		self.yPos = y

class whiteKnight():
	def __init__(self, name, x, y):
		self.image = pygame.image.load('Images/wknight.png')
		self.pieceType = "knight"
		self.name = name
		self.xPos = x
		self.yPos = y

class whiteBishop():
	def __init__(self, name, x, y):
		self.image = pygame.image.load('Images/wbishop.png')
		self.pieceType = "bishop"
		self.name = name
		self.xPos = x
		self.yPos = y

class whiteQueen():
	def __init__(self):
		self.image = pygame.image.load('Images/wqueen.png')
		self.pieceType = "queen"
		self.name = "White Queen"
		self.xPos = 250
		self.yPos = 570

class whiteKing():
	def __init__(self):
		self.image = pygame.image.load('Images/wking.png')
		self.pieceType = "king"
		self.name = "White King"
		self.xPos = 330
		self.yPos = 570

# BLACK PIECES

class blackPawn():
	def __init__(self, name, x, y):
		self.image = pygame.image.load('Images/bpawn.png')
		self.pieceType = "pawn"
		self.name = name
		self.xPos = x
		self.yPos = y
		self.canMoveTwoSpaces = True

class blackRook():
	def __init__(self, name, x, y):
		self.image = pygame.image.load('Images/brook.png')
		self.pieceType = "rook"
		self.name = name
		self.xPos = x
		self.yPos = y

class blackKnight():
	def __init__(self, name, x, y):
		self.image = pygame.image.load('Images/bknight.png')
		self.pieceType = "knight"
		self.name = name
		self.xPos = x
		self.yPos = y

class blackBishop():
	def __init__(self, name, x, y):
		self.image = pygame.image.load('Images/bbishop.png')
		self.pieceType = "bishop"
		self.name = name
		self.xPos = x
		self.yPos = y

class blackQueen():
	def __init__(self):
		self.image = pygame.image.load('Images/bqueen.png')
		self.pieceType = "queen"
		self.name = "Black Queen"
		self.xPos = 250
		self.yPos = 10

class blackKing():
	def __init__(self):
		self.image = pygame.image.load('Images/bking.png')
		self.pieceType = "king"
		self.name = "Black King"
		self.xPos = 330
		self.yPos = 10
