# def string_to_array(s):
#     array = []
#     inicio = 0
#     for i, letter in enumerate(s):
#         if letter == ' ':
#             array.append(s[inicio:i])
#             inicio = i+1
#     array.append(s[inicio:len(s)])
#     return array

def string_to_array(s):
    return s.split(" ")


def main():
    print(digitize(16786982))
    
def digitize(n):
    return [int(x) for x in reversed(str(n))]

def digitize2(n):
    array = []
    for digit in str(n):
        array.append(digit)
    if n:
        array = []
        while n > 0:
            array.append(n % 10)
            n //= 10
        return array
    return [0]
            
if __name__ == '__main__':
    main()
            
