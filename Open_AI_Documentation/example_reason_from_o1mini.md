Certainly! Below is a Bash script that takes a matrix represented as a string in the format `"[1,2],[3,4],[5,6]"` and prints its transpose in the same format.

### Script: `transpose_matrix.sh`

```bash
#!/bin/bash
Certainly! Below is a Bash script that takes a matrix represented as a string in the format `"[1,2],[3,4],[5,6]"` and prints its transpose in the same format.

### Script: `transpose_matrix.sh`

```bash
#!/bin/bash

# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 '[row1],[row2],...[rowN]'"
    echo "Example: $0 '[1,2],[3,4],[5,6]'"
    exit 1
fi

input="$1"

# Use awk to parse and transpose the matrix
echo "$input" | awk '
BEGIN {
    # Set the field separator to "],[" to split rows
    FS = "\\],\\["
}

{
    # Remove leading '[' from the first row and trailing ']' from the last row
    gsub(/^\[/, "", $0)
    gsub(/\]$/, "", $0)

    # Split the input into rows
    num_rows = split($0, rows, "],[")

    # Iterate over each row
    for (i = 1; i <= num_rows; i++) {
        # Split row into individual numbers
        num_cols = split(rows[i], nums, ",")

        # Iterate over each number and assign to the transposed matrix
        for (j = 1; j <= num_cols; j++) {
            transposed[j, i] = nums[j]
            if (j > max_cols) { max_cols = j }
            if (i > max_rows) { max_rows = i }
        }
    }
}

END {
    # Build the transposed matrix string
    output = ""
    for (j = 1; j <= max_cols; j++) {
        output = output "["

        for (i = 1; i <= max_rows; i++) {
            output = output transposed[j, i]
            if (i < max_rows) {
                output = output ","
            }
        }

        output = output "]"
        if (j < max_cols) {
            output = output ","
        }
    }

    print output
}
'
```

### How It Works

1. **Input Validation**: The script first checks if exactly one argument is provided. If not, it displays usage instructions and exits.

2. **Parsing the Matrix**:
    - **Field Separator (`FS`)**: The `awk` script sets the field separator to `"],["` to split the input string into individual rows.
    - **Cleaning Brackets**: It removes the leading `[` from the first row and the trailing `]` from the last row to simplify processing.
    - **Splitting Rows and Columns**: It splits the input into rows and then splits each row into individual numbers, storing them in a two-dimensional array `transposed`.

3. **Transposing the Matrix**:
    - It iterates over the `transposed` array to build the transposed matrix string.
    - The output is constructed in the format `"[1,3,5],[2,4,6]"` for the input `"[1,2],[3,4],[5,6]"`.

4. **Output**: Finally, the transposed matrix string is printed.

### Usage

1. **Save the Script**: Save the above script to a file named `transpose_matrix.sh`.

2. **Make It Executable**:
    ```bash
    chmod +x transpose_matrix.sh
    ```

3. **Run the Script**:
    ```bash
    ./transpose_matrix.sh '[1,2],[3,4],[5,6]'
    ```

    **Output**:
    ```
    [1,3,5],[2,4,6]
    ```

### Additional Examples

- **Example 1**:
    ```bash
    ./transpose_matrix.sh '[1,2,3],[4,5,6]'
    ```
    **Output**:
    ```
    [1,4],[2,5],[3,6]
    ```

- **Example 2**:
    ```bash
    ./transpose_matrix.sh '[7,8],[9,10],[11,12]'
    ```
    **Output**:
    ```
    [7,9,11],[8,10,12]
    ```

### Notes

- **Matrix Validation**: This script assumes that the input matrix is well-formed, meaning all rows have the same number of columns and are properly enclosed in square brackets and separated by commas.
  
- **Dependencies**: The script uses standard Unix tools (`bash` and `awk`) and doesn't require any external dependencies.

Feel free to integrate this script into your workflows or modify it to handle different input formats as needed!Certainly! Below is a Bash script that takes a matrix represented as a string in the format `"[1,2],[3,4],[5,6]"` and prints its transpose in the same format.

### Script: `transpose_matrix.sh`

```bash
#!/bin/bash

# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 '[row1],[row2],...[rowN]'"
    echo "Example: $0 '[1,2],[3,4],[5,6]'"
    exit 1
fi

input="$1"

# Use awk to parse and transpose the matrix
echo "$input" | awk '
BEGIN {
    # Set the field separator to "],[" to split rows
    FS = "\\],\\["
}

{
    # Remove leading '[' from the first row and trailing ']' from the last row
    gsub(/^\[/, "", $0)
    gsub(/\]$/, "", $0)

    # Split the input into rows
    num_rows = split($0, rows, "],[")

    # Iterate over each row
    for (i = 1; i <= num_rows; i++) {
        # Split row into individual numbers
        num_cols = split(rows[i], nums, ",")

        # Iterate over each number and assign to the transposed matrix
        for (j = 1; j <= num_cols; j++) {
            transposed[j, i] = nums[j]
            if (j > max_cols) { max_cols = j }
            if (i > max_rows) { max_rows = i }
        }
    }
}

