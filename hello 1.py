import math as m
import numpy as np
import matplotlib.pyplot as plt
from dateutil import parser
import time


# print('hello world')
# def count_matches(d):
#     count=0
#     for k,v in d.items():
#      if k==v:
#         count+=1
#     return count


song='RaH Rah AH AH rom mah RO mah MAH' 
def generate_word_dict(song):
    b=song.lower()
    w={}
    word_list=b.split()
    for words in word_list:
        if words in w:
            w[words]+=1
        else:
            w[words]=1
    return w
word_dict= (generate_word_dict(song))
print(word_dict)
# #b=max(word_dict.values())

# def find_frequent_word(word_dict):
#     b=max(word_dict.values())
#     w=[]
#     for k,v in word_dict.items():
#         if v==b:
#             w.append(k)
#     return (w,b)
# print(find_frequent_word(word_dict))

# def power_recur(n,p):
#     #n^p
#     if p==0:
#      return 1
#     elif p==1:
#        return n
#     else:
#        return n*power_recur(n,(p-1))
# print(power_recur(2,999))
# def factorial(n):
#    if n==1:
#       return 1
#    elif n==0:
#       return 0
#    else:
#       return n*factorial(n-1)
# print('whatever',factorial(9))
# def total_len_recur(l):
#    if len(l)==1:
#       return len(l[0])
#    else:
#        return len(l[0])+total_len_recur(l[1:])
# test=['ab','c','defgh']

# # test=['ab','c']
# print(total_len_recur(test))
# def in_list(l,e):
#    if len(l)==0:
#       return False
#    elif l[0]==e:
#       return True
#    else:
#       return in_list(l[1:],e)

   
# def flatten(l):
#    if len(l)==1: 
#      return (l[0])
#    else:
#       return (l[0])+(flatten(l[1:]))
# # print(flatten([[1,2],[3,4],[9,8,7]]))
# def list_of_list(l,e):
#     b=flatten(l)
#     return in_list(b,e)
# test=[[1,2],[3,4],[5,6,7]]
# print(list_of_list(test,0))
# def in_list(l,e):
#     # if len(l)==1:
#     #     return l[0]==e
#     if l[0]==e:
#         return True
#     else:
#         return in_list(l[1:],e)
# print(in_list([2,1,5,8],1))



# dict={(100,95):'A+',(95,90):'A-',(90,85):'B+',(85,80):'B-',(80,75):'C+',(75,70):'C-',(70,65):'D+',(65,30):'D-',(30,0):'F'}

# a=int(input('please enter your marks: ' ))
# b=int(input('what was the full marks ' ))
# def percentage(a,b):
#     # assert (type(a)==int or type(a)==float) and  (type(b)==int or type(b)==float)
#     return (((a/b)*100))
# percent=(percentage(a,b))
# print(f'your percentage is {percent}')
# def get_grade(percent):
#     for (upper,lower),grade in dict.items():
#         if lower<percent<=upper:
#             return grade
# print(f'your grade is {get_grade(percent)}')
# cost=int(input('what was retail price: '))
# given=int(input('amount given by buyer '))
# a=(given-cost)
# def prime(a):
#     for i in range(2,a):
#         if a%i!=0:
#             return 'is prime'
#         else:
#             return 'is not prime'
# a=int(input('please enter an integer: '))
# print(f'{a} {prime(a)}')
# def dep_rev(l):
#     if type(l)!=list:
#         return l
#     else:
#         return [dep_rev(i) for i in l[::-1]]
# test=[10,[20,30],40]
# # print(dep_rev(test))

# class cuboid(object):
#     def __init__(self,length,breadth,height):
#         self.x=length
#         self.y=breadth
#         self.z=height
#     def volume(self):
#         return (self.height*self.breadth*self.length)
#     def __str__(self):
#          return 'l='+str(self.length)+':'+'b='+str(self.breadth)+':'+str(self.height)

