from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Topic(models.Model):
    """用户储存学习知识的主题"""
    text = models.CharField(max_length=200)  # 储存主题的名字
    date = models.DateTimeField(auto_now_add=True)  # 自动记录主题创建的时间
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """用户学习到的有关某个主题的具体知识"""

    """
    外键, 数据库术语，指向数据库中的另一条记录，这里指将条目关联到具体的主题
    on_delete=models.CASCADE 用于实现删除主题时，同时删除与之相关联的条目，称为 级联删除(cascading delete)
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    """Meta类 用于储存管理模型的额外信息"""

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回该模型的字符串表示"""
        if len(self.text) >= 50:
            return f'{self.text[:50]}...'
        else:
            return f'{self.text}'
