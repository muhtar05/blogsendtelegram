from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from .telegram_utils import send_telegram_message


def send_post_to_telegram_view(request):
    post = Post.objects.first()
    send_telegram_message(chat_id="@gadjimuradov_space", post=post)
    return HttpResponse("Send telegram message")
