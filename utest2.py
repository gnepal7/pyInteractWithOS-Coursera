import re
# from rearrange import rearrange_name

def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  return "{} {}".format(result[2], result[1])

import unittest
class TestRearrange(unittest.TestCase):
    
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)

# Run the tests
unittest.main()
