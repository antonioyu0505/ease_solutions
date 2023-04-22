from sys import stdin

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def dfs(matrix, x, y, memo, n , m):
    if(memo[x][y]):
        return memo[x][y]

    current_value = matrix[x][y]
    longest_path = [current_value]
    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if(0 <= next_x < n and 0 <= next_y < m and matrix[next_x][next_y] < current_value):
            next_path = [current_value] + dfs(matrix, next_x, next_y, memo, n, m)
            if(len(next_path) > len(longest_path) or len(next_path) == len(longest_path) and next_path[0] - next_path[-1] > longest_path[0] - longest_path[-1]):
                longest_path = next_path
    memo[x][y] = longest_path
    return longest_path

def longest_descending_path(matrix, n, m):
    memo = [[None for _ in range(m)] for _ in range(n)]
    longest_path = []
    for i in range(n):
        for j in range(m):
            local_path = dfs(matrix, i, j, memo, n, m)
            if(len(local_path) > len(longest_path) or len(local_path) == len(longest_path) and local_path[0] - local_path[-1] > longest_path[0] - longest_path[-1]):
                longest_path = local_path
    return longest_path

def main():
    line = stdin.readline().strip()
    size_n, size_m = [int(i) for i in line.split()]
    line = stdin.readline().strip()
    matrix = []
    while(line != ''):
        matrix_line = [int(i) for i in line.split()]
        matrix.append(matrix_line)
        line = stdin.readline().strip()
    longest_path = longest_descending_path(matrix, size_n, size_m)
    print(f"Length of calculated path: {len(longest_path)}")
    print(f"Drop of calculated path: {longest_path[0] - longest_path[-1]}")
    print(f"Calculated path: {'-'.join(str(i) for i in longest_path)}")
main()