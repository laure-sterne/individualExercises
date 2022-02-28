# Step 1 : Structure
class Game:
    print("Mise en place de la grille")

    def __init__(self, nblines = 6, nbcolumns = 7):
        self.player = 1
        self.nblines = int(nblines)
        self.nbcolumns = int(nbcolumns)
        self.grid = []
        
        colonne = 1

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
            else:
                i + 1
                print("Go to the next index!")
                
        print(self.grid)
    
    def endOfTheGame(self): #boolean
        for p in self.grid:
            if p[p] & p[p+1] & p[p+2] & p[p+3] == self.joueur:
                print(self.joueur, "has won!")
            else:
                print("play an another game round!")
                
    def nextPlayer(self):
        if self.player == 1:
            self.player += 1
        else:
            self.player -= 1
        pass


structure = Game()
# structure.playGameRound()

structure.show()
structure.endOfTheGame()


# def playGameRound(self):
#     self.show()
#     self.placeAPawn()

#     if not self.endOfTheGame():
#         self.nextPlayer()
#         self.playGameRound()