class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Compter les chars de t
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        freq = {}
        left = 0
        minLen = float('inf')
        result = ""
        matched = 0
        total = len(countT)  # nombre de chars distincts à matcher

        for right in range(len(s)):
            # Ajouter s[right] à freq si dans countT
            if s[right] in countT:
                freq[s[right]] = freq.get(s[right], 0) + 1
                # on vient d'atteindre le bon compte pour ce char
                if freq[s[right]] == countT[s[right]]:
                    matched += 1

            # Si valide on essaie de réduire left
            while matched == total:
                # Update si meilleur
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    result = s[left:right+1]

                # Retirer left de freq et avancer
                if s[left] in countT:
                    if freq[s[left]] == countT[s[left]]:
                        matched -= 1
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        freq.pop(s[left])

                left += 1

                # Avancer left jusqu'au prochain char dans countT
                while left <= right and s[left] not in countT:
                    left += 1

        return result
