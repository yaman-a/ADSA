class HashTable:
    def __init__(self):
        # Initialise 26 slots with keys and another with "never used" status
        self.table = [None] * 26 
        self.status = ["never used"] * 26

    def _hash(self, key):
        # Hash function: Use the last character of the key
        return ord(key[-1]) - ord('a')
    
    def insert(self, key):
        index = self._hash(key)
        original_idx = index
        while self.status[index] == "occupied" and self.table[index] != key:
            index = (index + 1) % 26 # linear probing
            if index == original_idx:
                return # exit if table is full
        
        # check if the spot is empty
        if self.status[index] != "occupied":
            self.table[index] = key
            self.status[index] = "occupied"

    def delete(self, key):
        index = self._hash(key)
        original_idx = index
        while self.status[index] != "never used":
            if self.table[index] == key:
                self.status[index] = "tombstone"
                return
            index = (index + 1) % 26 # linear probing
            if index == original_idx:
                return # exit if wrapped around
    
    def process(self, commands):
        # parse commands
        for command in commands:
            action = command[0]
            key = command[1:]
            if action == 'A':
                self.insert(key)
            elif action == 'D':
                self.delete(key)
    
    def disp(self):
        # Only display keys that are marked as occupied
        result = [self.table[i] for i in range(26) if self.status[i] == "occupied"]
        print(" ".join(result))

if __name__ == "__main__":
    # split commands, parse it and print out result
    commands = input().split()

    table = HashTable()
    table.process(commands)

    table.disp()