from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

#Print an ASCII map
world.print_rooms()
player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited = set()
move_back = {'n': 's', 
             's': 'n', 
             'w': 'e', 
             'e':'w'}

def traverse(room, visited=None):
    path = []
    room = player.current_room
    if visited is None:                              #store visited nodes/rooms
        visited = set()
    for sequence in room.get_exits():                #current room to see possible exit
        player.travel(sequence)
        room = player.current_room
        if room in visited:                          #room visited, backtrack
            player.travel(move_back[sequence])
        else:                                        #not visited before, add room visited 
            visited.add(room)
            path.append(sequence)
            path = path + traverse(room, visited)    #append and path
            player.travel(move_back[sequence])
            path.append(move_back[sequence])

    return path
    print(path)

def graph(visited, move_back, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in move_back[node]:
            graph(visited, move_back, neighbour)

# Driver Code
graph(visited, move_back, 'n')
traversal_path = traverse(player.current_room)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")