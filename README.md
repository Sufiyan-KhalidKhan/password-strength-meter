# 🔐 Password Strength Meter

A simple and interactive **Password Strength Meter** web app built using **Streamlit**. This app evaluates whether a password is strong based on specific security criteria and provides real-time feedback to the user.

## 🚀 Features

* Checks if a password is:
  - At least 8 characters long
  - Contains an uppercase letter
  - Contains a lowercase letter
  - Includes at least one digit
  - Includes at least one special character (`!@#$%&`)
* Real-time feedback using an interactive web interface
* User-friendly password requirement display

## 🛠️ Technologies Used

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – For building the web UI
- [re (regex)](https://docs.python.org/3/library/re.html) – For pattern matching and validation

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sufiyan-KhalidKhan/password-strength-meter.git
   cd password-strength-meter
    ```
2. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**
   ```bash
   streamlit run app.py
   ```

## 💡 How It Works

The main function of this app is `check_password_strength(password)`, which validates a given password against the following rules:

1. **Length Check**: The password must be at least 8 characters long.
2. **Uppercase Check**: It should contain at least one uppercase letter.
3. **Lowercase Check**: It should contain at least one lowercase letter.
4. **Digit Check**: It should include at least one number.
5. **Special Character Check**: It should have at least one special character from `!@#$%&`.

If the password fails any of these checks, a descriptive error message is returned. Otherwise, the password is marked as valid.

### Streamlit Interface

* Users input their password in a secure password field.
* If the field is empty or the password is invalid, the app shows the full list of password requirements.
* If the password is valid, a success message is displayed.
* Uses `st.info()`, `st.error()`, and `st.success()` to provide visual feedback.

## 📸 Screenshot
![image](https://github.com/user-attachments/assets/0a1290c9-3973-43a0-adf8-f0c8f9ed652b)

## 🧑‍💻 Author

**Sufiyan Khalid Khan**
GitHub: [@Sufiyan-KhalidKhan](https://github.com/Sufiyan-KhalidKhan)

## 📄 License

This project is licensed under the Apache 2.0 License.
