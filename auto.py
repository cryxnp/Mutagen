import random
import subprocess

# Options
puzzle = 71
flips = 5
cpu = 26

# Constants for generating random number
LOWER = 1180591620717411303424
UPPER = 2361183241434822606847

def run_program():
    # Generate a random key within LOWER and UPPER
    random_key = random.randint(LOWER, UPPER)
    
    # Prepare command with random value for -k
    command = [
        "./mutagen",             # Path to your program
        "-p", str(puzzle),       # Parameter for puzzle number
        "-t", str(cpu),          # Parameter for the number of processors
        "-f", str(flips),        # Parameter for the number of flips
        "-k", str(random_key)    # Generated random key
    ]
    
    # Run the program and wait for completion
    result = subprocess.run(command, capture_output=True, text=True)

    # Output the entire program result (stdout and stderr)
    print(f"Output for key {random_key}:\n{result.stdout}")
    if result.stderr:
        print(f"Error output for key {random_key}:\n{result.stderr}")

    # Check the program output for a successful solution
    if "Solution saved" in result.stdout:
        print(f"WoW ! Congratulations !")
        return True  # Solution found
    elif "No solution found" in result.stdout:
        print(f"Trying again...")
        return False  # Solution not found
    else:
        print(f"Unexpected output: {result.stdout}")
        return False  # In case of unexpected conclusions, we also try again.

# A loop that will rerun the program with a new key until a solution is found
while True:
    if run_program():
        break  # If a solution is found, exit the loop
