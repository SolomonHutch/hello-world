from storyteller_base import add_connection, add_location, start_location

pond = add_location(start_location, 'jump in the pond', "The pond is very wet.", 'swim to shore')
river = add_location(start_location, 'go swimming', 'The river is nice', 'leave river')
add_connection(river, 'swim upstream', pond, 'go to the river')
barn = add_location(river, 'swim downriver', 'You reach an old barn', 'go swimming')
# current_location = game_map["The pond is very wet."]
add_location('You are in a grass field with a shed and a castle', 'walk to the castle', 'The castle is huge.', 'walk to the field')
