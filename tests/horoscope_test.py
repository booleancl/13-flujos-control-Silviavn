import unittest
from unittest.mock import patch
from io import StringIO
import importlib
import sys

class TestSuite(unittest.TestCase):
    fake_out=StringIO()

    @patch("builtins.input", side_effect=["Aries"])
    @patch("sys.stdout", fake_out)
    def test_horoscope_aries(self, mock_input):

        import src.horoscope
        output = TestSuite.fake_out.getvalue() 

        assert "You will find it easy to persuade people to follow your lead today but can you be sure you are doing the right thing? A testing Jupiter-Pluto link warns if you take too much for granted and make a mistake the powers that be will not be amused.\n" in output
     

    @patch("builtins.input", side_effect=["leo"])
    @patch("sys.stdout", fake_out)
    def test_horoscope_leo(self, mock_input):
        
        importlib.reload(sys.modules['src.horoscope'])
        output = TestSuite.fake_out.getvalue()

        assert "Jupiter’s influence in the career area of your chart means you are desperate to prove yourself, but as power planet Pluto is strong as well you must tread carefully when dealing with employers and senior colleagues. They could see you as a threat.\n" in output
   
    @patch("builtins.input", side_effect=["VIRGO"])
    @patch("sys.stdout", fake_out)
    def test_horoscope_virgo(self, mock_input):
        
        importlib.reload(sys.modules['src.horoscope'])

        output = TestSuite.fake_out.getvalue()  
        
        assert "The message of the stars is that you need to back off a bit and let things develop at their own pace. A whole new world of possibilities is about to open up for you but if your mind is all over the place you could easily miss them!\n" in output
        
   
    @patch("builtins.input", side_effect=["Whatever"])
    @patch("sys.stdout", fake_out)
    def test_horoscope_not_found(self, mock_input):
        
        importlib.reload(sys.modules['src.horoscope'])

        output = TestSuite.fake_out.getvalue()  
        assert "Sign not found. ¡Tell me a valid option!\n" in output
