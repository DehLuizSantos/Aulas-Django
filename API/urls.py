from home import views as home_views
from blog import views as blog_views
from django.contrib import admin
from django.urls import path

""" MVT - Função que recebe a request, e retorna uma resposta  """

""" http://127.0.0.1:800/ """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog_views.blog),
    path('', home_views.home)

]
