from django.db import models

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlıq")
    content = models.TextField(verbose_name="Məzmun")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma tarixi")

    def __str__(self):
        return self.title

     