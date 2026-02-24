
filename = input("Enter a filename (example: config.txt): ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile contents:")
        print(content)


except FileNotFoundError:
    print("Oops! That file doesn't exist yet 🙂")