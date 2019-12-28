from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import ArticleView, SingleArticleView
# from .views import ArticleView, ArticleViewSet
from .views import ArticleViewSet

"""
app_name = 'articles'

urlpatterns = [
    path('articles/', ArticleView.as_view({'get': 'list'})),
    path('articles/<int:pk>/', ArticleView.as_view({'get': 'retrieve'})),
]
"""

# Third part. 
# Generate URLs authomaticly
router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='user')

urlpatterns = router.urls
