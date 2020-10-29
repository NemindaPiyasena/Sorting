class QuikSort:

    def __init__(self,arr,key=None):

        if key is None:
            key=lambda x:x
        self.arr=arr
        self.key=key

    def partion(self,pivot,left=0,right=None):

        if right is None:
            right=len(self.arr)-1

        leftptr=left-1
        rightptr=right+1

        while True:

            while leftptr<right:
                leftptr += 1
                if pivot>self.arr[leftptr]:
                    continue
                else:
                    break

            while left<rightptr:
                rightptr -= 1
                if pivot<=self.arr[rightptr]:
                    continue
                else:
                    break

            if leftptr>=rightptr:
                break
            else:
                self.arr[leftptr],self.arr[rightptr]=self.arr[rightptr],self.arr[leftptr]
        return leftptr

    def sort(self,left,right):

        if right-left<=0:
            return None
        else:
            pivot=self.arr[right]
            partition=self.partion(pivot,left,right)
            self.arr[partition],self.arr[right]=self.arr[right],self.arr[partition]
            self.sort(left,partition-1)
            self.sort(partition+1,right)



o=[0,1,0]
q=QuikSort(o)
print(o)
print(q.sort(0,len(o)-1))
print(o)

