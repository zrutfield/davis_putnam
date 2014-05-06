class Variable:
    def __init__(self, __p):
        self.p = __p

    def print_obj(self):
        print self.p,

    def return_string(self):
        return self.p

    def obj_type(self):
        return "Variable"

class Conjunction:
    def __init__(self, __phi, __psi):
        self.phi = __phi
        self.psi = __psi

    def print_obj(self):
        print "(",
        self.phi.print_obj()
        print "^", 
        self.psi.print_obj()
        print ")",
    
    def return_string(self):
        return "(" + self.phi.return_string() + "^" + self.psi.return_string() + ")"

    def obj_type(self):
        return "Conjunction"

class Disjunction:
    def __init__(self, __phi, __psi):
        self.phi = __phi
        self.psi = __psi

    def print_obj(self):
        print "(",
        self.phi.print_obj()
        print "v", 
        self.psi.print_obj()
        print ")",
    
    def return_string(self):
        return "(" + self.phi.return_string() + "v" + self.psi.return_string() + ")"
    
    def obj_type(self):
        return "Disjunction"

class Negation:
    def __init__(self, __phi):
        self.phi = __phi

    def print_obj(self):
        print "~(", 
        self.phi.print_obj()
        print ")",
    
    def return_string(self):
        return u"\u00AC" + self.phi.return_string()  
    
    def obj_type(self):
        return "Negation"

class Implication:
    def __init__(self, __phi, __psi):
        self.phi = __phi
        self.psi = __psi

    def print_obj(self):
        print "(",
        self.phi.print_obj()
        print "->", 
        self.psi.print_obj()
        print ")",
    
    def return_string(self):
        return "(" + phi.return_string() + "->" + psi.return_string() + ")"
    
    def obj_type(self):
        return "Implication"

class Biconditional:
    def __init__(self, __phi, __psi):
        self.phi = __phi
        self.psi = __psi

    def print_obj(self):
        print "(",
        self.phi.print_obj()
        print "<->", 
        self.psi.print_obj()
        print ")",
    
    def return_string(self):
        return "(" + phi.return_string() + "<->" + psi.return_string() + ")"
    
    def obj_type(self):
        return "Biconditional"
