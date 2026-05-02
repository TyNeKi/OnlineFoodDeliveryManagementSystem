from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm, OrderItemForm, TempUserForm
from django.views import View

from .models import TempUser


# Create your views here.
class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        if 'user' in request.session:
            return redirect('/home/')
        return render(request, self.template_name)

    def post(self, request):
        msg = ''

        uname = request.POST['username']
        pwd = request.POST['password']

        try:
            user = TempUser.objects.get(username=uname, password=pwd)

            request.session['user'] = user.username
            return redirect('/home/')

        except TempUser.DoesNotExist:
            msg = 'Invalid username and/or password.'

        return render(request, self.template_name, context={'msg': msg})

class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        if 'user' not in request.session:
            return redirect('/')

        return render(request, self.template_name)

class LogoffView(View):

    def get(self, request):
        request.session.flush()
        return redirect('index')


class EditProfileView(View):
    template_name = 'editProfile.html'

    def get(self, request):
        username = request.session['user']
        user = get_object_or_404(TempUser, username=username)
        form = TempUserForm(instance=user)

        return render(request, self.template_name, context={'form':form})

    def post(self, request):
        username = request.session['user']
        user = get_object_or_404(TempUser, username=username)
        form = TempUserForm(request.POST, instance=user)

        if form.is_valid():
            update_user = form.save(commit=False)

            if form.cleaned_data['password']:
                update_user.password=form.cleaned_data['password']

            update_user.save()

            return redirect('/home/')

        return render(request, self.template_name, context={'form':form})

class AddNewOrderView(View):
    template_name = 'addNewOrder.html'

    def get(self, request):
        order_form = OrderForm()
        item_form = OrderItemForm()

        return render(request, self.template_name, {
            'order_form': order_form,
            'item_form': item_form
        })

    def post(self, request):
        order_form = OrderForm(request.POST)
        item_form = OrderItemForm(request.POST)

        if order_form.is_valid() and item_form.is_valid():
            order = order_form.save()

            item = item_form.save(commit=False)
            item.orderID = order
            item.save()

            return redirect('/orders/')

        return render(request, self.template_name, {
            'order_form': order_form,
            'item_form': item_form
        })