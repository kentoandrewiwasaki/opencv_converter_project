from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import GrayForm, FaceReadForm, AnimeForm
from .models import GrayModel, FaceReadModel, AnimeModel
import cv2
import numpy as np
from django.conf import settings

def indexfunc(request):
  return render(request, 'index.html')

#########################################################################

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
        'obj': obj,
    })

def gray(input_path,output_path):
    img = cv2.imread(input_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, img_gray)

################################################################################

def facereadfunc(request):
    if request.method == 'POST':
        form = FaceReadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('faceread')
    else:
        form = FaceReadForm()
        max_id = FaceReadModel.objects.latest('id').id
        obj = FaceReadModel.objects.get(id = max_id)
        input_path = settings.BASE_DIR + obj.image.url
        output_path = settings.BASE_DIR + "/media/faceread/faceread.jpg"
        faceread(input_path,output_path)

    return render(request, 'faceread.html', {
        'form': form,
        'obj': obj,
    })

def faceread(input_path,output_path):
    img = cv2.imread(input_path)
    cascade = cv2.CascadeClassifier(settings.CASCADE_FILE_PATH)    
    # グレースケール変換
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 顔領域の探索
    face = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
    
    # 顔領域を赤色の矩形で囲む
    for (x, y, w, h) in face:
        faceread_img = cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,200), 3)

    # 結果を出力
    cv2.imwrite(output_path, faceread_img)

#############################################################################################

def animefunc(request):
    if request.method == 'POST':
        form = AnimeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('anime')
    else:
        form = AnimeForm()
        max_id = AnimeModel.objects.latest('id').id
        obj = AnimeModel.objects.get(id = max_id)
        input_path = settings.BASE_DIR + obj.image.url
        output_path = settings.BASE_DIR + "/media/anime/anime.jpg"
        anime(input_path, output_path)

    return render(request, 'anime.html', {
        'form': form,
        'obj': obj,
    })

def anime_filter(img):
    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

    # ぼかしでノイズ低減
    edge = cv2.blur(gray, (3, 3))

    # Cannyアルゴリズムで輪郭抽出
    edge = cv2.Canny(edge, 50, 150, apertureSize=3) 

    # 輪郭画像をRGB色空間に変換
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    # 画像の領域分割
    img = cv2.pyrMeanShiftFiltering(img, 5, 20)
    
    # 差分を返す
    return cv2.subtract(img, edge)


def anime(input_path, output_path):
    # 入力画像の読み込み
    img = cv2.imread(input_path)

    # 画像のアニメ絵化
    anime_img = anime_filter(img)
    
    # 結果出力
    cv2.imwrite(output_path, anime_img)
