from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,

)

# Create your views here.

class BookListView(ListView):
    model = models.Book
    template_name = 'library/book_view.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    
class BookCreateView(CreateView):
    model = models.Book
    template_name = 'library/book_create.html'
    fields = '__all__'
    success_url = '/'
    
class BookUpdateView(UpdateView):
    model = models.Book
    template_name = 'library/book_create.html'
    fields = '__all__'
    success_url = '/'
 
class BookDeleteView(DeleteView):
    model = models.Book
    template_name = 'library/book_delete.html'
    success_url = '/'
    context_object_name = 'book'

def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.error(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'library/register.html', {'form': form})