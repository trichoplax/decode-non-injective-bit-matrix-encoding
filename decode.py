import sys

from math import floor

args = [int(arg) for arg in sys.argv[1:]]

size = args[0]
line_ones = args[1 : 1+size]
column_ones = args[1+size : 1+size*2]
main_diagonal_ones = args[1 + size*2]
antidiagonal_ones = args[2 + size*2]
quadrant_ones = args[3+size*2 : 7+size*2]
line_transitions = args[7+size*2 : 7+size*3]
column_transitions = args[7+size*3 : 7+size*4]


def all_bit_matrices(n):
    """Generate all n by n binary matrices."""
    matrix = [0] * size * size
    last = [1] * size * size
    while True:
        yield matrix
        if matrix == last:
            break
        matrix = next_matrix(matrix)


def next_matrix(m):
    """Return the matrix corresponding to the next binary string after m."""
    if m[-1] == 0:
        return m[: -1] + [1]
    return next_matrix(m[: -1]) + [0]


def matrix_encodes_to_encoding(m):
    """Return True if m encodes to the encoding."""
    return all((
        lines_match(m),
        columns_match(m),
        main_diagonal_matches(m),
        antidiagonal_matches(m),
        quadrants_match(m),
        line_transitions_match(m),
        column_transitions_match(m),
    ))


def lines_match(m):
    """Return True if m has the correct number of 1s per line."""
    return all(
        line_ones[j] == sum(m[i + j*size] for i in range(size))
        for j in range(size)
    )


def columns_match(m):
    """Return True if m has the correct number of 1s per column."""
    return all(
        column_ones[i] == sum(m[i + j*size] for j in range(size))
        for i in range(size)
    )


def main_diagonal_matches(m):
    """Return True if m has the correct number of 1s in the main diagonal."""
    return main_diagonal_ones == sum(m[i * (size+1)] for i in range(size))


def antidiagonal_matches(m):
    """Return True if m has the correct number of 1s in the antidiagonal."""
    return antidiagonal_ones == sum(
        m[i * size + size - i - 1] for i in range(size)
    )


def quadrants_match(m):
    """Return True if m has the correct number of 1s per quadrant."""
    return all((
        quadrant_ones[0] == sum(
            m[i + j*size]
            for j in range(floor(size/2))
            for i in range(floor(size/2))
        ),
        quadrant_ones[1] == sum(
            m[i + j*size]
            for j in range(floor(size/2))
            for i in range(floor(size/2), size)
        ),
        quadrant_ones[2] == sum(
            m[i + j*size]
            for j in range(floor(size/2), size)
            for i in range(floor(size/2))
        ),
        quadrant_ones[3] == sum(
            m[i + j*size]
            for j in range(floor(size/2), size)
            for i in range(floor(size/2), size)
        ),
    ))


def line_transitions_match(m):
    """Return True if m has the correct number of 1s per line."""
    return all(
        line_transitions[j] == sum(
            abs(m[i + j*size] - m[i + 1 + j*size]) for i in range(size - 1)
        )
        for j in range(size)
    )


def column_transitions_match(m):
    """Return True if m has the correct number of 1s per column."""
    return all(
        column_transitions[i] == sum(
            abs(m[i + j*size] - m[i + (j+1)*size]) for j in range(size - 1)
        )
        for i in range(size)
    )


def string_representation_of_matrix(m):
    """Return a newline separated string of space separated strings."""
    return "\n".join(
        " ".join(
            str(value) for value in m[i : i+size]
        ) for i in range(0, len(m), size)
    )


decoded_matrices = [
    m for m in all_bit_matrices(size) if matrix_encodes_to_encoding(m)
]

print(len(decoded_matrices))
print(
    "\n\n".join(string_representation_of_matrix(m) for m in decoded_matrices)
)
