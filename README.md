# Codewars

So! Yes. What else should I say? I just want to play and feel the emotion of those green ticks. And also learn more of Python in the way. Here I will write some tips or clever answers. Main goal: solve the kata. Second main goal: learn how to solve it better. 

Here we go! 

Disclaimer: There won't be a lot of scripts. It will be more a loooong readme. 

[This](https://www.codewars.com/users/ariasAleia) is how far I am til now. 


## Kata: Counting sheep...

My solution. I works but can be better.

```python
def count_sheeps(sheep):
    total = 0
    for animal in sheep:
        if animal: total += 1
    return total
```
Clever and better way:

```python
def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)
```

Lesson: Count is better to count. Obvious, isn't it? :P

## Kata: Convert boolean values to strings 'Yes' or 'No'.

My approach:

```python
def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    return 'No'
```

Another approach. Interesting how lines can be shorter. 
```python
def bool_to_word(bool):
    return "Yes" if bool else "No"
```

## Kata: You Can't Code Under Pressure #1

(Like the tittle hehe)

My approach: A normal one

```python
def doubleInteger(i):
    return i * 2
```
Better: Thinking hardwarish
```python
def doubleInteger(i):
    return i << 1
```
That would be really useful if we gotta take care of the speed

## Kata: Convert a string to an array

My attempt. It works but it can be definitely way better. (You can see how my C programming comes haha but ok, Python gives us a shortcut)

```python
def string_to_array(s):
    array = []
    inicio = 0
    for i, letter in enumerate(s):
        if letter == ' ':
            array.append(s[inicio:i])
            inicio = i+1
    array.append(s[inicio:len(s)])
    return array
```

Shorter way: Convert a string to an array

```python
def string_to_array(string):
    return string.split(" ")
```

The parameter is the delimiter. If we don't specify it, it will be the whitespace by default. If the string is empty, it returns []. 

## Kata: Simple multiplication

Mine:
```python
def simple_multiplication(number) :
    if number % 2:
        return number * 9
    return number * 8
```

No conditionals. Clever answer:
```python
def simple_multiplication(n) :
    return n * (8 + n%2)
```

## Kata: Even or Odd

My approach. A classic one.

```python
def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'
```

Be creative. What if there are no ifs...
```python
def even_or_odd(number):
  return ["Even", "Odd"][number % 2]
```
Cool way to take an element from a list that we just created


## Kata: Convert number to reversed array of digits

My not so effective approach (really C):

```python
def digitize(n):
    if n:
        array = []
        while n > 0:
            array.append(n % 10)
            n //= 10
        return array
    return [0]
```


Shorter and better way:

```python
def digitize(n):
    return [int(x) for x in reversed(str(n))]
```

**Important note:** Reversed returns sth backwards. That's they only thing it does. 

On the other hand, sorted, as the name says, sorts the elements in a collection. It has a boolean argument called reverse

## Kata: How good are you really?


Mine:
```python
def better_than_average(class_points, your_points):
    average = your_points
    for point in class_points:
        average += point
    average/= len(class_points) + 1
    return your_points > average
```


Function sum is a built-in function. Use it whenever you need it.

```python
def better_than_average(class_points, your_points):
    average = (sum(class_points) + your_points) / (len(class_points) + 1)
    return your_points > average
```

## Kata: Transportation on vacation

In this case, I liked the way my answer looks.
```python
def rental_car_cost(d):
    return d*40 - 20*(d>2) - 30*(d>6)
```

Other maybe more clear but not so short or cool answers:

```python
def rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result
```