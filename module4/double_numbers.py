import time

# Method 1: Read entire file into memory
def method_1():
    start_time = time.time()
    with open("file1.txt", "r") as infile, open("newfile1_method1.txt", "w") as outfile:
        numbers = infile.readlines()
        doubled_numbers = [str(int(num.strip()) * 2) + "\n" for num in numbers]
        outfile.writelines(doubled_numbers)
    print(f"Method 1 Execution Time: {time.time() - start_time:.2f} seconds")

# Method 2: Read one line at a time
def method_2():
    start_time = time.time()
    with open("file1.txt", "r") as infile, open("newfile1_method2.txt", "w") as outfile:
        for line in infile:
            outfile.write(str(int(line.strip()) * 2) + "\n")
    print(f"Method 2 Execution Time: {time.time() - start_time:.2f} seconds")

# Method 3: Split file into two parts and process separately
def method_3():
    start_time = time.time()
    with open("file1.txt", "r") as infile:
        lines = infile.readlines()

    half = len(lines) // 2
    part1, part2 = lines[:half], lines[half:]

    with open("newfile1_method3.txt", "w") as outfile:
        outfile.writelines([str(int(num.strip()) * 2) + "\n" for num in part1])
        outfile.writelines([str(int(num.strip()) * 2) + "\n" for num in part2])

    print(f"Method 3 Execution Time: {time.time() - start_time:.2f} seconds")

# Run all methods
method_1()
method_2()
method_3()