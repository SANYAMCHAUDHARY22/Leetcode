class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        g = defaultdict(dict)
        for p1, p2, t in meetings:
            g[t][p1] = g[t].get(p1, [])
            g[t][p1].append(p2)
            g[t][p2] = g[t].get(p2, [])
            g[t][p2].append(p1)
        known = {0, firstPerson}
        for t in sorted(g.keys()):
            seen = set()
            for p in g[t]:
                if p in known and p not in seen:
                    q = deque([p])
                    seen.add(p)
                    while q:
                        cur = q.popleft()
                        for nxt in g[t][cur]:
                            if nxt not in seen:
                                q.append(nxt)
                                seen.add(nxt)
                                known.add(nxt)
        return known