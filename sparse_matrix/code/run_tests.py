import subprocess

# Test matrix operations
tests = [
    {
        "desc": "✅ Test 1 - Valid Addition",
        "operation": "add",
        "matrix1": "../sample_inputs/matrix1.txt",
        "matrix2": "../sample_inputs/matrix2.txt"
    },
    {
        "desc": "✅ Test 2 - Valid Subtraction",
        "operation": "subtract",
        "matrix1": "../sample_inputs/matrix1.txt",
        "matrix2": "../sample_inputs/matrix2.txt"
    },
    {
        "desc": "✅ Test 3 - Valid Multiplication",
        "operation": "multiply",
        "matrix1": "../sample_inputs/matrix3.txt",
        "matrix2": "../sample_inputs/matrix4.txt"
    },
    {
        "desc": "❌ Test 4 - Invalid Format",
        "operation": "add",
        "matrix1": "../sample_inputs/invalid_format.txt",
        "matrix2": "../sample_inputs/matrix2.txt"
    },
    {
        "desc": "⚠️ Test 5 - Dimension Mismatch Multiplication",
        "operation": "multiply",
        "matrix1": "../sample_inputs/matrix1.txt",
        "matrix2": "../sample_inputs/matrix3.txt"
    }
]

with open("output.txt", "w") as f:
    for test in tests:
        f.write(f"{test['desc']}\n")
        try:
            process = subprocess.run(
                ["python3", "sparse_matrix.py"],
                input=f"{test['operation']}\n{test['matrix1']}\n{test['matrix2']}\n",
                capture_output=True,
                text=True,
                timeout=10
            )
            f.write(process.stdout + "\n")
            if process.stderr:
                f.write("Error:\n" + process.stderr + "\n")
        except Exception as e:
            f.write(f"Exception occurred: {str(e)}\n")
        f.write("="*40 + "\n")
