from django.urls import path,re_path

from . import views

app_name='polls'
urlpatterns=[
    path('index',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
    path('show/',views.show,name="show"),
    path('show2/',views.show2,name='show2'),
    path('show3/',views.show3,name="show3"),
    path('show4/',views.show4,name="show4"),
    path('show5/',views.show5,name="show5"),
    path('media/<media_id>/',views.media,name="media"),
#    path('home/',views.home,name="home"),
    path('',views.home,name="home"),
]