# d=cuboid(2,3,4)
# print(d.volume)
# class cordinate(object):
#     def __init__(self,xval,yval):
#         self.x=xval
#         self.y=yval
#     def distance(self,other):
#         x_diff_sq=(self.x-other.x)**2
#         y_diff_sq=(self.y-other.y)**2
#         return (x_diff_sq+y_diff_sq)**0.5
#         # return a float value.
# c=cordinate(3,4)
# origin=cordinate(0,0)
# print(c.distance(origin))
# print(type(c.distance(origin)))
# print(type(d.volume))
# class circle(object):
#     def __init__(self,center,radius):
#         """" radius is first one and center is the second one"""
#         assert (type(radius)==int and type(center)==cordinate)
#         self.center=center
#         self.radius=radius
#     def is_inside(self,point):
#         """returns true true is in self othereise false"""
#         return self.center.distance(point)<self.radius
# center=cordinate(2,2)
# my_circle=circle(center,2)
# p=cordinate(1,1)
# print(my_circle.is_inside(p))
# def factorial(l):
#     a=1
#     for i in range(1,l+1):
#         a=a*i
#     return a
# print(factorial(5))
# class fraction(object):
#     def __init__(self,n,d):
#         self.num=n
#         self.denom=d
#     def times(self,other):
#         top=self.num*other.num
#         bottom=self.denom*other.denom
#         return top/bottom
#     def plus(self,other):
#         top=self.num*other.denom+self.denom*other.num
#         bottom=self.denom*other.denom
#         return top/bottom
#     def inverse(self):
#         return self.denom/self.num
#     def __str__(self):
#         if self.denom!=1:
#           return str(self.num)+'/'+str(self.denom)
#         else:
#             return str(self.num)
#     def invert(self):
#         (self.num,self.denom)=(self.denom,self.num)
#     def __mul__(self,other):
#         top=self.num*other.num
#         bottom=self.denom*other.denom
#         return fraction(top/bottom)
#     def reduce(self):
#         def gcd(n,d):
#             while d!=0:
#                 (d,n)=(n%d)
#             return n
#         if self.denom==0:
#             return None
#         elif self.denom==0:
#             return self.num
#         else:
#             greatest_common_divisor=gcd(self.num,self.denom)
#             top=int(self.num/greatest_common_divisor)
#             bottom=int(self.denom/greatest_common_divisor)
#             return fraction(top,bottom)
# import math
# # print(math.__dict__.keys())

# def print_prime(a):
#     """ print all the no less then 1000 create list of prime no initially empty
#     two loops  inner loop run through the list of prime no next not divesible by any prime no then it can be added and prinnted"""
#     l=[]
#     #is_prime=True
#     #doesn't work as if is prime set to false it doesn't reset for 2nd iteration
#     for i in range(2,a):
#         is_prime=True
#         for i2 in range(2,i):
#             if i%i2==0:
#                 is_prime=False
#             #here if i add another if statement as if!=0 then the last iteration is taken into account it will not consider fot=r previuos checks
#         if is_prime:
#          l.append(i)
#     return l

# print(print_prime(1000))
# def look_up(name):
#     """Looks up a name in address.txt and returns full 3 line records."""
#     try:
#         with open('addressbook.txt', 'r') as file:
#             lines = file.readlines()
#             for i in range(0, len(lines), 3):
#                 if name == lines[i].strip().lower():
#                     name_found = lines[i].strip()
#                     phone = lines[i+2].strip()
#                     address = lines[i+1].strip()
#                     return f"Entry found\nName={name_found}\nPhone={phone}\nAddress={address}"
#     except FileNotFoundError:
#         return 'Address book not found.'
#     return None

# def add_entry(name, phone, address):
#     with open('addressbook.txt', 'a') as file:
#         file.write(f'{name}\n')
#         file.write(f'{address}\n')
#         file.write(f'Phone Number-{phone}\n')

# while True:
#     print("\nWelcome")
#     print("1) Look up a person by name")
#     print("2) Add a person to the phonebook")
#     print("3) Quit")

#     try:
#         choice = int(input("Enter your choice: "))
#         if choice == 1:
#             name = input("Please enter the person's name: ").strip().lower()
#             if not name.replace(" ", "").isalpha():
#                 raise ValueError("Name should contain only alphabets and spaces.")
#             result = look_up(name)
#             if result:
#                 print(result)
#             else:
#                 print("Person not found in the phonebook.")
#         elif choice == 2:
#             name = input("Please enter the person's name: ").strip().lower()
#             if not name.replace(" ", "").isalpha():
#                 raise ValueError("Name should contain only alphabets and spaces.")
#             phone_number = input("Please enter phone number: ")
#             if not phone_number.isdigit() or len(phone_number) != 10:
#                 raise ValueError("Invalid phone number. Please provide a 10-digit number.")
#             address = input("Please enter the address: ")
#             add_entry(name, phone_number, address)
#             print("Person added to the phonebook successfully.")
#         elif choice == 3:
#             print("Goodbye!")
#             break
#         else:
#             print("Please provide a number less than or equal to 3.")
#     except ValueError as e:
#         print(f"Error: {e}")
#     finally:
#         pass
# dont'use the len function

