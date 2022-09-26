# Codewars

So! Yes. What else should I say? I just want to play and feel the emotion of those green ticks. And also learn more of Python in the way. Here I will write some tips or clever answers. Main goal: solve the kata. Second main goal: learn how to solve it better. 

Here we go! 

Disclaimer: There won't be a lot of scripts. It will be more a loooong readme. 

[This](https://www.codewars.com/users/ariasAleia) is how far I am til now. 

And super hiper mega important! Rememeber to think and ask yourself...

* **How can this be easier?** (applies also for real life :P)
* **Is there a more pythonic way?**

**And to do that we can find a more simple way to achieve the same things. Think more like a computer. Think more in python. Use the tools you have and create magic.**

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

## Kata: Jaden Casing Strings

My answer (again like C):

```python
def to_jaden_case(string):
    array = string.split()
    for i, word in enumerate(array):
        array[i] = word[0].upper() + word[1:len(word)].lower()
        print(array[i])
    return " ".join(array)
```

Again another python function that looks to be really useful: capitalize

```python
def to_jaden_case(string):
    return ' '.join([x.capitalize() for x in string.split()])
```

I have realized sth. I tend to try to do things the way I know. I've done sth like that almost the whole of my life. And most of the time things work. The question is: Can things be easier? Can I achieve the same results making less effort and still learning? 

I think the answer is yes. And as one interesting person once said: Pain is there but suffering is an option. I want to open my mind and begin to learn from others. Seeing further standing on the shoulders of giants. 

## Kata: String to number and viceversa

This will be short: *int(variable)* or *str(variable)*

## Kata: Basic Mathematical Operations

My not at all efficient but listish approach:

```python
def basic_op(operator, value1, value2):
    op = ['+', '-', '*', '/']
    ans = [value1 + value2,
          value1 - value2,
          value1 * value2,
          value1 / value2]
    return ans[op.index(operator)]
```

A really interesting function: *eval*

```python
def basic_op(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')
```

Basically we run whatever is inside the function. That sounds great but... What happens if suddenly sb writes sth like: Erase the whole memory of the pc. Or... change passwords or whatever. That would be like a dangerous sudo power (linux mind :P) So! Great power comes with great responsibility.


## Kata: Regex validate PIN code

A little bit more pythonic with *in*. But anyway there is a better solution...

```python
def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for digit in pin:
            if not digit in "1234567890":
                return False
        return True        
    return False
```

Like this:

```python
def validate_pin(pin):
    return pin.isdigit() and len(pin) in (4, 6)
```

## Kata: Calculate BMI

Remember that to calculate power we use ** . For example 3**2 = 9

## Kata: Beginner - Lost Without a Map

My approach:

```python
def maps(a):
    b = []
    for number in a:
        b.append(number * 2)
    return b
```

Faster and better:
```python
def maps(a):
    return [x*2 for x in a]
```

## Kata: Are You Playing Banjo?

```python
def are_you_playing_banjo(name):
    a = name.capitalize()[0]
    if a == 'R': return name + " plays banjo"
    return name + " does not play banjo"
```

That was not bad but... this is shorter

```python
def are_you_playing_banjo(name):
    if name[0].upper() == 'R': return name + " plays banjo"
    return name + " does not play banjo"
```


## Kata: Sum of two lowest positive integers

```python
def sum_two_smallest_numbers(numbers):
    a = numbers.pop(numbers.index(min(numbers)))
    return a + numbers.pop(numbers.index(min(numbers)))
```

But.. IF we organize then everything could be shorter but!!! Maybe it takes longer to sort all and maybe it is way easier to find the minimum value. So... It's all a tradeoff. But anyway this looks better:

```python
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[0:2])
```


## Kata: Mumbling

Again.. My approach works and that's important

```python
def accum(s):
    array = []
    for i, letter in enumerate(s):
        array.append(letter.lower()*(i+1))
        array[i] = array[i].capitalize()
    return "-".join(array)
```

But this is easier and I think it is also faster:
```python
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
```
And.. I think that the only thing that we are missing is asking us two questions:


* **How can this be easier?**
* **Is there a more pythonic way?**

**And to do that we can find a more simple way to achieve the same things. Think more like a computer. Think more in python. Use the tools you have and create magic.**


## Kata: Odd or Even?

We are learning! Both solutions were great and we thought them for ourselves!

More in a list:
```python
def oddOrEven(arr):
    return ('even', 'odd')[sum(arr) % 2]
```

Shorter return with conditionals:
```python
def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'
```


## Kata: Square sum

Important! Well done. Every time you have a for loop. Try to turn it into sth shorter. Looks more elegant and looks more pythonic!

At first we thought about sth like this:
```python
def square_sum(numbers):
    ans = 0
    for i in numbers:
        ans += i**2
    return ans
```

But it we see carefully we can turn it into a beautiful one line code:
```python
def square_num(numbers):
    return sum([i**2 for i in numbers])
```

:D Well done :)

## Kata: DNA

And that's why it is much much much better to practice a lot after learning a little bit of theory than learning a lot of theory and practicing too little. Here to solve this, we knew that it was necessary (ok.. not mandatory) to use a dictionary.

Here we are!

```python
def DNA_strand(dna):
    letters = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return "".join(letters.get(x) for x in dna)
```

And it works! Yes. But hey! We don't have to display the dictionary in a vertical way. We can also display it horizontally and we can use get or []. The advantage with get is that we can specify a default value in case we don't find the key. (We remembered all that thanks to [the beginner repo](https://github.com/ariasAleia/Learning_Python#dictionaries)). (Standing on the shoulders of giants (also valid when we ourselves are the giants))

```python
def DNA_strand(dna):
    letters = {'A': 'T','T': 'A','C': 'G','G': 'C'
    }
    return "".join([letters[x] for x in dna])
```


Btw... We discovered a really nice [bioinformatics web page](https://rosalind.info/about/)


TODO: List of interesting functions or tips or lessons learned. Like a small dropdown list