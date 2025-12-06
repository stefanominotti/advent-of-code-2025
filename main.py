import argparse
import os
import sys
import runpy

def run_solution(day: int):
    """
    Finds and runs all python scripts in solutions/{day}/
    """
    day_str = f"{day:02d}"
    solution_dir = os.path.join("solutions", day_str)
    
    if not os.path.exists(solution_dir):
        print(f"Error: Directory for Day {day} not found ({solution_dir})")
        return

    # Find all python files in that directory (ignoring __init__.py)
    # We sort them so part_a runs before part_b
    files = sorted([
        f for f in os.listdir(solution_dir) 
        if f.endswith(".py") and f != "__init__.py"
    ])

    if not files:
        print(f"No python solutions found for Day {day}")
        return

    for filename in files:
        # Construct module path: solutions.01.part_a
        module_name = f"solutions.{day_str}.{filename[:-3]}"
        
        # run_module executes the file as if you ran "python solutions/.../file.py"
        # It triggers the "if __name__ == '__main__':" block in your solution files.
        runpy.run_module(module_name, run_name="__main__", alter_sys=True)

def run_all():
    """Runs solutions for days 1 to 25"""
    for day in range(1, 26):
        # Check if directory exists before trying to run, to avoid spamming errors
        if os.path.exists(os.path.join("solutions", f"{day:02d}")):
            run_solution(day)

def main():
    # 1. Setup Argument Parsing (replacing Go 'flag')
    parser = argparse.ArgumentParser(description="Advent of Code Runner")    
    parser.add_argument("--all", action="store_true", help="Run all solutions")
    parser.add_argument("--solution", type=int, help="Run a specific solution (e.g. 1, 2)")
    args = parser.parse_args()

    # 2. Logic Flow
    if args.all:
        run_all()
    elif args.solution is not None:
        if 0 <= args.solution <= 25:
            run_solution(args.solution)
        else:
            print(f"Error: {args.solution} is not a valid day (1-25)")
            sys.exit(1)
    else:
        print("Please specify a solution with --solution <day> or run all with --all")
        parser.print_help()

if __name__ == "__main__":
    main()