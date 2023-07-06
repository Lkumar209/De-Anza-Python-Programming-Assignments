# Laxya Kumar
# Description: This program reads an error log file, counts the lines, prints lines containing the word "error", and writes a report file.

try:
    error_log_file = input("Enter the backend error log file name: ")
    with open(error_log_file, 'r') as file:
        lines = file.readlines()
        
        line_count = len(lines)
        error_count = 0
        error_lines = []
        
        for line in lines:
            if line.strip() != '':
                if 'error' in line or 'Error' in line or 'ERROR' in line:
                    error_count += 1
                    error_lines.append(line)
        
        report_file = "reportError.txt"
        with open(report_file, 'w') as report:
            report.write(f"Total lines: {line_count}\n")
            report.write(f"Lines with 'error': {error_count}\n\n")
            report.writelines(error_lines)
        
        print(f"Total lines: {line_count}")
        print(f"Lines with 'error': {error_count}")
        print("\n".join(error_lines))
        
except FileNotFoundError:
    print("Error log file not found.")
except IOError:
    print("Error reading the file.")
