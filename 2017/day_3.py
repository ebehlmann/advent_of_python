input = 312051

def create_coordinates(end_point):

	coordinates = {}
	coordinates[1] = [0, 0]

	i = 2
	x = 0
	y = 0
	direction_to_move = 'right'
	amount_to_move = 1
	amount_moved = 0

	while(i <= end_point):
		if(direction_to_move == 'right'):
			x += 1
			amount_moved += 1
			if(amount_to_move == amount_moved):
				direction_to_move = 'up'
				amount_moved = 0
		elif(direction_to_move == 'up'):
			y += 1
			amount_moved += 1
			if(amount_to_move == amount_moved):
				direction_to_move = 'left'
				amount_moved = 0
				amount_to_move += 1
		elif(direction_to_move == 'left'):
			x -= 1
			amount_moved += 1
			if(amount_to_move == amount_moved):
				direction_to_move = 'down'
				amount_moved = 0
		elif(direction_to_move == 'down'):
			y -= 1
			amount_moved += 1
			if(amount_to_move == amount_moved):
				direction_to_move = 'right'
				amount_moved = 0
				amount_to_move += 1

		coordinates[i] = [x, y]
		i += 1

	return coordinates

def find_coordinate_distance(coord1, coord2):
	x_diff = abs(coord1[0]) + abs(coord2[0])
	y_diff = abs(coord1[1]) + abs(coord2[1])
	return x_diff + y_diff


coordinates = create_coordinates(input)

print(find_coordinate_distance(coordinates[1], coordinates[input]))