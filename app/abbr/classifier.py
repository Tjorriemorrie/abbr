'''
Classifier

Detect if an abbreviation is within the long form:
as a simple, complex or substring representaiton.
'''
import logging
from .models import CHOICES_CLASSIFICATION

logger = logging.getLogger(__name__)


class Classifier():
	def __init__(self, abbreviation, long_form, **kwargs):
		logger.info(abbreviation)
		logger.info(long_form)
		self.abbreviation = abbreviation.lower()
		self.long_form = long_form.lower()

	def run_sequential(self):
		'''
		This method check each method sequentially.

		Considered coroutines, but complex/substring will be True if simple is True,
		not certain it is worth the additional processing. If performance becomes a
		factor then refactor.

		Considered testing it in reverse, as substring would be true for most
		:return: classification
		'''
		print(self.abbreviation)
		print(self.long_form)
		if self.isSimple():
			return CHOICES_CLASSIFICATION[1][0]
		if self.isComplex():
			return CHOICES_CLASSIFICATION[2][0]
		if self.isSubstring():
			return CHOICES_CLASSIFICATION[3][0]
		return CHOICES_CLASSIFICATION[0][0]

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
		Scenario 3: mixed chunks (Fxxx Ed Dxx) - how to optimise over brute force? (given: of *each* word - d gets captured incorrectly)

		Revised:
		nested loops is not efficient. Will build tree structure of all possible
		permutations, loop and hopefully it has good enough performance.

		Revised:
		Not sure what the big O notation for this is, as the abbr list n is actually
		n! and is stopped when abbr does not startswith.

		:return: boolean
		'''

		def matchAbbrToWord(words, abbr):
			# print('words left', words)

			# get next word from list
			word = words[0]
			# print('next word = ', word)
			# print('abbr left = ', abbr)

			# get abbr possibilities for word
			for _ in range(1, len(abbr) + 1):
				# print('_ ', _)

				abbr_slice = abbr[:_]
				# print('abbr_slice', abbr_slice)

				if not word.startswith(abbr_slice):
					# print('word does not start with abbr_splice, stopping')
					return False

				words_remainder = words[1:]
				abbr_remainder = abbr[_:]

				if not words_remainder and abbr_remainder:
					# print('no more words for abbr left')
					continue

				if not abbr_remainder and words_remainder:
					# print('no more abbr for words left')
					return False

				if not words_remainder and not abbr_remainder:
					# print('all words and abbr matched')
					return True

				# print('abbr matched word start, continuing')
				if matchAbbrToWord(words_remainder, abbr_remainder):
					return True

		return matchAbbrToWord(self.long_form.split(), self.abbreviation)

	def isSubstring(self):
		'''
		Check if abbr is a substring of the long form
		they may take any part of any word as long as the letters appear in the original presented order.
		:return: boolean
		'''
		i = 0
		for char in self.abbreviation:
			# print(char)
			i = self.long_form.find(char, i)
			# print(i)
			if i == -1:
				return False
		return True
