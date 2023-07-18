from Session10_Stack import Stack,ScreenInterface
def main():

    interface1 = ScreenInterface("App Home Page")
    interface2 = ScreenInterface("Product 1 Page")
    interface3 = ScreenInterface("Product 2 Page")

    stack = Stack()
    stack.push(interface1)
    stack.push(interface2)
    stack.push(interface3)

    stack.iterate()
    stack.pop()
    stack.pop()
    print("*************************")
    stack.iterate()
    print("*************************")
    stack.pop()
    print("*************************")
    stack.iterate()
    print("*************************")
    print("Stack: ",vars(stack))

if __name__ =="__main__":
    main()