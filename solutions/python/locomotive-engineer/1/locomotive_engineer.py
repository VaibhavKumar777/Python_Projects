"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)
    


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    x,y,*last = each_wagons_id
    new_order = last + [x,y]
    loco_index = new_order.index(1)
    loco, *after_loco = new_order
    fixed_list = [loco, *missing_wagons, *after_loco]
    return fixed_list



def add_missing_stops(route,**kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops = []
    for value in kwargs.values():   # take all values from the keyword arguments
        stops.append(value)         # add them one by one into stops list
    route["stops"] = stops          # add stops list into the route dict
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    route.update(more_route_information)
    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    result = []
    for group in zip(*wagons_rows):
        result.append(list(group))
    return result
