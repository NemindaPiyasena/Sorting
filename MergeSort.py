class MergeSort:

    def __init__(self,arr,key=None):

        if key is None:
            key=lambda x:x
        self.key=key
        self.arr=arr

    def sort(self,init,end):

        if init==end:
            return end
        dev = (init + end) // 2
        a=self.sort(init,dev)
        b=self.sort(dev+1,end)
        self.merge(init,a,b)
        return end

    def merge(self,init,a,b):

        adex=init
        bdex=a+1
        arr=[]
        while adex<a+1 and bdex<b+1:

            if self.key(self.arr[adex])<=self.key(self.arr[bdex]):
                arr.append(self.arr[adex])
                adex+=1
            else:
                arr.append(self.arr[bdex])
                bdex += 1


        while adex<a+1:
            arr.append(self.arr[adex])
            adex += 1

        while bdex<b+1:
            arr.append(self.arr[bdex])
            bdex += 1
        i=init
        for item in arr:
            self.arr[i]=item
            i+=1



if __name__=='__main__':
    li=['peach','straw','apple','spork']
    print(li)
    m=MergeSort(li,key=lambda x:x[0])
    m.sort(0,len(li)-1)
    print(li)