# user=str(input('please provide your list of number seperated by comma: ' ))
# lists=[int(i) for i in user.split(',')]
# a=[]
# for items in lists:
#      if (items>=0 and items<=100):
#          a.append(items)
# print(a)
# l=input('please enter the list seperated by comma: ' )
# l=[int(x) for x in l.split(',')]
# print(l[0])
# print(l[1:])
# def reverse(l):
#     if len(l)==1:
#         return l
#     return reverse(l[1:])+[l[0]]    
# print(reverse(l))
# table={'a':4.0,'a-':3.7,'b+':3.3,'b':3.0,'b-':2.7,'c+':2.3,'c':2.0,'c-':1.7,'d+':1.3,'d':1.0,'d-':0.7,'f':0}
# # don't forget to lower the character given y user
# flag=True
# sum=0
# fre=0
# while flag:
#  try:
#   frequency=int(input('please enter the frequency of the grade: '))
#   if frequency==0:
#       flag=False
#       break
#   l=str(input('please enter the grade: '))
  
#   l=l.lower()
#   no=table[l]
#   b=no*frequency
#   fre+=b
#   sum+=frequency

#  except KeyError:
#     print('please enter a valid grade and restart')
#     continue
# try:
#  print(f"your GPA is {fre/sum}")
# except ZeroDivisionError:
#   print("your GPA is 0")
# print('_________')
# for i in range(3,6,2):
#     print(i)
# import turtle
# he=turtle.Turtle()
# he.speed(10)
# he.color('red','yellow')
# he.begin_fill() 
# screen=he.getscreen() 
# he.forward(350) 
# he.left(90)
# he.forward(50)
# he.left(90)
# he.forward(50) 
# he.right(50)
# he.forward(70)
# he.left(50)
# he.forward(70) 
# he.left(90)
# he.forward(60) 
# he.right(90)
# he.forward(185)
# he.left(90)
# he.forward(50) 
# he.end_fill()
# he.left(90) 
# he.penup()
# he.forward(40)
# he.right(90)
# he.forward(25)
# he.pendown() 
# he.color('red','black')
# he.begin_fill()
# he.circle(30)
# he.end_fill() 
# he.penup() 
# he.left(90)
# he.forward(250)
# he.left(90)
# he.pendown()
# he.color('red','black') 
# he.begin_fill()
# he.circle(30)
# he.end_fill() 
# screen.exitonclick()
# turtle.done()
# b = [1, 2, 3, 2]

# def remove_duplicates(a):
#     """ if a number accur in a list more then once it removes from the list and return it
#      [1,2,3,2] will return [1,2,3] order is preserved"""
#     seen = []       
#     for i in a:     
#         if i in seen:   
#             continue    # skip duplicates
#         seen.append(i)  # keep first occurrence
#     return seen

