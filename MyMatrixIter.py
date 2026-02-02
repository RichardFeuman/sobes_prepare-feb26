class RowWiseIter:
    def __init__(self, mat):
        self.mat = mat 
        self.ci = 0 
        self.ri = 0
    
    def __iter__(self):
        return self
        
    
    def __next__(self):
        while self.ri < len(self.mat):

            elem = self.mat[self.ri][self.ci]
            if self.ci == len(self.mat[0]) - 1:
                self.ri+=1
                self.ci =0 
            
            self.ci+=1
            return elem

        else:
            raise StopIteration
                
my_ri = RowWiseIter([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

for elem in my_ri:
    print(elem)
