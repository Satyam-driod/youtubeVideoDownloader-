from django.shortcuts import render, redirect
from django.http import HttpResponse
import youtube_dl
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'downloader\home.html')

def download_video(request):
    if request.method == 'POST':
        video_url = request.POST['url']
        if video_url:
            ydl_out = {'outtmp': 'D:/'}
            with youtube_dl.YoutubeDL(ydl_out) as ydl:
                ydl.download([video_url])
            messages.success(request, 'Video Dowmloaded. ')
            return redirect('home')
        else:
            messages.warning(request, 'Please Enter Video URL')
            return redirect('home')
    return redirect('home')