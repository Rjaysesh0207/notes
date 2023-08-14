from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Notes

# Create your views here.


class NotesList(ListView):
    model = Notes
    fields = "__all__"


class NotesDetail(DetailView):
    model = Notes


class NoteCreate(CreateView):
    model = Notes
    fields = "__all__"
    success_url = "/notes"


class NoteUpdate(UpdateView):
    model = Notes
    fields = "__all__"


class NoteDelete(DeleteView):
    model = Notes
    success_url = "/notes"
