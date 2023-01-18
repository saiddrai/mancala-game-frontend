class MancalaBoard:
    def __init__(self):
        # Initialisation du plateau de jeu
        # Les clés sont les indices des fosses et magasins, et les valeurs sont le nombre de seeds
        self.board = {'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 4, 'F': 4,
                     'G': 4, 'H': 4, 'I': 4, 'J': 4, 'K': 4, 'L': 4,
                      'Goal1': 0, 'Goal2': 0}
        
        # pits of the first player
        self.pits1 = ('A', 'B', 'C', 'D', 'E', 'F')
        
        # pitds of the second player
        self.pits2 = ('G', 'H', 'I', 'J', 'K', 'L')
        
        # Dictionary to store every opposite pits to each other
        self.opposite_pit = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K',
                         'F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D', 'K': 'E', 'L': 'F'}
        
        # Dictionary to store the next pit to each pit
        self.next_pit = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'Goal1',
                     'Goal1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G', 'G': 'Goal2', 'Goal2': 'A'}

    #Possible moves, retun the indexes where we can take seeds using the ASCII Code of the pits
    def possibleMoves(self, player):
        # Si le joueur 1 joue, on retourne les indices des fosses du joueur 1 qui contiennent des seeds
        if player == 1:
            return [pit for pit in self.pits1 if self.board[pit] > 0]
        
        # Si le joueur 2 joue, on retourne les indices des fosses du joueur 2 qui contiennent des seeds
        else:
            return [pit for pit in self.pits2 if self.board[pit] > 0]
        # possibleMoves = []
        # for i in range(ord('A'), ord('L')+1):
        #     if board[chr(i)] !=0:
        #         possibleMoves.append(chr(i))
        # return possibleMoves

    def doMove(self, player, pit):
        # Récupération du nombre de seeds dans la fosse choisie
        seeds = self.board[pit]
        self.board[pit] = 0
        
        # putting the seed we took from the pit in the next pits
        while seeds > 0:
            pit = self.next_pit[pit]
            self.board[pit] += 1
            seeds = seeds-1
            
        # if the last seed finishes in the Goal of the player, we'll play again
        if (pit == 'Goal1' and player == 1) or (pit == 'Goal2' and player == 2):
            return player
          
        # if the next pit doesn't contain a stone, we will take all the seeds i the opposite pit and add it to the player goal
        if player == 1 and pit in self.pits1 and self.board[pit] == 1:
            oppositePosition = self.oppositePit[pit]
            self.board['Goal1'] += self.board[oppositePosition]+1
            self.board[oppositePosition] = 0
            self.board[pit] = 0

        if player == 2 and pit in self.pits2 and self.board[pit] == 1:
            oppositePosition = self.oppositePit[pit]
            self.board['Goal2'] += self.board[oppositePosition]+1
            self.board[oppositePosition] = 0 
            self.board[pit] = 0

        
        if (player == 1):
            return 2
        else:
            return 1