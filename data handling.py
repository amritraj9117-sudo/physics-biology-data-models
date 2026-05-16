# b = [1, 2, 3, 2]

def remove_duplicates(a):
    """ if a number accur in a list more then once it removes from the list and return it
     [1,2,3,2] will return [1,2,3] order is preserved"""
    seen = []       
    for i in a:     
        if i in seen:   
            continue    # skip duplicates
        seen.append(i)  # keep first occurrence
    return seen

class Int_set(object):
    """an Int_set is a set of integer"""
    def __init__(self):
        """creates an empty set of integer using a list"""
        self._vals=[]
    def insert(self,e):
        """assumes e is an integer and insert e into self"""
        if e not in self._vals:
          self._vals.append(e)
    def member(self,e):
        """assumes e  is an inetger  
        Returns True if e is in self, and false otherwise"""
        return e in self._vals
    def remove(self,e):
        """ assumes e is an integer and removes e from self 
        raise a value error if e is not in self"""
        if e in self._vals:
            self._vals.remove(e)
    def get_member(self):
        """return a list containing the element of self._ 
        nothing can be said about the order of the elements"""
        return self._vals[:]
    def __str__(self):
        """returns a string representig of self """
        Str=""
        if self._vals==[]:
            return ("{}")
        for i in self._vals:
            Str=Str+str(i)+","
        return f"{{{Str[:-1]}}}"
    def __add__(self, other):
     """returns a new Int_set that is the union of self and other"""
     new_set = Int_set()
    # add elements from self
     for x in self.get_member():
        new_set.insert(x)
    # add elements from other
     for i in other.get_member():
        new_set.insert(i)
     return new_set

class Toy(object):
    def __init__(self):
      self._elems=[]
    def add(self,new_elems):
        """ New element is a list"""
        self._elems+=new_elems
    def __len__(self):
        return len(self._elems)
    def __add__(self,other):
        new_toy=Toy()
        new_toy._elem=self._elems+other._elems
        return new_toy
    def __eq__(self,other):
        return self._elems==other._elems
    def __str__(self):
        return str(self._elems)
    def __hash__(self):
       return id(self)