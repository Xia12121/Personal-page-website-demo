# Programmer: Xia Linhan
# Date: 2023.12.3

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)   # 姓名
    age = models.PositiveIntegerField(blank=True, null=True)         # 年龄
    bio = models.TextField(blank=True, null=True)                    # 个人简介
    major = models.CharField(max_length=100, blank=True, null=True)  # 专业
    school = models.CharField(max_length=100, blank=True, null=True) # 毕业院校
    birthday = models.CharField(max_length=100, blank=True, null=True)# 生日
    email = models.EmailField(blank=True, null=True)                 # Email
    gpa = models.CharField(max_length=10, blank=True, null=True)     # GPA（绩点），用文本形式表示

    def __str__(self):
        return self.name or "Personal Information"

    def save(self, *args, **kwargs):
        if not self.pk and PersonalInfo.objects.exists():
            # 如果已存在实例，不创建新的
            raise ValidationError('An instance of PersonalInfo already exists.')
        return super(PersonalInfo, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Personal Information"


class SkillIntroduction(models.Model):
    introduction = models.TextField(blank=True, null=True)  # 技能介绍

    def save(self, *args, **kwargs):
        if not self.pk and SkillIntroduction.objects.exists():
            # 如果已存在实例，不创建新的
            raise ValidationError('An instance of SkillIntroduction already exists.')
        return super(SkillIntroduction, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Skill Introduction"

    class Meta:
        verbose_name_plural = "Skill Introduction"

class WorkExperience(models.Model):
    company = models.CharField(max_length=100)           # 公司
    position = models.CharField(max_length=100)          # 职位
    job_description = models.TextField()                 # 工作内容
    start_date = models.CharField(max_length=20)         # 开始日期（字符串格式）
    end_date = models.CharField(max_length=20)           # 结束日期（字符串格式）

    def __str__(self):
        return f"{self.position} at {self.company}"

    class Meta:
        verbose_name_plural = "Work Experiences"

class Message(models.Model):
    name = models.CharField(max_length=100)    # 留言者的名字
    email = models.EmailField()                # 留言者的邮箱
    content = models.TextField()               # 留言内容

    def __str__(self):
        return f"Message from {self.name}"

    class Meta:
        verbose_name_plural = "Messages"