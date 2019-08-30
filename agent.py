import numpy as np

class Agent:
    def __init__(self):
        self.actions = [0, 1] # Jump, Nothing
        self.is_falling = False
        self.is_jumping = False
        
        self.height = 1
        self.MAX_HEIGHT = 1
        
        self.q_table = dict()
        
    def act(self, action):
        is_jumping = self.is_jumping
        is_falling = self.is_falling
        
        height = self.height  
        
        # Jump logic (if not max height keep jumping, fall once you reach max height)
        if is_jumping or is_falling:
            # if you are jumping and haven't reached your max height
            if is_jumping and height > 0:
                self.height -= 1
            # if you reached max height, start falling
            elif is_jumping:
                self.is_jumping = False
                self.is_falling = True
            # if you aren't on the ground, continue to fall
            elif is_falling and height < self.MAX_HEIGHT:
                self.height += 1
            # once you've hit the ground, stop falling
            else:
                is_falling = False
        else:
            # Jump
            if action == 0:
                is_jumping = True
                self.height = 1
            # Nothing
            else:
                pass
                
    def update_q_table(self, state, action):
        if state not in self.q_table:
            self.q_table.update(state)