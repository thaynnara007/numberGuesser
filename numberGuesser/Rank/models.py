from django.db import models


class Rank(models.Model):
    name = models.CharField(max_length=150)
    attempts = models.IntegerField()
    number_guessed = models.IntegerField()
    time = models.IntegerField()

    def __str__(self):
        return "{}, steps: {}, number: {}, time: {}".format(
            self.name,
            self.attempts,
            self.number_guessed,
            self.time
        )
