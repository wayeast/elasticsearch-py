class AndFilter(dict):
    def __init__(self, *args):
        self['and'] = args


class TermsFilter(dict):
    def __init__(self, **kwargs):
        self['terms'] = kwargs


class RangeFilter(dict):
    def __init__(self, **kwargs):
        self['range'] = kwargs

