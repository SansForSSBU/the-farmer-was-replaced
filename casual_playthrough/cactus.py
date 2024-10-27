# THIS IS VERY SUBOPTIMAL. DOES NOT SORT IN Y DIRECTION, AND IS NOT APPROPRIATE FOR DINOSAURS
e = Entities.Dinosaur
g = None
if e == Entities.Dinosaur:
	g = Grounds.Soil
elif e == Entities.Cactus:
	g = Grounds.Soil
def moveto(coords):
	x = coords[0]
	y = coords[1]
	while (get_pos_x() != x):
		if get_pos_x() < x:
			move(East)
		else:
			move(West)
	while (get_pos_y() != y):
		if get_pos_y() < y:
			move(North)
		else:
			move(South)
def plant_cac():
	if get_entity_type() == e:
		return 1
	if can_harvest():
		harvest()
	if (e == Entities.Cactus):
		trade(Items.Cactus_Seed)
	elif (e == Entities.Dinosaur):
		trade(Items.Egg)
	if g != get_ground_type():
		till()
	if e != Entities.Dinosaur:
		plant(e)
	else:
		use_item(Items.Egg)
def line_of_cac():
	moveto((0, get_pos_y()))
	steps = 1
	for i in range(get_world_size()):
		plant_cac()
		while measure(West) != None and measure(West) > measure():
			swap(West)
			move(West)
			steps += 1
		for i in range(steps):
			move(East)
		steps = 1
def harvest_all_tiles():
	for x in range(get_world_size()):
		move(East)
		for y in range(get_world_size()):
			move(North)
			if can_harvest():
				harvest()
while True:
	moveto((0, 0))
	for idx in range(get_world_size()):
		line_of_cac()
		move(North)
	harvest_all_tiles()