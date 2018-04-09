from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView,TemplateView
from . import forms

from demo import Hand
import numpy as np

def text(request):
    return render(request,'text.html')

def create(request):
    lines=None
    if request.method=="GET":
        lines = [request.GET.get('sentence')]
        biases = [.75 for i in lines]
        styles = [9 for i in lines]
        hand = Hand()
        hand.write(
            filename='templates/out.svg',
            lines=lines,
            biases=biases,
            styles=styles,
            )
        return render(request,'created.html')
