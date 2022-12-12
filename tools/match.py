class Match:
    def __init__(self, country1, country2, flag1, flag2, max_score):
        # 1080 x 1920
        self.country1 = country1
        self.country2 = country2
        self.flag1 = flag1
        self.flag2 = flag2
        self.max_score = max_score

    def __str__(self):
        return f'{self.flag1} {self.country1.upper()} vs {self.flag2} {self.country2.upper()}'

    def possibilities(self):
        res = []
        for i in range(self.max_score + 1):
            for j in range(self.max_score + 1):
                res.append(f"{self.country1.upper()} {self.flag1} {i} - {j} {self.flag2} {self.country2.upper()}")
        return res
