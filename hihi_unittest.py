import unittest
import print_text

class TestHihi(unittest.TestCase):
  def test_print_text(self):
    self.assertEqual(print_text.print_text("Hello, World!"), "Hello, World!")
  

       
if __name__ == "__main__":
  unittest.main()