# class Int_set(object):
#     """an Int_set is a set of integer"""
#     def __init__(self):
#         """creates an empty set of integer using a list"""
#         self._vals=[]
#     def insert(self,e):
#         """assumes e is an integer and insert e into self"""
#         if e not in self._vals:
#           self._vals.append(e)
#     def member(self,e):
#         """assumes e  is an inetger  
#         Returns True if e is in self, and false otherwise"""
#         return e in self._vals
#     def remove(self,e):
#         """ assumes e is an integer and removes e from self 
#         raise a value error if e is not in self"""
#         if e in self._vals:
#             self._vals.remove(e)
#     def get_member(self):
#         """return a list containing the element of self._ 
#         nothing can be said about the order of the elements"""
#         return self._vals[:]
#     def __str__(self):
#         """returns a string representig of self """
#         Str=""
#         if self._vals==[]:
#             return ("{}")
#         for i in self._vals:
#             Str=Str+str(i)+","
#         return f"{{{Str[:-1]}}}"
#     def __add__(self, other):
#      """returns a new Int_set that is the union of self and other"""
#      new_set = Int_set()
#     # add elements from self
#      for x in self.get_member():
#         new_set.insert(x)
#     # add elements from other
#      for i in other.get_member():
#         new_set.insert(i)
#      return new_set
# class Toy(object):
#     def __init__(self):
#       self._elems=[]
#     def add(self,new_elems):
#         """ New element is a list"""
#         self._elems+=new_elems
#     def __len__(self):
#         return len(self._elems)
#     def __add__(self,other):
#         new_toy=Toy()
#         new_toy._elem=self._elems+other._elems
#         return new_toy
#     def __eq__(self,other):
#         return self._elems==other._elems
#     def __str__(self):
#         return str(self._elems)
#     def __hash__(self):
#        return id(self)
# class person(object):
#     def __init__(self,name):
#         """assumes name is a string. Create a person """
#         self._name=name
#         try:
#             last_blank=name.rindex(' ')
#             self._last_name=name[last_blank+1:]
#         except:
#             self._last_name=name
#         self._birthday=None
#     def get_name(self):
#         """Returns self's full name"""
#         return self._name
#     def get_last_name(self):
#         """  returns persons last name"""
#         return self._last_name
#     def set_birthday(self, birthdate):
#         """Sets birthday. Accepts datetime.date, datetime.datetime, or string."""
#         if isinstance(birthdate, datetime.datetime):
#             # normalize datetime.datetime to date
#             birthdate = birthdate.date()
#         elif isinstance(birthdate, str):
#             # parse string into datetime.date
#             birthdate = parser.parse(birthdate).date()
#         elif not isinstance(birthdate, datetime.date):
#             raise TypeError("birthdate must be datetime.date, datetime.datetime, or a date string")
#         self._birthday = birthdate
#     def get_age(self):
#         if  self._birthday==None:
#             raise ValueError
#         return (datetime.date.today()-self._birthday).days
#     def __lt__(self,other):
#         """ asssume other a person 
#         returns True if self precedes other in alphabetical order if not  then returns False.
#         comparisin is based on first name, but if these are same then full name is compared"""
#         return self._name<other._name
#     def __str__(self):
#         """return self name"""
#         return self._name
# class poltician(person):
#     """ poltician is perso who belongs to a politival party"""
#     def __init__(self,name):
#         super().__init__(name)
#         self._party=None
#     def set_party(self,party_name):
#         self._party=party_name
#     def get_party(self):
#         return self._party
# class Course(object):
#     def __init__(self,course_code,course_title):
#        """code and title is a string"""
#        self.code=course_code
#        self.title=course_title
#        self._student=[]
#     def add_student(self,student_name):
#         self._student.append(student_name)
#     def get_student(self):
#         for stud in self._student:
#             yield stud
#     def __str__(self):
#         return (self.code+':'+self.title)
# import datetime


# class Person(object):
#     def __init__(self, name):
#         """Assumes name is a string"""
#         self._name = name
#         try:
#             last_blank = name.rindex(' ')
#             self._last_name = name[last_blank+1:]
#         except:
#             self._last_name = name
#         self._birthday = None
        
#     def get_name(self):
#         """Returns self's full name"""
#         return self._name
    
#     def get_last_name(self):
#         """Returns self's last name"""
#         return self._last_name
    
#     def set_birthday(self, birthdate):
#         """Assumes birthdate is a datetime.date object
#            Sets self's birthday"""
#         self._birthday = birthdate
        
#     def get_age(self):
#         """Returns self's current age in days"""
#         if self._birthday == None:
#             raise ValueError
#         return (datetime.date.today() - self._birthday).days
    
#     def __lt__(self, other):
#         """Returns True if self's name is lexicographically
#            less than other's name, and False otherwise"""
#         if self._last_name == other._last_name:
#             return self._name < other._name
#         return self._last_name < other._last_name
    
#     def __str__(self):
#         """Returns self's name"""
#         return self._name
        

# class MIT_person(Person):
#     _next_id_num = 0 # Class variable
    
#     def __init__(self, name):
#         super().__init__(name)
#         self._id_num = MIT_person._next_id_num
#         MIT_person._next_id_num += 1
        
#     def get_id_num(self):
#         return self._id_num
    
#     def __lt__(self, other):
#         """Returns True if self's ID number is less than
#            other's ID number, and False otherwise"""
#         return self._id_num < other._id_num
        

# class Student(MIT_person):
#     def __init__(self,name):
#      super().__init__(name)
#      self._course=[]

