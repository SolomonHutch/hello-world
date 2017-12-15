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
        self.ways_out = {}

    def add_exit_action(self, leaving_direction: Direction):
        self.ways_out[leaving_direction.leaving_action] = leaving_direction


class Direction:
    def __init__(self, entering_action: str, entering_location: Location):
        self.entering_action = entering_action
        self.entering_location = entering_location
        self.leaving_action = None
        self.leaving_location = None