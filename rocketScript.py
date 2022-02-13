from rocket import RocketBoard, Rocket

board1 = RocketBoard(2)

board1[0].x = 24

print(board1[0].get_distance(board1[1]))

print(len(board1))