#     def enroll(self,course):
#         """take course object as an arguument"""
#         if isinstance(course,Course):
#             self._course.append(course)
#     def get_course(self):
#         return self._course

        

# class UG(Student):
#     def __init__(self, name, class_year):
#         super().__init__(name)
#         self._year = class_year
        
#     def get_class(self):
#         return self._year
        
# class Grad(Student):
#     pass
# # --- Test Code ---

# # Create Students
# s1 = UG('Billy Beaver', 1984)
# s2 = Grad('Buzz Aldrin')
# s3 = UG('Jane Doe', 2023)

# # Create Courses
# c1 = Course('6.001', 'Introduction to CS Programming')
# c2 = Course('18.01', 'Calculus')

# # Enroll Students
# s1.enroll(c1)
# s1.enroll(c2)
# s2.enroll(c1)

# # Print Course Rosters
# print("--- Course Rosters ---")
# for course in [c1, c2]:
#     print(f"\n{course}") # This tests your Course __str__
#     for student in course.get_student():
#         print(f"  {student.get_name()} ({student.get_id_num()})")

# # Print Student Schedules
# print("\n--- Student Schedules ---")
# for student in [s1, s2, s3]:
#     print(f"\n{student.get_name()}'s Schedule:")
#     courses = student.get_course()
#     if not courses:
#         print("  Not enrolled in any courses.")
#     for course in courses:
#         print(f"  {course}") # This also tests your Course __str__


# def is_subset(l1,l2):
#     """Assumes l1 and l2 are list.
#     return true if each element in l1 is also in l2 and false otherwise"""
#     for e in l1:
#         matched=False
#         for e2 in l2:
#             if e==e2:
#                 matched=True
#                 break
#         if not matched:
#                 return False
#     return True
# l1=[1,2,3,4]
# l2=[4,3,2]
# print(is_subset(l1,l2))
# def search(l,e):
#     """assumes l is a list, the elements of which are in 
#     ascending order"""
#     def bin_search(l,e,low,high):
#         if high==low:
#             return l[low]==e
#         mid=(low+high)//2
#         if l[mid]==e:
#             return True
#         elif l[mid]>e:
#             if low==mid:
#                 return False
#             else:
#                 return bin_search(l,e,low,mid-1)
#         else:
#             return bin_search(l,e,mid+1,high)
#     if len(l)==0:
#         return False
#     else:
#         return bin_search(l,e,0,len(l)-1)
# def sel_sort(l):
#     """Assumes that l is a list of elements that 
#     can be compared using >.
#     sorts l i ascending order"""
#     suffix_start=0
#     while suffix_start!=len(l):
#         # look at each element in suffix
#         for i in range(suffix_start,len(l)):
#             if l[i]<l[suffix_start]:
#                 # swap postion
#                 l[suffix_start],l[i]=l[i],l[suffix_start]
#         suffix_start+=1
# def merge(left,right,compare):
#     """Assumes left and right are sorted lists and 
#     compare defines an ordering  on the elements.
#     Returns a new sorted(by compare) list containing the
#     the same elements as left+right would contain."""
#     result=[]
#     i,j=0,0
#     while i<len(left) and j<len(right):
#         if compare(left[i],right[j]):
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#         while (i<len(left)):
#             result.append(left[i])
#             i+=1
#         while (j<len(right)):
#             result.append(right[j])
#             j+=1
#         return result
# def merge_sort(l,compare=lambda x,y: x<y):
#     """Assumes l is a list, compare defines an ordering
#     on elements of l
#     returns a new sorted list with the same elements as l"""    
#     if len(l)<2:
#         return l[:]
#     else:
#         middle=len(l)//2
#         left=merge_sort(l[:middle],compare)
#         right=merge_sort(l[middle:],compare)
#         return merge(left,right,compare)
# start=time.perf_counter()
# def count_ways(n, steps, memo={}):
#     if n == 0:
#         return 1 #dont move
#     if n < 0:
#         return 0  # Can't reach a negative step0
#     if n in memo:
#         return memo[n]

#     count = 0
#     for step in steps:
#         ways = count_ways(n-step, steps, memo)
#         count += ways

#     memo[n] = count
#     return count

# n = 100
# steps = (1, 2)
# print(count_ways(n, steps))
# start=time.perf_counter()
# end=time.perf_counter()
# print(end-start)
# with open()
