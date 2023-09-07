from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('<int:id>/', views.home_page, name='home_page'),
    path('get_search_sheet/', views.get_search_sheet, name='get_search_sheet'),
    path('get_top_bottom_sheet/<str:query>/', views.get_top_bottom_sheet, name='get_top_bottom_sheet'),
    path('get_pre_and_next_sheet/<int:id>/<str:query>/', views.get_pre_and_next_sheet, name='get_pre_and_next_sheet'),
    path('report/', views.report, name='report'),
]
