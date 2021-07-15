from application.models import Cliente
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()

class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('application:list')

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('application:list')

class ClienteDetail(DetailView):
    model = Cliente
    queryset = Cliente.objects.all()

class ClienteDelete(DeleteView):
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('application:list')