# Advent of Code 2024

**Go** solutions for the [Advent of Code 2025](https://adventofcode.com/2025).

## Setup instructions

To run the solutions, you'll need to set up an environment variable with your Advent of Code session token.

### Step 1: Get your session token
1. Log in to the [Advent of Code](https://adventofcode.com) website.
2. Open your browser's developer tools (usually accessible via `F12` or `Ctrl+Shift+I` / `Cmd+Option+I`).
3. Navigate to the **Application** tab (or **Storage** tab in some browsers).
4. Look for your cookies under `https://adventofcode.com`.
5. Find the `session` cookie, and copy its value.

### Step 2: Set the environment variable
Set the session token as an environment variable named `AOC_SESSION`. For example:
- On Linux/macOS:
  ```bash
  export AOC_SESSION=your-session-token
  ```
- On Windows (PowerShell):
  ```powershell
  $env:AOC_SESSION="your-session-token"
  ```

## Running the solutions

Once the environment variable is set, you can run the code in two ways:

### 1. Run all solutions
To run all solutions for the available days:
```bash
python3 main.py -all
```

### 2. Run a specific solution
To run the solution for a specific day (replace `X` with the day number, e.g., `1` for Day 1):
```bash
python3 main.py -solution=X
```

## Solutions summary

Here is a summary of the solutions so far, including their approximate execution times and links to the respective Advent of Code pages:

| Day | Link                                           | Part A    | Part B    |
|----:|------------------------------------------------|----------:|----------:|
| 1   | [Day 1](https://adventofcode.com/2025/day/1)   | 1.11ms   | 1.21ms   |
| 2   | [Day 2](https://adventofcode.com/2025/day/2)   | 323.95ms   | 1459.25ms   |
| 3   | [Day 3](https://adventofcode.com/2025/day/3)   | 2.51ms   | 7.88ms   |
| 4   | [Day 4](https://adventofcode.com/2025/day/4)   | 13.59ms   | 42.85ms   |
| 5   | [Day 5](https://adventofcode.com/2025/day/5)   | 18.37ms   | 0.15ms   |
| 6   | [Day 6](https://adventofcode.com/2025/day/6)   | 0.94ms   | 2.94ms   |
| 7   | [Day 7](https://adventofcode.com/2025/day/7)   | 1.24ms   | 3.26ms   |
| 8   | [Day 8](https://adventofcode.com/2025/day/8)   | 440.81   | 770.79ms   |
