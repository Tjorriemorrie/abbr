'''
Classifier

Detect if an abbreviation is within the long form:
as a simple, complex or substring representaiton.
'''
import re
import logging

logger = logging.getLogger(__name__)


class Classifier():

	def __init__(self, abbreviation, long_form):
		logger.info(abbreviation)
		logger.info(long_form)
		self.abbreviation = abbreviation.lower()
		self.long_form = long_form.lower()

	def run(self):
		'''
		This method check each method sequentially.

		Considered coroutines, but complex/substring will be True if simple is True,
		not certain it is worth the additional processing. If performance becomes a
		factor then refactor.
		:return: classification
		'''
		print(self.abbreviation)
		print(self.long_form)
		return

	def isSimple(self):
		'''
		Check for simple abbreviation
		(a.k.a. acronyms); the abbreviation if formed by taking the first letter of each word in the list.
		:return: boolean
		'''
		long_form_words = self.long_form.split()
		first_letters = ''.join([w[0] for w in long_form_words])
		return first_letters == self.abbreviation

	def isComplex(self):
		'''
		Check for complex abbreviation
		they consist of one or more letters from the beginning of each word in the list.

		Scenario 1: large chunks (FEDxxx EXxxx) - optimum to search words from abbr backwards
		Scenario 2: small chunks (Fxxx Exxx Dxx) - optimum to search words from abbr forwards
		Scenario 3: mixed chunks (Fxxx Ed Dxx) - how to optimise over brute force?

		Revised:
		nested loops is not efficient. Will build tree structure of all possible
		permutations, loop and hopefully it has good enough performance.


		:return:
		'''
		long_form_words = self.long_form.split()

		# searching backwards
		abbr = self.abbreviation
		for word in long_form_words:
			print('w = ' + word)
			print(abbr)
			word_found = False
			for _ in range(len(abbr), 0, -1):
				print(abbr[:_])
				if word.startswith(abbr[:_]):
					word_found = True
					print('found ' + abbr[:_])
					abbr = abbr[_:]
					break
				if word_found:
					break
			if not word_found:
				return False
		return True

	def isSubstring(self):
		'''
		Check if abbr is a substring of the long form
		they may take any part of any word as long as the letters appear in the original presented order.
		:return:
		'''
		i = 0
		for char in self.abbreviation:
			print(char)
			i = self.long_form.find(char, i)
			print(i)
			if i == -1:
				return False
		return True
