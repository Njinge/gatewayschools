#!/usr/bin/env python3
"""
Development setup script for Gateway Schools website.
This script helps with common development tasks.
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and print the description."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        print(f"Error: {e.stderr}")
        return False

def main():
    print("🚀 Gateway Schools Development Setup")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("manage.py").exists():
        print("❌ Error: Please run this script from the project root directory (where manage.py is located)")
        sys.exit(1)
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        sys.exit(1)
    
    # Run migrations
    if not run_command("python manage.py migrate", "Running database migrations"):
        sys.exit(1)
    
    # Create superuser if it doesn't exist
    print("\n👤 Creating superuser...")
    print("Please enter the following information for the admin user:")
    try:
        subprocess.run("python manage.py createsuperuser", shell=True, check=True)
        print("✅ Superuser created successfully!")
    except subprocess.CalledProcessError:
        print("⚠️  Superuser creation skipped or failed. You can create one manually later.")
    
    # Populate sample data
    if not run_command("python manage.py populate_sample_data", "Populating sample data"):
        print("⚠️  Sample data population failed. You can run it manually later.")
    
    # Collect static files
    if not run_command("python manage.py collectstatic --noinput", "Collecting static files"):
        print("⚠️  Static file collection failed. You can run it manually later.")
    
    print("\n🎉 Setup completed!")
    print("\n📋 Next steps:")
    print("1. Start the development server: python manage.py runserver")
    print("2. Visit the website: http://127.0.0.1:8000/")
    print("3. Access admin panel: http://127.0.0.1:8000/admin/")
    print("4. Login with your superuser credentials")
    
    print("\n🔧 Development commands:")
    print("- python manage.py runserver (start development server)")
    print("- python manage.py makemigrations (create new migrations)")
    print("- python manage.py migrate (apply migrations)")
    print("- python manage.py createsuperuser (create admin user)")
    print("- python manage.py populate_sample_data (add sample data)")

if __name__ == "__main__":
    main() 