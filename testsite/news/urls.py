from django.urls import path
from .views import CategoryNews, CreateNews, HomeNews, ViewNews, user_login, user_logout, register, contact

urlpatterns = [
    #Основной вывод при помощи классов
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', CategoryNews.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # Вывод при помощи функций
    path('contact/', contact, name='contact'),
    # path('', index, name='home'),
    # path('news/add-news/', add_news, name='add_news'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    # path('category/<int:category_id>/', get_category, name='category'),
]