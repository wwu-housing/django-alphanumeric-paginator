class Page(object):
    def __init__(self, object_list, character, paginator):
        self.object_list = object_list
        self.character = character
        self.paginator = paginator

    def __nonzero__(self):
        return self.is_empty

    @property
    def is_empty(self):
        return not bool(self.object_list)

    def __repr__(self):
        return "<%s.%s: %s>" % (__name__, type(self).__name__, self.character)

    def __iter__(self):
        return iter(self.object_list)
