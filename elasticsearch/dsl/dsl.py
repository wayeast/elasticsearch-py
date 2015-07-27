class DSL(dict):
    def __init__(self,
                 size=10,
                 from_ind=0,
                 fields=None,
                 sort=None,
                 query=None,
                 filter=None):
        self['size'] = size
        self['from'] = from_ind
        if fields:
            self['fields'] = fields
        if sort:
            self['sort'] = sort
        if query:
            self['query'] = query
        if filter:
            self['filter'] = filter

