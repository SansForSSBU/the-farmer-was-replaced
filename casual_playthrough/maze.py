directions = [North, East, South, West]
coords_found = []
def get_coords():
	return (get_pos_x(), get_pos_y())

def inverse_dir(dir):
	if dir == North:
		return South
	if dir == South:
		return North
	if dir == East:
		return West
	if dir == West:
		return East
		
def get_move_coords(coords, dir):
	if dir == North:
		return (coords[0], coords[1]+1)
	elif dir == South:
		return (coords[0], coords[1]-1)
	elif dir == East:
		return (coords[0]+1, coords[1])
	elif dir == West:
		return (coords[0]-1, coords[1])
def solve_maze():
	for dir in directions:
		if not get_move_coords(get_coords(), dir) in coords_found and move(dir):
			if not get_coords() in coords_found:
				coords_found.append(get_coords())
				if get_entity_type() == Entities.Treasure:
					harvest()
					return 1
				if solve_maze() == 1:
					return 1
			move(inverse_dir(dir))
		
def make_maze():
	plant(Entities.Bush)
	while get_entity_type() == Entities.Bush:
		trade(Items.Fertilizer)
		use_item(Items.Fertilizer)

while True:
	coords_found = []
	make_maze()
	solve_maze()