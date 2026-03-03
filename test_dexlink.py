# test_dexlink.py
"""
Tests for DexLink module.
"""

import unittest
from dexlink import DexLink

class TestDexLink(unittest.TestCase):
    """Test cases for DexLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DexLink()
        self.assertIsInstance(instance, DexLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DexLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
