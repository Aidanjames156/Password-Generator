# Password Generator

A simple and secure desktop password generator built with Python and Tkinter. Generate strong, customizable passwords with an intuitive graphical interface.

## Features

- **Customizable Length**: Generate passwords from 4 to 64 characters
- **Character Type Selection**: Choose from lowercase, uppercase, numbers, and symbols
- **Ambiguous Character Exclusion**: Option to exclude similar-looking characters (0, O, l, 1, I)
- **Real-time Password Strength**: Visual indicator showing password strength
- **One-click Copy**: Copy generated passwords to clipboard instantly
- **Modern Dark Theme**: Clean, professional interface

## Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually included with Python)

### Setup
1. Clone this repository:
```bash
git clone https://github.com/Aidanjames156/Password-Generator.git
cd Password-Generator
```

2. Run the application:
```bash
python main.py
```

## Usage

1. **Set Password Length**: Use the slider to choose your desired password length (4-64 characters)

2. **Select Character Types**: Check the boxes for the types of characters you want to include:
   - Lowercase letters (a-z)
   - Uppercase letters (A-Z)
   - Numbers (0-9)
   - Symbols (!@#$%...)

3. **Exclude Similar Characters** (Optional): Check this option to avoid confusing characters like 0/O and 1/l

4. **Generate Password**: Click "Generate New" or adjust any setting to automatically generate a new password

5. **Copy Password**: Click the "Copy" button to copy the password to your clipboard

6. **Check Strength**: The strength indicator shows how secure your password is (Weak, Medium, Strong, Very Strong)

## Password Strength Criteria

The strength indicator evaluates passwords based on:
- **Length**: 8+ characters (1 point), 12+ characters (2 points)
- **Character Variety**: Each character type adds 1 point
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Symbols

**Strength Levels:**
- 🔴 **Weak**: 0-1 points
- 🟠 **Medium**: 2-3 points
- 🟡 **Strong**: 4-5 points
- 🟢 **Very Strong**: 6+ points

## Security Features

- Uses Python's `random.choice()` for cryptographically secure random generation
- No password storage - generates fresh passwords each time
- Option to exclude ambiguous characters for better readability
- Real-time strength analysis

## File Structure

```
Password-Generator/
├── main.py              # Main application file
├── README.md            # This file
```

## Requirements

- Python 3.6+
- tkinter (standard library)
- random (standard library)
- string (standard library)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Aidan James** - [Aidanjames156](https://github.com/Aidanjames156)

## Acknowledgments

- Built with Python's Tkinter library
---
