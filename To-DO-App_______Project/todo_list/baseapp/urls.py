#baseapp Urls
from django.urls import path
from .views import TaskTableList,TaskDetail,TaskCreate,Taskupdate,Taskdelete,customloginview,RegisterPage,TaskReorder
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', customloginview.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',RegisterPage.as_view(), name='register'),
    path('',TaskTableList.as_view(),name ="tasks"),
    path('task/<int:pk>/',TaskDetail.as_view(),name ="task"),
    path('task-create/',TaskCreate.as_view(),name ="task-create"),
    path('task-update/<int:pk>/',Taskupdate.as_view(),name ="task-update"),
    path('task-delete/<int:pk>/',Taskdelete.as_view(),name ="task-delete"),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]