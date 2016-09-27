class minstack(list):
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        self.min_value=0
        

    def push(self, value):
        
        if(len(self.stack) == 0):
            self.min_value=value

        self.stack.append(value) 
        if(self.min_value > value):
            self.min_value= value
            self.min_stack.append(self.min_value)
            
            


    def pop(self):
        result=self.stack.pop()
        if(result == self.min_value):
            self.min_stack.pop()
            self.min_value= self.min_stack[-1]
        return result

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_value


s= minstack();
s.push(2)
s.push(1)
s.push(8)
s.push(0)
s.pop()
print("Minimum in the stack is " + str(s.min()))
print("Top of the stack"+ str(s.top()))
            
            
        
