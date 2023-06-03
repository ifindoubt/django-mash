from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import Client as ClientView, ClientForm

def index(request):
    """View base for index. A redirect"""
    return render(request, template_name="index.html")

def oops(request):
    """View for a 404, an error has occured"""
    if request.method == "POST":
        render(request, template_name="oops.html")

def success(request):
    """View for success or oops-404. A redirect"""
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, template_name="success.html")
    else:
        return redirect(request, oops())

from django.views import generic

class ClientListView(generic.ListView):
    """Generic class for list of clients"""
    model = ClientView
    paginate_by = 5