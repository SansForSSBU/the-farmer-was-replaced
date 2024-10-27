route = [Unlocks.Speed, Unlocks.Expand, Unlocks.Plant]
route_ptr = 0

world_sizes = [
[1, 1],
[1, 3],
]
world_ptr = 0
requirements = {
Entities.Grass: {
	"Ground": Grounds.Turf,
	"Seed": None,
	"Plant": None,
}
}
def replant(thing):
	reqs = requirements[thing]
	if get_ground_type() != reqs["Ground"]:
		till()
	if reqs["Seed"] and num_items(reqs["Seed"]) == 0:
		trade(reqs["Seed"])
	if reqs["Plant"] != None:
		plant(reqs["Plant"])

def simple_farm(thing):
	for y in range(world_size[1]):
		if (world_size[1] > 1):
			move(North)
		for x in range(world_size[0]):
			if (world_size[0]) > 1:
				move(East)
			if can_harvest():
				harvest()
				replant(thing)
			
				
			

world_size = world_sizes[world_ptr]
timed_reset()
while route_ptr < len(route):	
	simple_farm(Entities.Grass)
	objective = route[route_ptr]
	if unlock(objective):
		route_ptr += 1
		if objective == Unlocks.Expand:
			world_ptr += 1
			world_size = world_sizes[world_ptr]

timed_reset()
	