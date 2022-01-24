from django.urls import path
from .views import CategoryNews, CreateNews, HomeNews, ViewNews, login, register

urlpatterns = [
    #Основной вывод при помощи классов
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', CategoryNews.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    # Вывод при помощи функций
    # path('test/', test, name='test'),
    # path('', index, name='home'),
    # path('news/add-news/', add_news, name='add_news'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    # path('category/<int:category_id>/', get_category, name='category'),
]