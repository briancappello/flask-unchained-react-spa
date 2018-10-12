from flask_unchained.bundles.api import ModelResource

from ..models import Series


class SeriesResource(ModelResource):
    class Meta:
        model = Series
        include_methods = ('get', 'list')
