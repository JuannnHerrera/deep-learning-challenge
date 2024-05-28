import subprocess

# Create and activate the virtual environment
subprocess.check_call(['python', '-m', 'venv', 'env'])
subprocess.check_call(['env\\Scripts\\pip', 'install', '--upgrade', 'pip'])
subprocess.check_call(['env\\Scripts\\pip', 'install', 'pandas', 'scikit-learn', 'tensorflow'])

# Run the created_code.py script
subprocess.check_call(['env\\Scripts\\python', 'created_code.py'])

# Run the AlphabetSoupCharity_Optimization.py script
subprocess.check_call(['env\\Scripts\\python', 'AlphabetSoupCharity_Optimization.py'])

# Generate the report based on the model results
# Update the loss and accuracy values as per your actual results
subprocess.check_call(['env\\Scripts\\python', 'generate_report.py'])
