import re


# A regular expression is a string like what you see below between the quote
# marks, and the ``re`` module interprets it as a pattern. Each regular
# expression describes a small program that takes another string as input and
# returns information about that string. See
# http://docs.python.org/library/re.html. The ``re`` module provides the
# ``compile`` function, which prepares regex patterns for use in searching input
# strings.
#
# We put an ``r`` before the string so that Python doesn't interpret the
# backslashes before the ``re`` module gets to see them. (E.g., ``\n`` means a
# newline character, so ``\n`` is a single character, not two as they appear in
# the source code.)
#
# The Unicode flag lets us handle words with accented characters.
FIRST_LAST = re.compile(r"(\w*)\s+((?:\w|\s|['-]){2,})", flags=re.UNICODE)


def split_name(name):
	'''Return ("First", "Last") tuple from a string like "First Last".

	``name`` is a string. This function returns a tuple of strings. When a
	non-matching string is encoutered, we return ``None``.
	'''
	match = FIRST_LAST.search(name)
	if match is None:
		return None
	return match.group(1), match.group(2)
