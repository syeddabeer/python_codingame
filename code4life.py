import sys
import math

def separate_files(files):
    player_files = []    # files of the player
    other_files = []    # files of the opponent
    cloud_files = []    # files in the cloud
    
    for file in files:
        if file["carried_by"] == 0:
            player_files.append(file)
        elif file["carried_by"] == 1:
            other_files.append(file)
        elif file["carried_by"] == -1:
            cloud_files.append(file)
    
    return player_files, other_files, cloud_files


def what_need(user_files, user_bot):
    """Return what and how many i need for each file the user have"""
    need = []
    # cette fonction est a changer
    for idx, file in enumerate(user_files):
        need.append([
            max(file["cost_a"] - max(user_bot["storage_a"] - sum([file["cost_a"] for file in user_files[:idx]]), 0), 0),
            max(file["cost_b"] - max(user_bot["storage_b"] - sum([file["cost_b"] for file in user_files[:idx]]), 0), 0),
            max(file["cost_c"] - max(user_bot["storage_c"] - sum([file["cost_c"] for file in user_files[:idx]]), 0), 0),
            max(file["cost_d"] - max(user_bot["storage_d"] - sum([file["cost_d"] for file in user_files[:idx]]), 0), 0),
            max(file["cost_e"] - max(user_bot["storage_e"] - sum([file["cost_e"] for file in user_files[:idx]]), 0), 0)
        ])
    
    return need
            

def sum_storage(robot):
    return sum((
        robot["storage_a"],
        robot["storage_b"],
        robot["storage_c"],
        robot["storage_d"],
        robot["storage_e"]
    ))


def file_completed_eh(file, robot):
    for molecule in range(97, 102):
        if 0 <= file["cost_" + chr(molecule)] <= robot["storage_" + chr(molecule)]:
            continue
        else:
            return False
    return True
    
    
def have_completed_file(files, robot):
   return any([file_completed_eh(file, robot) for file in files])


def all_file_completed_eh(files, robot):
    for molecule in range(97, 102):
        if sum([file["cost_" + chr(molecule)] for file in files]) <= robot["storage_" + chr(molecule)]:
            continue
        else:
            return False
    return True
    
#    return all([file_completed_eh(file, robot) for file in files])
    

def file_completed(files, robot):
    for idx, file in enumerate(files):
        if all([robot["storage_" + chr(lettre)] >= file["cost_" + chr(lettre)] for lettre in range(97, 102)]):
            return idx


def get_sample(robot):
    if robot["target"] != "SAMPLES":
        print("GOTO SAMPLES")
    else:
        print("CONNECT 1")
        
def exchange_sample_to_diagnosis(robot, our_files):
    # if we are at the diagnosis, we take a file
    if robot["target"] == "DIAGNOSIS":
        for file in our_files:
            if file["health"] == -1:    # may we already convert the sample
                print("CONNECT", file["sample_id"])
                break
    # otherwise, we go to the diagnosis
    else:
        print("GOTO DIAGNOSIS")


def get_molecule(robot, file_needed):
    # we aren't at the molecules
    if robot["target"] != "MOLECULES":
        print("GOTO MOLECULES")
    # we are at the molecules and we need molecules
    else:
        # we take molecule for file one by one to assure when ou storage is full
        # we have a completed molecule
        for file in file_needed:
            for idx, molecule_type in enumerate(file):
                if molecule_type != 0:
                    print("CONNECT", chr(idx+65))
                    break
            else:
                continue
            break


def lodge_medication(robot, our_files):
    # we aren't at the laboratory but we have to
    if robots[0]["target"] != "LABORATORY":
        print("GOTO LABORATORY")
    else:
        print("CONNECT", my_files[file_completed(my_files, robots[0])]["sample_id"])


def nb_sample_files(files):
    nb = 0
    for file in files:
        if file["health"] == -1:
            nb += 1
    return nb


def nb_diagnosis_files(files):
    nb = 0
    for file in files:
        if file["health"] != -1:
            nb += 1
    return nb


project_count = int(input())
for i in range(project_count):
    a, b, c, d, e = [int(j) for j in input().split()]

