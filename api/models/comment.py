from textwrap import shorten

from django.db import models

from api.models.review import Review
from users.models import CustomUser


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='review',
        help_text='add a comment'
    )
    text = models.TextField(
        'comment text',
        help_text='enter your comment here'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='author'
    )
    pub_date = models.DateTimeField(
        'date published',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        app_label = 'api'
        verbose_name = 'comments'
        ordering = ('-pub_date',)

    def __str__(self):
        shorten_comment_text = shorten(self.text, width=10, placeholder='...')
        return f'[{self.review}] : {shorten_comment_text}'
