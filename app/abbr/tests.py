from django.test import TestCase
from .classifier import Classifier


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
			}
		]

	def test_is_abbr_correctly_classified(self):
		for item in self.data:
			clf = Classifier(item['abbr'], item['long_form'])
			# self.assertEqual(clf.isSimple(), item['simple'], item)
			self.assertEqual(clf.isComplex(), item['complex'], item)
			# self.assertEqual(clf.isSubstring(), item['substring'], item)
