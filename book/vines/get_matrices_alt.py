import os
import numpy as np

def get_matrices(matrix_dir):
   
    files = [f for f in os.listdir(matrix_dir) if f.endswith('.csv')]

    matrices = []

    # Process each CSV file in the directory
    for file in files:
        file_path = os.path.join(matrix_dir, file)
        mat = np.loadtxt(file_path, dtype=int, delimiter=',')  # Load CSV as matrix

        # Flip the matrix along the rows (axis=0)
        flipped_mat = np.flip(mat, axis=0)

        # Index the matrix in blocks of 4 rows
        mat_idx = list(range(0, len(flipped_mat) + 1, 4))
        for i in range(len(mat_idx) - 1):
            matrices.append(flipped_mat[mat_idx[i]:mat_idx[i + 1]])

    return matrices
