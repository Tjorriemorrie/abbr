from django.test import TestCase
from .classifier import Classifier
from profilehooks import profile


class ClassifierTests(TestCase):

	def setUp(self):
		self.data = [
			{
				'abbr': 'RADIUS', 'long_form': 'Remote Authentication Dial In User Service',
				'simple': True, 'complex': True, 'substring': True,
			},
			{
				'abbr': 'TCP/IP', 'long_form': 'Transmission Control Protocol / Internet Protocol',
				'simple': True, 'complex': True, 'substring': True,
			},
			{
				'abbr': 'FedEx', 'long_form': 'Federal Express',
				'simple': False, 'complex': True, 'substring': True,
			},
			{
				'abbr': 'Auspost', 'long_form': 'Australia Post',
				'simple': False, 'complex': True, 'substring': True,
			},
			{
				'abbr': 'frisco', 'long_form': 'San Francisco',
				'simple': False, 'complex': False, 'substring': True,
			},
			{
				'abbr': 'staple', 'long_form': 'Preposterous Examples',
				'simple': False, 'complex': False, 'substring': True,
			},
		]

		self.custom = [
			{
				'abbr': 'ANSI', 'long_form': 'American National Standards Institute',
				'simple': True, 'complex': True, 'substring': True,
			},
			{
				'abbr': 'bit', 'long_form': 'binary digit',
				'simple': False, 'complex': False, 'substring': True,
			},
			{
				'abbr': 'CSV', 'long_form': 'Comma-Separated Values',
				'simple': False, 'complex': False, 'substring': True,
			},
			{
				'abbr': 'DB', 'long_form': 'Database',
				'simple': False, 'complex': False, 'substring': True,
			},
			{
				'abbr': 'ESCON', 'long_form': 'Enterprise Systems Connection',
				'simple': False, 'complex': True, 'substring': True,
			},
			{
				'abbr': 'FTP', 'long_form': 'File Transfer Protocol',
				'simple': True, 'complex': True, 'substring': True,
			},
			{
				'abbr': 'Gimp', 'long_form': 'GNU Image Manipulation Program',
				'simple': True, 'complex': True, 'substring': True,
			},
			{
				'abbr': 'UX', 'long_form': 'User Experience',
				'simple': False, 'complex': False, 'substring': True,
			},
			{
				'abbr': 'XP', 'long_form': 'Cross-Platform',
				'simple': False, 'complex': False, 'substring': False,
			},
		]

	@profile
	def test_is_abbr_correctly_classified(self):
		for item in self.data + self.custom:
			clf = Classifier(item['abbr'], item['long_form'])
			self.assertEqual(clf.isSimple(), item['simple'], item)
			self.assertEqual(clf.isComplex(), item['complex'], item)
			self.assertEqual(clf.isSubstring(), item['substring'], item)
