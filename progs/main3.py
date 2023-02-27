
class Stack:
    def __init__(self):
        self.__stack_list = [] #One private attribute
    #Two methods
    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self) #Inherit init from the superclass
        self.__sum = 0

    #Add functionality to an existing method! 
    def get_sum(self):
        return self.__sum 

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
    
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val

stack_object_1 = Stack()
stack_object_2 = AddingStack()

stack_object_2.push(3)
stack_object_2.push(5)
stack_object_2.push(2)

print(stack_object_2.get_sum())

