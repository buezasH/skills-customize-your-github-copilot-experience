# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practice working with strings, file I/O, and text manipulation in Python. You will read text from a file, analyze its contents, and write transformed output to a new file.

## 📝 Tasks

### 🛠️	Analyze a Text File

#### Description
Write a Python program that reads a text file and produces a summary of its contents, including word count, line count, and the most frequently used words.

#### Requirements
Completed program should:

- Read the contents of `sample-text.txt` using Python file I/O
- Count and display the total number of lines, words, and characters
- Identify the 5 most frequently used words (case-insensitive) and display them with their counts
- Handle the case where the file does not exist by printing a helpful error message

Example output:
```
=== Text File Analysis ===
Lines: 12
Words: 85
Characters: 436

Top 5 most frequent words:
  the    - 7
  and    - 5
  python - 4
  is     - 3
  for    - 3
```

### 🛠️	Transform and Write Text Output

#### Description
Extend your program to perform text transformations on the input file and write the results to a new output file called `output.txt`.

#### Requirements
Completed program should:

- Convert all text to title case and write it to `output.txt`
- Remove any blank lines from the output
- Add a line number prefix to each line in the format `001: `
- Print a confirmation message showing how many lines were written to the output file

Example output:
```
=== Text Transformation ===
Written 10 lines to output.txt

Preview (first 3 lines):
001: Python Is A Versatile Programming Language.
002: It Supports Multiple Programming Paradigms.
003: Developers Use Python For Web Development And Data Science.
```
