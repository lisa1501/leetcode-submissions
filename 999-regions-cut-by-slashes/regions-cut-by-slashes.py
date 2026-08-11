class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        # every node is root of itself, 
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        # we are unioning child and parent, if child and parent has same parent, this is impossible, this means there is a cycle in grandparent, parent, child, so this is not tree,
        if pu == pv:
            return False

        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)

        # Each cell has 4 triangles
        dsu = DSU(4 * n * n) # DSU(16)

        def get_id(r, c, part):
            return (r * n + c) * 4 + part

        for r in range(n):
            for c in range(n):
                # r=0,c=0
                # Current cell's 4 triangles
                top = get_id(r, c, 0) #0
                right = get_id(r, c, 1) #1
                bottom = get_id(r, c, 2) #2
                left = get_id(r, c, 3) #3

                # Connect parts inside the cell
                if grid[r][c] == ' ':
                    # No slash
                    dsu.union(top, right)
                    dsu.union(right, bottom)
                    dsu.union(bottom, left)
                elif grid[r][c] == '/':
                    # / separates top-left from bottom-right
                    dsu.union(top, left)
                    dsu.union(right, bottom)
                else:  # '\'
                    # \ separates top-right from bottom-left
                    dsu.union(top, right)
                    dsu.union(bottom, left)

                # Connect to cell above
                if r > 0:
                    dsu.union(top, get_id(r - 1, c, 2)) #2:bottom
    
                # Connect to cell below
                if r < n - 1:
                    dsu.union(bottom, get_id(r + 1, c, 0)) #0:top
                    
                # Connect to cell on the left
                if c > 0:
                    dsu.union(left, get_id(r, c - 1, 1)) #1:right
                    
                # Connect to cell on the right
                if c < n - 1:
                    dsu.union(right, get_id(r, c + 1, 3)) #3:left
                    
        # Count distinct roots
        return len({
            dsu.find(i)
            for i in range(4 * n * n)
        })