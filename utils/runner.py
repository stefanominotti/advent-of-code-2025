import os
import time
import functools
import urllib.request
import urllib.error

YEAR = 2025
BASE_DIR = "solutions"

def _get_file_path(day: int) -> str:
    # Ensure directory exists
    directory = os.path.join(BASE_DIR, f"{day:02d}")
    os.makedirs(directory, exist_ok=True) 
    return os.path.join(directory, "input.txt")

def _download_input(day: int):
    """
    Checks for file, checks ENV, downloads from AoC if missing.
    """
    path = _get_file_path(day)
    
    # Check if file exists
    if os.path.exists(path):
        return

    # Check Session
    session = os.environ.get("AOC_SESSION")
    if not session:
        raise ValueError("AOC_SESSION environment variable is not set")

    print(f"Downloading input for Day {day}...")
    
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    req = urllib.request.Request(url)
    req.add_header("Cookie", f"session={session}")

    try:
        with urllib.request.urlopen(req) as response:
            if response.status != 200:
                raise ValueError(f"Error downloading input: status code {response.status}")
            
            content = response.read()
            
            with open(path, 'wb') as f:
                f.write(content)
                
    except urllib.error.HTTPError as e:
        raise ValueError(f"HTTP Error downloading input: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        raise ValueError(f"URL Error: {e.reason}")

def aoc_solution(day: int, part: str = "A"):
    """
    Handles downloading, file reading, and benchmarking.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper():
            # 1. Download Input (if needed)
            _download_input(day)

            # 2. Prepare Iterator
            file_path = _get_file_path(day)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                line_iterator = (line.rstrip('\n') for line in f)

                # 3. Execution & Timing
                print(f"--- Day {day} Part {part} ---")
                
                start_time = time.perf_counter() # More precise than time.now()
                
                result = func(line_iterator)
                
                end_time = time.perf_counter()
                elapsed = end_time - start_time

                # 4. Format Output
                if elapsed < 1e-3:
                    time_str = f"{elapsed*1e6:.2f}µs"
                elif elapsed < 1:
                    time_str = f"{elapsed*1e3:.2f}ms"
                else:
                    time_str = f"{elapsed:.4f}s"

                print(f"Result: {result} ({time_str})")
                return result

        return wrapper
    return decorator