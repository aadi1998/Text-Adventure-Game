class Location:
    def __init__(self, num, x, y, brief_desc, long_desc, action, items):
        """Creates a new location.

        Data that could be associated with each Location object:
        a position in the world map,
        a brief description,
        a long description,
        a list of available commands/directions to move,
        items that are available in the location,
        and whether or not the location has been visited before.
        Store these as you see fit.
        """

        self.position_num = num
        self.position = (x, y)
        self.brief_description = str(brief_desc)
        self.long_description = str(long_desc)
        self.action = action
        self.item = items
        self.is_visit = False

    def get_brief_description(self):
        """Return str brief description of location."""

        return str(self.brief_description)

    def get_full_description(self):
        """Return str long description of location."""

        return self.long_description

    def available_actions(self):
        """
        -- Suggested Method (You may remove/modify/rename this as you like) --
        Return list of the available actions in this location.
        The list of actions should depend on the items
        available in the location
        and the x,y position of this location on the world map."""

        return self.action


class Item:
    def __init__(self, name, start, target, target_points):
        """Create item referred to by string name, with integer "start"
        being the integer identifying the item's starting location,
        the integer "target" being the item's target location, and
        integer target_points which is the number of points player gets
        if item is deposited in target location.

        This is just a suggested starter class for Item.
        You may change these parameters and the data available for each
        Item class as you see fit.
        Consider every method in this Item class as a "suggested method":
        -- Suggested Method (You may remove/modify/rename these as you like) --

        The only thing you must NOT change is the name of this class: Item.
        All item objects in your game MUST be represented as an instance
        of this class.
        """

        self.name = name
        self.start = start
        self.target = target
        self.target_points = target_points

    def get_starting_location(self):
        """Return int location where item started."""

        return self.start

    def get_name(self):
        """Return the str name of the item."""

        return self.name

    def get_target_location(self):
        """Return item's int target location."""

        return self.target

    def get_target_points(self):
        """Return int points awarded for depositing the item in
        its target location."""

        return self.target_points


