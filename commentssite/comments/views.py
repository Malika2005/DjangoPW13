from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Comment
import json

def get_comments(request):
    comments = Comment.objects.all()
    comment_list = list(comments.values())
    return HttpResponse(json.dumps({'comments': comment_list}), content_type='application/json')

def get_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return HttpResponse(json.dumps({'comment': comment}), content_type='application/json')

def delete_comment_by_sms_id(request, sms_id):
    comment = get_object_or_404(Comment, sms_id=sms_id)
    comment.delete()
    return HttpResponse(json.dumps({'message': 'Comment successfully deleted'}), content_type='application/json')