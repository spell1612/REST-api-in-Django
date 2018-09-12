from django.urls import path
from . import views
#
app_name='CRUD'
urlpatterns=[
    path('',views.DisplayList.as_view(),name='disp'),
    # path('enter/',views.enterDetails,name='enter'),
    path('enter/',views.EnterDetails.as_view(),name='enter'),
    path('<int:pk>/details/',views.DetailView.as_view(),name='details'),
    # path('edit/<int:id>/',views.editDetails,name='edit'),
    path('edit/<int:pk>/',views.EditDetails.as_view(),name='edit'),
    # path('delete/<int:id>/',views.deleteDetails,name='delete'),
    path('delete/<int:pk>/',views.DeleteDetails.as_view(),name='delete'),
]
