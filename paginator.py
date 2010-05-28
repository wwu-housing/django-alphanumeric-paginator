from .page import Page
from django.core.paginator import InvalidPage

_ALPHANUMERICS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Paginator(object):
    """
    Provides pagination and filtering alphanumerically, rather than by page
    numbers.
    """
    def __init__(self, object_list, pagination_field=None):
        self.chunks = {}

        def first_char(obj):
            if pagination_field:
                return str(getattr(obj, pagination_field))[:1].upper()
            else:
                return str(obj)[:1].upper()

        for c in _ALPHANUMERICS:
            self.chunks[c] = filter(lambda obj: c == first_char(obj),
                                    object_list)

    def page(self, character):
        character = character.upper()
        if character not in _ALPHANUMERICS:
            raise InvalidPage("'%s' is not in '%s'" % (character,
                                                       _ALPHANUMERICS))
        else:
            return Page(self.chunks[character], character, self)

    @property
    def page_range(self):
        return [self.page(c) for c in _ALPHANUMERICS]

    @property
    def num_pages(self):
        return len([l for l in self.chunks.values() if len(l) > 0])
