from flask_unchained.bundles.api import ma

from ..models import SeriesArticle

ARTICLE_SERIES_FIELDS = ('part', 'slug', 'title')


# used when serializing a list of series
class SeriesArticleSerializer(ma.ModelSerializer):
    slug = ma.Pluck('ArticleSerializer', 'slug', attribute='article', dump_only=True)
    title = ma.Pluck('ArticleSerializer', 'title', attribute='article', dump_only=True)

    class Meta:
        model = SeriesArticle
        fields = ARTICLE_SERIES_FIELDS


# used when serializing a list of articles
class ArticleSeriesSerializer(ma.ModelSerializer):
    slug = ma.Pluck('SeriesSerializer', 'slug', attribute='series', dump_only=True)
    title = ma.Pluck('SeriesSerializer', 'title', attribute='series', dump_only=True)

    class Meta:
        model = SeriesArticle
        fields = ARTICLE_SERIES_FIELDS


# used when serializing an article detail
class ArticleSeriesDetailSerializer(ArticleSeriesSerializer):
    articles = ma.Nested('SeriesArticleSerializer',
                         attribute='series.series_articles', many=True)

    class Meta:
        model = SeriesArticle
        fields = ARTICLE_SERIES_FIELDS + ('articles',)
