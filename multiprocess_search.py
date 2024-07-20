import os
import time
import multiprocessing
from multiprocessing import Queue


# Функція для пошуку ключових слів у файлах
def search_keywords(files, keywords, result_queue):
    keyword_results = {keyword: [] for keyword in keywords}
    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                for keyword in keywords:
                    if keyword in content:
                        keyword_results[keyword].append(file)
        except Exception as e:
            print(f"Error reading file {file}: {e}")
    result_queue.put(keyword_results)


# Функція для розподілу файлів між процесами
def multiprocess_search(files, keywords, num_processes=4):
    result_queue = Queue()
    processes = []
    chunk_size = len(files) // num_processes
    for i in range(num_processes):
        chunk = files[i * chunk_size:(i + 1) * chunk_size]
        process = multiprocessing.Process(target=search_keywords, args=(chunk, keywords, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    final_results = {keyword: [] for keyword in keywords}
    while not result_queue.empty():
        result = result_queue.get()
        for keyword, files in result.items():
            final_results[keyword].extend(files)
    return final_results


if __name__ == "__main__":
    keywords = ["example", "test", "search", "keyword", "file"]
    files = [os.path.join('test_files', f) for f in os.listdir('test_files') if f.endswith('.txt')]
    start_time = time.time()
    results = multiprocess_search(files, keywords)
    end_time = time.time()
    print("Multiprocessing results:", results)
    print("Multiprocessing execution time:", end_time - start_time)
