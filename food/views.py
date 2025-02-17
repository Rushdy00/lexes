from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

# Create your views here.
def index(request):
    item_list = Item.objects.all()  # Fetch all items from the database
    context = {
        'item_list': item_list,  # Pass the item list to the template
    }
    return render(request, 'food/index.html', context)  # Render the template with context

def item(request):
    return HttpResponse('This is an item view')