END {
    # Build the transposed matrix string
    output = ""
    for (j = 1; j <= max_cols; j++) {
        output = output "["

        for (i = 1; i <= max_rows; i++) {
            output = output transposed[j, i]
            if (i < max_rows) {
                output = output ","
            }
        }

        output = output "]"
        if (j < max_cols) {
            output = output ","
        }
    }

    print output
}
'
```

### How It Works

1. **Input Validation**: The script first checks if exactly one argument is provided. If not, it displays usage instructions and exits.

2. **Parsing the Matrix**:
    - **Field Separator (`FS`)**: The `awk` script sets the field separator to `"],["` to split the input string into individual rows.
    - **Cleaning Brackets**: It removes the leading `[` from the first row and the trailing `]` from the last row to simplify processing.
    - **Splitting Rows and Columns**: It splits the input into rows and then splits each row into individual numbers, storing them in a two-dimensional array `transposed`.

3. **Transposing the Matrix**:
    - It iterates over the `transposed` array to build the transposed matrix string.
    - The output is constructed in the format `"[1,3,5],[2,4,6]"` for the input `"[1,2],[3,4],[5,6]"`.

4. **Output**: Finally, the transposed matrix string is printed.

### Usage

1. **Save the Script**: Save the above script to a file named `transpose_matrix.sh`.

2. **Make It Executable**:
    ```bash
    chmod +x transpose_matrix.sh
    ```

3. **Run the Script**:
    ```bash
    ./transpose_matrix.sh '[1,2],[3,4],[5,6]'
    ```

    **Output**:
    ```
    [1,3,5],[2,4,6]
    ```

### Additional Examples

- **Example 1**:
    ```bash
    ./transpose_matrix.sh '[1,2,3],[4,5,6]'
    ```
    **Output**:
    ```
    [1,4],[2,5],[3,6]
    ```

- **Example 2**:
    ```bash
    ./transpose_matrix.sh '[7,8],[9,10],[11,12]'
    ```
    **Output**:
    ```
    [7,9,11],[8,10,12]
    ```

### Notes

- **Matrix Validation**: This script assumes that the input matrix is well-formed, meaning all rows have the same number of columns and are properly enclosed in square brackets and separated by commas.
  
- **Dependencies**: The script uses standard Unix tools (`bash` and `awk`) and doesn't require any external dependencies.

Feel free to integrate this script into your workflows or modify it to handle different input formats as needed!
# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 '[row1],[row2],...[rowN]'"
    echo "Example: $0 '[1,2],[3,4],[5,6]'"
    exit 1
fi

input="$1"

# Use awk to parse and transpose the matrix
echo "$input" | awk '
BEGIN {
    # Set the field separator to "],[" to split rows
    FS = "\\],\\["
}

{
    # Remove leading '[' from the first row and trailing ']' from the last row
    gsub(/^\[/, "", $0)
    gsub(/\]$/, "", $0)

    # Split the input into rows
    num_rows = split($0, rows, "],[")

    # Iterate over each row
    for (i = 1; i <= num_rows; i++) {
        # Split row into individual numbers
        num_cols = split(rows[i], nums, ",")

        # Iterate over each number and assign to the transposed matrix
        for (j = 1; j <= num_cols; j++) {
            transposed[j, i] = nums[j]
            if (j > max_cols) { max_cols = j }
            if (i > max_rows) { max_rows = i }
        }
    }
}

END {
    # Build the transposed matrix string
    output = ""
    for (j = 1; j <= max_cols; j++) {
        output = output "["

        for (i = 1; i <= max_rows; i++) {
            output = output transposed[j, i]
            if (i < max_rows) {
                output = output ","
            }
        }

        output = output "]"
        if (j < max_cols) {
            output = output ","
        }
    }

    print output
}
'
```

### How It Works

1. **Input Validation**: The script first checks if exactly one argument is provided. If not, it displays usage instructions and exits.

2. **Parsing the Matrix**:
    - **Field Separator (`FS`)**: The `awk` script sets the field separator to `"],["` to split the input string into individual rows.
    - **Cleaning Brackets**: It removes the leading `[` from the first row and the trailing `]` from the last row to simplify processing.
    - **Splitting Rows and Columns**: It splits the input into rows and then splits each row into individual numbers, storing them in a two-dimensional array `transposed`.

3. **Transposing the Matrix**:
    - It iterates over the `transposed` array to build the transposed matrix string.
    - The output is constructed in the format `"[1,3,5],[2,4,6]"` for the input `"[1,2],[3,4],[5,6]"`.

4. **Output**: Finally, the transposed matrix string is printed.

### Usage

1. **Save the Script**: Save the above script to a file named `transpose_matrix.sh`.

2. **Make It Executable**:
    ```bash
    chmod +x transpose_matrix.sh
    ```

3. **Run the Script**:
    ```bash
    ./transpose_matrix.sh '[1,2],[3,4],[5,6]'
    ```

    **Output**:
    ```
    [1,3,5],[2,4,6]
    ```

### Additional Examples

- **Example 1**:
    ```bash
    ./transpose_matrix.sh '[1,2,3],[4,5,6]'
    ```
    **Output**:
    ```
    [1,4],[2,5],[3,6]
    ```

- **Example 2**:
    ```bash
    ./transpose_matrix.sh '[7,8],[9,10],[11,12]'
    ```
    **Output**:
    ```
    [7,9,11],[8,10,12]
    ```

### Notes

- **Matrix Validation**: This script assumes that the input matrix is well-formed, meaning all rows have the same number of columns and are properly enclosed in square brackets and separated by commas.
  
- **Dependencies**: The script uses standard Unix tools (`bash` and `awk`) and doesn't require any external dependencies.

Feel free to integrate this script into your workflows or modify it to handle different input formats as needed!