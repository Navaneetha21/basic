from django.shortcuts import render,redirect
from .models import News
from .forms import NewsForm

# Create your views here.
def home(request):
    list = News.objects.all()
    return render(request, 'home.html', {'newlist': list})

def add_news(request):
    print("KK")
    print(request.method)
    if request.method == "POST":
        titleww = request.POST.get("title")
        contentww = request.POST.get("content")
        pub_dateww = request.POST.get("pub_date")
        print(titleww, contentww, pub_dateww)
        data = News()
        data.title = titleww
        data.content = contentww
        data.pub_date = pub_dateww
        data.save()
        return redirect("/")

    return render(request, 'add_news.html')
