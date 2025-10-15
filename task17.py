import os
import tempfile
import time
import tracemalloc
from lib.heap import MinHeap


def external_sort(input_file, output_file):
    chunk_size = 1024*8*2 
    
    temp_files = []
    with open(input_file, 'r', encoding='utf-8') as f:
        chunk = []
        for line in f:
            chunk.append(line)
            if len(chunk) >= chunk_size:
                chunk.sort()
                temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8')
                temp_file.writelines(chunk)
                temp_file.flush()
                temp_files.append(temp_file)
                chunk = []
        
        if chunk:
            chunk.sort()
            temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8')
            temp_file.writelines(chunk)
            temp_file.flush()
            temp_files.append(temp_file)
    
    files = [open(f.name, 'r', encoding='utf-8') for f in temp_files]
    
    heap = MinHeap()

    try:
        for i, file in enumerate(files):
            line = file.readline().strip()
            if line:
                heap.insert((line, i))
        
        with open(output_file, 'w', encoding='utf-8') as out:
            while heap:
                min_line, file_index = heap.pop()
                out.write(min_line + '\n')
                
                next_line = files[file_index].readline().strip()
                if next_line:
                    heap.insert((next_line, file_index))
    
    finally:
        for file in files:
            file.close()

def main():
    input_file = '1.txt'
    output_file = '2.txt'
    
    if not os.path.exists(input_file):
        print(f"Ошибка: Файл {input_file} не найден!")
        return
    tracemalloc.start()

    start_time = time.time()
    
    external_sort(input_file, output_file)
    
    current, peak = tracemalloc.get_traced_memory()
    print('Memory usage: ', peak / 1024 / 1024, 'MiB')
    print('Time: ', (time.time() - start_time ), 'c')
    tracemalloc.stop()
main()
