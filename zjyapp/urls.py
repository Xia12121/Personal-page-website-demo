# Programmer: Xia Linhan
# Date: 2023.12.3

from django.urls import path
from .views import index, create_message,Data_analysis_page,Business_CO2,Vedio_work,UI_design

urlpatterns = [
    path('', index, name='index'),
    path('Data_analysis', Data_analysis_page, name='Data_analysis_page'),
    path('Business_CO2', Business_CO2, name='Business_CO2'),
    path('UI_design', UI_design, name='UI_design'),
    path('Vedio_work', Vedio_work, name='Vedio_work'),
    path('message/create/', create_message, name='create_message'),
]
