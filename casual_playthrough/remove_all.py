for i in range(get_world_size()):
	move(North)
	for v in range(get_world_size()):
		move(East)
		if can_harvest():
			harvest()