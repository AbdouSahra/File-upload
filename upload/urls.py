from django.urls import path
from .views import FilesListView, FilesCreateView, FilesDeleteView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', FilesCreateView.as_view(), name='home'),
    path('files/', FilesListView.as_view(), name='files'),
    path('files/<int:pk>', FilesDeleteView.as_view(), name='delete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
