from django.db import models


class File(models.Model):
    title = models.CharField(max_length=100)
    editor = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='files/zip')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
