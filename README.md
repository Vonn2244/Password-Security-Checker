# Password Security Checker

## Project Overview

The Password Security Checker is a Python-based security automation tool designed to evaluate the basic security strength of a password. The program automatically checks a password against several predefined security requirements and provides a security score and overall rating.

This project demonstrates how Python can be used to automate repetitive security checks instead of requiring a user to manually evaluate each password requirement.

## Features

The Password Security Checker evaluates passwords using five basic security checks:

- Checks whether the password contains at least 8 characters
- Checks for at least one uppercase letter
- Checks for at least one lowercase letter
- Checks for at least one number
- Checks for at least one special character
- Calculates a security score out of 5
- Assigns an overall security rating

The possible security ratings are:

- Weak
- Moderate
- Strong
- Very Strong

## Requirements

- Python 3
- Visual Studio Code or another Python-compatible editor
- No external Python packages are required

## How to Run

1. Download or clone the project repository.
2. Open the project folder in Visual Studio Code.
3. Open `main.py`.
4. Run the Python program.
5. Enter a test password when prompted.
6. Review the security checks, score, and overall rating displayed by the program.

## Example

A test password containing at least eight characters, an uppercase letter, a lowercase letter, a number, and a special character should receive a score of 5/5 and a rating of Very Strong.

## Security Note

This project is intended for educational purposes. Use test passwords when demonstrating the program. The Password Security Checker does not store or save passwords entered by the user.

## Project Purpose

The purpose of this project is to demonstrate how security automation can be implemented using Python. By automatically applying predefined security rules, the program provides a simple and repeatable way to evaluate password security.