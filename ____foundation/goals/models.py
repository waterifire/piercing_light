from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Goal(models.Model):
    priority_choices = (
        (1, 1),
        (2, 2),
        (3, 3)
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    all_users = models.ManyToManyField(User, related_name="all_users", blank=True)

    # What user will see
    name = models.CharField(max_length=50, blank=True, null=True)
    priority = models.IntegerField(choices=priority_choices, help_text="low(1), medium(2) or high(3)")
    description = models.CharField(max_length=50, blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)


    #times
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    # will add pastor jimeneze list here
    # it will be under advanced goal setting
    # quater1 =
    # quater2 =
    # quater3 =
    # quater4 =


    def __str__(self):
        return self.name
