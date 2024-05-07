import os

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'csk.pkl')

with open(file_path, 'rb') as model_file:
