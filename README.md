# Regex Validator

A comprehensive Python utility for extracting and validating various data types from text using regular expressions. This tool supports multiple data formats including emails, URLs, phone numbers, credit cards, times, HTML tags, hashtags, and currency amounts.

**Author:** Okechukwu Wisdom Ikechukwu  
**Created:** 2025  
**Version:** 2.0.0

## 🚀 Features

- **Interactive CLI** with comprehensive input validation
- **Robust regex patterns** for common data types
- **Cross-platform compatibility** (Windows, macOS, Linux)
- **Comprehensive error handling** and input validation
- **Type-safe validation** with detailed error messages
- **Extensive test coverage** with real-world examples

## 📋 Supported Data Types

| Data Type | Examples | Validation Rules |
|-----------|----------|------------------|
| **Emails** | `user@example.com`, `firstname.lastname@company.co.uk` | RFC 5322 compliant |
| **URLs** | `https://www.example.com`, `http://api.example.org/path` | HTTP/HTTPS protocols |
| **Phone Numbers** | `(123) 456-7890`, `123-456-7890`, `123.456.7890` | US format with separators |
| **Credit Cards** | `1234 5678 9012 3456`, `1234-5678-9012-3456` | 16 digits with separators |
| **Time** | `14:30`, `2:30 PM`, `09:15` | 24h and 12h formats |
| **HTML Tags** | `<div>`, `<p class="example">`, `<img src="image.jpg">` | Opening tags with attributes |
| **Hashtags** | `#example`, `#ThisIsAHashtag`, `#123test` | Social media style tags |
| **Currency** | `$19.99`, `$1,234.56`, `$100` | US dollar format |

## 🛠️ Installation

### Prerequisites
- Python 3.9 or higher
- No external dependencies required

### Setup
1. Clone or download the project folder
2. Navigate to the project directory
3. Run the tool directly

```bash
# Navigate to project directory
cd alu_regex-data-extraction-owizdom

# Run the interactive tool
python alu_regex_data_extraction.py
```

## 🎯 Usage

### Interactive CLI
Run the main script for an interactive validation experience:

```bash
python alu_regex_data_extraction.py
```

The tool will display a menu with options for each data type. Each option includes:
- **Input validation** with type checking
- **Error handling** for invalid inputs
- **Retry loops** until valid input is provided
- **Clear feedback** on validation results

## 🚨 Error Handling

The tool includes comprehensive error handling:

- **Input validation** with type checking
- **Retry loops** for invalid inputs
- **Clear error messages** with suggestions
- **Graceful handling** of edge cases
- **Keyboard interrupt** support (Ctrl+C)

### Error Examples
```
Error: Email cannot be purely numeric. Please enter a valid email address.
Error: Phone number must contain digits. Please enter a valid phone number.
Error: URL should start with 'http://', 'https://', or 'www.' or contain a domain.
Error: Credit card number must contain digits. Please enter a valid credit card number.
```

## 📁 Project Structure

```
# ├── core/
# │   ├── extractors.py        # extract_all function
# │   ├── regex_patterns.py    # Regex patterns
# ├── main.py                  # Entry point
# ├── README.md
# ├── requirements.txt
# └── .gitignore
```

## 🔍 Regex Patterns

### Email Pattern
```regex
\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b
```
- Local part: letters, numbers, dots, underscores, %, +, -
- Domain: letters, numbers, dots, hyphens
- TLD: 2+ letters

### Phone Pattern
```regex
^(?:\(\d{3}\)\s*\d{3}[-.]\d{4}|\d{3}[-.]\d{3}[-.]\d{4})$
```
- Supports: (123) 456-7890, 123-456-7890, 123.456.7890
- Requires consistent separators

### URL Pattern
```regex
\bhttps?://(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}(?:/[^\s]*)?\b
```
- HTTP/HTTPS protocols only
- Domain with TLD required
- Optional path/query/fragment

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional data types (IP addresses, dates, SSNs)
- International phone number formats
- Enhanced regex patterns
- Performance optimizations
- Additional test cases

## 📄 License

This project is provided as-is without warranty. You may adapt for personal or organizational use.

## 🎓 Learning Outcomes

This project demonstrates:
- **Regex pattern design** and optimization
- **Input validation** and error handling
- **Object-oriented programming** with dataclasses
- **Type hints** and documentation
- **Test-driven development** practices
- **User experience** design for CLI tools
- **Code organization** and modularity

---

**Created by:** Okechukwu Wisdom Ikechukwu  
**Institution:** ALU (African Leadership University)  
**Year:** 2025
