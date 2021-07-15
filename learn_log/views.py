from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect  # render() 函数用于根据视图提供的数据渲染响应

from .forms import TopicForm, EntryForm
from .models import Topic, Entry


# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'learn_log/index.html')


@login_required
def topics(request):
    """显示所有的主题"""
    _topics = Topic.objects.filter(owner=request.user).order_by('date')  # 从数据库中获取数据，限制用户访问，并按日期排序
    context = {'topics': _topics}  # 定义一个上下文，上下文是一个字典，用于传给模板，其中键值模板中用来访问的数据名称，值为发送给模板是数据
    return render(request, 'learn_log/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示单个主题，及其所有条目"""
    _topic = Topic.objects.get(id=topic_id)  # 该操作称为查询，建议先在 Django shell 中验证一下结果，再写进代码
    __check_topic_owner(_topic, request)

    entries = _topic.entry_set.order_by('-date')  # -号表示降序排列
    context = {'topic': _topic, 'entries': entries}
    return render(request, 'learn_log/topic.html', context)


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # 对 POST 提交的数据进行处理
        form = TopicForm(data=request.POST)
        if form.is_valid():
            _new_topic = form.save(commit=False)
            _new_topic.owner = request.user
            _new_topic.save()
            return redirect('learn_log:topics')

    context = {'form': form}
    return render(request, 'learn_log/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """在特定主题中添加新条目"""
    _topic = Topic.objects.get(id=topic_id)
    __check_topic_owner(_topic, request)

    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = EntryForm()
    else:
        # 对 POST 提交的数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            _new_entry = form.save(commit=False)  # 让 Django 创建一个新的条目对象但不储存到数据库中
            _new_entry.topic = _topic  # 使新的 entry 匹配相应的 topic
            _new_entry.save()  # 保存新的 entry 到数据库中
            return redirect('learn_log:topic', topic_id=topic_id)

    context = {'topic': _topic, 'form': form}
    return render(request, 'learn_log/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """修改已有条目"""
    _entry = Entry.objects.get(id=entry_id)
    _topic = _entry.topic
    __check_topic_owner(_topic, request)

    if request.method != 'POST':
        form = EntryForm(instance=_entry)
    else:
        form = EntryForm(instance=_entry, data=request.POST)  # 根据既有条目对象创建一个表单，数据使用 POST 中的数据
        if form.is_valid():
            form.save()
            return redirect('learn_log:topic', topic_id=_topic.id)

    context = {'topic': _topic, 'entry': _entry, 'form': form}

    return render(request, 'learn_log/edit_entry.html', context)


def __check_topic_owner(_topic, request):
    if _topic.owner != request.user:
        raise Http404
