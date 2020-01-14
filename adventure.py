from game_data import World, Item, Location
from player import Player


if __name__ == "__main__":

    """
    Creates local variables for future calling
    """
    WORLD = World("map.txt", "locations.txt", "items.txt")

    PLAYER = Player(0, 0)

    total_turns = 50

    turns_counter = 0

    menu = ["look", "inventory", "score", "quit", "back"]

    list_of_location_history = []

    load_map = WORLD.map

    item_list = WORLD.item

    score = 0

    victory_items = []

    while not PLAYER.victory:

        location = WORLD.get_location(PLAYER.x, PLAYER.y)

        """
        for each object stored in gamedata, find it position and if player
        have already visited. if the location number of the object matches
        the current, prints out description of location
        """
        for search_object in WORLD.store_location:

            visit_or_not = getattr(search_object[0], 'is_visit')

            get_location = getattr(search_object[0], 'position_num')

            if str(get_location) == location:

                if visit_or_not is False:

                    setattr(search_object[0], 'is_visit', True)

                    score += int(WORLD.store_points[int(get_location)][0])

                    print('\n'.join(WORLD.location[int(location)][1:]) +
                          '\n' + 'END\n')

                    list_of_location_history += location

                if visit_or_not is True and 'GO' in choice:
                    print(''.join(WORLD.location[int(location)][0]) + '\n' + 'END\n')

        # if length of list of location is greater than , delete the first
        # element in list
        if len(list_of_location_history) > 2:
            list_of_location_history.pop(0)

        print("What to do? \n")
        print("[menu]")

        for objects in WORLD.store_location:
            read_location = getattr(objects[0], 'position_num')

            get_action = getattr(objects[0], 'action')

            if str(read_location) == location:

                for action in get_action:

                    print(action)

        """
        For each choice player chooses, there will be a certain output
        """

        choice = input("\nEnter action: ")

        choice = str(choice).upper()

        if choice == "[menu]".upper():
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")

        # if choice is look, print out full description
        elif choice == 'LOOK':
            print('\n'.join(WORLD.location[int(location)][2:]) + '\n' +
                  'END\n')

        # if choice is inventory, print out the full description
        elif choice == 'INVENTORY':

            # for every entry in dictionary, prints out the entry
            keys_of_inventory = list(PLAYER.get_inventory().keys())
            print(keys_of_inventory)

        # if choice is score, prints score
        elif choice == 'SCORE':

            print(score)

        # if choice is back
        elif choice == 'BACK':

            """
            For loop used to find the object class corresponding with the
            x, y coordinate. The x, y coordinate then is usd to find the
            location number associated with it. If the location number is
            equal to the first element in the list of location, then
            update the new x and y value of the payer
            """
            for sub_object in WORLD.store_location:

                get_object_location = getattr(sub_object[0], 'position')

                current_location = WORLD.get_location(get_object_location[0],
                                                      get_object_location[1])

                if current_location == list_of_location_history[0]:

                    PLAYER.x = get_object_location[0]

                    PLAYER.y = get_object_location[1]

            turns_counter += 1

            print(''.join(WORLD.location[int(location)][0]) +
                  '\n' + 'END\n')

        # if choice is pick
        elif choice[:4] == 'PICK':
            """
            If item exists, add it into inventory and deleted from item
            dictionary. If item does not exist, prints items does not exist
            """
            if choice[5:] not in item_list:
                print("That item does not exist.")

            else:
                if item_list[choice[5:]][0] == location:
                    print(choice[5:], " was picked up")
                    PLAYER.add_item(choice[5:], item_list[choice[5:]])

                    # PUZZLE

                    if choice[5:] == "FOOD":
                        print("There is food scattered around this cafeteria, "
                              "you see a 'bag of chips', 'grapes', \
                                            '\nhalf eaten container of pasta. "
                              "Your stomach is rumbling and if you do not eat soon, \
                                             \nyou might faint.")
                        eat = input("\nWhat would you like to eat?\n"
                                    "Pick a letter option:\nA: bag of chips \
                                             \nB: grapes"
                                    "\nC: half eaten container of pasta")

                        if eat.upper() == 'A':
                            print("The bag of chips game you a headache "
                                  "because you were slightly illergic to one of \
                                                \nof the ingredients. You got"
                                  " dizzy and passed out.")
                            print('Game over')
                            break
                        elif eat.upper() == 'B':
                            print("The grapes were out for so long that the "
                                  "got expired, when you ate them you got \
                                                you got really sick and had "
                                  "to be rushed to the hospital")
                            print('Game Over')
                            break
                        elif eat.upper() == 'C':
                            print(
                                "Surprisingly, the pasta was really good, "
                                "and filling. Your energy is replenished.")
                            continue
                        else:
                            print("Seems like you do not want to eat these")

                    del(item_list[choice[5:]])
                else:
                    print(choice[5:], "is not here")

        # if choice is drop
        elif choice[:4] == 'DROP':

            """
            drop the item if player is in the right location,
            or else cannot drop it
            """

            players_items = PLAYER.get_inventory()

            if choice[5:] not in PLAYER.get_inventory():
                print("You do not have that item")

            elif players_items[choice[5:]][1] != location:
                print('This is not the correct place')

            else:
                print(choice[5:], " was dropped")
                if players_items[choice[5:]][1] == location:
                    score += int(players_items[choice[5:]][2])

                    # If the target location for item is 8
                    if players_items[choice[5:]][1] == '8':

                        # Add to list
                        victory_items += [choice[5:]]

                        # If the length of the list is 5
                        if len(victory_items) == 5:

                            # Player victory is true
                            PLAYER.victory = True

                            # Break the loop
                            break

                item_list[choice[5:]] = players_items[choice[5:]]
                PLAYER.remove_item(choice[5:])

        if 'GO' in choice:

            if 'NORTH' in choice:  # TO GO NORTH
                if WORLD.get_location(PLAYER.x, PLAYER.y-1) is not None:
                    PLAYER.move_north()
                    turns_counter += 1
                else:
                    print("cannot go that way")

            elif 'SOUTH' in choice:  # TO GO SOUTH
                if WORLD.get_location(PLAYER.x, PLAYER.y+1) is not None:
                    PLAYER.move_south()
                    turns_counter += 1
                else:
                    print("cannot go that way")

            elif 'EAST' in choice:  # TO GO EAST
                if WORLD.get_location(PLAYER.x+1, PLAYER.y) is not None:
                    PLAYER.move_east()
                    turns_counter += 1
                else:
                    print("cannot go that way")

            elif 'WEST' in choice:  # TO GO WEST

                if WORLD.get_location(PLAYER.x-1, PLAYER.y) is not None:
                    PLAYER.move_west()
                    turns_counter += 1
                else:
                    print("cannot go that way")

        # Turn counter
        # if turn is under the total turn
        if turns_counter != total_turns:
            print('Turns left: ' + str(total_turns - turns_counter))

        elif turns_counter == total_turns:

            print('Game Over')

            break

        # if choice is quit, break the loop
        if choice == 'QUIT':

            break
