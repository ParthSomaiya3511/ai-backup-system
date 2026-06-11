from collections import defaultdict

file_actions = defaultdict(int)

def record_action(action):

    file_actions[action] += 1

    return file_actions[action]


def detect_mass_delete():

    if file_actions["delete"] > 100:

        return True

    return False