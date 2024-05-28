import subprocess
import sys

# Create virtual environment
subprocess.check_call([sys.executable, '-m', 'venv', 'env'])

# Install required packages
subprocess.check_call(['env\\Scripts\\pip', 'install', 'pandas', 'scikit-learn', 'tensorflow'])

# Run the created_code.py script
subprocess.check_call(['env\\Scripts\\python', 'created_code.py'])
