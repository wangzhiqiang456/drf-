"""
GET         /books/          查询所有的记录
POST        /books/          新增一条记录
GET         /books/<pk>/     查询指定id的记录
PUT         /books/<pk>/     修改指定id的记录
DELETE      /books/<pk>/     删除指定id的记录
"""
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.viewsets import ModelViewSet

from k.models import *
from .serializers import BookInfoSerializer
"""
class BookListView(View):
    #列表视图

    def get(self,request):
        #查询所有图书接口
        #1.查询出所有图书模型
        books = BookInfo.objects.all()
        #2.遍历查询集，取出里面的每个书籍模型对象，把模型对象转换成字典
        #定义一个列表变量用来保存这个字典
        book_list = []

        for book in books:
            book_dict = {
                'bittle': book.bittle,
                'bpub_date': book.bpub_date,
                'bread':book.bread,
                'bcomment': book.bcomment,
            }
"""
class BookInfoView(ModelViewSet):
    #定义类视图
    #指定查询集
    queryset = BookInfo.objects.all()

    #指定序列化器
    serializer_class = BookInfoSerializer

#序列化
#book = BookInfo.objects.get(id=1)
#s = BookInfoSerializer(instance=book)   #创建序列化对象，并序列化
#s.data   #获取序列化后的数据

"""
#反序列化
data = {
    'bname':'li',
    'bdate':'2022-03-29T09:08:01.570524Z'
}
serializer = BookInfoSerializer(data=data)
serializer.is_valid()  #先进行校验，调用序列化器的校验方法返回值为True,False
serializer.is_valid(raise_exception=True)  #raise_exception=True如果多指定这个，将来校验出错后，会自动抛出错误信息
serializer.errors  #获取校验的错误信息
serializer.validated_data  #获取反序列化校验后的数据，字典

book = serializer.save()#当调用序列化器的save方法时，会执行序列化器中的create方法或update方法
"""