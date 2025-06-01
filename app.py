import streamlit as st
import re

def check_password_strength(password):
    """
    Check if password meets all requirements:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character (!@#$%&)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit"
    
    if not re.search(r'[!@#$%&]', password):
        return False, "Password must contain at least one special character (!@#$%&)"
    
    return True, "Valid Password"

def main():
    st.title("Password Strength Meter")
    
    st.write("Enter a password to check its strength")
    
    password = st.text_input("Password", type="password")
    
    show_requirements = False
    is_valid = False
    message = ""
    
    if not password:
        show_requirements = True
    else:
        is_valid, message = check_password_strength(password)
        if not is_valid:
            show_requirements = True
        else:
            show_requirements = False
    
    if show_requirements:
        st.info("""
        Password Requirements:
        - At least 8 characters long
        - Contains at least one uppercase letter
        - Contains at least one lowercase letter
        - Contains at least one digit
        - Contains at least one special character (!@#$%&)
        """)
    
    if password:
        if is_valid:
            st.success(message)
        else:
            st.error(message)

if __name__ == "__main__":
    main()