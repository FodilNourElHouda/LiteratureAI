import unittest
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # add the parent to the search path

from app.core.config import settings

class MyTestCase(unittest.TestCase):
    def test_project_name_and_version(self):
        self.assertEqual(settings.PROJECT_NAME, "Litterature RAG")
        self.assertIsInstance(settings.VERSION, str)


if __name__ == '__main__':
    unittest.main()
