from django.urls import path
from . import views
urlpatterns=[
    path('',views.index, name='index'),
    path('info/',views.info,name='info'),
    path('validatetask/<str:data>',views.taskverify,name='taskverify'),
    path('vc/<str:data>',views.voteCasted,name='voteCasted'),
    path('user/<str:id>',views.updateUser,name='updateUser'),
    path('vote/<str:num>/<str:vote>', views.vote, name='vote'),
    path('headlines/<int:num>', views.updateHeadline,name='updateHeadline')
]