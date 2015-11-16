def sort(stack):
    buf = []
    
    while len(stack):
        v = stack.pop()
        while len(buf) and v < buf[-1]:
            stack.append(buf.pop())
        buf.append(v)

    return buf

if __name__ == "__main__":
    stack = [3, 6, 1, 7, 2, 4, 1]
    print(sort(stack))