# game loop
while True:
    robots = []
    for i in range(2):
        (target, eta, score,
        storage_a, storage_b, storage_c, storage_d, storage_e,
        expertise_a, expertise_b, expertise_c, expertise_d, expertise_e) = input().split()
        
        robots.append({
            "target": target,
            "eta": int(eta),
            "score": int(score),
            
            # we manualy manage the sorage of robots
            "storage_a": int(storage_a),
            "storage_b": int(storage_b),
            "storage_c": int(storage_c),
            "storage_d": int(storage_d),
            "storage_e": int(storage_e),
            
            "expertise_a": int(expertise_a),
            "expertise_b": int(expertise_b),
            "expertise_c": int(expertise_c),
            "expertise_d": int(expertise_d),
            "expertise_e": int(expertise_e)
        })
    
    available_a, available_b, available_c, available_d, available_e = [int(i) for i in input().split()]
    
    sample_count = int(input())
    fichiers = []
    for i in range(sample_count):
        sample_id, carried_by, rank, expertise_gain, health, cost_a, cost_b, cost_c, cost_d, cost_e = input().split()
        
        fichiers.append(
            {
                "sample_id": int(sample_id),
                "carried_by": int(carried_by),
                "rank": int(rank),
                "health": int(health),
                "cost_a": int(cost_a),
                "cost_b": int(cost_b),
                "cost_c": int(cost_c),
                "cost_d": int(cost_d),
                "cost_e": int(cost_e)
            }
        )
    
    # sort files by their health point (higher is better, so the highest is the first)
    fichiers.sort(key=lambda file: file["health"], reverse=True)
    
    # separate the files
    my_files, other_player_files, cloud_files = separate_files(fichiers)
    
    # molecules we needed by files
    needed = what_need(my_files, robots[0])
    # sum of molecules we need 
    sum_needed = [sum(cathegorie) for cathegorie in zip(*needed)]
    
    # some logs
    print("molecules we need by files:\n", needed, file=sys.stderr)
    print("totale molecules we need:\n", sum_needed, file=sys.stderr)
    print("have a completed file ?:", have_completed_file(my_files, robots[0]), file=sys.stderr)
    print("all completed ?:", all_file_completed_eh(my_files, robots[0]), file=sys.stderr)
    
    
    # in function of the case we are, we do thing
    if (
        0 <= nb_sample_files(my_files) <= 2 and    # we have less than 3 samples and
        nb_diagnosis_files(my_files) == 0    # we don't have any diagnosis
    ):
        # we go take a sample
        get_sample(robots[0])
    
    elif (
        0 <= nb_diagnosis_files(my_files) <= 2 and    # we have less than 3 diagnosis and
        1 <= nb_sample_files(my_files) <= 3    # we have at least one sample
    ):
        # we convert one sample to a diagnosis
        exchange_sample_to_diagnosis(robots[0], my_files)
    
    elif (
        sum_storage(robots[0]) < 10 and    # we have place in our storage and
        1 <= nb_diagnosis_files(my_files) <= 3 and    # we have file diagnosed
        not all_file_completed_eh(my_files, robots[0])    # we haven't completed all our files
    ):
        # we take a molecule we need
        get_molecule(robots[0], needed)
    
    elif (
        (
            sum_storage(robots[0]) == 10 and    # our storage is full and
            have_completed_file(my_files, robots[0])    # we have at least one file completed
        ) or
        all_file_completed_eh(my_files, robots[0])    # all our files are completed
    ):
        # we deposit a medication
        lodge_medication(robots[0], my_files)
        
    else:
        print("WAIT")
    
    
    # some logs
    print(file=sys.stderr)
    print("module:", robots[0]["target"], file=sys.stderr)
    print("files we have:", file=sys.stderr)
    [print(file, file=sys.stderr) for file in my_files]
    print("totale storage:", sum_storage(robots[0]), file=sys.stderr)
    print("our storage by molecules:", file=sys.stderr)
    print([robots[0]["storage_" + chr(nb)] for nb in range(97, 102)], file=sys.stderr)