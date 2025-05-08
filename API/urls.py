from django.contrib import admin
from django.urls import path, include

""" MVT - Função que recebe a request, e retorna uma resposta  """

""" http://127.0.0.1:800/ """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('home.urls'))

]
