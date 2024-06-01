# Programmer: Xia Linhan
# Date: 2023.12.3

from django.contrib import admin
from .models import PersonalInfo,WorkExperience,SkillIntroduction,Message

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    # 显示的字段
    pass

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'start_date', 'end_date')
    search_fields = ('company', 'position')

@admin.register(SkillIntroduction)
class SkillIntroductionAdmin(admin.ModelAdmin):
    list_display = ('introduction', )

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'content')
    search_fields = ('name', 'email')