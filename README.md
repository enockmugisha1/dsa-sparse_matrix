# Sparse Matrix Implementation - DSA Assignment 2

A Python implementation of sparse matrices using dictionaries to efficiently store and operate on large matrices with predominantly zero values.

## Features

- � **Sparse Storage**: Efficiently stores only non-zero elements
- 📂 **File I/O**: Load matrices from and save results to text files
- ➕ **Operations**: 
  - Matrix addition
  - Matrix subtraction
  - Matrix multiplication
- 🛠 **Built from Scratch**: No external dependencies
- 🚨 **Error Handling**: Custom parsing and validation
- 📝 **Dual Output**: Results displayed in console and saved to `output.txt`

## File Format Specification

Matrix files must adhere to the following structure:
rows=3
cols=3
(0, 0, 5)
(1, 2, -3)
(2, 1, 4)

- First line: `rows=<number>` (matrix row count)
- Second line: `cols=<number>` (matrix column count)
- Subsequent lines: Non-zero elements as `(row, col, value)` tuples
  - Row and column indices start at 0
  - One element per line

## Usage

1. Run the script:
   ```bash
   python sparse_matrix.py
2. Follow the interactive prompts:Enter operation (add, subtract, multiply): add
Enter first matrix file path: matrix1.txt
Enter second matrix file path: matrix2.txt
3.Results will be:

Printed to the console

Saved to output.txt in the same format
Example
Input (matrix1.txt):
rows=2
cols=2
(0, 0, 1)
(1, 1, 2)
Input (matrix2.txt):
rows=2
cols=2
(0, 1, 3)
(1, 0, 4)

Requirements
Python 3.x

No external dependencies

Constraints
⚠️ Addition/Subtraction: Matrices must have identical dimensions

✖️ Multiplication: First matrix's columns must match second matrix's rows

✔️ Validation: All input files must follow the specified format

Notes
Zero elements are not stored in memory

Operations automatically handle sparse matrix optimizations

Results maintain the sparse format (only non-zero values are saved)
