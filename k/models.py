from django.db import models

# Create your models here.
class BookInfo(models.Model):
    id = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=100)
    bdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u'BookInfo:%s'%self.bname
