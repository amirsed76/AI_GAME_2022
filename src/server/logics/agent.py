from logics.network import Socket
from logics.map import Tile
from logics import game_rules

PLAYER_CHARACTERS = ["A", "B", "C", "D"]


class Agent:
    def __init__(self, agent_id, tile, init_score, connection: Socket):
        self.tile = tile
        self.init_score = init_score  # change_it maybe
        self._id = agent_id
        self.connection = connection
        self.gems = []
        self.hit_hurts = []
        self.turn_age = 0
        self.move_history = []
        self.keys = []

    @property
    def id(self):
        return self._id + 1

    @property
    def score(self):
        # change_it
        point = self.init_score
        gem_counts = self.get_gems_count()
        for i, gem_count in enumerate(gem_counts.values()):
            point += gem_count * game_rules.GEM_SCORES[i]
        point += len(self.hit_hurts) * game_rules.HIT_HURT
        point += self.turn_age * game_rules.TURN_HURT
        return point

    @property
    def character(self):
        return PLAYER_CHARACTERS[self._id]

    @property
    def name(self):
        return PLAYER_CHARACTERS[self._id]

    def add_gem(self, gem):
        self.gems.append(gem)

    def add_key(self, key):
        # TODO validate
        # can agent agg duplicated keys??
        self.keys.append(key)

    def get_keys_count(self):
        return {
            "key1": self.gems.count(Tile.TileType.KEY1),
            "key2": self.gems.count(Tile.TileType.KEY2),
            "key3": self.gems.count(Tile.TileType.KEY3),
        }

    def has_key(self, key):
        return key in self.keys

    def get_gems_count(self):
        return {
            "gem1": self.gems.count(Tile.TileType.GEM1),
            "gem2": self.gems.count(Tile.TileType.GEM2),
            "gem3": self.gems.count(Tile.TileType.GEM3),
            "gem4": self.gems.count(Tile.TileType.GEM4),
        }

    def get_information(self):
        gem1, gem2, gem3, gem4 = self.get_gems_count().values()

        return {
            "score": self.score,
            "hit_hurts_count": len(self.hit_hurts),
            "gem1": gem1,
            "gem2": gem2,
            "gem3": gem3,
            "gem4": gem4,
        }
