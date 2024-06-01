# Programmer: Xia Linhan
# Date: 2023.12.3

from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import PersonalInfo, SkillIntroduction, WorkExperience, Message
# 业务逻辑

def index(request):
    # 尝试获取个人信息实例，如果不存在则为 None
    personal_info = PersonalInfo.objects.first()
    # 尝试获取技能介绍实例，如果不存在则为 None
    skill_introduction = SkillIntroduction.objects.first()
    # 获取所有工作经验实例并按开始日期排序
    work_experiences = WorkExperience.objects.all().order_by('start_date')

    # print(work_experiences.all())

    # 渲染首页index.html，并传递个人信息、技能介绍和工作经验
    return render(request, 'index.html', {
        'personal_info': personal_info,
        'skill_introduction': skill_introduction,
        'work_experiences': work_experiences
    })

def create_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # 重定向到首页
    else:
        form = MessageForm()

def Data_analysis_page(request):
    # 渲染数据分析项目页面
    return render(request,'Data_analysis.html')

def Business_CO2(request):
    # 渲染数据分析项目页面
    return render(request,'Business_CO2.html')

def Vedio_work(request):
    # 渲染数据分析项目页面
    return render(request,'Vedio.html')

def UI_design(request):
    # 渲染UI设计界面
    return render(request,'UI_design.html')