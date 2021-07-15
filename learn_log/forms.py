from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):

    """Meta 类告诉 Django 根据哪个模型创建表单，以及在表单中包含哪些字段"""
    class Meta:
        model = Topic  # 告诉 Django 根据 Topic 创建表单
        fields = ['text']  # 只包含 text 一个字段
        labels = {'text': ' '}  # 让 Django 不为 text 生成标签


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ' '}
        """
        widgets，HTML 中的小部件，表单元素
        设置 widgets 属性，可覆盖 Django 选择的默认小组件
        通过让 Django 使用 forms.Textarea，定制 text 的输入小部件
        """
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
