from environment import Environment

env = Environment()

for i in range(100):
    env.update_state()
    env.print_state()
