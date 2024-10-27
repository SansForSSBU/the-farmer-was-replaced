buy_water = False
e = Entities.Pumpkin
b = None
g = None
w = None
prot = None
if e == Entities.Grass:
	g = Grounds.Turf
	prot = False
	
if e == Entities.Bush:
	g = Grounds.Turf
	prot = False
	
if e == Entities.Tree:
	g = Grounds.Soil
	w = 0.75
	prot = False
	
if e == Entities.Carrots:
	g = Grounds.Soil
	b = Items.Carrot_Seed
	prot = False

if e == Entities.Pumpkin:
	g = Grounds.Soil
	b = Items.Pumpkin_Seed
	prot = True

n = 0
while True:
	size = get_world_size()
	for i in range(size):
		move(East)
		for v in range(size):
			move(North)
			if can_harvest() and (not prot or e != get_entity_type()):
				harvest()
			elif e == Entities.Pumpkin:
				if get_entity_type() == Entities.Pumpkin and can_harvest():
					n += 1
				else:
					n = 0
				if n == size*size:
					harvest()
			if (get_entity_type() == None or get_entity_type() == Entities.Grass) and get_entity_type() != e:
				if get_ground_type() != g:
					till()
				if b != None:
					trade(b)
				if e != Entities.Grass:
					plant(e)
			while w != None and get_water() < w:
				if buy_water:
					trade(Items.Empty_Tank)
				use_item(Items.Water_Tank)