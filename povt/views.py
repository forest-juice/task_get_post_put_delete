from django.shortcuts import render
from rest_framework import generics
from .serializers import TextListSerializer, TextDetailSerializer
from povt.models import Order
from django.http import HttpResponseRedirect

class TextListView(generics.ListAPIView):
    serializer_class = TextListSerializer
    queryset = Order.objects.all()

class TextDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TextDetailSerializer
    queryset = Order.objects.all()

def index(request):
    text = request.GET.get("order_text")
    # people = Order.objects.all()
    return render(request, "index.html", {"order_text": text})

def first_page(request):
    if request.method == "POST":
        person = Order()
        person.order_text = request.POST.get("order_text")
        person.save()
    return HttpResponseRedirect("/otvet")

def otvet(request):
    people = Order.objects.all()
    return render(request, "otvet.html", {"people": people})

def get(request):
    order_text = request.GET.get("order_text")
    return render(request, "get.html", {"order_text": order_text})
