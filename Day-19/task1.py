import os
import subprocess
import sys

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running: {command}")
        print(result.stderr)
        sys.exit(1)
    return result.stdout.strip()

try:
    git_version = run_command("git --version")
    print("Git found:", git_version)
except:
    print("Git is NOT installed or not added to PATH.")
    sys.exit(1)


project_name = "ds_project_branch_demo"

if not os.path.exists(project_name):
    os.mkdir(project_name)

os.chdir(project_name)

run_command("git init")

run_command("git checkout -b main")

with open("main.py", "w") as f:
    f.write("print('Stable Main Branch Code')")

run_command("git add main.py")
run_command("git commit -m \"Initial commit on main\"")

run_command("git checkout -b feature-viz")

with open("plots.py", "w") as f:
    f.write("print('Experimental Visualization Code')")

run_command("git add plots.py")
run_command("git commit -m \"Added plots.py in feature branch\"")

print("\nFiles in feature-viz branch:")
print(os.listdir())

run_command("git checkout main")

print("\nFiles after switching to main branch:")
print(os.listdir())

run_command("git checkout feature-viz")

print("\nFiles after switching back to feature-viz branch:")
print(os.listdir())