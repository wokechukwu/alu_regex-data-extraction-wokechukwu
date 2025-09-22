import os
import sys
from typing import Iterable, List, Dict

from .regex_patterns import (
    EMAIL, URL, PHONE, CREDIT_CARD, TIME, TIME_24H, TIME_12H,
    HTML_TAG, HASHTAG, CURRENCY
)


def clear_screen() -> None: #clear the screen
    command = 'cls' if os.name == 'nt' else 'clear'
    try:
        os.system(command)
    except Exception:
        print('\n' * 100)


def print_banner() -> None: #print the banner
    print("Regex_Validator: Made By Wisdom")
    print("-------------------------------")
    print("Overview")
    print("-------------------------------")
    print(
        "Regex_Validator is a tool designed to extract specific data from large volumes of "
        "string responses retrieved from APIs. Instead of manually searching through hundreds "
        "of thousands of lines, it leverages the power of Regular Expressions (Regex) to "
        "identify and extract the required information efficiently."
    )
    print("-------------------------------")


def find_all_in_text(text: str) -> dict[str, List[str]]: #find all the data in the text
    return {
        "emails": EMAIL.find_all(text),
        "urls": URL.find_all(text),
        "phones": PHONE.find_all(text),
        "credit_cards": CREDIT_CARD.find_all(text),
        "times": TIME.find_all(text),
        "html_tags": HTML_TAG.find_all(text),
        "hashtags": HASHTAG.find_all(text),
        "currency": CURRENCY.find_all(text),
    }


def validate_examples(examples: dict[str, Iterable[str]]) -> dict[str, List[bool]]: #validate the examples
    results: dict[str, List[bool]] = {}
    for key, values in examples.items():
        validator = {
            "email": EMAIL,
            "url": URL,
            "phone": PHONE,
            "credit_card": CREDIT_CARD,
            "time_24h": TIME_24H,
            "time_12h": TIME_12H,
            "html_tag": HTML_TAG,
            "hashtag": HASHTAG,
            "currency": CURRENCY,
        }.get(key)
        if validator is None:
            continue
        results[key] = [validator.is_match(v) for v in values]
    return results


def get_valid_input(prompt: str, input_type: str = "string") -> str: #get the valid input
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("Error: Input cannot be empty. Please try again.\n")
                continue

            if input_type == "email":
                if user_input.isdigit() or "@" not in user_input:
                    print("Error: Invalid email. Please try again.\n")
                    continue
            elif input_type == "phone":
                if user_input.isalpha() or not any(c.isdigit() for c in user_input):
                    print("Error: Invalid phone number. Please try again.\n")
                    continue
            elif input_type == "url":
                if user_input.isdigit() or not (
                    user_input.startswith(("http://", "https://", "www."))
                    or "." in user_input
                ):
                    print("Error: Invalid URL. Please try again.\n")
                    continue
            elif input_type == "credit_card":
                if user_input.isalpha() or not any(c.isdigit() for c in user_input):
                    print("Error: Invalid credit card number. Please try again.\n")
                    continue
            elif input_type == "html_tag":
                if not (user_input.startswith("<") and user_input.endswith(">")):
                    print("Error: Invalid HTML tag. Please try again.\n")
                    continue
            elif input_type == "hashtag":
                if not user_input.startswith("#") or user_input == "#":
                    print("Error: Invalid hashtag. Please try again.\n")
                    continue
            elif input_type == "currency":
                if user_input.isalpha() or not (
                    user_input.startswith("$") or any(c.isdigit() for c in user_input)
                ):
                    print("Error: Invalid currency amount. Please try again.\n")
                    continue
            elif input_type == "time":
                if user_input.isalpha() or ":" not in user_input or not any(
                    c.isdigit() for c in user_input
                ):
                    print("Error: Invalid time. Please try again.\n")
                    continue

            return user_input

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.\n")
            continue


def prompt_user() -> None: #prompt the user for the data type           
    print_banner()
    while True:
        while True:
            print()
            print("Please select the type of data that you want to validate:")
            print("1. Emails")
            print("2. Phone numbers")
            print("3. URLs")
            print("4. Credit Card Numbers")
            print("5. HTML tags")
            print("6. Hashtags")
            print("7. Currency amounts")
            print("8. Time (24h or 12h)")
            print("0. Exit")
            print()
            try:
                selection = input("Select 0-8: ").strip()
                if not selection.isdigit() or selection not in {
                    "0","1","2","3","4","5","6","7","8"
                }:
                    print("Error: Please select a valid option (0-8).\n")
                    continue
                break
            except KeyboardInterrupt:
                print("\n\n Goodbye!")
                return
            except Exception as e:
                print(f"Error: {e}. Please try again.\n")
                continue

        if selection == "0":
            print("Goodbye!")
            break

        mapping = {
            "1": ("email", EMAIL),
            "2": ("phone", PHONE),
            "3": ("url", URL),
            "4": ("credit_card", CREDIT_CARD),
            "5": ("html_tag", HTML_TAG),
            "6": ("hashtag", HASHTAG),
            "7": ("currency", CURRENCY),
            "8": ("time", TIME),
        }
        input_type, validator = mapping[selection]
        candidate = get_valid_input(f"Enter a {input_type} to validate: ", input_type)
        result = "Valid" if validator.is_match(candidate) else "Invalid"
        print(f"Result: {result}")

        print()
        while True:
            try:
                again = input("Do you want to continue? (y/n): ").strip().lower()
                if again in {"y", "yes"}:
                    clear_screen()
                    print_banner()
                    break
                elif again in {"n", "no"}:
                    print("Goodbye!")
                    return
                else:
                    print("Error: Please enter 'y' or 'n'.\n")
                    continue
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                return
            except Exception as e:
                print(f"Error: {e}. Please try again.\n")
                continue
