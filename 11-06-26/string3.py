class Solution(object):
    def maskPII(self, s):
        if "@" in s:
            s = s.lower()
            name, domain = s.split("@")
            return name[0] + "*****" + name[-1] + "@" + domain

        digits = "".join(c for c in s if c.isdigit())
        country = len(digits) - 10

        if country == 0:
            return "***-***-" + digits[-4:]

        return "+" + "*" * country + "-***-***-" + digits[-4:]
