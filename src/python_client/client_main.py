import random
from base import BaseAgent, Action



class Agent(BaseAgent):
    # actions = [Action.RIGHT] + [Action.TELEPORT] * 100
    def do_turn(self) -> Action:
        # return self.actions.pop(0)
        return random.choice(
            [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT, Action.DOWN_RIGHT, Action.DOWN_LEFT, Action.UP_LEFT,
             Action.UP_RIGHT, Action.NOOP])


if __name__ == '__main__':
    data = Agent().play()
    print("FINISH : ", data)
