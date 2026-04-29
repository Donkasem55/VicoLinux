import sys, os

def execute(command=""):
    print(command)

execute("clear")
print("Hello! Welcome to Vico Linux!")
ans = ""
while ans not in ["y", "Y", "n", "N"]:
    ans = input("Would you like to begin setup now? [Y/N] ")

if ans in "nN":
    print("Alright! You can continue to setup by running vico-setup on the TTY. Goodbye!")
    sys.exit(0)

print("\nContinuing to setup. First, partition the disk.\nMake sure to have about 700mb-1gb of EFI ESP (/boot) and a root partition (/), along with optionally a separate /home partition.")
execute("lsblk")
disk = input("Pick your main disk: ")
execute("cfdisk")
x = {}
execute("lsblk")
print("Now let's add our partitions! Use 'q' to quit, 'boot <partition name>' to add the EFI boot partition (/boot), 'root <partition name>' to add the root partition (/), 'home <partition name>' to add the home partition (/home), and 'r <partition mountpoint>' to remove a partition!\nPartition names start with /dev/..., meanwhile partition mountpoints are directories like /, /home, or /boot.")
while True:
    print(f"Current partitions added: ", end="")
    for i in x:
        if x[i] != "":
            print(f"{i}: {x[i]} ", end="")
        
    y = input("\nAdd your partitions: ")
    if y in ["quit", "exit", "q", "x"]:
        break
    elif y.split(" ")[0] == "r":
        try:
            x[y.split(" ")[1]] = ""
        except IndexError:
            print("Error: must include a partition")
    elif y.split(" ")[0] == "root":
        try:
            x["/"] = y.split(" ")[1]
        except IndexError:
            print("Error: must include a partition")
    elif y.split(" ")[0] == "boot":
        try:
            x["/boot"] = y.split(" ")[1]
        except IndexError:
            print("Error: must include a partition")
    elif y.split(" ")[0] == "home":
        try:
            x["/home"] = y.split(" ")[1]
        except IndexError:
            print("Error: must include a partition")
    print()

print("This program is incomplete, sorry")

