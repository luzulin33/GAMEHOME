from django.http import HttpResponse
from django.shortcuts import render
from GAMEHOME.settings import MEDIA_URL, BASE_DIR
from users.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def upload(request):
    msg = None
    file = request.FILES.get('upload', None)
    if file:
        import os
        pic = open(os.path.join(r'/workspace/django/d_test/env/GAMEHOME/media/uploads', file.name), 'wb+')
        for chunk in file.chunks():
            pic.write(chunk)
        pic.close()
        msg = "文件上传成功"
        return render(request, 'home/upload.html', locals())

    else:
        return render(request, 'home/upload.html', locals())



