"""This module keeps api for tour application"""

__author__ = 'Artikov A.K'

from typing import List, Dict

import data
from .tour_services import TOUR_CONTROLLER, DEPARTURE_CONTROLLER, AttrMinMax


def is_departure_exists(departure: str) -> bool:
    """
    The function checks that departure exists in data
    :param departure: departure id
    :return: True if exists, else False
    """
    return bool(get_departures_data({'id': departure}))


def is_tour_exists(tour_id: int) -> bool:
    """
    The function checks that departure exists in data
    :param tour_id: tour id
    :return: True if exists, else False
    """
    return bool(get_tours_data({'id': tour_id}))


def get_min_max_attr_for_tours(tours: List['Tour'], *min_max_attributes: str) -> Dict[str, AttrMinMax]:
    """
    The function returns min and max attributes value for tours.
    :param tours: list of tours
    :param min_max_attributes: name of attributes
    :return:
    """
    result_min_max_attributes = TOUR_CONTROLLER.get_min_max_attr_for_data(tours, *min_max_attributes)
    return result_min_max_attributes


def get_main_data() -> dict:
    """
    The function returns data for filling main page
    :return:
    """
    title_data = dict(
        title=data.title,
        subtitle=data.subtitle,
        description=data.description
    )
    return title_data


def get_departures_data(departures_filter: list = None) -> List['Departure']:
    """
    The function returns departures.
    :param departures_filter: filter for select departure
    :return:
    """
    return DEPARTURE_CONTROLLER.get(departures_filter)


def get_tours_data(tours_filter: dict = None) -> List['Tour']:
    """
    The function returns tours.
    :param tours_filter: filter for select tour
    :return: tour list
    """
    return TOUR_CONTROLLER.get(tours_filter)


def plural_word(word: str, count: int) -> str:
    """
    This function return plural form for sended word.
    :param word: word for modification
    :param count: count
    :return:
    """
    words = {
        'тур': ['тур', 'тура', 'туров']
    }

    if word not in words:
        raise Warning(f"For word {word} the plural form doesn't setup")

    if count % 10 == 1 and count % 100 != 11:
        return words[word][0]
    elif 2 <= count % 10 <= 4 and (count % 100 < 10 or count % 100 >= 20):
        return words[word][1]
    else:
        return words[word][2]
