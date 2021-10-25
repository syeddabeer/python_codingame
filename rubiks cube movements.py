rotations = input().split(" ")
faces = [input(), input()]

for rotate in rotations:
    if rotate == "z":
        transition = {"U": "R", "R": "D", "D": "L", "L": "U", "F": "F", "B": "B"}
    elif rotate == "z'":
        transition = {"U": "L", "R": "U", "D": "R", "L": "D", "F": "F", "B": "B"}
    elif rotate == "y":
        transition = {"F": "L", "L": "B", "B": "R", "R": "F", "U": "U", "D": "D"}
    elif rotate == "y'":
        transition = {"F": "R", "L": "F", "B": "L", "R": "B", "U": "U", "D": "D"}
    elif rotate == "x":
        transition = {"F": "U", "U": "B", "B": "D", "D": "F", "R": "R", "L": "L"}
    elif rotate == "x'":
        transition = {"F": "D", "U": "F", "B": "U", "D": "B", "R": "R", "L": "L"}
    
    for idx, face in enumerate(faces):
        faces[idx] = transition[face]

print("\n".join(faces))