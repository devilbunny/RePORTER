#! /usr/bin/env python
# ~*~ encoding: utf-8 ~*~
import unittest

from names import split_name


class TestSplitName(unittest.TestCase):

	"Test the ``names.split_name`` function to ensure it works as intended."

	# The test data below is called a "data fixture" because it's fixed ahead of
	# when the test is run. Constant values like the ones below usually get
	# all-caps names. Recall that strings prepended with ``u`` are Unicode and
	# can include characters with accents, Chinese, etc. Otherwise the string is
	# a sequence of raw bytes, where each character stands for one byte, per
	# http://www.asciitable.com.
	NAMES = (u"William Schwartz",
			  "Jillian Foley",
			 u"bLeRdiE flAdElStEiN",
			 u"Pred_alpop Gormer-tin",
			 u"James Van Der Beek",
			 u"Daniel O'Hanlon",
			 u"Piña colada",
			 u"colada Piña",
	)

	EXPECTED = ((u"William",    u"Schwartz"),
				( "Jillian",     "Foley"),
				(u"bLeRdiE",    u"flAdElStEiN"),
				(u"Pred_alpop", u"Gormer-tin"),
				(u"James",      u"Van Der Beek"),
				(u"Daniel",     u"O'Hanlon"),
				(u"Piña",       u"colada"),
				(u"colada",     u"Piña"),
	)

	def test_split_name(self):
		"Test that input matches the expected output."
		output = sorted(split_name(name) for name in self.NAMES)
		self.assertEqual(output, sorted(self.EXPECTED))

	def test_bad_input(self):
		"Test ``split_name`` responds with appropriate errors to bad input."
		for bad_name in 1, 1.0, 1j, [1, 1.0], {1: 1.0}, None:
			# Check that ``split_name(bad_name)`` raises a ``TypeError``.
			self.assertRaises(TypeError, split_name, bad_name)

	def test_None_on_non_matching_strings(self):
		"Test that we return ``None`` on non-matching strings."
		# Sorry, Yao Ming.
		for name in u"姚明", "1234":
			self.assertIsNone(split_name(name))


if __name__ == '__main__':
	unittest.main()
