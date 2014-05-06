import formula

def parse_input(inp, var_set):
#    print inp
    if len(inp) == 1:
        var_set.add(inp)
        return formula.Variable(inp)
    if len(inp) == 2 and inp[0] == u'\u00AC':
        return formula.Negation(parse_input(inp[1], var_set))
#    i = 0
#    j = len(inp)-1
#    while(inp[i] == '(' and inp[j] == ')' and inp[i+1] == '(' and ):
#        i+=1
#        j-=1
#    inp = inp[i:j+1]
    left_par = 0
    right_par = 0
    sub_len = 1
    itr = 1
    if(inp[0] == '('):
        left_par +=1
    elif(inp[1] == '('):
        left_par +=1
        sub_len+=1
        itr+=1
    while(left_par != right_par):
        if(inp[itr] == '('):
            left_par+=1
        elif(inp[itr] == ')'):
            right_par+=1
        itr+=1
        sub_len+=1
    if(itr == len(inp) and inp[0] == u'\u00AC'):
        return formula.Negation(parse_input(inp[1:], var_set))
    elif (itr == len(inp)):
        return parse_input(inp[1:len(inp)-1], var_set)
    else:
        phi = inp[0:sub_len]
        conn= inp[sub_len]
        psi = inp[sub_len+1:]
        if conn == u'\u2227':
            return formula.Conjunction(parse_input(phi, var_set), parse_input(psi, var_set))
        elif conn == u'\u2228':
            return formula.Disjunction(parse_input(phi, var_set), parse_input(psi, var_set))
        elif conn == u'\u2192':
            return formula.Implication(parse_input(phi, var_set), parse_input(psi, var_set))
        elif conn == u'\u2194':
            return formula.Biconditional(parse_input(phi, var_set), parse_input(psi, var_set))
    if left_par ==0 and right_par == 0:
        sublen = 0
        for i in range(0, len(inp)):
            if inp[i] == u'\u2228' or inp[i] == u'\u2227' or inp[i] == u'\u2192' or inp[i] == u'\u2194':
                sublen = i
        phi = inp[0:sub_len+1]
        conn = inp[sub_len+1]
        psi = inp[sub_len+2:]
        if inp[sublen] == u'\u2228':
            return formula.Disjunction(parse_input(phi, var_set), parse_input(psi, var_set))
        elif inp[sublen] == u'\u2227':
            return formula.Conjunction(parse_input(phi, var_set), parse_input(psi, var_set))
        elif inp[sublen] == u'\u2192':
            return formula.Implication(parse_input(phi, var_set), parse_input(psi, var_set))
        elif inp[sublen] == u'\u2194':
            return formula.Biconditional(parse_input(phi, var_set), parse_input(psi, var_set))

def convert(form):
#    form.print_obj()
#    print ""
    if form.obj_type() == "Variable":
        return form
    if form.obj_type() == "Negation":
        if form.phi.obj_type() == "Variable":
            return form
        elif form.phi.obj_type() == "Negation":
            return convert(form.phi.phi)
        elif form.phi.obj_type() == "Conjunction":
            conjunct_a = formula.Negation(form.phi.phi)
            conjunct_b = formula.Negation(form.phi.psi)
            return convert(formula.Disjunction(conjunct_a, conjunct_b))
        elif form.phi.obj_type() == "Disjunction":
            disjunct_a = formula.Negation(form.phi.phi)
            disjunct_b = formula.Negation(form.phi.psi)
            return convert(formula.Conjunction(disjunct_a, disjunct_b))
        elif form.phi.obj_type() == "Implication":
            return convert(formula.Conjunction(form.phi.phi, formula.Negation(form.phi.psi)))
        elif form.phi.obj_type() == "Biconditional":
            conjunct_a = formula.Disjunction(formula.Negation(form.phi.phi), formula.Negation(form.phi.psi))
            conjunct_b = formula.Disjunction(form.phi.phi, form.phi.psi)
            return convert(formula.Conjunction(conjunct_a, conjunct_b))
    if form.obj_type() == "Conjunction":
        return formula.Conjunction(convert(form.phi), convert(form.psi))
    if form.obj_type() == "Disjunction":
        return distribute_disjunction(convert(form.phi), convert(form.psi))
    if form.obj_type() == "Implication":
        return convert(formula.Disjunction(formula.Negation(form.phi), form.psi))
    if form.obj_type() == "Biconditional":
        disjunct_a = formula.Conjunction(form.phi, form.psi)
        disjunct_b = formula.Conjunction(formula.Negation(form.phi), formula.Negation(form.psi))
        return convert(formula.Disjunction(disjunct_a, disjunct_b))

def distribute_disjunction(phi, psi):
#    phi.print_obj()
#    print "<Phi"
#    psi.print_obj()
#    print"<Psi"
    statement_phi = break_down(phi)
    statement_psi = break_down(psi)
    conjunct_list = []
    for x in statement_phi:
        for y in statement_psi:
            conjunct_list.append(formula.Disjunction(x,y))
    if len(conjunct_list) == 1:
        return conjunct_list[0]
    curr_disjunct = formula.Conjunction(conjunct_list[0], conjunct_list[1])
    for x in range(2, len(conjunct_list)):
        curr_disjunct = formula.Conjunction(curr_disjunct, conjunct_list[x])
#    curr_disjunct.print_obj()
#    print "< Result"
    return curr_disjunct

def break_down(form):
    if form.obj_type() != "Conjunction":
        return list([convert(form)])
    if form.phi.obj_type() == "Variable" and form.psi.obj_type() == "Variable":
        return list([form.phi, form.psi])
    conjunct_list = list([form.phi, form.psi])
    still_conjunct = True
    while(still_conjunct):
        still_conjunct = False
        new_conjunct_list = []
        for x in conjunct_list:
            if x.obj_type() == "Conjunction":
                still_conjunct = True
#                if(x.phi.obj_type() != "Variable" and x.psi.obj_type() != "Variable" ):
#                    still_conjunct = True
#                    new_conjunct_list.append(x.phi)
#                    new_conjunct_list.append(x.psi)
#                else:
                new_conjunct_list.append(x.phi)
                new_conjunct_list.append(x.psi)
            else:
                new_conjunct_list.append(x) 
        conjunct_list = new_conjunct_list 
    return conjunct_list

def make_disjuncts(cnf_form):
    disjuncts = []
    if(cnf_form.obj_type() != "Conjunction"):
        return list([cnf_form])
    else:
        disjuncts = make_disjuncts(cnf_form.phi) + make_disjuncts(cnf_form.psi)
    return disjuncts

def make_clauses(disjuncts):
    clauses = set()
    for statement in disjuncts:
        curr_clause = set()
        if statement.obj_type() == "Variable":
            curr_clause.add(statement.p)
        elif(statement.obj_type() == "Negation"):
            curr_clause.add(statement.return_string())
        elif statement.obj_type() == "Disjunction":
            curr_clause = form_clause(statement.phi)+form_clause(statement.psi)
        curr_clause = frozenset(curr_clause)
        clauses.add(curr_clause)
    return clauses

def form_clause(disjunct):
    if disjunct.obj_type() != "Disjunction":
        return list([disjunct.return_string()])
    else:
        return form_clause(disjunct.phi) + form_clause(disjunct.psi)
