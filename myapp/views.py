import os
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
            
    images = Image.objects.all()
    return render(request, 'myapp/index.html', {'images':images, 'form':form})
    
def delete_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)

    # delete photo from static folder i.e. from media
    if os.path.exists(image.photo.path):
        os.remove(image.photo.path)

    image.delete()
    return redirect('home')