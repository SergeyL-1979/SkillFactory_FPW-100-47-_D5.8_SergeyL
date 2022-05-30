from django.urls import path
from .views import NewsList, NewsDetail, CategoryDetail, SearchListViews, PostCreateView, PostUpdateView, PostDeleteView  #, add_like
from .views import PostAuthorView
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('', NewsList.as_view(), name='post_list'),
    path('news/', NewsList.as_view(), name='post_list'),
    # path('news/<str:slug>/', NewsDetail.as_view(), name='post_detail'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='post_detail'),  # возможен переход по id статьи\новости
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('search/', SearchListViews.as_view(), name='search'),
    # path('like/', add_like, name='add_like'),  # не знаю как сделать
    path('add/', PostCreateView.as_view(), name='post_create_view'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update_view'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete_view'),
    path('my_post/', PostAuthorView.as_view(), name='post_author_view'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html'),
         name='change_password'),
]
