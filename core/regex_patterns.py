import re
from dataclasses import dataclass
from typing import List, Pattern

@dataclass(frozen=True)
class RegexValidator:
    """
    A data class representing a regex validator with pattern matching capabilities.
    """
    name: str
    pattern: Pattern[str]

    def find_all(self, text: str) -> List[str]:
        if not isinstance(text, str):
            raise TypeError("Input text must be a string")
        return [match.group(0) for match in self.pattern.finditer(text)]

    def is_match(self, text: str) -> bool:
        if not isinstance(text, str):
            raise TypeError("Input text must be a string")
        return bool(self.pattern.fullmatch(text))


# Email
EMAIL_PATTERN = re.compile(r"""
\b  #local part \b
[A-Za-z0-9._%+-]+ #letters, numbers, dots, underscores, %, +, -
@  #at
[A-Za-z0-9.-]+  #domain/subdomains
\.[A-Za-z]{2,}  #TLD \b
\b
""", re.VERBOSE)

# # URLs (http/https, domain with TLD, optional path)
URL_PATTERN = re.compile(r"""
\b
https?:\/\/ #scheme
(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,} #host
(?:\/[\w\-\.%~:?#\[\]@!$&'()*+,;=]*)? #optional path/query/fragment
\b #optional path/query/fragment \b
""", re.VERBOSE)

# Phones
PHONE_PATTERN = re.compile(r"^(?:\(\d{3}\)\s*\d{3}[-.]\d{4}|\d{3}[-.]\d{3}[-.]\d{4})$") #(123) 456-7890 | 123-456-7890 | 123.456.7890

# Credit Cards
CREDIT_CARD_PATTERN = re.compile(r"""
\b
\d{4}(?:[ -]\d{4}){3} #1234 5678 9012 3456 or 1234-5678-9012-3456 (exactly 16 digits with uniform separator)
\b
""", re.VERBOSE)

# Time
TIME_24H_PATTERN = re.compile(r"\b(?:[01]?\d|2[0-3]):[0-5]\d\b") #24-hour HH:MM
TIME_12H_PATTERN = re.compile(r"\b(?:1[0-2]|0?[1-9]):[0-5]\d(?:\s?[APap][Mm])\b") #12-hour h:MM AM/PM
TIME_COMBINED_PATTERN = re.compile(
    r"(?:\b(?:[01]?\d|2[0-3]):[0-5]\d\b)|(?:\b(?:1[0-2]|0?[1-9]):[0-5]\d(?:\s?[APap][Mm])\b)" #24h and 12h independently    
)

# HTML tags
HTML_TAG_PATTERN = re.compile(r"<([A-Za-z][A-Za-z0-9-]*)(?:\s+[^<>]*?)?>") #<div> | <p class="example"> | <img src="image.jpg">

# Hashtags
HASHTAG_PATTERN = re.compile(r"\#[A-Za-z0-9_]+\b") ##example | #ThisIsAHashtag | #123test

# Currency
CURRENCY_PATTERN = re.compile(r"""
\$
(?:
  (?:\d{1,3}(?:,\d{3})+) #with commas
  |
  \d+ #or plain digits
)
(?:\.\d{2})?
\b #optional cents \b
""", re.VERBOSE)


# Public validators
EMAIL = RegexValidator("email", EMAIL_PATTERN)
URL = RegexValidator("url", URL_PATTERN)
PHONE = RegexValidator("phone", PHONE_PATTERN)
CREDIT_CARD = RegexValidator("credit_card", CREDIT_CARD_PATTERN)
TIME_24H = RegexValidator("time_24h", TIME_24H_PATTERN)
TIME_12H = RegexValidator("time_12h", TIME_12H_PATTERN)
TIME = RegexValidator("time", TIME_COMBINED_PATTERN)
HTML_TAG = RegexValidator("html_tag", HTML_TAG_PATTERN)
HASHTAG = RegexValidator("hashtag", HASHTAG_PATTERN)
CURRENCY = RegexValidator("currency", CURRENCY_PATTERN)
