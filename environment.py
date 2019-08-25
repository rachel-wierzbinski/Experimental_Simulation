import numpy as np
import random

class Environment:
    def __init__(self):
        self.state = np.zeros([2, 10], dtype = int)
        self.count_since_obstacle = 0
        
    def step(self):
        old_state = self.state()
        
        self.update_state()
        new_state = self.state()
        
        reward = self.reward()
        
        return old_state, new_state, reward
        
    def update_state(self):
        for i in range(9):
            self.state[0][i] = self.state[0][i + 1]
            self.state[1][i] = self.state[1][i + 1]
        
        if self.count_since_obstacle > 3:
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
            
    def reward(self):
        # penalty for dying and reward for accumulating score?
        return 0
        
    # TODO
    def is_done(self, agent_height):
        # we can change this function later to work with any matrix (state size)... but let's be lazy for now
        if agent_height == 0 and self.state[1][0] == 1:
            return True
        elif agent_height == 1 and self.state[0][0] == 1:
            return True
        else:
            return False
    
    def print_state(self):
        print(self.state)
        print()
