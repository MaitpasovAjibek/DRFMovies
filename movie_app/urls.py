from django.urls import path
from . import views


urlpatterns = [
    path('director/',views.director_list_api_view),
    path('director/<int:id>/',views.director_detail_api_view),
    path('movie',views.movie_list_api_view),
    path('movie/<int:id>/',views.movie_detail_api_view),
    path('rewiew/',views.rewiew_list_api_view),
    path('rewiew/<int:id>/',views.rewiew_detail_api_view)
]