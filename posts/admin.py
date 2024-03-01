from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf import settings

from posts.telegram_utils import send_telegram_message
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    change_form_template = "post_change_form.html"
    list_display = ('title', 'created_at', 'is_published')

    def response_change(self, request, post_obj):
        if "publish-telegram" in request.POST:
            send_telegram_message(
                chat_id=settings.CHAT_ID,
                post=post_obj
            )
            post_obj.is_published = True
            post_obj.save()
            self.message_user(request, "Опубликовано сообщение об этом посте в телеграм канале")
            return HttpResponseRedirect(request.path_info)

        return super().response_change(request, post_obj)
