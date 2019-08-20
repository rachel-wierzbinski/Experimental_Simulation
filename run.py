from environment import Environment
from agent import Agent

env = Environment()
agent = Agent()

for i in range(100):
    env.update_state()
    env.print_state()
