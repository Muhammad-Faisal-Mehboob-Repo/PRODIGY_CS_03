# Password Strength Checker

A simple GUI application built using Python's `tkinter` library to evaluate the strength of a password based on predefined criteria. The application provides real-time feedback as the user types the password and color-codes the requirements to visually indicate which conditions are met.

## Features

- **Live password strength check**: As you type, the application evaluates your password and displays feedback immediately.
- **Visual cues**: The criteria (minimum length, uppercase letter, lowercase letter, number, special character) are color-coded, turning green when fulfilled.
- **Strength levels**: Passwords are classified as:
  - **Strong**: Meets all requirements.
  - **Medium**: Satisfies most requirements but can be improved.
  - **Weak**: Fails to meet the essential criteria for a secure password.

## Criteria for a Strong Password
The password should:
1. Be at least 8 characters long.
2. Contain at least one uppercase letter.
3. Contain at least one lowercase letter.
4. Include at least one number.
5. Have at least one special character (e.g., `!@#$%^&*()`).

## Installation

To use this application, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd password-strength-checker
   ```

3. Run the Python script:

   ```bash
   python password_checker.py
   ```

   (Make sure you have Python installed.)

## How to Use

1. Launch the application by running the script.
2. Enter your password into the input field.
3. As you type, the app will update the strength indicators:
   - Green text means the criterion is satisfied.
   - The result will show whether your password is strong, medium, or weak based on the criteria it meets.

## Dependencies

- `tkinter`: Standard Python library for GUI development (no external installation required).
- `re`: Standard Python library for regular expressions (used to validate password requirements).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

Feel free to contribute or open issues if you find any bugs. Feedback is always appreciated! 😊
