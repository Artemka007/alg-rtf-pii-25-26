from enum import Enum
import os
import sys
import tempfile


class ExternalHash:
    def __init__(self, size=10003, base_dir="database"):
        self.size = size
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)
    
    def get(self, key):
        filename = self._get_filename(key)
        return self._get_in_file(filename, key)
    
    def add(self, key, value):
        filename = self._get_filename(key)
        existing_value = self._get_in_file(filename, key)
        if existing_value is not None:
            return False
        
        return self._add_in_file(filename, key, value)
    
    def delete(self, key):
        filename = self._get_filename(key)
        return self._delete_in_file(filename, key)
    
    def update(self, key, value):
        filename = self._get_filename(key)
        existing_value = self._get_in_file(filename, key)
        if existing_value is None:
            return False
        
        return self._update_in_file(filename, key, value)
    
    def _hash(self, key):
        hash_value = 0
        for i, symbol in enumerate(key):
            hash_value = (hash_value * 31 + ord(symbol)) % self.size
        return hash_value % self.size

    def _get_filename(self, key):
        return os.path.join(self.base_dir, str(self._hash(key)))

    def _get_in_file(self, filename, key):
        try:
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    parts = line.strip().split(', ', 1)
                    if len(parts) == 2 and parts[0] == key:
                        return parts[1]
        except FileNotFoundError:
            pass
        return None

    def _add_in_file(self, filename, key, value):
        try:
            with open(filename, 'a') as f:
                f.write(f'{key}, {value}\n')
            return True
        except Exception:
            return False

    def _update_in_file(self, filename, key, value):
        try:
            if not os.path.exists(filename):
                return False
                
            with open(filename, 'r') as old_file, \
                tempfile.NamedTemporaryFile(mode='w', delete=False, dir=os.path.dirname(filename) or '.') as new_file:
                
                updated = False
                while True:
                    line = old_file.readline()
                    if not line:
                        break
                    
                    parts = line.strip().split(', ', 1)
                    if len(parts) == 2 and parts[0] == key:
                        new_file.write(f'{key}, {value}\n')
                        updated = True
                    else:
                        new_file.write(line)
                
                temp_filename = new_file.name
                
            os.replace(temp_filename, filename)
            return updated
        except Exception:
            return False

    def _delete_in_file(self, filename, key):
        try:
            if not os.path.exists(filename):
                return False
                
            with open(filename, 'r') as old_file, \
                tempfile.NamedTemporaryFile(mode='w', delete=False, dir=os.path.dirname(filename) or '.') as new_file:
                
                deleted = False
                while True:
                    line = old_file.readline()
                    if not line:
                        break
                    
                    parts = line.strip().split(', ', 1)
                    if len(parts) == 2 and parts[0] == key:
                        deleted = True
                        continue
                    else:
                        new_file.write(line)
                
                temp_filename = new_file.name
                
            os.replace(temp_filename, filename)
            return deleted
        except Exception:
            return False

def solution():
    db = ExternalHash()
    
    n = int(sys.stdin.readline())
    
    while True:
        line = sys.stdin.readline()
        if not line: 
            break
        
        parts = line.split()
        cmd = parts[0]

        def handle_add():
            if len(parts) < 3:
                print("ERROR")
                return
            key = parts[1]
            value = ' '.join(parts[2:])
            if db.add(key, value):
                pass
            else:
                print("ERROR")
        
        def handle_delete():
            if len(parts) < 2:
                print("ERROR")
                return
            key = parts[1]
            if db.delete(key):
                pass
            else:
                print("ERROR")
        
        def handle_update():
            if len(parts) < 3:
                print("ERROR")
                return
            key = parts[1]
            value = ' '.join(parts[2:])
            if db.update(key, value):
                pass
            else:
                print("ERROR")
        
        def handle_print():
            if len(parts) < 2:
                print("ERROR")
                return
            key = parts[1]
            result = db.get(key)
            if result is not None:
                print(f"{key} {result}")
            else:
                print("ERROR")
        
        match cmd:
            case 'ADD':
                handle_add()
                continue
            case 'DELETE':
                handle_delete()
                continue
            case 'UPDATE':
                handle_update()
                continue
            case 'PRINT':
                handle_print()
                continue