class World:
    def __init__(self, mapdata, locdata, itemdata):
        """
        Creates a new World object, with a map, and data about every
        location and item in this game world.

        You may add parameters/attributes/methods to this class as you see
        fit.
        BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES.

        :param mapdata: name of text file containing map data in grid format
        (integers represent each location, separated by space)
              map text file MUST be in this format.
              E.g.
              1 -1 3
              4 5 6
        Where each number represents a different location,
        and -1 represents an invalid, inaccessible space.
        param locdata: name of text file containing location data
        (format left up to you)
        param itemdata: name of text file containing item data
        (format left up to you)
        """

        # Storing variable for later use
        self.map = self.load_map(mapdata)
        self.location = {}
        self.item = {}
        self.store_location = []  # For class object
        self.store_item = []  # For class object
        self.store_points = {}
        self.load_locations(locdata)
        self.load_items(itemdata)

    def load_map(self, filename):
        """
        THIS FUNCTION MUST NOT BE RENAMED OR REMOVED.
        Store map from filename (map.txt) in the variable "self.map"
        as a nested list of integers like so:
            1 2 5
            3 -1 4
        becomes [[1, 2, 5], [3, -1, 4]]
        RETURN THIS NEW NESTED LIST.
        param filename: string that gives name of text file in which map data
        is located
        return: return nested list of integers representing map of
        game world as specified above
        """
        # Opening files and storing them into map_info
        map_data = open(filename, 'r')
        map_info = map_data.readlines()
        map_data.close()
        nested_data = []  # Initializing a list

        for data in map_info:
            data = data.rstrip('\n')  # removing ('\n') at the end of the line

            # making data equal to list of numbers
            # separated by a  space in a line
            data = data.split(' ')

            # adding data to nested_data, which makes a
            # nested list ( a list of lists)
            nested_data += [data]

        return nested_data

    def load_locations(self, filename):
        """
        Store all locations from filename (locations.txt) into the variable
        "self.locations"
        Remember to keep track of the integer number representing each
        location
        Make sure the Location class is used to represent each location.
        Change this docstring as needed.
        param filename:
        """

        # Setting up variables and opening location file
        location = open(filename, 'r')
        read_location = location.readlines()
        location.close()
        list_of_location = []
        location_number = []
        list_of_description = []
        list_of_item = {}
        x = 0
        y = 0
        list_of_action = []

        # for every lines in location file
        for sub_location in read_location:

            # Strip new line
            sub_location = sub_location.rstrip('\n')

            # if the lines have LOCATION in it
            if 'LOCATION' in sub_location:

                # add it into a list
                list_of_location += [sub_location]

                # split it by a space
                sub_location = sub_location.split(' ')

                location_number = int(sub_location[1])

                # for every item in self.item
                for item in self.item:

                    # if the item's starting position is same as location
                    # number
                    if int(self.item[item][0]) == location_number:

                        # if the location number is in list of item
                        if location_number in list_of_item:
                            list_of_item[location_number] += [item]

                        # if location not in list of item
                        elif location not in list_of_item:
                            list_of_item[location_number] = [item]

                # while the output from get_location does not eqaul to
                # location number
                while self.map[y][x] != str(location_number):
                    if x < len(self.map[y]):
                        x += 1

                    if x == len(self.map[y]):
                        x = 0
                        y += 1

                    if self.map[y][x] == str(location_number):
                        x = x
                        y = y

            # If sub_location = END
            elif sub_location == 'END':

                """
                The part below creates custom action
                """
                if str(location_number) == str(1):

                    list_of_action = ['Pick pencil', 'Pick Tcard']

                elif str(location_number) == str(2):

                    list_of_action = ['Pick Calculator']

                elif str(location_number) == str(3):

                    list_of_action = ['Check time', 'Play games',
                                      'Pick up Phone', 'Pick phone',
                                      'pick pen']

                elif str(location_number) == str(4):

                    list_of_action = ['Examine Exam info']

                elif str(location_number) == str(5):

                    list_of_action = ['Play on phone', 'Study']

                elif str(location_number) == str(6):

                    list_of_action = ['Pick up food',
                                      'pull out your phone to check time']

                elif str(location_number) == str(7):

                    list_of_action = ['Surf the web on laptop',
                                      'Listen to music', 'Play games',
                                      'Pick up Laptop', 'Pick up Eraser']

                elif str(location_number) == str(8):

                    list_of_action = ['Look at the wall of poster']

                """
                This part below creates the location objects
                """

                self.location[location_number] = list_of_description

                brief_description = ''.join(self.location[location_number][1])

                long_description = ''.join(self.location[location_number][2:])

                store_location = Location(location_number, x, y,
                                          brief_description, long_description,
                                          list_of_action, list_of_item)

                self.store_location.append([store_location])

                list_of_description = []

                x = 0

                y = 0

            # if the sub_location is a number
            elif sub_location.isdigit():

                # store it as points
                self.store_points[location_number] = [sub_location]

            # if the sub_location is '', do nothing
            elif sub_location is '':
                pass

            # add description into a list
            else:
                list_of_description += [sub_location]

    def load_items(self, filename):
        """
        Store all items from filename (items.txt) into ...
        whatever you think is best.
        Make sure the Item class is used to represent each item.
        Change this docstring accordingly.
        param filename:
        """

        open_items = open(filename, 'r')

        store_items = open_items.readlines()

        open_items.close()

        for attribute in store_items:  # For every line in store_items
            """
            As an example for item data, we might store items in "items.txt"
            using a one line per item format, such as:
            1 10 5 Cheat Sheet
            Where it is found, where to deposit, points received, item 
            """
            # x is a list of every /number in one line (split at space)
            x = attribute.split(' ')
            numbers = x[:3]  # The first 3 indexes of x are numbers
            # The rest of the indexes are part of the name of item,
            # so they are joined
            name_of_item = " ".join(x[3:])

            # Making an Item object
            new_item = Item(name_of_item,
                            numbers[0], numbers[1], numbers[2])

            # Getting item name from Item object
            item_name = new_item.get_name()
            item_name = item_name.rstrip('\n')  # Deleting '\n' from item name

            # getting initial location from object
            item_initial = new_item.get_starting_location()

            # getting target location from object
            item_target = new_item.get_target_location()

            # getting point reward from object
            item_points = new_item.get_target_points()

            self.item[item_name] = [item_initial] + [item_target] + \
                                   [item_points]

    def get_location(self, x, y):
        """Check if location exists at location (x,y) in world map.
        Return Location object associated with this location if it does.
        Else, return None.
        Remember, locations represented by the number -1 on the map
        should return None.
        :param x: integer x representing x-coordinate of world map
        :param y: integer y representing y-coordinate of world map
        :return: Return Location object associated with this location
        if it does. Else, return None.
        """

        game_map = self.map
        # checking if y is in the length of the nested list
        # (the vertical component)
        if len(game_map) > y and y >= 0:
            # checking if x is in the length of the list inside the nested
            # list at index y (the horizontal component)
            if len(game_map[y]) > x and x >= 0:
                # y comes before y because y is the nested_list component,
                # however it is still the vertical component
                # checking if the value at (x,y) is -1
                if game_map[y][x] == '-1':
                    return None
                else:
                    # if (x,y) location is in nested list and is not -1,
                    # it returns the location at game_map[y][x]
                    #  Returns none otherwise
                    return game_map[y][x]
