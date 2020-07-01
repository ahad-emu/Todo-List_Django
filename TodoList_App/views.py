from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import List
from .forms import FormList
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "apps/home.html")

def about(request):
    return render(request, "apps/about.html")

def show_list(request):
        all_info = List.objects.all()
        return render(request, "apps/show_list.html", {'all_information': all_info})

def insert_item(request):
    return render(request, "apps/insert.html")

def insert(request):
    if request.method == 'POST':
        form = FormList(request.POST)
        if form.is_valid() :
            form.save()
            messages.info(request, ("Item has been added"))
            return show_list(request)
        else:
            return HttpResponse("something wrong!!!!!")
    else:
        return render(request, "apps/insert.html")


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.error(request, ("item has been deleted"))
    return redirect("show_list")

def edit(request,list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = FormList(request.POST, instance=item)
        if form.is_valid() :
            form.save()
            messages.success(request, ("Item has been edited"))
            return show_list(request)
        else:
            return HttpResponse("something wrong!!!!!")
    else:
        item = List.objects.get(pk=list_id)
        return render(request, "apps/edit.html", {'item': item})
