import collections
import copy

class IndicesQuery(dict):
    def __init__(self, **kwargs):
        """
        Populate object's 'indices' dict.

        According to Elasticsearch Reference/Query DSL/Queries/Indices Query
        documentation, the order of the fields in an indices query
        matters.  Hence, an OrderedDict is used to ensure that the 
        'indices' field appears before the 'query' field.
        """
        self['indices'] = collections.OrderedDict()
        self['indices']['indices'] = kwargs.pop('indices')
        self['indices']['query'] = kwargs.pop('query',
                                              {'match_all': {}})
        self['indices'].update(kwargs)

