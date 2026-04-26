import copy

name = "B Mahesh Kumar"
name_len = len(name.replace(" ", ""))

reg_no = input("Enter Register Number: ")
last_digits = int(reg_no[-2:])

def create_data():
    return [
        {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}},
        {"id": 2, "data": {"files": ["c.txt"], "usage": 300}}
    ]

def make_copies(data):
    return data, data[:], copy.deepcopy(data)

def update_data(data):
    # Even → add file, Odd → remove file
    if last_digits % 2 == 0:
        data[0]["data"]["files"].append("new.txt")
    else:
        if data[0]["data"]["files"]:
            data[0]["data"]["files"].pop()

    data[0]["data"]["usage"] += 50

    # Modify second user slightly
    if data[1]["data"]["files"]:
        data[1]["data"]["files"].pop()

    return data

def analyze(before, after, shallow, deep):
    leak = 1 if before != after else 0
    safe = 1 if before == deep else 0

    files_after = {f for user in after for f in user["data"]["files"]}
    files_shallow = {f for user in shallow for f in user["data"]["files"]}

    overlap = len(files_after & files_shallow)

    if before[0]["data"] != after[0]["data"]:
        print("Inner level changed")
    else:
        print("Only outer level changed")

    return (leak, safe, overlap)

# Execution starts here
original = create_data()
backup = copy.deepcopy(original)

print("\n---Before---\n", original)

assign, shallow, deep = make_copies(original)

assign = update_data(assign)

print("\n---After Assignment---\n", assign)
print("\n---Original---\n", original)
print("\n---Shallow Copy---\n", shallow)
print("\n---Deep Copy---\n", deep)

result = analyze(backup, original, shallow, deep)

print("\n---Integrity Summary---")
print("Leakage, Safe, Overlap:", result)

if name_len % 2 == 0:
    print("Observation: Shared reference caused modification in original data")
else:
    print("Observation: Deep copy successfully preserved original data")

print("\nInsight: Improper copying can lead to unintended data changes.")
