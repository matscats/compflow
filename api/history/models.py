from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class History(models.Model):
    subject = models.ForeignKey("subject.Subject", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attended_in_period = models.PositiveSmallIntegerField()
    average = models.DecimalField(max_digits=3, decimal_places=1)

    @property
    def attended_late(self) -> bool:
        return self.attended_in_period > self.subject.period

    @property
    def attended_early(self) -> bool:
        return self.attended_in_period < self.subject.period

    @property
    def attended_correctly(self) -> bool:
        return self.attended_in_period == self.subject.period

    class Meta:
        unique_together = ("subject", "user")
