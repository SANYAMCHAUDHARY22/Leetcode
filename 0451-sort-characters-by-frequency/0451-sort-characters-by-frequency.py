class Solution:
    def frequencySort(self, s: str) -> str:
	    sCounter = Counter(s)
	    result = []
	    for key, value in sorted(sCounter.items(), key=lambda x:x[1], reverse=True):
		    result.append(key*value)
	    return ''.join(result)
        