fruits = ("apple", "strawberry", "grape", "cherry", "kiwi")

(green, *red, purple) = fruits
print(red)


mytuple = fruits * 2

print(mytuple)

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))


# Keyword arguments

def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

# my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# You can use both *args and **kwargs in the same function.

# The order must be:

# regular parameters
# *args
# **kwargs

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

# global keyword

def myfunc():
  global x
  x = 300

myfunc()

print(x)


def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())



x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)


def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())


def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(2)
def myfunction():
  return "Hello Linus"

print(myfunction())


#---------------------------------------------------------------------------------

sessions = [
    {"employee_id": "E1", "work_date": "2025-01-01", "minutes_worked": 120},
    {"employee_id": "E1", "work_date": "2025-01-01", "minutes_worked": 60},   # same day, duplicate
    {"employee_id": "E1", "work_date": "2025-01-02", "minutes_worked": 90},
    {"employee_id": "E1", "work_date": "2025-01-03", "minutes_worked": -30},  # bad data, ignore
    {"employee_id": "E1", "work_date": "2025-01-03", "minutes_worked": 150},

    {"employee_id": "E2", "work_date": "2025-01-01", "minutes_worked": 200},
    {"employee_id": "E2", "work_date": "2025-01-02", "minutes_worked": 180},
    {"employee_id": "E2", "work_date": "2025-01-03", "minutes_worked": 0},    # ignore
    {"employee_id": "E2", "work_date": "2025-01-04", "minutes_worked": 220},

    {"employee_id": "E3", "work_date": "2025-01-01", "minutes_worked": 30},
    {"employee_id": "E3", "work_date": "2025-01-02", "minutes_worked": 45},
    {"employee_id": "E3", "work_date": "2025-01-03", "minutes_worked": 60},
    {"employee_id": "E3", "work_date": "2025-01-04", "minutes_worked": 75},
    {"employee_id": "E3", "work_date": "2025-01-05", "minutes_worked": 90},

    {"employee_id": "E4", "work_date": "2025-01-01", "minutes_worked": 500},  # only 1 day
]


def top_employees_by_avg_daily_minutes(
    sessions,
    start_date,
    end_date,
    top_n,
    min_days=5
):
    pass