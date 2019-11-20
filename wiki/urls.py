from django.urls import path
from wiki.views import PageListView, PageDetailView, NewWikiView


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    path('/new/', NewWikiView.as_view(), name='new-wiki'),

]
