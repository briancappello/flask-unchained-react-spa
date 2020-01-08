import os

from flask_unchained import BundleConfig


class Config(BundleConfig):
    BLOG_ARTICLES_FOLDER = os.path.join(BundleConfig.current_app.root_path, 'articles')
    BLOG_ARTICLE_PREVIEW_LENGTH = 400
    BLOG_FRONTMATTER_LIST_DELIMETER = ','
    BLOG_MARKDOWN_EXTENSIONS = ['extra']
    BLOG_DEFAULT_ARTICLE_AUTHOR_EMAIL = 'a@a.com'
    BLOG_SERIES_FILENAME = 'series.md'
    BLOG_ARTICLE_FILENAME = 'article.md'
    BLOG_ARTICLE_STYLESHEET_FILENAME = 'styles.css'
