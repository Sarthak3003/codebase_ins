from hashlib import sha256

def merkle(data):
    if len(data) == 0:
        return None
    hashed_data = [sha256(d.encode('utf-8')).hexdigest() for d in data]

    while len(hashed_data) > 1:
        if (len(hashed_data) % 2 != 0):
            hashed_data.append(hashed_data[-1])
        next_level = []
        for i in range(0, len(hashed_data), 2):
            pair = hashed_data[i] + hashed_data[i+1]
            h = sha256(pair.encode('utf-8')).hexdigest()
            next_level.append(h)
        hashed_data = next_level
    return hashed_data[0]
data =  ["Rosita", "Raj", "Rohan", "Riya", "Ram"]
print("Merkle root: ", merkle(data))