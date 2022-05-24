import uuid
from django.db import models

class BookJournalBase(models.Model):
    name = models.CharField(max_length=500, null=True)
    price = models.IntegerField(default=0)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Book(BookJournalBase):
    genre = models.CharField(max_length=500, null=True)
    num_pages = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}: {self.title}'

    def check_num_pages(self):
        if self.num_pages > 10:
            return True
        return False

    @classmethod
    def active_books(cls):
        cls.objects.filter(is_active=True)

    @staticmethod
    def compare_books(b1, b2):
        return b1.num_pages > b2.num_pages

    def to_json(self):
        return {
            'id': self.id,
            'is_active': self.is_active
        }

    def to_json_detail(self):
        return {
            'id': self.id,
            'is_active': self.is_active,
            'num_pages': self.num_pages
        }

class Journal(BookJournalBase):
    journal_type_choices = ((1, "Bullet"), (2, "Food"), (3, "Travel"), (4, "Sport"))
    journal_type = models.IntegerField(choices=journal_type_choices, default=1)
    publisher = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}: {self.title}'

    def check_num_pages(self):
        if self.num_pages > 10:
            return True
        return False

    @classmethod
    def active_books(cls):
        cls.objects.filter(is_active=True)

    @staticmethod
    def compare_books(b1, b2):
        return b1.num_pages > b2.num_pages

    def to_json(self):
        return {
            'id': self.id,
            'is_active': self.is_active
        }

    def to_json_detail(self):
        return {
            'id': self.id,
            'is_active': self.is_active,
            'num_pages': self.num_pages
        }

