from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video, Comment
from showvideo.serializer import CommentSerializer, VideoSerializer
from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from json import dumps






# Create your views here.
class VideoList(ListAPIView):
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

class CommentList(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class CreateVideo(CreateAPIView):
    serializer_class = VideoSerializer

class UpdateDestroyVideo(RetrieveUpdateDestroyAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()



def hello(request):
    return HttpResponse("<h1>hello world</h1>")


def world(request):
    response = {"name":"Bogdan", "d":34,"arr":[1,2,3,4,5]}
    response["content"] = Video.objects.all()
    return render(request, "index.html", response)


def accept_comment(request, id):
    #1
    Comment.objects.create(text=request.POST["com"] , comment_video_id=id)
    #2
    #  video=Video.objects.get(id=id)
    # Comment.objects.create(text="hello world", comment_video=video)
    #3
    #c = Comment(text=request.GET["com"], comment_video=id)
    #c.save()
    # print(id)
    # print(request.GET["com"])
    return redirect("main_page")

def one_video(request,id):
    response = {"video":Video.objects.get(id=id)}
    return  render(request, "one_video.html", response)

def add_like(request, id):
    video = Video.objects.get(id= id)
    video.likes += 2
    video.save()
    return  redirect("main_page")

def ajax_like(request):
    id = (request.GET["id"])
    video = Video.objects.get(id=id)
    video.likes += 1
    video.save()
    return HttpResponse(video.likes)

def ajax_comment(request):
    id = request.GET["id"]
    val = request.GET["val"]
    com = Comment.objects.create(text=val, comment_video_id=id)
    response = {"id":com.id, "date":com.date.__str__()}
    response = dumps(response)
    return HttpResponse(response)
