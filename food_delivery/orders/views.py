from django.shortcuts import render, redirect
from .forms import OrderForm, OrderItemForm
from .models import Order


# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_new_order(request):
    order_form = OrderForm(request.POST or None)
    item_form = OrderItemForm(request.POST or None)

    if request.method == 'POST':
        if order_form.is_valid() and item_form.is_valid():
            order = order_form.save()

            item = item_form.save(commit=False)
            item.orderID = order
            item.save()

            return redirect('/orders/')

    return render(request, 'addNewOrder.html', {
        'order_form': order_form,
        'item_form': item_form
    })