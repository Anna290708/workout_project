from django.db import models
from django.conf import settings

class Quote(models.Model):
    text = models.TextField(unique=True)

    def __str__(self):
        return self.text


class UserQuoteHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    seen_count = models.PositiveIntegerField(default=1)
    last_seen = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('user', 'quote')

    def __str__(self):
        return f"{self.user.email} - {self.quote.text[:30]}"
