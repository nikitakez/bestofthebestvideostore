from django.db import models



class Video(models.Model):
    urls = models.URLField()
    title = models.CharField(max_length = 150)
    date = models.DateField(auto_now_add= True)
    descruptions = models.TextField()
    likes = models.PositiveIntegerField(default= 0)


    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment_video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comment")


