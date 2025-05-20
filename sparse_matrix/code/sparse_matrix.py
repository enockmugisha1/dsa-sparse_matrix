# Sparse Matrix Implementation for DSA Assignment 2
# Implements a sparse matrix using a dictionary for non-zero elements.
# Supports loading from file, addition, subtraction, and multiplication.
# No external libraries used; custom parsing and error handling implemented.

class SparseMatrix:
    def __init__(self, file_path_or_rows, cols=None):
        """Initialize a sparse matrix from file or dimensions."""
        self.data = {}  # Dictionary to store non-zero elements: (row, col) -> value
        self.rows = 0
        self.cols = 0

        if isinstance(file_path_or_rows, str):
            self.load_from_file(file_path_or_rows)
        elif isinstance(file_path_or_rows, int) and isinstance(cols, int):
            self.rows = file_path_or_rows
            self.cols = cols
        else:
            raise ValueError("Invalid constructor arguments")

    def load_from_file(self, file_path):
        """Load matrix from file with format: rows=X, cols=Y, (row, col, value)."""
        try:
            with open(file_path, 'r') as f:
                lines = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            raise ValueError(f"Input file not found: {file_path}")

        # Validate and parse rows
        if len(lines) < 2:
            raise ValueError(f"Input file has wrong format: too few lines in {file_path}")
        if not lines[0].startswith("rows="):
            raise ValueError(f"Input file has wrong format: first line must start with 'rows=' in {file_path}")
        if not lines[0][5:].isdigit():
            raise ValueError(f"Input file has wrong format: rows value must be an integer in {file_path}")
        self.rows = int(lines[0][5:])

        # Validate and parse cols
        if not lines[1].startswith("cols="):
            raise ValueError(f"Input file has wrong format: second line must start with 'cols=' in {file_path}")
        if not lines[1][5:].isdigit():
            raise ValueError(f"Input file has wrong format: cols value must be an integer in {file_path}")
        self.cols = int(lines[1][5:])

        # Parse entries
        for i, line in enumerate(lines[2:], start=3):
            # Check format: (row, col, value)
            if not (line.startswith('(') and line.endswith(')')):
                raise ValueError(f"Input file has wrong format: line {i} must be in (row, col, value) format in {file_path}")

            # Custom parsing for (row, col, value)
            try:
                # Remove parentheses and split by comma
                parts = line[1:-1].split(',')
                if len(parts) != 3:
                    raise ValueError(f"Input file has wrong format: line {i} must have exactly 3 values (row, col, value) in {file_path}")
                row = parts[0].strip()
                col = parts[1].strip()
                value = parts[2].strip()

                # Validate integers
                if not (row.isdigit() and col.isdigit() and value.lstrip('-').isdigit()):
                    raise ValueError(f"Input file has wrong format: values in line {i} must be integers in {file_path}")
                row, col, value = int(row), int(col), int(value)

                # Validate indices
                if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                    raise ValueError(f"Invalid row or column index in line {i} of {file_path}")

                # Store non-zero value
                if value != 0:
                    self.data[(row, col)] = value
            except Exception as e:
                raise ValueError(f"Input file has wrong format: error parsing line {i} in {file_path}: {str(e)}")

    def get_element(self, row, col):
        """Get element at (row, col); return 0 if not set."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Index out of bounds")
        return self.data.get((row, col), 0)

    def set_element(self, row, col, value):
        """Set element at (row, col)."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Index out of bounds")
        if value == 0:
            self.data.pop((row, col), None)  # Remove zero values
        else:
            self.data[(row, col)] = value

    def add(self, other):
        """Add two sparse matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition")
        result = SparseMatrix(self.rows, self.cols)

        # Copy elements from self
        for key, value in self.data.items():
            result.data[key] = value

        # Add elements from other
        for key, value in other.data.items():
            result.data[key] = result.data.get(key, 0) + value
            if result.data[key] == 0:
                del result.data[key]
        return result

    def subtract(self, other):
        """Subtract two sparse matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for subtraction")
        result = SparseMatrix(self.rows, self.cols)

        # Copy elements from self
        for key, value in self.data.items():
            result.data[key] = value

        # Subtract elements from other
        for key, value in other.data.items():
            result.data[key] = result.data.get(key, 0) - value
            if result.data[key] == 0:
                del result.data[key]
        return result

    def multiply(self, other):
        """Multiply two sparse matrices."""
        if self.cols != other.rows:
            raise ValueError("Number of columns in first matrix must equal number of rows in second")
        result = SparseMatrix(self.rows, other.cols)

        # Iterate over non-zero elements of self
        for (i, k), val1 in self.data.items():
            # Iterate over non-zero elements of other
            for (k2, j), val2 in other.data.items():
                if k == k2:  # Matching inner dimension
                    result_key = (i, j)
                    result.data[result_key] = result.data.get(result_key, 0) + val1 * val2
                    if result.data[result_key] == 0:
                        del result.data[result_key]
        return result

    def to_string(self):
        """Convert matrix to string for output."""
        output = f"rows={self.rows}\ncols={self.cols}\n"
        for (row, col), value in sorted(self.data.items()):  # Sort for consistent output
            output += f"({row}, {col}, {value})\n"
        return output

def perform_matrix_operation(operation, file1_path, file2_path):
    """Perform the specified operation on two matrices."""
    try:
        matrix1 = SparseMatrix(file1_path)
        matrix2 = SparseMatrix(file2_path)
        if operation.lower() == 'add':
            return matrix1.add(matrix2).to_string()
        elif operation.lower() == 'subtract':
            return matrix1.subtract(matrix2).to_string()
        elif operation.lower() == 'multiply':
            return matrix1.multiply(matrix2).to_string()
        else:
            raise ValueError('Invalid operation. Use "add", "subtract", or "multiply".')
    except Exception as e:
        raise ValueError(f"Operation failed: {str(e)}")

def main():
    """Driver function to handle user input and perform operations."""
    try:
        operation = input("Enter operation (add, subtract, multiply): ").strip().lower()
        file1_path = input("Enter first matrix file path: ").strip()
        file2_path = input("Enter second matrix file path: ").strip()
        result = perform_matrix_operation(operation, file1_path, file2_path)
        print("Result:")
        print(result)
        # Optionally save to output file
        with open("output.txt", "w") as f:
            f.write(result)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()