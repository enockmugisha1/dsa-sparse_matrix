Sparse Matrix - DSA Assignment 2
This project implements a Sparse Matrix in Python using a dictionary to store non-zero elements. It is designed to efficiently handle large matrices with mostly zero values, as required in Data Structures and Algorithms Assignment 2.

Features
✅ Load sparse matrices from a custom-formatted file

➕ Perform matrix addition, subtraction, and multiplication

🔍 Custom parsing and error handling

❌ No external libraries used – fully built from scratch

📁 Output result saved to output.txt

File Format
Matrix files must follow this format:

makefile
Copy
Edit
rows=3
cols=3
(0, 0, 5)
(1, 2, -3)
(2, 1, 4)
The first line defines the number of rows.

The second line defines the number of columns.

Each following line defines a non-zero element in the format (row, col, value).

How to Use
Run the script:

bash
Copy
Edit
python sparse_matrix.py
Follow prompts:

bash
Copy
Edit
Enter operation (add, subtract, multiply): add
Enter first matrix file path: matrix1.txt
Enter second matrix file path: matrix2.txt
Check output:

The result is printed in the console

The result is also saved to output.txt

Example Output
makefile
Copy
Edit
rows=3
cols=3
(0, 0, 8)
(1, 2, 4)
(2, 1, 1)
Requirements
Python 3.x

No external packages needed

Notes
All matrices must be in valid format.

Addition and subtraction require matrices with the same dimensions.

Multiplication requires the first matrix's columns to match the second matrix's rows.

