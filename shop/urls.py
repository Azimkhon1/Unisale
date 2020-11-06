from django.urls import path, include  # import path and include for urls
from . import views  # import views module
from django.contrib.auth.decorators import login_required


app_name = 'shop'

urlpatterns = [  # urls patterns to have urls from global urls
    path('', views.IndexList.as_view(), name='index'),  # tail of shop url with function
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),  # tail of shop url with function
    path('index/categories/', views.CategoriesList.as_view(), name='categories'),  # tail of shop url with function
    path('index/create/', login_required(views.UseView.as_view()), name='user'),  # tail of shop url with function
    path('index/support', views.SupportView.as_view(), name='support'),  # tail of shop with function

]










