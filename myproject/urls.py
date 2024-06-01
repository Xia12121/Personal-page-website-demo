# Programmer: Xia Linhan
# Date: 2023.12.3

from django.contrib import admin
from django.urls import path, include  # 添加include，用于包含其他的URLconf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zjyapp.urls')), # 添加include，用于包含其他的URLconf
]
