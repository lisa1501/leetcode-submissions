# DSU, time: O((n*m)log(n*m)) space:O(n*m)

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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        email_to_acc = {} # email to account idx

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in email_to_acc:
                    dsu.union(i, email_to_acc[e])
                else:
                    email_to_acc[e] = i

        email_group = defaultdict(list)

        for e, i in email_to_acc.items():
            leader = dsu.find(i)
            email_group[leader].append(e)

        res = []
        for i, emails in email_group.items():
            name = accounts[i][0]
            res.append([name] + sorted(email_group[i]))

        return res

        