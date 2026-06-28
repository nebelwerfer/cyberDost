#!/usr/bin/env python3
"""
CyberDost X Installer
Version: 0.2.0-alpha
Platform: Termux / Linux

Prepares the CyberDost workspace and checks the environment.
"""

import os
import sys
import sqlite3
import shutil
from pathlib import Path

VERSION = "0.2.0-alpha"

DIRECTORIES = [
    "core",
    "executor",
    "llm",
    "memory",
    "plugins",
    "protocol",
    "security",
    "tests",
    "workspace",
    "logs",
    "docs",
    "examples",
]

FILES = {
    "config.yaml": """backend: openai
workspace: workspace
permission: ask
memory: sqlite
log_level: INFO
""",
    ".gitignore": """__pycache__/
*.pyc
*.db
logs/
.cache/
.venv/
""",
}


def banner():
    print("=" * 50)
    print(" CyberDost X Installer")
    print(f" Version : {VERSION}")
    print(" Platform: Termux / Linux")
    print("=" * 50)


def check_program(name):
    return shutil.which(name) is not None


def check_environment():
    print("[*] Checking environment...")

    print(f"Python : {sys.version.split()[0]}")

    if check_program("git"):
        print("[OK] Git found")
    else:
        print("[WARN] Git not found")

    if "com.termux" in os.environ.get("PREFIX", ""):
        print("[OK] Running inside Termux")
    else:
        print("[INFO] Running outside Termux")


def create_directories():
    print("\n[*] Creating directories...")

    for directory in DIRECTORIES:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"  + {directory}")


def create_files():
    print("\n[*] Creating configuration files...")

    for filename, content in FILES.items():
        path = Path(filename)
        if not path.exists():
            path.write_text(content)
            print(f"  + {filename}")
        else:
            print(f"  = {filename} already exists")


def initialize_database():
    print("\n[*] Initializing SQLite database...")

    db = sqlite3.connect("memory/cyberdost.db")

    db.execute("""
        CREATE TABLE IF NOT EXISTS missions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mission TEXT,
            status TEXT,
            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level TEXT,
            message TEXT,
            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    db.commit()
    db.close()

    print("[OK] Database initialized")


def finish():
    print("\nInstallation complete.\n")
    print("Next steps:")
    print("1. Edit config.yaml if needed")
    print("2. Run:")
    print("   python cyberdost.py")


def main():
    banner()
    check_environment()
    create_directories()
    create_files()
    initialize_database()
    finish()


if __name__ == "__main__":
    main()
