def process_grid(grid):
    # Split the input into individual grids
    grids = grid.strip().split('\n\n')
    
    # Function to transform a single grid
    def transform_grid(lines):
        num_rows = len(lines)
        max_len = max(len(line) for line in lines)
        transformed = [['.' for _ in range(max_len)] for _ in range(num_rows)]
        
        # List to keep track of which columns have been used
        used_columns = set()
        
        for row_idx, line in enumerate(lines):
            stars = line.count('*')
            col_idx = max_len - 1
            for _ in range(stars):
                # Find the next available column from the right
                while col_idx in used_columns:
                    col_idx -= 1
                if col_idx >= 0:
                    transformed[row_idx][col_idx] = '*'
                    used_columns.add(col_idx)
                    col_idx -= 1
        
        return [''.join(row) for row in transformed]

    # Process each grid and apply the transformation
    transformed_grids = []
    for grid in grids:
        lines = grid.split('\n')
        transformed_grid = transform_grid(lines)
        transformed_grids.append('\n'.join(transformed_grid))
    
    # Combine all transformed grids into the final output
    result = '\n\n'.join(transformed_grids)
    return result

if __name__ == "__main__":
    import sys
    import fileinput

    input_lines = []
    for line in fileinput.input():
        input_lines.append(line)
    
    input_data = ''.join(input_lines)
    output = process_grid(input_data)
    print(output)
