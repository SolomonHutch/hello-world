"""File for mature code to be imported into a notebook.

Authors: Solomon and Josiah"""


class Location:
    def __init__(self, description):
        """There's a chicken and egg problem with the Location and Direction both knowing about each other.
        The solution is that the Location pre-exists the Direction.  Multiple directions can then tie
        into, and leave from an already existing Location.  see: add_exit_action.

        For now, Locations only need to know about their exits, since Directions know about where
        they are entering."""
        self.description = description
        self.exits = {}

    def add_exit_action(self, my_exit):
        self.exits[my_exit.action.lower()] = my_exit

    def __repr__(self):
        exit_str = "; ".join([str(x) for x in self.exits.values()])
        return f'<Location "{self.description[:40]}" exits:{exit_str}>'

    def __hash__(self):
        return self.description.__hash__()

    def __eq__(self, other):
        if isinstance(other, Location):
            return self.__hash__() == other.__hash__()
        else:
            return self == other


start_location = Location('You are in a grass field with a shed and a castle')
game_map = {start_location.description: start_location}


class Direction:
    def __init__(self, action: str, destination: Location):
        self.action = action
        self.destination = destination

    def __repr__(self):
        return f'<"{self.action}" -> "{self.destination.description[:15]}...">'


def add_location(room_that_youre_leaving: Location,
                 action_taken: str,
                 description: str,
                 how_to_get_back: str,
                 save=False):
    """Solves the chicken and Egg problem of creating Locations and Directions
    that know about each other.  Use this to expand the game_map."""
    if isinstance(room_that_youre_leaving, str):  # look up based on description
        try:
            room_that_youre_leaving = game_map[room_that_youre_leaving]
        except KeyError:
            print(f"I couldn't find {room_that_youre_leaving} on the map")
    save_string = f"add_location({room_that_youre_leaving.description!r}, {action_taken!r}, {description!r}, {how_to_get_back!r})\n"
    old_loc = room_that_youre_leaving
    new_loc = Location(description)
    action_just_taken = Direction(action_taken, new_loc)
    old_loc.add_exit_action(action_just_taken)
    return_route = Direction(how_to_get_back, old_loc)
    new_loc.add_exit_action(return_route)
    game_map[new_loc.description] = new_loc  # description is also used as the hash key in the dict
    if save:
        with open('level_save.py', 'a') as save_file:
            save_file.write(save_string)

    return new_loc


def add_connection(location_A: Location,
                   action_A: str,
                   location_B: Location,
                   action_B: str):
    dir_A = Direction(action_A, location_A)
    location_B.add_exit_action(dir_A)
    dir_B = Direction(action_B, location_B)
    location_A.add_exit_action(dir_B)
    return (dir_A, dir_B)