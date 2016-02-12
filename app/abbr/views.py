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
		"""
		data = request.data
		print(data)

		serializer = AbbreviationSerializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		clf = Classifier(**data)
		clf_val = clf.run()

		return Response(serializer.data, status=status.HTTP_200_OK)

