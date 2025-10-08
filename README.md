# Personal Password Manager

A lightweight, secure, terminal-based password manager built using Python and SQLite. This application allows users to sign up, log in, and safely store passwords for various websites or services using SHA-256 encryption.

---

## Features

- User Sign-Up & Login with SHA-256 password hashing  
- Secure storage of credentials (site name, username, password)  
- View and search stored credentials by username  
- User-specific data storage (per-user tables)  
- Simple and intuitive CLI-based interface

---

## Technologies Used

- **Python 3**
- **SQLite** (for local database storage)
- **Hashlib** (SHA-256 encryption)
- **Random** (for unique user ID generation)

---

## Installation

```bash
git clone https://github.com/yourusername/password-manager.git
cd password-manager
python password_system.py
