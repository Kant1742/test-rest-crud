from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404,\
    GenericAPIView, CreateAPIView, ListAPIView, ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin


from .models import Article, Author
from .serializers import ArticleSerializer


"""First part

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({'articles': serializer.data})

    def post(self, request):
        article = request.data.get('article')
        # Create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()

        # f-string in dicts looks like shit.
        return Response({'success': f'Article "{article_saved.title}" created successfully'})

    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(
            instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()

        return Response({
            'success': f'Article "{article_saved.title}" updated successfully'
        })

    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)
"""


# The difference between GenericAPIView and APIView is that we
# can get List and Detail in GenericAPIView

"""Second 
class ArticleView(ListModelMixin, CreateModelMixin, GenericAPIView):
    # Get objects in our case.
    # If we would need, for example, a query with filtering, etc.,
    # we could override the get_queryset method and return the
    # required query through it.
    queryset = Article.objects.all()
    # It uses to check and deserialize (? not to serialize)
    # objects from DB
    serializer_class = ArticleSerializer

    # Opportunity to get List of Articles
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # CreateModelMixin provides .create(request, *args, **kwargs)
    # method, that implements creating and saving a new model instance
    def perform_create(self, serializer):
        author = get_object_or_404(
            Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
"""

'''
# Second V2.0
class ArticleView(CreateAPIView, ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(
            Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)
'''

'''
# Second V3.0
class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(
            Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
'''

"""
# Third part
class ArticleView(viewsets.ViewSet):
    # A simple ViewSet for listing and retrieving people.

    def list(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(user)
        return Response(serializer.data)
"""

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
