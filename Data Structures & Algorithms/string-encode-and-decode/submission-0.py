class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded
    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            print("I is : " + str(i))
            j = i
            while j < len(s):
                if s[j] == '#':
                    print("J is :" + str(j))
                    print("s[j] is :" + str(s[j]))
                    length = s[i:j]
                    print("length is : " + str(length))
                    result.append(s[j+1:j+1 + int(length)])
                    break
                j += 1
            
            i = j+ 1 +int(length)
        return result

