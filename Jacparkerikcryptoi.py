import random
from datetime import datetime

def generate_commit_message():
    verbs = ["Fix", "Add", "Improve", "Update", "Refactor", "Remove", "Optimize"]
    objects = ["RPC handler", "CLI argument", "ENS lookup", "token logic", "logging", "balance fetch"]
    contexts = ["flow", "code", "support", "case", "handler", "logic"]
    return f"{random.choice(verbs)} {random.choice(objects)} in {random.choice(contexts)}"

def log_fake_activity():
    now = datetime.now().isoformat()
    with open("log.txt", "a") as f:
        f.write(f"[AUTO LOG] {now} {random.randint(100000, 999999)}\n")

if __name__ == "__main__":
    print("Generating fake GitHub commit entry...")
    log_fake_activity()
    print("Done.")
