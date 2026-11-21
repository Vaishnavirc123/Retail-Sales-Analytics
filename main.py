
import os
import subprocess
import sys

print("====================================")
print("     RETAIL SALES ANALYTICS")
print("====================================")

print("\nStep 1: Generating Sales Dataset...")

subprocess.run([sys.executable, "generate_data.py"], check=True)

print("\nStep 2: Performing Sales Analysis...")

subprocess.run([sys.executable, "sales_analysis.py"], check=True)

print("\n====================================")
print("     PROJECT COMPLETED SUCCESSFULLY")
print("====================================")

print("\nGenerated Files:")
print("- Sales Dataset")
print("- Sales Reports")
print("- Sales Charts")
