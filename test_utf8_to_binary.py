#!/usr/bin/env python3
"""Unit tests for utf8_to_binary module.

This module contains unit tests for the string_to_binary function to ensure
correct conversion of various types of strings to their binary representation
using UTF-8 encoding.
"""

import unittest
from utf8_to_binary import string_to_binary


class TestStringToBinary(unittest.TestCase):
    """Test cases for the string_to_binary function.
    
    This test suite validates the conversion of strings to binary sequences
    using UTF-8 encoding for various input types including ASCII, Unicode,
    and special characters.
    """

    def test_single_ascii_character(self):
        """Test conversion of a single ASCII character.
        
        The letter 'A' (ASCII 65) should convert to '01000001'.
        """
        result = string_to_binary('A')
        self.assertEqual(result, '01000001')

    def test_multiple_ascii_characters(self):
        """Test conversion of multiple ASCII characters.
        
        The string 'AB' should produce two 8-bit sequences.
        """
        result = string_to_binary('AB')
        self.assertEqual(result, '0100000101000010')

    def test_word_hello(self):
        """Test conversion of the word 'Hello'.
        
        Each character in 'Hello' should be properly converted to binary.
        """
        result = string_to_binary('Hello')
        expected = '0100100001100101011011000110110001101111'
        self.assertEqual(result, expected)

    def test_empty_string(self):
        """Test conversion of an empty string.
        
        An empty string should produce an empty binary string.
        """
        result = string_to_binary('')
        self.assertEqual(result, '')

    def test_space_character(self):
        """Test conversion of a space character.
        
        A space (ASCII 32) should convert to '00100000'.
        """
        result = string_to_binary(' ')
        self.assertEqual(result, '00100000')

    def test_unicode_euro_symbol(self):
        """Test conversion of Unicode character (Euro symbol).
        
        The Euro symbol '€' (U+20AC) is encoded as E2 82 AC in UTF-8,
        which should produce a 24-bit binary sequence.
        """
        result = string_to_binary('€')
        self.assertEqual(result, '111000101000001010101100')
        # Verify the length is 24 bits (3 bytes * 8 bits)
        self.assertEqual(len(result), 24)

    def test_unicode_chinese_characters(self):
        """Test conversion of Chinese characters.
        
        Chinese characters require 3 bytes each in UTF-8 encoding.
        """
        result = string_to_binary('世')
        # '世' is encoded as E4 B8 96 in UTF-8
        self.assertEqual(len(result), 24)  # 3 bytes * 8 bits
        self.assertEqual(result, '111001001011100010010110')

    def test_unicode_emoji(self):
        """Test conversion of an emoji character.
        
        Emojis are typically 4-byte UTF-8 sequences.
        """
        result = string_to_binary('😀')
        # Emoji takes 4 bytes in UTF-8
        self.assertEqual(len(result), 32)  # 4 bytes * 8 bits
        self.assertEqual(result, '11110000100111111001100010000000')

    def test_mixed_ascii_and_unicode(self):
        """Test conversion of mixed ASCII and Unicode characters.
        
        Strings with both ASCII and Unicode should be properly handled.
        """
        result = string_to_binary('A€')
        # 'A' is 1 byte (8 bits), '€' is 3 bytes (24 bits)
        self.assertEqual(len(result), 32)  # 1 + 3 bytes = 32 bits

    def test_numbers_as_string(self):
        """Test conversion of numeric string.
        
        Numeric characters should be converted like any other ASCII character.
        """
        result = string_to_binary('123')
        # '1' = 49, '2' = 50, '3' = 51 in ASCII
        expected = '001100010011001000110011'
        self.assertEqual(result, expected)

    def test_special_characters(self):
        """Test conversion of special characters.
        
        Special characters like newline should be properly encoded.
        """
        result = string_to_binary('\n')
        # Newline is ASCII 10
        self.assertEqual(result, '00001010')

    def test_result_is_string(self):
        """Test that the result is always a string type.
        
        The function should return a string containing only '0' and '1'.
        """
        result = string_to_binary('test')
        self.assertIsInstance(result, str)
        # Verify it contains only binary digits
        self.assertTrue(all(c in '01' for c in result))

    def test_binary_length_is_multiple_of_eight(self):
        """Test that binary output length is always a multiple of 8.
        
        Since UTF-8 encodes in bytes (8 bits), the output should always
        be divisible by 8.
        """
        test_strings = ['A', 'Hello', '世界', '😀🎉', '']
        for text in test_strings:
            result = string_to_binary(text)
            self.assertEqual(len(result) % 8, 0,
                           f"Binary length for '{text}' is not a multiple of 8")


if __name__ == '__main__':
    unittest.main()
