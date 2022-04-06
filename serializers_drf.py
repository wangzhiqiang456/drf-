from rest_framework import serializers
from k.models import *
#class BookInfoSerializer(serializers.ModelSerializer):
    #定义序列化器
    #class Meta:
        #model = BookInfo #指定序列化从那个模型映射字段
        #fields = '__all__'  #映射那些字段，这里用all代表所有

class BookInfoSerializer(serializers.Serializer):   #与models.py一一对应
    #定义图书序列化器
    id = serializers.IntegerField(label='ID',read_only=True)  #read_only表示输出,且只做序列化，write_only表示输入
    bname = serializers.CharField(max_length=100,label='名称',required=True) #required=True表示需要输入值
    bdate = serializers.DateTimeField(label='日期')





    def create(self,validated_data):
        book = BookInfo.objects.create(**validated_data)
        return book

    def update(self,instance,validated_data):
        instance.bname = validated_data.get('bname')
        instance.bdate = validated_data.get('bdate')
        instance.save()
        return instance


class BookInfoModelSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()    #可以在这里新增加一个新的字段，

    class Meta:
        model = BookInfo        #指定序列化器字段从那个模型去映射
        #fields = '__all__'     #映射model类属性中指定的模型中的那些字段
        #fields = ['id','bname']   #定义指定的字段
        exclude = ['bdate']   #除了bdate其它字段都要
        #extra_kwargs = {   #修改选项参数
            #'bname':{'max_length':80}      #这里将bname中的max_length=100改为80
        #}
        read_only_fields = ['password1']    #将password1字段改为read_only=True即只做序列化
