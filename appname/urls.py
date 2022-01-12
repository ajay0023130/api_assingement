from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path('list/',views.EmpList,name="emplist"),
    path("empdetails/<int:pk>",views.EmpDetails,name="empdetials"),
    path('empcreate/',views.EmpCreate,name="empcreate"),
    path('empupdate/<int:pk>/',views.EmpUpdate,name="update"),
    path('empdelete/<int:pk>/',views.EmpDelete,name="delete"),
]