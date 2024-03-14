from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField(timezone.now())

    def __str__(self):
        self.title

    class Meta:
        db_table="news"


