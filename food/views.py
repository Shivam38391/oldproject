from multiprocessing import context
from re import template
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .models import Item
from django.template import loader
from .forms import ItemForm

from django.views.generic import CreateView



# Create your views here.
def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list
    }
    
    # return HttpResponse(template.render(context,request)) #another way 
    return render(request, 'food/index.html', context)


def item(request):
    return HttpResponse("This is an item view")


def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    # template = loader.get_template('food/index.html')
    context = {
        'item': item
    }
    
    # return HttpResponse(template.render(context,request)) #another way 
    return render(request, 'food/detail.html', context)


def create_item(request):
    form = ItemForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    context= {
        'form':form
    }
    
    return render(request, 'food/item-form.html', context)

# THIS IS A CLASSED BASED VIEW

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = "food/item-form.html"
    
    def form_valid(self,form):
        form.instance.user_name = self.request.user # user who is curently loged in
        
        
        return super().form_valid(form)
  




def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    context= {
        'form': form,
        'item': item,
    }
    
    return render(request, 'food/item-form.html' , context)


def delete_item(request,id):
    item = Item.objects.get(id=id)
    
    if request.method == 'POST':
        item.delete()
        
        return redirect('food:index')
    
    return render(request,'food/item-delete.html', {'item':item})