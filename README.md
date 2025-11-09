# cyphers
playing with python to create and decode cyphers

## UTF-8 to Binary Converter

A Python script that converts text strings to their binary representation using UTF-8 encoding.

### Features

- Converts any UTF-8 compatible string to binary
- Supports ASCII, Unicode, emojis, and special characters
- Provides verbose mode for detailed conversion information
- Fully documented with Google Style docstrings
- Comprehensive unit test coverage

### Usage

Basic usage:
```bash
python3 utf8_to_binary.py "Hello World"
```

Verbose mode:
```bash
python3 utf8_to_binary.py "Hello World" --verbose
```

Get help:
```bash
python3 utf8_to_binary.py --help
```

### Examples

```bash
# Simple ASCII text
$ python3 utf8_to_binary.py "A"
01000001

# Unicode characters
$ python3 utf8_to_binary.py "€"
111000101000001010101100

# Emoji
$ python3 utf8_to_binary.py "😀"
11110000100111111001100010000000

# Verbose output
$ python3 utf8_to_binary.py "Hello" --verbose
Input string: Hello
UTF-8 bytes: 48 65 6c 6c 6f
Number of bytes: 5
Binary length: 40 bits
Binary output: 0100100001100101011011000110110001101111
```

### Testing

Run the unit tests:
```bash
python3 -m unittest test_utf8_to_binary.py -v
```

### Implementation Details

The script uses Python's built-in `encode()` method to convert strings to UTF-8 bytes, then formats each byte as an 8-bit binary string. This approach:
- Uses standard library functions (no external dependencies)
- Follows Python best practices
- Handles all Unicode characters properly
- Is well-documented with Google Style docstrings
