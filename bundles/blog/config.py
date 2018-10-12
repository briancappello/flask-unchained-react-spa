import os

from backend.config import Config as AppConfig


class Config(AppConfig):
    BLOG_ARTICLES_FOLDER = os.path.join(AppConfig.PROJECT_ROOT, 'articles')
    BLOG_ARTICLE_PREVIEW_LENGTH = 400
    BLOG_FRONTMATTER_LIST_DELIMETER = ','
    BLOG_MARKDOWN_EXTENSIONS = ['extra']
    BLOG_DEFAULT_ARTICLE_AUTHOR_EMAIL = 'a@a.com'
    BLOG_SERIES_FILENAME = 'series.md'
    BLOG_ARTICLE_FILENAME = 'article.md'
    BLOG_ARTICLE_STYLESHEET_FILENAME = 'styles.css'
