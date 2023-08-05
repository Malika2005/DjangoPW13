from django.db import models


class Comment(models.Model):
    sms_id = models.IntegerField()
    comment = models.TextField(null=True)

    def __str__(self):
        return f'{self.comment}'
