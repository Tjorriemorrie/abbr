from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Abbreviation
from .serializers import AbbreviationSerializer
import logging
from abbr.classifier import Classifier

logger = logging.getLogger(__name__)


@permission_classes((permissions.AllowAny,))
class AbbreviationCtrl(APIView):
	def post(self, request):
		"""
		List all code snippets, or create a new snippet.
		@todo ensure handling of FormData. I see on the web view at
		http://127.0.0.1:8000/abbr/classify that the OPTIONS are generated
		out of the box as well as the parser can parse  "multipart/form-data".
		"""
		data = dict(request.data)
		print(data)
		# @todo investigate why values are lists
		data['abbreviation'] = data['abbreviation'][0]
		data['long_form'] = data['long_form'][0]
		print(data)

		serializer = AbbreviationSerializer(data=data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		clf = Classifier(**serializer.data)
		data['classification'] = clf.run_sequential()
		print('data w clf', data)

		serializer = AbbreviationSerializer(data=data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(serializer.data, status=status.HTTP_200_OK)

