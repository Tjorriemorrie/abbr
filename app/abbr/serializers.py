from rest_framework import serializers
from .models import Abbreviation


class AbbreviationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Abbreviation
		fields = ('long_form', 'abbreviation', 'classification')
