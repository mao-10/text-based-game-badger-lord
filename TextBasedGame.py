# function showing the goal of the game and move commands
def intro_instructions():
   #print a main menu and the commands
   print("Badger Lord Adventure Game")
   print("The Evil Badge Lord has kidnapped your six friends.")
   print("Save them all and then confront the Badger Lord.")
   print("To win, you must rescue all six friends. Without their powers you'll lose to the destructive power of the Badger.")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: rescue")

# function that gives command instructions after each move
def move_instructions():
    print("\n Move commands: go South, go North, go East, go West")
    print("\n Add to Inventory: rescue")

# function to display user status
def display_status(rooms, current_room, inventory):
    # display current location and directions
    print('\n You are in the {}'.format(current_room))
    print("\n Inventory:", inventory)
    print('\n In this room you see {}'.format(rooms[current_room]['item']))

def main():
    # A dictionary for badger lord rooms
    # and linking one item for each room except the Start room (Great Hall) and the room containing the villain
    rooms = {
        'The Great Hall of Doom': {'South': 'The Great Kitchen', 'North': 'The Observatory', 'item': 'no friends'},
        'The Observatory': {'South': 'The Great Hall of Doom', 'item': 'Hoot The Wise Owl'},
        'The Great Kitchen': {'North': 'The Great Hall of Doom', 'West': 'The Great Cellar', 'item': 'Greg The Angry Alligator'},
        'The Great Cellar': {'East': 'The Great Kitchen', 'North': 'The Great Room of Death Beds', 'item': 'Omni The Dark Cat'},
        'The Great Room of Death Beds': {'South': 'The Great Cellar', 'North': 'The Great Bathroom', 'West': 'The Great Corridor', 'item': 'Ploppy The Lazy Dog'},
        'The Great Bathroom': {'South': 'The Great Room of Death Beds', 'item': 'Sansa The Great Beaver'},
        'The Great Corridor': {'East': 'The Great Room of Death Beds', 'North': 'Great Chamber', 'item': 'Slinky The Slithery Snake'},
        'Great Chamber': {'South': 'The Great Corridor', 'item': 'Badger Lord'}  # villain
    }

    # starts player in starting room
    current_room = 'The Great Hall of Doom'
    inventory = []
    intro_instructions()
    # while not in the final room get user moves
    while current_room != "Great Chamber":
        display_status(rooms, current_room, inventory)
        move_instructions()
        user_move = input('\n Enter your move: ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # if user move is rescue, get input for item name and append to inventory
        if user_move == "rescue":
            item = input("\n Enter your friend's name:").title()
            if item in rooms[current_room]['item']:
                inventory.append(item)
                print("\n You rescued {}".format(item))
                rooms[current_room]['item'] = 'no friends'
            else:
                print('\n There is no {} here'.format(item))
        # else if user move is a directional command, update the current room
        elif user_move.split()[-1].capitalize() in rooms[current_room]:
            current_room = rooms[current_room][user_move.split()[-1].capitalize()]
        else:
            # not valid move
            print("\n You can't do that...")
            print("\n Please give another command...")
    # if user enters final room without all items
    if len(inventory) != 6:
        print("\n You were eaten by the Badger Lord...")
        print("\n I hope someday the Badger Lord may be defeated...")
        print("\n Thanks for playing!!")
    else:
        print("\n Congratulations! You have defeated the Badge Lord and freed all of your friends!")
        print("\n Thanks for Playing!! I hope you enjoyed!")

main()
