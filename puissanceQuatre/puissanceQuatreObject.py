# Step 1 : Structure
class Game:
    print("Mise en place de la grille")

    def __init__(self, nblines = 6, nbcolumns = 7):
        self.player = 1
        self.nblines = int(nblines)
        self.nbcolumns = int(nbcolumns)
        self.grid = []
        
        colonne = 0

        for l in range(0, nblines):
            ligne = [colonne for i in range(0, nbcolumns)]
            self.grid.append(ligne)
    
    # Step 2 : Show the grid of the game  
    def show(self):
        print(self.grid)

    def placeAPawn(self, column = input("Choose your column to place your pawn: ")):
        self.column = int(column)

        for i in self.grid:
            if i[self.column] == 0:
                i[self.column] = self.player
                print("I place my pawn with my number's player", i[self.column], "below")
                break

        print(self.grid)
    
    def endOfTheGame(self): #boolean
        win = 0

        for line in self.grid:
            # print(line)
            for column in line:
                # print(column)
                if column == self.player:
                    win += 1
                    print("count win: ", win)
                else:
                    win = column
                    # print("reset count win:", win)
        
        if win >= 4:
            return True
        else:
            return False

    def nextPlayer(self):
        if self.player == 1:
            self.player += 1
        else:
            self.player -= 1


    def playGameRound(self):
        self.show()
        self.placeAPawn()
    
        if not self.endOfTheGame():
            self.nextPlayer()
            self.playGameRound()

structure = Game()
structure.playGameRound()
