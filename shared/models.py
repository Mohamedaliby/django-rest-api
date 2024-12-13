from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        db_table = 'Tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'