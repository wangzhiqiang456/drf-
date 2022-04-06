"""
GET         /books/          查询所有的记录
POST        /books/          新增一条记录
GET         /books/<pk>/     查询指定id的记录
PUT         /books/<pk>/     修改指定id的记录
DELETE      /books/<pk>/     删除指定id的记录
"""
from django.db import DatabaseError
from rest_framework import status, mixins
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, GenericViewSet, ModelViewSet

from k.models import BookInfo
from k.serializers import BookInfoModelSerializer
from serializers_drf import BookInfoSerializer


class BookListView(APIView):
    """列表视图"""
    def get(self,request):
        """查询所有"""
        qs = BookInfo.objects.all()
        serializer = BookInfoModelSerializer(instance=qs,many=True)
        return Response(serializer.data)

    def post(self, request):
        """新增记录"""
        # 获取前端传入的请求体数据
        data = request.data
        # 创建序列化器进行反序列化
        serializer = BookInfoModelSerializer(data=data)
        # 调用序列化器的is_valid(raise_exception=True)
        serializer.is_valid(raise_exception=True)
        # 调用序列化器的save方法进行执行create方法
        serializer.save()

        # 响应
        return Response(serializer.data)


class BookDetailView(APIView):
    """详情视图"""
    def get(self,request,pk):
        """查询指定的数据"""
        #查询pk指定的模型对象
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #创建序列化器进行序列化
        serializer = BookInfoModelSerializer(instance=book)
        #响应
        return Response(serializer.data)

    def put(self,request,pk):
        """修改指定的数据"""
        #查询pk指定的模型对象
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #创建序列化器进行反序列化
        serializer = BookInfoModelSerializer(instance=book,data=request.data)
        #校验
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #响应
        return Response(serializer.data)

    def delete(self,request,pk):
        """删除数据"""
        #查询指定pk的模型对象
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookListGenericView(GenericAPIView):
    """列表视图"""
    #指定序列化器类
    serializer_class = BookInfoModelSerializer
    #指定查询集'数据来源'
    queryset = BookInfo.objects.all()

    def get(self,request):
        """查询所有"""
        qs = self.get_queryset()
        serializer = self.get_serializer(qs,many=True)
        return Response(serializer.data)


class BookDetailGenericView(GenericAPIView):
    """详情视图"""
    #指定序列化器类
    serializer_class = BookInfoModelSerializer
    # 指定查询集'数据来源'
    queryset = BookInfo.objects.all()

    def get(self,request,pk):
        """查询指定pk的模型对象"""
        book = self.get_object()   #在这个里面已经根据pk查到了数据，不用进行传参，函数名里面写了就行
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    def put(self,request,pk):
        """修改指定pk的数据"""
        book = self.get_object()  #返回详情视图所需的模型类数据对象
        serializer = self.get_serializer(instance=book,data=request.data)  #用于序列化时，将模型类对象传入instance参数,用于反序列化时，将要被反序列化的数据传入data参数
        serializer.is_valid(raise_excertion=True)
        serializer.save()
        return Response(serializer.data)

"""GenericAPIView+Mixin实现接口实现增删改查"""
class BookListGenericView(ListModelMixin,CreateModelMixin):
    """列表视图"""
    #指定序列化器类
    serializer_class = BookInfoModelSerializer
    #指定查询集'数据来源'
    queryser = BookInfo.objects.all()

    def get(self,request):
        """查询"""
        return self.list(request)

    def post(self,request):
        """新增数据"""
        return self.create(request)

class BookDetailGenericView(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    """详情视图"""
    #指定序列化器类
    serializer_class= BookInfoModelSerializer
    #指定查询集'数据来源'
    queryset = BookInfo.objects.all()

    def get(self,request,pk):
        """查询指定的pk数据"""
        return self.retrieve(request,pk)

    def put(self,request,pk):
        """修改指定pk的数据"""
        return self.update(request,pk)

    def delete(self,request,pk):
        """删除指定pk的数据"""
        return self.destroy(request,pk)

"""GenericAPIView+Mixin合成类实现增删改查"""
class BookListGenericView(ListCreateAPIView):
    """列表视图"""
    #指定序列化器类
    serializer_class = BookInfoModelSerializer
    #指定查询集'数据来源'
    queryset = BookInfo.objects.all()

class BookDetailGenericView(RetrieveUpdateDestroyAPIView):
    """详情视图"""
    # 指定序列化器类
    serializer_class = BookInfoModelSerializer
    # 指定查询集'数据来源'
    queryset = BookInfo.objects.all()

"""将两个get查询写到一个类下，我们写APIVIEW的视图集"""
class BookViewSet(ViewSet):
    """视图集"""
    def list(self,request):
        """查询所有数据"""
        qs = BookInfo.objects.all()
        serializer = BookInfoModelSerializer(qs,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk):
        """查询指定的pk数据"""
        try:
            book = BookInfo.objects.all()
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookInfoModelSerializer(book)
        return Response(serializer.data)


class LargeResultsSetPagination(PageNumberPagination):
    """自定义分页"""
    page_size = 2  #默认每页显示多少条数据
    page_query_param = 'page'  #前端在查询字符串的关键字 指定显示第几页的名字，不写就默认为page
    page_size_query_param = 'page_size'   #用来控制每页显示多少条的关键字
    max_page_size = 4    #前端控制每页显示多少条

class BookViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    #权限
    #permission_classes = [IsAuthenticated]   #只有登录用户才能访问此视图中的所有接口
    #permission_classes = [IsAuthenticatedOrReadOnly]   #认证过的用户可读可写，没有认证的用户可读不可写

    filter_fields = ['id','bname']   #对id或bname进行过滤，形式为:?id=1,或者?bname=li

    #排序
    #指定过滤后端为排序
    filter_backends = [OrderingFilter]
    #指定排序字段
    ordering_fields = ['bdate']

    pagination_class = LargeResultsSetPagination   #指定分页类

    @action(methods=['get'],detail=False)
    #@action(method=[指定下面的行为接收什么请求],detail=是不是详情视图，如果不是详情视图就是books/latest/为False)
    def latest(self, request):
        """
        返回最后一本书的图书信息
        """
        raise DatabaseError()
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)
    @action(methods=['put'],detail=True)
    def name(self, request, pk):
        """
        修改图书的名称
        """
        book = self.get_object()
        book.bname = request.data.get('bname')
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)

