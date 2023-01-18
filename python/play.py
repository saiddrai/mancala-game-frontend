import math
from copy import deepcopy
import time
class Play:
    # def __init__(self):

    def humanTurn(self, game,returnedPit):
        move_made = False
        
        while not move_made:
            if returnedPit in game.state.possibleMoves(1):
                 current_player = game.state.doMove(1, returnedPit )
                 move_made = True
                 break
        return current_player,game


    def computerTurn(self, game, play, depth = 10):
        if len(game.state.possibleMoves(2)) > 0:
            
            player_1_four = all(game.state.board[x] == 4 for x in game.state.pits1)
            player_2_four = all(game.state.board[x] == 4 for x in game.state.pits2)
            
            if player_1_four and player_2_four:
              current_player = game.state.doMove(2, 'J')
            
            else:  
              best_node = play.minmaxAlphaBetaPruning( game, 2, depth, -math.inf, math.inf)
              current_player = game.state.doMove(2, best_node[1])
            
        return current_player, game

    def minmaxAlphaBetaPruning(self, game, player, depth, alpha, beta):
        if depth == 0 or game.gameOver():
            return game.evaluate(), None

        if player == 1:
            best_value = -math.inf
            best_move = None
            
            for move in game.state.possibleMoves(player):
                new_game = deepcopy(game)
                # Jouer le coup sur la copie du jeu
                new_game.state.doMove(player, move)
                
                # Utiliser récursivement l'algorithme Minimax avec élagage alpha-beta
                # pour trouver la valeur du meilleur coup
                value, _ = self.minmaxAlphaBetaPruning(new_game, 2, depth - 1, alpha, beta)
                
                # Si la valeur du coup est supérieure à la meilleure valeur actuelle, 
                # mettre à jour la meilleure valeur et le meilleur mouvement
                if value > best_value:
                    best_value = value
                    best_move = move
                    
                # Mettre à jour alpha en prenant la valeur maximale entre alpha et la meilleure valeur actuelle
                alpha = max(alpha, best_value)
                
                # Si alpha est supérieur ou égal à beta, interrompre l'exécution de la boucle grâce à l'élagage alpha-beta
                if alpha >= beta:
                    break
                  
            # Retourner la meilleure valeur et le meilleur mouvement
            return best_value, best_move
        else:
            # Initialiser la meilleure valeur et le meilleur mouvement
            best_value = math.inf
            best_move = None
            
            # Pour chaque mouvement possible
            for move in game.state.possibleMoves(player):
              # Créer une copie profonde du jeu
                new_game = deepcopy(game)
                # Jouer le coup sur la copie du jeu
                new_game.state.doMove(player, move)
                
                # Utiliser récursivement l'algorithme Minimax avec élagage alpha-beta
                # pour trouver la valeur du meilleur coup
                value, _ = self.minmaxAlphaBetaPruning(new_game, 1, depth - 1, alpha, beta)
                
                # Si la valeur du coup est inférieure à la meilleure valeur actuelle, 
                # mettre à jour la meilleure valeur et le meilleur mouvement
                if value < best_value:
                    best_value = value
                    best_move = move
                
                # Mettre à jour beta en prenant la valeur minimale entre beta et la meilleure valeur actuelle
                beta = min(beta, best_value)
                
                # Si alpha est supérieur ou égal à beta, interrompre l'exécution de la boucle grâce à l'élagage alpha-beta
                if alpha >= beta:
                    break
            
            # Retourner la meilleure valeur et le meilleur mouvement
            return best_value, best_move