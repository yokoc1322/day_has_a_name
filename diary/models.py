from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

MAX_TITLE_LEN = 50
MAX_CONTENT_LEN = 2000
MAX_STATUS_LEN = 20


class Writer(AbstractUser):
    def get_absolute_url(self):
        return reverse("diary:writer-detail", kwargs={"pk": self.pk})


class Record(models.Model):
    STATE_GREAT = 'great'
    STATE_GOOD = 'good'
    STATE_BAD = 'bad'
    STATES = [
        (STATE_GREAT, 'great'),
        (STATE_GOOD, 'good'),
        (STATE_BAD, 'bad'),
    ]

    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    title = models.CharField(max_length=MAX_TITLE_LEN)
    content = models.TextField(max_length=MAX_CONTENT_LEN)
    date = models.DateField()
    status = models.CharField(max_length=MAX_STATUS_LEN,
                              choices=STATES, default=STATE_GOOD)

    class Meta:
        ordering = ["date"]

    def get_absolute_url(self):
        return reverse("diary:record-detail", kwargs={"pk": self.pk})
