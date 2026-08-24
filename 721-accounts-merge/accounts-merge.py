class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [1] * (n+1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu

        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)

        email_to_idx = defaultdict(int)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_to_idx:
                    email_to_idx[email] = i
                else:
                    dsu.union(i, email_to_idx[email])

        leader_to_emails = defaultdict(list)

        for email,idx in email_to_idx.items():
            leader_idx = dsu.find(idx)
            leader_to_emails[leader_idx].append(email)

        res = []
        for leader_idx, eamils in leader_to_emails.items():
            name = accounts[leader_idx][0]
            res.append([name] + sorted(leader_to_emails[leader_idx]))

        return res
        