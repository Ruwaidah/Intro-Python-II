from room import Room
from player import Player
from item import Item

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


rock = Item("rock", "this is a small rock")
sword = Item("sword", "this is an old sword")
coin = Item("coin", "this is a coin")
key = Item("key", "this is a silver key")


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Items in rooms
room['foyer'].items = [rock, sword, coin, key]


player = Player(input("Please enter your name: "), room['outside'])
print(player.current_room)


valid_directions = ("n", "s", "e", "w")

while True:
    cmd = input("\n inter a direction >> ")
    if cmd == "q":
        print("Goodbye!")
        exit(0)
    elif cmd in valid_directions:
        player.travel(cmd)
        print(player.current_room)
    else:
        print("I did not understand that command")
