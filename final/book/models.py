import uuid
from django.db import models

# Create your models here.
class BookJournalBase(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name or 'nolan'


class Book(BookJournalBase):
    num_pages = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Journal(BookJournalBase):
    type = models.CharField(max_length=100, choices=[('0', 'Bullet'), ('1', 'Food'), ('2', 'Travel'), ('3', 'Sport')],
                            default=0)
    publisher = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'