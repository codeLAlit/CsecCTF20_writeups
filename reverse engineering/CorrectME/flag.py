from hashlib import md5
from this import s as zen

def solve(challenge):
    words = zen.split()
    unique = set(words)
    if len(unique) == 96:
        msg = 'len' + 'set' + 'split' + challenge + 's'
        hidden = md5(msg.encode())
        return getattr(hidden, 'hexdigest')()
    else:
        raise 'Wrong'

flag = solve('7f/dd')
print(len(flag), flag)