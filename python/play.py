import math
from copy import deepcopy
import time
class Play:
    # def __init__(self):

    def humanTurn(self, game):
        # Initialiser une variable (flag) pour suivre si un coup valide a été joué
        move_made = False
        
        # Exécuter la boucle jusqu'à ce qu'un coup valide soit joué
        while not move_made:
            returnedPit = game.state.playFoss()
            # Si la fosse est un coup valide, jouer le coup et définir le drapeau sur True
            if returnedPit['fosse'] in game.state.possibleMoves(1):
                 current_player = game.state.doMove(1, returnedPit['fosse'] )
                 move_made = True
                 break
            # Pause de la boucle de jeu pendant un court moment pour permettre au ordinateur de traiter les événements
            time.sleep(50)
        # Retourner le joueur suivant
        return current_player


    def computerTurn(self, game, play, depth = 8):
        # Si il y a au moins un coup valide pour le joueur 2
        if len(game.state.possibleMoves(2)) > 0:
            # Trouver le meilleur coup à jouer grâce à l'algorithme Minimax avec élagage alpha-beta
            
            player_1_four = all(game.state.board[x] == 4 for x in game.state.player_1_pits)
            player_2_four = all(game.state.board[x] == 4 for x in game.state.player_2_pits)
            
            if player_1_four and player_2_four:
              current_player = game.state.doMove(2, 'J')
            
            else:  
              best_node = play.minmaxAlphaBetaPruning( game, 2, depth, -math.inf, math.inf)
              # Jouer le coup et récupérer l'identifiant du joueur suivant
              current_player = game.state.doMove(2, best_node[1])
            
        # Retourner le joueur suivant et l'état du jeu    
        return current_player, game

    def minmaxAlphaBetaPruning(self, game, player, depth, alpha, beta):
        # Si la profondeur de recherche atteint zéro ou si le jeu est terminé, 
        # retourner la valeur d'évaluation du jeu et aucun mouvement (None)
        if depth == 0 or game.gameOver():
            return game.evaluate(), None

        # Si c'est au tour du joueur 1 de jouer
        if player == 1:
            # Initialiser la meilleure valeur et le meilleur mouvement
            best_value = -math.inf
            best_move = None
            
            # Pour chaque mouvement possible
            for move in game.state.possibleMoves(player):
                # Créer une copie profonde du jeu
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