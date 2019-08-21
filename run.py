from environment import Environment
from agent import Agent

env = Environment()
agent = Agent()

FRAMES_TO_RUN = 10

for i in range(FRAMES_TO_RUN):
    env.update_state()
    env.print_state()
