from django.urls import path
from news.api.views import (ArticleListCreateAPIView, 
                            ArticleDetailAPIView)

""" from news.api.views import (article_list_create_api_view, 
                            article_detail_api_view) """

urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="article-list"),
    path("articles/<int:pk>", ArticleDetailAPIView.as_view(), name="article-detail"),
    # path("articles/", article_list_create_api_view, name="article-list"),
    # path("articles/<int:pk>", article_detail_api_view, name="article-detail"),
]
