from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import GrayForm
from .models import GrayModel
import cv2
from django.conf import settings

def indexfunc(request):
  return render(request, 'index.html')

def grayfunc(request):
    if request.method == 'POST':
        form = GrayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gray')
    else:
        form = GrayForm()
        max_id = GrayModel.objects.latest('id').id
        obj = GrayModel.objects.get(id = max_id)
        input_path = settings.BASE_DIR + obj.image.url
        output_path = settings.BASE_DIR + "/media/gray/gray.jpg"
        gray(input_path,output_path)

    return render(request, 'gray.html', {
        'form': form,
        'obj':obj,
    })


###########ここをカスタマイズ############

def gray(input_path,output_path):
    img = cv2.imread(input_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, img_gray)

######################################