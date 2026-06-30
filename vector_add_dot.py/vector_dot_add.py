class vector_dot_add:
    def __init__(self,vector):
        self.vector = vector
    
        
    def __add__(self, other):
        new_vector = []
        for i in range(0,3):
            new_vector.append( self.vector[i] + other.vector[i])
            
        return vector_dot_add(new_vector)
    
    def __str__(self):
        return f"{self.vector[0]}i+{self.vector[1]}j+{self.vector[2]}K"
    
                
                   
    
    
    def __mul__(self, other):
        result = 0
        for i in range(0,3):
            result += self.vector[i]*other.vector[i]
        return result
        
            


        
            
    
v1 =vector_dot_add([4,5,6])
v2 = vector_dot_add([9,3,5])
v3 = v1 + v2
print(v3)    
v1 =vector_dot_add([4,9,8])
v2 = vector_dot_add([7,9,7])
v3 = v1 * v2
print(v3)
    
            

        
