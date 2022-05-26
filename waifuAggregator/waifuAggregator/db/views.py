from django.shortcuts import render, redirect
from .models import pegs
from .forms import pegsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def db(request):
    peges = pegs.objects.all()
    return render(request, 'db/db.html', {'peges': peges})

class PegsDetailView(DetailView):
    model = pegs
    template_name = 'db/details_view.html'
    context_object_name = 'peg'

class PegsUpdateView(UpdateView):
    model = pegs
    template_name = 'db/create.html'
    form_class = pegsForm

class PegsDeleteView(DeleteView):
    model = pegs
    success_url = '/db'
    template_name = 'db/db_delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = pegsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('db_home')
        else:
            error = 'Error input'

    form = pegsForm()
    return render(request, 'db/create.html', {'form': form, 'error': error})