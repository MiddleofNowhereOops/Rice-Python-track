"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    end = min(len(line1), len(line2))
    for index in range(end):
        if line1[index] != line2[index]:
            return index
    if len(line1) == len(line2):
        return IDENTICAL
    
    return end

#print(singleline_diff("abcd", "abcef"))



def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    # If either line contains a newline or carriage return character, returns an empty string 
    if "\n" in line1 or "\n" in line2:
        return ""
    
    if "\r" in line1 or "\r" in line2:
        return ""
    
    # If idx is not a valid index, then returns an empty string
    if idx > min(len(line1), len(line2)) or idx < 0:
        return ""
    
    # Store the formatted string into a variable
    diff_format = "{0}\n{1}\n{2}\n". format(line1, "=" * idx + "^", line2)
    
    # Return the result
    return diff_format

#print(singleline_diff_format("abcd", "abcef", 3))


    
def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    end = min(len(lines1), len(lines2))
    
    for index in range(end):
        diff_idx = singleline_diff(lines1[index], lines2[index])
        if diff_idx == -1 and index == end - 1 and len(lines1) == len(lines2):
            return (IDENTICAL, IDENTICAL)
        elif diff_idx == -1 and index == end - 1:
            return (end, 0)
        elif diff_idx == -1:
            continue
        else:
            return (index, diff_idx)

# print(multiline_diff(["ab", "abc"], ["bc", "bcd"]))



def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    with open(filename, "rt") as open_file:
        file_text = open_file.read().splitlines()
    
    return file_text



def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    # Get the lines from both files
    file1 = get_file_lines(filename1)
    file2 = get_file_lines(filename2)
    
    # Find the first difference between the two lists
    diff = multiline_diff(file1, file2)
    
    # If the files are identical, the function returns the string "No differences\n"
    if diff == (-1, -1):
        return "No differences\n"
    
    line = diff[0]
    idx = diff[1]
    
    result = singleline_diff_format(file1[line], file2[line], idx)
    
    return "Line " + str(line) + ":\n" + result