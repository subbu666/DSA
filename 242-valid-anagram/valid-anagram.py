class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_list=[0]*26
        for i in s:
            ord_value=ord(i)
            idx_value=ord_value-97
            hash_list[idx_value]+=1
        # print(hash_list)
        for i in t:
            ord_value=ord(i)
            idx_value=ord_value-97
            hash_list[idx_value]-=1
        return hash_list.count(0)==26
            