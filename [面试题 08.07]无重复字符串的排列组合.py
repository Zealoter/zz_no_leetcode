class Solution:
    def permutation(self, S: str) -> List[str]:
        len_s=len(S)
        flag=[0]*len_s
        ans=[]
        def fun(now_str,num):
            if num==len_s:
                ans.append(now_str)
            for i in range(len_s):
                if flag[i]==0:
                    flag[i]=1
                    fun(now_str+S[i],num+1)
                    flag[i]=0
        fun('',0)
        return ans