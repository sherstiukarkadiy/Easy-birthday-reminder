from pathlib import Path
from collections import namedtuple

users_path = Path(__file__).parent.joinpath("participants.csv")
User = namedtuple('User', ["name",'date'])
users = []

with open(users_path,"r") as f:
    header= f.readline()
    new_line = f.readline()
    while len(new_line):
        name,date = new_line.replace("\n","").split(",")
        users.append(User(name,date)._asdict())
        new_line = f.readline()
