import random
import time
import math
import hashlib

# too lazy to improve and rename variables from p.js lol.

def make_id() -> str:
    _0x5054b6 = ""
    for i in range(32):
        _0x5054b6 += "0123456789abcdef"[math.floor(0x10 * random.random())]
    return _0x5054b6

def get_hash_difficulty(hash: str) -> float:
    return 0x10000000000000 / (int('0x' + hash[:13], 16) + 1)

def find_answers(st: int|str, id_hash: str) -> list|str:
    answers = []
    _0x35709e = hashlib.sha256(f"tp-v2-input, {st}, {id_hash}".encode()).hexdigest()
    for i in range(2):
        _0x2898d9 = 1
        while True:
            _0x42a2ec = hashlib.sha256(f"{_0x2898d9}, {_0x35709e}".encode()).hexdigest()
            if int(get_hash_difficulty(_0x42a2ec)) >= 5:
                answers.append(_0x2898d9)
                _0x35709e = _0x42a2ec
                break
            _0x2898d9 += 1
    return answers, _0x35709e

def generate_server_offset() -> int:
    timestamp = int(time.time() * 1000)
    timestamp_2 = timestamp + random.randint(1400, 2700)
    return timestamp_2 - timestamp, timestamp, timestamp_2


def solve() -> dict:
    _0x4eef7e, st, rst = generate_server_offset()
    _0xced0ee = int(time.time() * 1000)
    _0x4529a2 = random.uniform(5325.5, 10525.5) # Runtime
    _0x25fc0c = _0xced0ee - _0x4eef7e
    _id = make_id()
    answers, final_hash = find_answers(_0x25fc0c, _id)
    _0x1225b8 = random.uniform(_0x4529a2, (_0x4529a2 * random.uniform(1.1, 1.5)))
    _0x1f5d7b = round((0x3e8 * (_0x1225b8 - _0x4529a2)) / 0x3e8)
    return str({
        "workTime": _0x25fc0c,
        "id": _id,
        "answers": answers,
        "duration": _0x1f5d7b,
        'd': _0x4eef7e,
        'st': st,
        'rst': rst
    }).replace("'", '"').replace(", ", ",").replace(": ", ":")

print(solve())
input()

