import Pizza from Pizza

class Sparcity:
    def __init__(self, pizza):
        map = pizza.ingredient_map()
        for i in range(len(map)):
            for j in range(len(map[i])):
                position = (i,j)
                # check 8 different directions
                check(map, position, -1,  0)
                check(map, position, -1,  1)
                check(map, position,  0,  1)
                check(map, position,  1,  1)
                check(map, position,  1,  0)
                check(map, position,  1, -1)
                check(map, position,  0, -1)
                check(map, position, -1, -1)
