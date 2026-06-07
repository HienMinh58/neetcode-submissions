class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        cntS1 = [0] * 26
        cntS2 = [0] * 26

        for i in range(window):
            cntS1[ord(s1[i]) - ord('a')] += 1
        for i in range(len(s2)):
            cntS2[ord(s2[i]) - ord('a')] += 1
            
            if i >= window:
                cntS2[ord(s2[i - window]) - ord('a')] -= 1
                
            if cntS1 == cntS2:
                return True
        return False
