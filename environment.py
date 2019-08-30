import numpy as np
import random

class Environment:
    def __init__(self):
        self.state = np.zeros([2, 10], dtype = int)
        self.count_since_obstacle = 0
        
    def step(self):
        old_state = self.state
        
        self.update_state()
        new_state = self.state
        
        reward = self.reward()
        
        return old_state, new_state, reward
        
    def update_state(self):
        for i in range(9):
            self.state[0][i] = self.state[0][i + 1]
            self.state[1][i] = self.state[1][i + 1]
        
        if self.count_since_obstacle > 8:
            n = random.randint(0, 1)
            
            if n == 0:
                self.state[0][9] = 1
                self.state[1][9] = 0
            else:
                self.state[0][9] = 0
                self.state[1][9] = 1
              
            self.count_since_obstacle = 0
            
        else:
            self.state[0][9] = 0
            self.state[1][9] = 0

            self.count_since_obstacle += 1
            
    # TODO
    @staticmethod
    def reward():
        # penalty for dying and reward for accumulating score?
        return 0
        
    # TODO
    def is_done(agent_height):
        # check if there is a collision at a given frame
        
        # if game over return false, else return true
        return False
    
    def print_state(self):
        print(self.state)
        print()
