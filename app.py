import os
import subprocess

def run_snyk_test():
    try:
        # Check if Snyk is installed
        subprocess.run(['snyk', '--version'], check=True)
        print("Snyk CLI is installed.")

        # Run the Snyk test
        print("Running Snyk test...")
        result = subprocess.run(['snyk', 'test'], capture_output=True, text=True)

        # Output the result
        print("Snyk Test Output:")
        print(result.stdout)

        if result.returncode != 0:
            print("Snyk detected vulnerabilities.")
        else:
            print("No vulnerabilities found.")
    except subprocess.CalledProcessError:
        print("Snyk is not installed or an error occurred.")
        print("Please install Snyk with 'npm install -g snyk'")

if __name__ == "__main__":
    run_snyk_test()
