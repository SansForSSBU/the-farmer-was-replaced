suns = []
best = 0
w = 0.75
while True:
	planted = 0
	size = get_world_size()
	# Plant
	for i in range(size):
		move(East)
		for v in range(size):
			move(North)
			if can_harvest():
				harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			trade(Items.Sunflower_Seed)
			plant(Entities.Sunflower)
			planted += 1
			while get_water() < w:
				use_item(Items.Water_Tank)
			best = max(best, measure())
	for i in range(0):
		do_a_flip()
	move(East)
	while planted > 0:
		for i in range(size):
			move(East)
			for v in range(size):
				move(North)
				if can_harvest() and measure() == best:
					harvest()
					planted -= 1
		best = best - 1
		