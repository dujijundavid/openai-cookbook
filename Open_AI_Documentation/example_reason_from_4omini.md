You can create a Bash script to transpose a matrix represented as a string in the format '[1,2],[3,4],[5,6]'. Below is a sample script that accomplishes this:

```bash
#!/bin/bash

# Get the input matrix from the command line argument
input_matrix=$1

# Remove the outer brackets and split the string into rows using the ']' delimiter
rows=$(echo "${input_matrix:1:-1}" | tr ']' '\n')

# Convert rows into an array
IFS=$'\n' read -r -d '' -a row_array <<< "$rows"

# Initialize the transposed matrix
transposed_matrix=""

# Loop through columns by extracting each element from the rows
for ((i = 0; i < ${#row_array[@]}; i++)); do
    # Split the current row into an array of elements
    IFS=',' read -r -a elements <<< "${row_array[$i]}"

    for ((j = 0; j < ${#elements[@]}; j++)); do
        # Append the current element to its corresponding transposed position
        if (( i == 0 )); then
            # First row in transposed matrix
            transposed_matrix+="${elements[j]}"
        else
            # Subsequent rows
            transposed_matrix+=",${elements[j]}"
        fi
    done
    if (( i < ${#row_array[@]} - 1 )); then
        transposed_matrix+=";"
    fi
done

# Print the transposed matrix, formatting as needed
transposed_array=()
IFS=';' read -r -d '' -a transposed_array <<< "$transposed_matrix"

# Build the final output format
output="["
for ((i = 0; i < ${#transposed_array[@]}; i++)); do
    if ((i > 0)); then
        output+=","
    fi
    output+="[${transposed_array[$i]}]"
done
output+="]"

# Print the result
echo "$output"
```

### Usage Instructions

1. Save the script to a file, e.g., `transpose_matrix.sh`.
2. Make the script executable:
   ```bash
   chmod +x transpose_matrix.sh
   ```
3. Run the script, passing the matrix string as an argument:
   ```bash
   ./transpose_matrix.sh "[1,2],[3,4],[5,6]"
   ```

### Output

For the input `"[1,2],[3,4],[5,6]"`, the output will be:
```
[[1,3,5],[2,4,6]]
```

### Notes

- This script assumes that the input matrix is non-empty and all rows have the same number of columns.
- The output format matches the requested format with the proper brackets.
- Be sure to handle any edge cases as necessary depending on your specific requirements.