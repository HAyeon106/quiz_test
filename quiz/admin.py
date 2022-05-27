from django.contrib import admin
from .models import Quiz

# quiz 모델을 관리하기 위해 관리자 페이지에서 register 하여 관리할 수 있게 한다.
# Register your models here.
admin.site.register(Quiz)

# 관리자 계정을 생성해야 한다.
# python manage.py createsuperuser
# 유저  이름: root
# 비밀번호: 그거