#!/usr/bin/env python3
"""Convert strings to binary sequences based on UTF-8 encoding.

This module provides functionality to convert text strings into their binary
representation using UTF-8 encoding. Each character is converted to its UTF-8
byte representation, and then each byte is converted to its 8-bit binary form.

Example:
    $ python utf8_to_binary.py "Hello"
    0100100001100101011011000110110001101111

    $ python utf8_to_binary.py "世界"
    111001011000100010010110111001011011000010000010
"""

import argparse
import sys


def string_to_binary(text: str) -> str:
    """Convert a string to its binary representation using UTF-8 encoding.

    This function takes a string and converts each character to its UTF-8 byte
    representation, then converts each byte to an 8-bit binary string. The
    resulting binary strings are concatenated together.

    Args:
        text: The input string to convert to binary. Can contain any Unicode
            characters supported by UTF-8 encoding.

    Returns:
        A string containing the binary representation of the input text, where
        each character is represented by one or more 8-bit binary sequences
        (depending on UTF-8 encoding).

    Raises:
        UnicodeEncodeError: If the string contains characters that cannot be
            encoded in UTF-8 (extremely rare, as UTF-8 supports all Unicode).

    Examples:
        >>> string_to_binary("A")
        '01000001'
        >>> string_to_binary("AB")
        '0100000101000010'
        >>> string_to_binary("€")
        '111000101000001010101100'
    """
    # Encode the string to UTF-8 bytes
    utf8_bytes = text.encode('utf-8')
    
    # Convert each byte to its 8-bit binary representation
    binary_string = ''.join(format(byte, '08b') for byte in utf8_bytes)
    
    return binary_string


def main() -> int:
    """Parse command-line arguments and convert the input string to binary.

    This function serves as the entry point for the script when run from the
    command line. It sets up argument parsing, processes the input string,
    and outputs the binary representation.

    Returns:
        Exit code: 0 for success, 1 for errors.

    Examples:
        $ python utf8_to_binary.py "Hello World"
        010010000110010101101100011011000110111100100000010101110110111101110010011011000110010000001010
    """
    parser = argparse.ArgumentParser(
        description='Convert a string to binary sequence using UTF-8 encoding.',
        epilog='Example: %(prog)s "Hello World"'
    )
    parser.add_argument(
        'text',
        type=str,
        help='The text string to convert to binary'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Display additional information about the conversion'
    )
    
    args = parser.parse_args()
    
    try:
        # Convert the input string to binary
        binary_result = string_to_binary(args.text)
        
        if args.verbose:
            # Display verbose output with additional information
            utf8_bytes = args.text.encode('utf-8')
            print(f"Input string: {args.text}")
            print(f"UTF-8 bytes: {' '.join(f'{b:02x}' for b in utf8_bytes)}")
            print(f"Number of bytes: {len(utf8_bytes)}")
            print(f"Binary length: {len(binary_result)} bits")
            print(f"Binary output: {binary_result}")
        else:
            # Standard output: just the binary string
            print(binary_result)
        
        return 0
    
    except UnicodeEncodeError as e:
        print(f"Error: Unable to encode the string to UTF-8: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
