from django.db import models


# classification value objects
CHOICES_CLASSIFICATION = [
	(0, 'unrelated'),
	(1, 'simple'),
	(2, 'complex'),
	(3, 'substring'),
]


class Abbreviation(models.Model):
	long_form = models.TextField(blank=False)
	abbreviation = models.CharField(max_length=100, blank=False)
	classification = models.IntegerField(choices=CHOICES_CLASSIFICATION, null=True)
