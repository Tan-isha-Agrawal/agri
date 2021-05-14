from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('prediction_page/', views.main, name='prediction_page'),
    
    path('main/', views.predict_chances, name='submit_prediction'),
    path('results/', views.view_results, name='results'),
]