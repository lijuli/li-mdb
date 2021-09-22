from textwrap import shorten

from django.db import models

from api.models.title import Title
from users.models import CustomUser


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='title',
        help_text='add a title item'
    )
    text = models.TextField(
        'review text',
        help_text='enter your review here'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='author'
    )
    score = models.PositiveSmallIntegerField(
        'review score',
        help_text='enter your review score'
    )
    pub_date = models.DateTimeField(
        'date published',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        app_label = 'api'
        verbose_name = 'reviews'
        ordering = ('-pub_date',)

    def __str__(self):
        shorten_review_text = shorten(self.text, width=10, placeholder='...')
        return f'[{self.title}]: {shorten_review_text}'
