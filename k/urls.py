#coding=utf-8
from django.urls import path,re_path
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter

urlpatterns = [
    #path('books/',views.BookListView.as_view()),
    #re_path('books/(?P<pk>\d+)/',views.BookDetailView.as_view()),


    #path('books/',views.BookListGenericView.as_view()),
    #re_path('books/(?P<pk>\d+)/',views.BookDetailGenericView.as_view()),

    #ViewSet视图集指定路由
    #path('books/',views.BookViewSet.as_view({'get':'list','post':'create'})),
    #re_path('books/(?P<pk>\d+)/',views.BookViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}))

    #如果在增删改查之外进行额外的行为，应该单独定义路由
    #如果此行为不需要pk，那么它就是列表视图，但是列表视图默认只有list,create
    #path('books/latest/', views.BookViewSet.as_view({'get': 'latest'})),
    #path('books/(?P<pk>\d+)/name/', views.BookViewSet.as_view({'put': 'name'}))

]
#router = DefaultRouter()   #创建路由器
router = SimpleRouter()   #创建路由器
router.register('books',views.BookViewSet)  #注册路由
urlpatterns += router.urls  #把生成好的路由拼接到urlpatterns中去
