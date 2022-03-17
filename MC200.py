from MonteCarloTreeSearch import MonteCarloTreeSearch
from Frame import Frame

class MC200:

    def get_move(frame: Frame):
        
        iterations = 200
        exploratory_factor = 5
        
        MC200 = MonteCarloTreeSearch(frame, exploratory_factor)
        action = MC200.monte_carlo_tree_search(iterations)
        
        return action