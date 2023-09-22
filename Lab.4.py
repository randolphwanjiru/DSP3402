#!/usr/bin/env python
# coding: utf-8

# # Lab 4- Object Oriented Programming
# 
# For all of the exercises below, make sure you provide tests of your solutions.
# 

# 1. Write a "counter" class that can be incremented up to a specified maximum value, will print an error if an attempt is made to increment beyond that value, and allows reseting the counter. 

# In[3]:


class Counter:
    def __init__(self, max_value):
        # Initialize the counter with a maximum value.
        self.max_value = max_value
        self.value = 0

    def increment(self):
        # Increase the counter by 1, if not at max value.
        if self.value < self.max_value:
            self.value += 1
        else:
            print(f"Error: Counter is already at maximum value of {self.max_value}")

    def reset(self):
        # Reset the counter back to 0.
        self.value = 0

    def get_value(self):
        # Get the current value of the counter.
        return self.value


# In[5]:


# Create a counter with a maximum value of 5
my_counter = Counter(5)

# Increment and print
my_counter.increment()
print(my_counter.get_value())  # Output: 1

# Increment and print
my_counter.increment()
print(my_counter.get_value())  # Output: 2

# Reset and print
my_counter.reset()
print(my_counter.get_value())  # Output: 0

# Attempt to increment beyond maximum value
for _ in range(7):
    my_counter.increment()  # Output: Error: Counter already at maximum value of 5
    print(my_counter.get_value())  # Output: 5 (for the 6th and 7th iterations)


# 2. Copy and paste your solution to question 1 and modify it so that all the data held by the counter is private. Implement functions to check the value of the counter, check the maximum value, and check if the counter is at the maximum.

# In[6]:


class Counter:
    def __init__(self, max_value):
        self.__max_value = max_value
        self.__value = 0

    def __increment(self):
        if self.__value < self.__max_value:
            self.__value += 1
        else:
            print(f"Error: Counter is already at maximum value of {self.__max_value}")

    def reset(self):
        self.__value = 0

    def get_value(self):
        return self.__value

    def get_max_value(self):
        return self.__max_value

    def is_at_maximum(self):
        return self.__value == self.__max_value

    def increment(self):
        self.__increment()


# In[7]:


my_counter = Counter(5)

my_counter.increment()
print(my_counter.get_value())      # Output: 1

my_counter.increment()
print(my_counter.get_value())      # Output: 2

print(my_counter.is_at_maximum())  # Output: False

my_counter.reset()
print(my_counter.get_value())      # Output: 0

print(my_counter.get_max_value())  # Output: 5

for _ in range(7):
    my_counter.increment()  # Output: Error: Counter is already at maximum value of 5

print(my_counter.get_value())      # Output: 5
print(my_counter.is_at_maximum())  # Output: True


# 3. Implement a class to represent a rectangle, holding the length, width, and $x$ and $y$ coordinates of a corner of the object. Implement functions that compute the area and perimeter of the rectangle. Make all data members private and privide accessors to retrieve values of data members. 

# In[8]:


class Rectangle:
    def __init__(self, length, width, x, y):
        self.__length, self.__width, self.__x, self.__y = length, width, x, y

    def length(self): return self.__length
    def width(self): return self.__width
    def x(self): return self.__x
    def y(self): return self.__y

    def set_length(self, length): self.__length = length
    def set_width(self, width): self.__width = width
    def set_x(self, x): self.__x = x
    def set_y(self, y): self.__y = y

    def area(self): return self.__length * self.__width
    def perimeter(self): return 2 * (self.__length + self.__width)


# In[9]:


my_rectangle = Rectangle(5, 3, 2, 2)

print(my_rectangle.length())       # Output: 5
print(my_rectangle.width())        # Output: 3
print(my_rectangle.x())            # Output: 2
print(my_rectangle.y())            # Output: 2

my_rectangle.set_length(6)
my_rectangle.set_width(4)
my_rectangle.set_x(3)
my_rectangle.set_y(3)

print(my_rectangle.area())      # Output: 24
print(my_rectangle.perimeter()) # Output: 20


# 4. Implement a class to represent a circle, holding the radius and $x$ and $y$ coordinates of center of the object. Implement functions that compute the area and perimeter of the rectangle. Make all data members private and privide accessors to retrieve values of data members. 

# In[10]:


class Circle:
    def __init__(self, radius, x, y):
        self.__radius, self.__x, self.__y = radius, x, y

    def radius(self): return self.__radius
    def x(self): return self.__x
    def y(self): return self.__y

    def set_radius(self, radius): self.__radius = radius
    def set_x(self, x): self.__x = x
    def set_y(self, y): self.__y = y

    def area(self): return 3.14159 * (self.__radius**2)
    def perimeter(self): return 2 * 3.14159 * self.__radius


# In[11]:


my_circle = Circle(5, 2, 2)

print(my_circle.radius())       # Output: 5
print(my_circle.x())            # Output: 2
print(my_circle.y())            # Output: 2

my_circle.set_radius(6)
my_circle.set_x(3)
my_circle.set_y(3)

print(my_circle.area())     
print(my_circle.perimeter()) 


# 5. Implement a common base class for the classes implemented in 3 and 4 above which implements all common methods as not implemented functions (virtual). Re-implement those classes to inherit from the base class and overload the functions accordingly. 

# In[ ]:





# 6. Implement an analogous triangle class.

# In[ ]:





# 7. Add a function to the object classes that tests if a given set of $x$ and $y$ coordinates are inside of the object.

# In[ ]:





# 8. Add a function to the object classes that return a list of up to 16 pairs of  $x$ and $y$ points on the parameter of the object.
# 
# 

# In[ ]:





# 9. Add a function in the base class of the object classes that returns true/false testing that the object overlaps with another object.

# In[ ]:





# 10. Copy the `Canvas` class from lecture to in a python file creating a `paint` module. Copy your classes from above into the module and implement paint functions. Implement a `CompoundShape` class. Create a simple drawing demonstrating that all of your classes are working.

# In[ ]:





# 11. Create a `RasterDrawing` class. Demonstrate that you can create a drawing made of several shapes, paint the drawing, modify the drawing, and paint it again. 

# In[ ]:





# 12. Implement the ability to load/save raster drawings and demonstate that your method works. One way to implement this ability:
# 
#    * Overload `__repr__` functions of all objects to return strings of the python code that would construct the object.
#    
#    * In the save method of raster drawing class, store the representations into the file.
#    * Write a loader function that reads the file and uses `eval` to instantiate the object.
# 
# For example:

# In[1]:


class foo:
    def __init__(self,a,b=None):
        self.a=a
        self.b=b
        
    def __repr__(self):
        return "foo("+repr(self.a)+","+repr(self.b)+")"
    
    def save(self,filename):
        f=open(filename,"w")
        f.write(self.__repr__())
        f.close()
        
   
def foo_loader(filename):
    f=open(filename,"r")
    tmp=eval(f.read())
    f.close()
    return tmp


# In[2]:


# Test
print(repr(foo(1,"hello")))


# In[3]:


# Create an object and save it
ff=foo(1,"hello")
ff.save("Test.foo")


# In[4]:


# Check contents of the saved file
get_ipython().system('cat Test.foo')


# In[5]:


# Load the object
ff_reloaded=foo_loader("Test.foo")
ff_reloaded


# In[ ]:





# In[ ]:




