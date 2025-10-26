# test_primercss.py
"""
Tests for PrimerCSS module.
"""

import unittest
from primercss import PrimerCSS

class TestPrimerCSS(unittest.TestCase):
    """Test cases for PrimerCSS class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimerCSS()
        self.assertIsInstance(instance, PrimerCSS)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimerCSS()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
