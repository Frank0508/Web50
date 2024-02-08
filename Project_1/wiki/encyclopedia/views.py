from django.shortcuts import render
from django import forms
from . import util
from django.urls import reverse
from django.http import HttpResponseRedirect

class NewTaskForm(forms.Form):
    search = forms.CharField(label="q")

class NewEntryForm(forms.Form):
    new_entry = forms.CharField(label="New Entry")

def search(request):

    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            if search in util.list_entries():
                return HttpResponseRedirect(reverse("wiki"/search))
            else:
                return render(request, "encyclopedia/search.html", {
                    "form": NewTaskForm(),
                    "entries":util.list_entries()
                })
        else:
            return render(request, "encyclopedia/search.html", {
                "form": form
            })

    return render(request, "encyclopedia/search.html", {
        "form": NewTaskForm(),
    })



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def wiki(request, title):
    return render(request, "encyclopedia/wiki.html", {
        "title": title,
        "entry": util.get_entry(title),
    })

def new(request):
    return render(request, "encyclopedia/new.html", {
        "form": NewEntryForm()
    })

