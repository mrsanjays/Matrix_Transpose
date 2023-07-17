class Solution:
    def Matrix_Transpose(self,array,row):
        col=len(array[0])
        trans=[[0 for _ in range(row)] for _ in range(col)]
        for i in range(row):
            for j in range(col):
                trans[j][i]=array[i][j]
        return trans
if __name__ == '__main__':
    row=int(input())
    array=[]
    for i in range(row):
        col=list(map(int,input().split()))
        array.append(col)
    print(*Solution().Matrix_Transpose(array,row))

