from django.urls import path

from .views import BooksViewSet, JournalViewSet, BookListView, JournalListView

urlpatterns = [
    path('books/', BookListView.as_view()),
    path('books/create/', BooksViewSet.as_view({'post': 'create'})),
    path('books/<int:pk>/', BooksViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'delete': 'destroy'})),
    path('journals/', JournalListView.as_view()),
    path('journals/create/', JournalViewSet.as_view({'post': 'create'})),
    path('journals/<int:pk>/', JournalViewSet.as_view({'get': 'retrieve',
                                                       'put': 'update',
                                                       'delete': 'destroy'})),
]