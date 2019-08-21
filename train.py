from environment import Environment
from agent import Agent

env = Environment()
agent = Agent()

EPISODES = 100

EXPLORATION_RATE = 0.1

for episode in range(EPISODES):
    if random.uniform(0, 1) < EXPLORATION_RATE:
        # random action
        action = -1
        agent.act(action)
    else:
        # learned action
        action = -1
        agent.act(action)
    
