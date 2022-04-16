from django import template
from ..services.api import plural_word

register = template.Library()


@register.filter()
def repeat_symbol(count_symbols, symbol):
    return symbol * (int(count_symbols))


@register.filter()
def plural_ru(count, word):
    return plural_word(word, int(count))
