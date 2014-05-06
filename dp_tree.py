from PyQt4 import QtCore, QtGui

class dp_tree:
    def __init__(self, _clauses, _vars):
        uid = 0
        self.head = Node(_clauses, "", uid)
        uid+=1
        level_list = [self.head]
        while(len(_vars) > 0):
            key = _vars.pop()
            tmp = []
            for x in level_list:
                x.left = Node(x.clauses, key, uid)
                uid+=1
                x.right = Node(x.clauses, u'\u00AC'+key,uid)
                uid+=1
                x.left.parent = x
                x.right.parent = x
                tmp.append(x.left)
                tmp.append(x.right)
            level_list = tmp

    def print_tree(self):
        level_list = [self.head]
        print self.head.clauses
        print ""
        while len(level_list) > 0:
            tmp = []
            for x in level_list:
                if(x.left != None):
                    print x.left.clauses
                    tmp.append(x.left)
                if(x.right != None):
                    print x.right.clauses
                    tmp.append(x.right)
            level_list = tmp
            print ""

    def trim(self):
        level_list = [self.head]
        while len(level_list) > 0:
            tmp = []
            for x in level_list:
                print x.clauses
                if(frozenset([]) in x.clauses):
                    x.left = None
                    x.right = None
                    x.closed = True
                elif(x.clauses == set()):
                    x.left = None
                    x.right = None
                else:
                    if(x.left !=None):
                        tmp.append(x.left)
                    if(x.right!=None):
                        tmp.append(x.right)
            level_list = tmp

    def verify(self):
        level_list = [self.head]
        while len(level_list) > 0:
            tmp = []
            for x in level_list:
                if(x == None):
                    continue
                if(x.left == None and x.right == None and not x.closed):
                    validity_string =  u"Tree failed to close. Argument invalid for: "
                    while(x.parent.key != ""):
                        validity_string+= x.key + u", " 
                        x = x.parent
                    validity_string += x.key
                    return validity_string
                else:
                    tmp.append(x.left)
                    tmp.append(x.right)
            level_list = tmp
        return "Tree closed. Argument valid"

    def return_string(self):
        return self.head.return_string()

    def show_tree(self):
        scene = QtGui.QGraphicsScene()
        p = QtCore.QProcess()
        a = self.prepare_graph()
        p.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        p.start("dot", QtCore.QStringList() << "-Tpng")
        p.write(a)
        data = QtCore.QByteArray()
        pixmap = QtGui.QPixmap()
        while(p.waitForReadyRead(100)):
            data.append(p.readAll())
        pixmap.loadFromData(data)
        scene.addPixmap(pixmap)
        p.close()
        return scene

    def prepare_graph(self):
        a = QtCore.QByteArray()
        stream = QtCore.QTextStream(a, QtCore.QIODevice.ReadWrite)
        stream << "graph " << "{" << "\n"
        stream << "\tnode[ranksep=0.5,fontsize=13,margin=0,width=\"1\", height=\".2\", shape=plaintext];\n"
        stream << "\tsubgraph cluster17{\n"
        self.graph_walk(self.head, stream)
        stream << "\t}\n" << "}" << "\n"
        stream.flush()
        return a

    def graph_walk(self, p, stream):
        if (p != None):
            stream << "\t\t" << "n" << p.uid << "[label=\"" << p.return_string() << "\"];\n"
        if(p.left != None):
            stream << "\t\tn" << p.uid << "--" << "n" << p.left.uid << ";\n"
            self.graph_walk(p.left, stream)
        if(p.right != None):
            stream << "\t\tn" << p.uid << "--" << "n" << p.right.uid << ";\n"
            self.graph_walk(p.right, stream)
        
class Node:
    def __init__(self, _clauses, _key, _uid):
        self.key = _key
        print self.key
        self.clauses = _clauses.copy()
        self.left = None
        self.right = None
        self.closed = False
        self.parent = None
        self.uid = _uid
        if(self.key != ""):
            if(self.key[0] == u'\u00AC'):
                self.satisfy_negative()
            else:
                self.satisfy_positive()

    def satisfy_positive(self):
        clause_to_remove = []
        for clause in self.clauses:
            if(self.key in clause):
                clause_to_remove.append(clause)
        for clause in clause_to_remove:
            self.clauses.remove(clause)
        clause_to_remove = []
        clause_to_add = []
        for clause in self.clauses:
            if(u'\u00AC'+self.key in clause):
                curr_clause = set(clause.copy())
                clause_to_remove.append(clause)
                curr_clause.remove(u'\u00AC'+self.key)
                clause_to_add.append(frozenset(curr_clause))
        for clause in clause_to_remove:
            self.clauses.remove(clause)
        for clause in clause_to_add:
            self.clauses.add(clause)

    def satisfy_negative(self):
        clause_to_remove = []
        for clause in self.clauses:
            if(self.key in clause):
                clause_to_remove.append(clause)
        for clause in clause_to_remove:
            self.clauses.remove(clause)
        clause_to_remove = []
        clause_to_add = []
        for clause in self.clauses:
            if(self.key[1] in clause):
                curr_clause = set(clause.copy())
                clause_to_remove.append(clause)
                curr_clause.remove(self.key[1])
                clause_to_add.append(frozenset(curr_clause))
        for clause in clause_to_remove:
            self.clauses.remove(clause)
        for clause in clause_to_add:
            self.clauses.add(clause)

    def return_string(self):
        tree_string = ""
        if(self.key != ""):
            tree_string += self.key
            tree_string += "\n"
        for clause in self.clauses:
            tree_string += "{"
            for statement in clause:
                tree_string += statement
                tree_string += ","
            if tree_string[-1] == ',':
                tree_string = tree_string[:-1]
            tree_string+= "}\n"
        if(self.closed):
            tree_string += "X"
        elif(self.left == None and self.right == None and not self.closed):
            tree_string += "O"
        tree_string = tree_string.strip('\n')
        return tree_string
