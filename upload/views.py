from django.views.generic import ListView, CreateView, DeleteView
from .models import File


class FilesListView(ListView):
    model = File
    template_name = 'file_list.html'
    context_object_name = 'files'


class FilesCreateView(CreateView):
    model = File
    fields = ('title', 'editor', 'file')
    template_name = 'home.html'
    success_url = 'files'


class FilesDeleteView(DeleteView):
    model = File
    success_url = '/'

    def get(self, request, *arg, **kwargs):
        return self.post(request, *arg, **kwargs)
