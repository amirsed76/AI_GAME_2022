# change_it
GEM_SCORES = [50, 100, 200, 300]

HIT_HURT = -20
BARBED_HURT = -20
STRAIGHT_MOVE_HURT = -1
DIAGONAL_MOVE_HURT = -2

GEM_SEQUENCE_SCORE = [
    [50,   0,   0, 0],
    [50, 200, 100, 0],
    [100, 50, 200, 100],
    [50, 100, 50,  200],
    [250, 50, 100, 50]

]


if __name__ == '__main__':
    gems=[None,1,2,3]
    point=0
    for i in range(1, len(gems)):
        if i == 1:
            first = 0
        else:
            first = int(gems[i - 1])
        second = int(gems[i]) - 1
        print(first,"  ",second)
        print(GEM_SEQUENCE_SCORE[first][second])
        point += GEM_SEQUENCE_SCORE[first][second]