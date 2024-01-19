class Solution:
    def isFascinating(self, n: int) -> bool:
        
        dic = {}
        a = n*2
        b = n*3
        lis = list()
        lis.append(str(n))
        lis.append(str(a))
        lis.append(str(b))
        st_r = ''.join(lis)
        for i in st_r:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                
        for i in range(1,10):
            a = str(i)
            digit_count = dic.get(a,0)
            if digit_count != 1:
                return False
        return True
            

        


        