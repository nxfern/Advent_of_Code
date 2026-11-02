import copy

def getHash(elevator: int, floors: list[list[int]]) -> str:
	return str(elevator) + str([(len(floors[i]), sum(x < 0 for x in floors[i])) for i in range(4)])

def move(elevator: int, floors: list[list[int]], direction: int, from_index: int | None, to_index: int | None) -> None:
	if from_index != None and to_index != None:
		floors[elevator + direction].insert(to_index, floors[elevator].pop(from_index))

def exploreState(req: int, elevator: int, floors: list[list[int]], direction: int, moves: int, index1: int, index2: int | None = None) -> None:
	if direction * elevator < req:
		move(elevator, floors, direction, index2, 0)
		move(elevator, floors, direction, index1, 0)

		next_hash = getHash(elevator + direction, floors)

		if next_hash not in states and floors[elevator + direction] and isValidState(floors[elevator + direction]) and isValidState(floors[elevator]):
			queue.append([elevator + direction, copy.deepcopy(floors), moves + 1, next_hash])

		move(elevator + direction, floors, -direction, 0, index1)
		move(elevator + direction, floors, -direction, 0, index2)

def isValidState(floor: list[int]) -> bool:
	hasGen   = sum(x < 0 for x in floor)
	unpaired = sum(x > 0 and -x not in floor for x in floor)

	return not (hasGen and unpaired)

# Part 1
start    = [[-1, -2, 2, -3, -4, 4, -5, 5], [1, 3], [], []]
end_hash = getHash(3, [[], [], [], sum(start, [])])
states   = set()
queue    = []

queue.append([0, start, 0, getHash(0, start)])

while True:
	elevator, floors, moves, cur_hash = queue.pop(0)

	if cur_hash not in states:
		states.add(cur_hash)

		if cur_hash == end_hash:
			print(f"Part 1: {moves}")
			break

		for index1 in range(len(floors[elevator])):
			for index2 in range(index1 + 1, len(floors[elevator])):
				exploreState(3, elevator, floors, 1, moves, index1, index2)
				exploreState(0, elevator, floors, -1, moves, index1, index2)

			exploreState(3, elevator, floors, 1, moves, index1)
			exploreState(0, elevator, floors, -1, moves, index1)

# Part 2
start    = [[-1, -2, 2, -3, -4, 4, -5, 5, -6, 6, -7, 7], [1, 3], [], []]
end_hash = getHash(3, [[], [], [], sum(start, [])])
states   = set()
queue    = list()

queue.append([0, start, 0, getHash(0, start)])

while True:
	elevator, floors, moves, cur_hash = queue.pop(0)

	if cur_hash not in states:
		states.add(cur_hash)

		if cur_hash == end_hash:
			print(f"Part 2: {moves}")
			break

		for index1 in range(len(floors[elevator])):
			for index2 in range(index1 + 1, len(floors[elevator])):
				exploreState(3, elevator, floors, 1, moves, index1, index2)
				exploreState(0, elevator, floors, -1, moves, index1, index2)

			exploreState(3, elevator, floors, 1, moves, index1)
			exploreState(0, elevator, floors, -1, moves, index1)