from django import template
from ..services.api import plural_word

register = template.Library()


@register.filter()
def make_stars(count_stars):
    return '★' * int(count_stars)


@register.filter()
def plural_ru(count, word):
    return plural_word(word, int(count))
