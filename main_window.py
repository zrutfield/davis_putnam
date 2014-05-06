from Layout import Ui_MainWindow
from PyQt4 import QtGui
import logic_manip
import formula
import dp_tree

class main_window(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super(main_window, self).setupUi(MainWindow)
        self.selected = "premiseBox"
        self.actionRun.triggered.connect(self.run_davis_putnam)
        self.actionConjunction.triggered.connect(self.insert_conjunction)
        self.actionDisjunction.triggered.connect(self.insert_disjunction)
        self.actionNegation.triggered.connect(self.insert_negation)
        self.actionImplies.triggered.connect(self.insert_implication)
        self.actionBiconditional.triggered.connect(self.insert_biconditional)
        self.premiseBox.mouseReleaseEvent = self.set_premise
        self.conclusionBox.mouseReleaseEvent = self.set_conclusion

    def run_davis_putnam(self):
        statements = []
        premise_text = self.premiseBox.toPlainText()
        premise_text = premise_text.__str__()
#        print premise_text
        premise_text_list = premise_text.split('\n')
        var_set = set()
        if(len(premise_text) > 0):
            for prem in premise_text_list:
                prem_stripped = prem.replace(" ", "")
                statements.append(logic_manip.parse_input(prem_stripped, var_set))
        conclusion_text = self.conclusionBox.toPlainText()
        conclusion_text = conclusion_text.__str__()
#        print conclusion_text
        conclusion_text_list = conclusion_text.split('\n')
        for con in conclusion_text_list:
            con_stripped = con.replace(" ", "")
            statements.append(formula.Negation(logic_manip.parse_input(con_stripped, var_set)))
#        for state in statements:
#            state.print_obj()
#            print ""
        statements_cnf = []
        for state in statements:
            statements_cnf.append(logic_manip.convert(state)) 
#        for state in statements_cnf:
#            state.print_obj()
#            print ""
        disjuncts  = []
        for state in statements_cnf:
            disjuncts += logic_manip.make_disjuncts(state)
        clauses = logic_manip.make_clauses(disjuncts)
#        print clauses
#        print var_set
#        print ""
        tree = dp_tree.dp_tree(clauses, var_set)
        tree.trim()
#        tree.print_tree()
        self.validityLabel.setText(tree.verify())
        scene = tree.show_tree()
        self.treeDrawView.setScene(scene)

    def set_premise(self,event):
        self.selected = "premiseBox"
    
    def set_conclusion(self,event):
        self.selected = "conclusionBox"

    def insert_conjunction(self):
        if(self.selected == "premiseBox"):
            cursor = self.premiseBox.textCursor()
            cursor.insertText(u"\u2227")
        elif(self.selected == "conclusionBox"):
            cursor = self.conclusionBox.textCursor()
            cursor.insertText(u"\u2227")
    def insert_disjunction(self):
        if(self.selected == "premiseBox"):
            cursor = self.premiseBox.textCursor()
            cursor.insertText(u"\u2228")
        elif(self.selected == "conclusionBox"):
            cursor = self.conclusionBox.textCursor()
            cursor.insertText(u"\u2228")
    def insert_negation(self):
        if(self.selected == "premiseBox"):
            cursor = self.premiseBox.textCursor()
            cursor.insertText(u"\u00AC")
        elif(self.selected == "conclusionBox"):
            cursor = self.conclusionBox.textCursor()
            cursor.insertText(u"\u00AC")
    def insert_implication(self):
        if(self.selected == "premiseBox"):
            cursor = self.premiseBox.textCursor()
            cursor.insertText(u"\u2192")
        elif(self.selected == "conclusionBox"):
            cursor = self.conclusionBox.textCursor()
            cursor.insertText(u"\u2192")
    def insert_biconditional(self):
        if(self.selected == "premiseBox"):
            cursor = self.premiseBox.textCursor()
            cursor.insertText(u"\u2194")
        elif(self.selected == "conclusionBox"):
            cursor = self.conclusionBox.textCursor()
            cursor.insertText(u"\u2194")
