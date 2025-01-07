from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUser


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def result(self):
        total_votes = self.total_votes

        if total_votes == 0:
            return {
                'result': None
            }

        left_votes = self.votes.filter(value=-1).count()
        right_votes = self.votes.filter(value=1).count()

        if total_votes > 0:
            left_percentage = (left_votes / total_votes) * 100
            right_percentage = (right_votes / total_votes) * 100
        else:
            left_percentage = right_percentage = 0

        if left_percentage > right_percentage:
            result = 'left'
        elif right_percentage > left_percentage:
            result = 'right'
        else:
            result = 'tie'

        return {
            'left': left_percentage,
            'right': right_percentage,
            'result': result,
        }

    @property
    def total_votes(self):
        total_votes = self.votes.count()
        return total_votes if total_votes else 0

    def __str__(self):
        return self.name


class Vote(models.Model):

    class VoteChoices(models.IntegerChoices):
        LEFT = -1, _('Left winged')
        RIGHT = 1, _('Right winged')

    subject = models.ForeignKey(Subject, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='votes', on_delete=models.CASCADE)
    value = models.IntegerField(max_length=2, choices=VoteChoices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} voted {self.value} for {self.subject.name}'

    class Meta:
        unique_together = ('subject', 'user',)
