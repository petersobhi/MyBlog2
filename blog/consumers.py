import json

from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http

from .models import Post


# Connected to websocket.connect
@channel_session_user_from_http
def ws_add(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group("posts").add(message.reply_channel)


# Connected to websocket.receive
@channel_session_user
def ws_message(message):
    post_dict = json.loads(message.content['text'])
    action = post_dict['action']

    user = message.user

    if action == 0:  # add
        subject = post_dict['subject']
        body = post_dict['body']

        post = Post(subject=subject, body=body, user=user)
        post.save()

        post_dict['username'] = user.username
        post_dict['post_id'] = post.id

    elif action == 1:  # edit
        post_id = post_dict['post_id']
        subject = post_dict['subject']
        body = post_dict['body']

        post = Post.objects.get(id=post_id)
        post.subject = subject
        post.body = body
        post.save()

    else:  # delete
        post_id = post_dict['post_id']
        post = Post.objects.get(id=post_id)
        post.delete()

    Group("posts").send({
        "text": json.dumps(post_dict),
    })


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("posts").discard(message.reply_channel)
