from django.db import models
from django.utils.safestring import mark_safe



class Video(models.Model):
    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "много видео"


    slug = models.SlugField(unique=True, verbose_name="СЛАГ", help_text="слаг должен быть уникальным")
    urls = models.URLField(verbose_name="Урл")
    title = models.CharField(max_length = 150, verbose_name="Название")
    date = models.DateField(auto_now_add= True, verbose_name="Дата")
    descruptions = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True)
    likes = models.PositiveIntegerField(default= 0, verbose_name="Нравится")



    def __str__(self):
        return self.title

    @property
    def test(self):
        return f"hello{self.title},{self.likes **2}"

    @property
    def tv(self):
        return mark_safe(f"<iframe width='100' height='50' src='{self.urls }'></iframe>")

class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment_video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comment")


