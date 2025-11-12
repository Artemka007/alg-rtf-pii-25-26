class HashedStr(str):
    prefix_hash = []
    power = []
    mod = 10**18 + 3
    p = 29

    def __init__(self, s):
        super().__init__()
        self._compute_prefix_hashes()

    def _compute_prefix_hashes(self):
        n = len(self)
        self.prefix_hash = [0] * (n + 1)
        self.power = [1] * (n + 1)

        for i in range(n):
            self.prefix_hash[i+1] = (self.prefix_hash[i] * self.p + (ord(self[i]) - ord('a') + 1)) % self.mod
            self.power[i+1] = (self.power[i] * self.p) % self.mod

    def get_substr_hash(self, start, length):
        hash_val = (self.prefix_hash[start + length] - self.prefix_hash[start] * self.power[length]) % self.mod
        return hash_val if hash_val >= 0 else hash_val + self.mod

    def __hash__(self):
        return self.get_substr_hash(0, len(self))