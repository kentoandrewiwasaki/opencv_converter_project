from django.shortcuts import render, redirect
from .forms import GrayForm, FaceReadForm, AnimeForm, MosaicForm, FaceMosaicForm
from .models import GrayModel, FaceReadModel, AnimeModel, MosaicModel, FaceMosaicModel
import cv2
import numpy as np
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.db.models.base import ObjectDoesNotExist

def indexfunc(request):
    try:
        gray_obj = GrayModel.objects.get(id = GrayModel.objects.latest('id').id)
    except GrayModel.ObjectDoesNotExist:
        gray_obj = ""

    try:
        anime_obj = AnimeModel.objects.get(id = AnimeModel.objects.latest('id').id)
    except AnimeModel.ObjectDoesNotExist:
        anime_obj = ""

    try:
        faceread_obj = FaceReadModel.objects.get(id = FaceReadModel.objects.latest('id').id)
    except FaceReadModel.ObjectDoesNotExist:
        faceread_obj = ""

    try:
        mosaic_obj = MosaicModel.objects.get(id = MosaicModel.objects.latest('id').id)
    except MosaicModel.ObjectDoesNotExist:
        mosaic_obj = ""

    try:
        facemosaic_obj = FaceMosaicModel.objects.get(id = FaceMosaicModel.objects.latest('id').id)
    except FaceMosaicModel.ObjectDoesNotExist:
        facemosaic_obj = ""

    return render(request, 'index.html', {
        'gray_obj': gray_obj,
        'anime_obj': anime_obj,
        'faceread_obj': faceread_obj,
        'mosaic_obj': mosaic_obj,
        'facemosaic_obj': facemosaic_obj,
    })

##################################################################################################

def grayfunc(request):
    if request.method == 'POST':
        form = GrayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gray')
    else:
        form = GrayForm()
        try:
            gray_obj = GrayModel.objects.get(id = GrayModel.objects.latest('id').id)
            input_path = settings.BASE_DIR + gray_obj.image.url
            input_path = settings.BASE_DIR + gray_obj.image.url
            output_path = settings.BASE_DIR + "/media/output/gray/gray.jpg"
            gray(input_path, output_path)
        except:
            gray_obj = ""
    return render(request, 'gray.html', {
        'form': form,
        'gray_obj': gray_obj,
    })

def gray(input_path, output_path):
    img = cv2.imread(input_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, img_gray)

##################################################################################################

def facereadfunc(request):
    if request.method == 'POST':
        form = FaceReadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('faceread')
    else:
        form = FaceReadForm()
        try:
            faceread_obj = FaceReadModel.objects.get(id = FaceReadModel.objects.latest('id').id)
            input_path = settings.BASE_DIR + faceread_obj.image.url
            output_path = settings.BASE_DIR + "/media/output/faceread/faceread.jpg"
            faceread(input_path, output_path)
        except:
            faceread_obj = ""
    return render(request, 'faceread.html', {
        'form': form,
        'faceread_obj': faceread_obj,
    })

def faceread(input_path, output_path):
    img = cv2.imread(input_path)
    cascade = cv2.CascadeClassifier(settings.CASCADE_FILE_PATH)
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
    for (x, y, w, h) in face:
        faceread_img = cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,200), 3)
    cv2.imwrite(output_path, faceread_img)

##################################################################################################

def animefunc(request):
    if request.method == 'POST':
        form = AnimeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('anime')
    else:
        form = AnimeForm()
        try:
            anime_obj = AnimeModel.objects.get(id = AnimeModel.objects.latest('id').id)
            input_path = settings.BASE_DIR + anime_obj.image.url
            output_path = settings.BASE_DIR + "/media/output/anime/anime.jpg"
            anime(input_path, output_path)
        except:
            anime_obj = ""
    return render(request, 'anime.html', {
        'form': form,
        'anime_obj': anime_obj,
    })

def anime(input_path, output_path):
    img = cv2.imread(input_path)
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
    anime_img = cv2.subtract(img, edge)
    # 結果出力
    cv2.imwrite(output_path, anime_img)

##################################################################################################

def mosaicfunc(request):
    if request.method == 'POST':
        form = MosaicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mosaic')
    else:
        form = MosaicForm()
        try:
            mosaic_obj = MosaicModel.objects.get(id = MosaicModel.objects.latest('id').id)
            input_path = settings.BASE_DIR + mosaic_obj.image.url
            output_path = settings.BASE_DIR + "/media/output/mosaic/mosaic.jpg"
            mosaic(input_path, output_path)
        except:
            mosaic_obj = ""
    return render(request, 'mosaic.html', {
        'form': form,
        'mosaic_obj': mosaic_obj,
    })

def mosaic(input_path, output_path):
    img = cv2.imread(input_path)
    ratio = 0.1
    mosaiced = cv2.resize(img, dsize=None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    h, w = img.shape[:2]
    mosaiced = cv2.resize(mosaiced, dsize=(w, h), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite(output_path, mosaiced)

##################################################################################################

def facemosaicfunc(request):
    if request.method == 'POST':
        form = FaceMosaicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('facemosaic')
    else:
        form = FaceMosaicForm()
        try:
            facemosaic_obj = FaceMosaicModel.objects.get(id = FaceMosaicModel.objects.latest('id').id)
            input_path = settings.BASE_DIR + facemosaic_obj.image.url
            output_path = settings.BASE_DIR + "/media/output/facemosaic/facemosaic.jpg"
            facemosaic(input_path, output_path)
        except:
            facemosaic_obj = ""
    return render(request, 'facemosaic.html', {
        'form': form,
        'facemosaic_obj': facemosaic_obj,
    })

def facemosaic(input_path, output_path):
    img = cv2.imread(input_path)
    cascade = cv2.CascadeClassifier(settings.CASCADE_FILE_PATH)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
    
    def mosaic(img, ratio=0.1):
        mosaiced_img = cv2.resize(img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
        return cv2.resize(mosaiced_img, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
    
    def mosaic_area(img, x, y, w, h, ratio=0.1):
        img[y:y + h, x:x + w] = mosaic(img[y:y + h, x:x + w], ratio)
        return img

    for (x, y, w, h) in face:
        mosaiced_face_img = mosaic_area(img, x, y, w, h)

    cv2.imwrite(output_path, mosaiced_face_img)

##################################################################################################