from django.shortcuts import render, redirect, get_object_or_404
from .models import Message, Comment, Like
from .forms import MessageForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    return render(request, 'feed/home.html')

def feed(request):
    messages = Message.objects.all()
    return render(request, 'feed/feed.html', {'messages': messages})

def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    comments = Comment.objects.filter(message=message)
    form = CommentForm()
    return render(request, 'feed/message_detail.html', {'message': message, 'comments': comments, 'form': form})

def post_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('feed')
    else:
        form = MessageForm()
    return redirect('feed')

def post_comment(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.message = message
            comment.save()
            return redirect('message_detail', message_id=message_id)
    else:
        form = CommentForm()
    return render(request, 'feed/message_detail.html', {'message': message, 'form': form})

def like_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.user.is_authenticated:
        Like.objects.get_or_create(message=message, user=request.user)
    return redirect('feed')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
