# quiz앱에 있는 url 관리
# myapi는 전체 프로젝트 url 관리

# quiz 폴더의 url을 먼저 설정하고 이것을 myapi의 url에 연결시킨다.

from django.urls import path, include
from .views import helloAPI, randomQuiz

# urlpatterns는 []에 담아야 한다.
urlpatterns = [
    path('hello/',helloAPI),
    path("<int:id>/", randomQuiz)
]