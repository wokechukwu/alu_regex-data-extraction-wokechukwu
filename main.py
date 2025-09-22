"""

FILE PURPOSE: Main entry point for the application. This is the file you run
to start the interactive CLI interface. It imports and calls the CLI module
to provide the user interface for testing regex patterns and data extraction.
"""

from __future__ import annotations #for type hints

import re #for regular expressions      
import os #for operating system
import sys #for system
from dataclasses import dataclass #for data classes
from typing import Iterable, List, Pattern, Dict, Any, Optional, Union #for typing
from datetime import datetime #for datetime

"""
ALU Regex Data Extraction Tool
Author: Okechukwu Wisdom Ikechukwu
Created: 2025
"""

from core.extractors import prompt_user #for prompt_user

if __name__ == "__main__": #for main    
    prompt_user()
