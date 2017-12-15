"""File for mature code to be imported into a notebook.

Authors: Solomon and Josiah"""


class Location:
    def __init__(self, description, name, ):
        """There's a chicken and egg problem with the Location and Direction both knowing about each other.
        The solution is that the Location pre-exists the Direction.  Multiple directions can then tie
        into, and leave from an already existing Location.  see: add_exit_action.

        For now, Locations only need to know about their exits, since Directions know about where
        they are entering."""
        self.description = description
        self.name = name
        self.exits = {}

    def add_exit_action(self, my_exit):
        self.exits[my_exit.action] = my_exit


game_map = {'start': Location('You are in a grass field with a shed and a castle', 'start')}


class Direction:
    def __init__(self, action: str, destination: Location):
        self.action = action
        self.destination = destination


def add_location(room_that_youre_leaving: Location, action_taken: str,
                 room_entering: str, description: str, how_to_get_back: str):
    """Solves the chicken and Egg problem of creating Locations and Directions
    that know about each other.  Use this to expand the game_map."""
    old_loc = room_that_youre_leaving
    new_loc = Location(description, room_entering)
    action_just_taken = Direction(action_taken, new_loc)
    old_loc.add_exit_action(action_just_taken)
    return_route = Direction(how_to_get_back, old_loc)
    new_loc.add_exit_action(return_route)
    game_map[room_entering] = new_loc
