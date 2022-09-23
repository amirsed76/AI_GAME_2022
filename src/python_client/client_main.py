import random
from base import BaseAgent, Action

actions = [
    Action.DOWN_RIGHT, Action.RIGHT, Action.RIGHT, Action.RIGHT,Action.RIGHT, Action.DOWN_RIGHT, Action.UP, Action.UP_LEFT,
    Action.DOWN_RIGHT,
    Action.DOWN_LEFT
]


class Agent(BaseAgent):
    i = -1

    def do_turn(self) -> Action:
        self.i += 1

        if self.i < len(actions):
            return actions[self.i]

        return random.choice(
            [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT, Action.TELEPORT, Action.NOOP])


if __name__ == '__main__':
    data = Agent().play()
    print("FINISH : ", data)
