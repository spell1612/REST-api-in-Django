from django.urls import path
from . import views
#
app_name='CRUD'
urlpatterns=[
    path('',views.DisplayList.as_view(),name='disp'),
    path('enter/',views.enterDetails,name='enter'),
    path('<int:pk>/details/',views.DetailView.as_view(),name='details'),
]
