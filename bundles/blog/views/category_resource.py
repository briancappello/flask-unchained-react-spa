from flask_unchained.bundles.api import ModelResource
from flask_unchained import injectable

from ..models import Category
from ..services import ArticleManager, SeriesManager


class CategoryResource(ModelResource):
    class Meta:
        model = Category
        include_methods = ('get', 'list')

    article_manager: ArticleManager = injectable
    series_manager: SeriesManager = injectable

    def get(self, category):
        return self.Meta.serializer.dump({
            'name': category.name,
            'slug': category.slug,
            'series': self.series_manager.find_by_category(category),
            'articles': self.article_manager.find_by_category(category),
        })
