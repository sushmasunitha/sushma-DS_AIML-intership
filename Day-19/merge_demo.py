import os
import subprocess

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode

project = "merge_conflict_demo"

if not os.path.exists(project):
    os.mkdir(project)

os.chdir(project)

run("git init")
run("git checkout -b main")

run('git config user.name "Demo User"')
run('git config user.email "demo@example.com"')

with open("app.py", "w") as f:
    f.write("print('Hello from Main Branch')\n")

run("git add app.py")
run('git commit -m "Initial commit on main"')


run("git checkout -b feature-branch")

with open("app.py", "w") as f:
    f.write("print('Hello from Feature Branch')\n")

run("git commit -am \"Modified line in feature branch\"")

run("git checkout main")

with open("app.py", "w") as f:
    f.write("print('Hello from Main - Updated')\n")

run("git commit -am \"Modified line in main branch\"")


print("\nAttempting merge...\n")
run("git merge feature-branch")

print("\nNow open app.py to see conflict markers like:")
print("<<<<<<< HEAD")
print("=======")
print(">>>>>>> feature-branch")



with open("app.py", "w") as f:
    f.write("print('Conflict resolved version')\n")

run("git add app.py")
run('git commit -m "Resolved merge conflict"')

print("\nMerge conflict resolved successfully!")