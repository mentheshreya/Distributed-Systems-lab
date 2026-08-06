# Ring Election Algorithm

# Number of processes
n = int(input("Enter number of processes: "))

# Process IDs
process = []
print("Enter Process IDs:")
for i in range(n):
    process.append(int(input()))

# Display processes
print("\nProcesses in the Ring:")
for p in process:
    print("P" + str(p), end=" ")
print()

# Current coordinator
coordinator = max(process)
print("\nCurrent Coordinator: P", coordinator)

# Coordinator fails
print("Coordinator P", coordinator, "has failed.")
process.remove(coordinator)

# Election starts
starter = int(input("\nEnter process to start election: "))

if starter not in process:
    print("Invalid process!")
else:
    print("\nElection Process:")

    index = process.index(starter)
    highest = starter

    # Election message travels around the ring
    for i in range(len(process)):
        current = process[(index + i) % len(process)]
        print("P", current, "sends election message")

        if current > highest:
            highest = current

    print("\nProcess P", highest, "becomes the new Coordinator.")

    # Coordinator message
    print("\nCoordinator Message:")
    start = process.index(highest)

    for i in range(len(process)):
        current = process[(start + i) % len(process)]
        print("P", current, "accepts P", highest, "as Coordinator")