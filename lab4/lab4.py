Vn = ['S', 'A', 'B', 'C', 'E']
Vt = ['a', 'd']
Prod = ['S->dB', 'S->A', 'A->d', 'A->dS', 'A->aAdB', 'B->aC', 'B->aS', 'B->AC', 'C->empty', 'E->AS']

class Chomsky:
    Vn = []
    Vt = []
    P = {}
    
    def __init__(self, Vn, Vt, P):
        self.Vn = Vn
        self.Vt = Vt
        self.P = self.create_P(P)

    def create_P(self, P):
        P1 = {}

        for key in self.Vn:
            P1[key] = []
        
        for el in P:
            P1[el[0]].append(el[(el.index("->") + 2):])
        
        return P1
    
    def normalize_grammar(self):
        print("Original grammar\nVn =", self.Vn, "\nVt=", self.Vt, "\nP=")
        for i in self.P:
            print(i ,":",self.P[i])
        P1 = self.eliminate_empty(self.P)
        print("\n","Empty-elimination")
        for i in P1 : 
            print(i , ":" , P1[i])
        P2 = self.eliminate_renaming(P1)
        print("Unit production elimination")
        for i in P2 : 
            print(i , ":" , P2[i])
        P3, Vn, Vt = self.eliminate_inaccessible(P2)
        print("Inaccesible elimination")
        for i in P3 : 
            print(i , ":" , P3[i])
        P4, Vn = self.eliminate_non_productive(P3, Vn, Vt)
        print("Non-Productive elimination")
        for i in P4 : 
            print(i , ":" , P4[i])
        P5, Vn = self.bring_to_chomsky(P4, Vn, Vt)
        print("Chomsky normal form transformation")
        for i in P5 : 
            print(i , ":" , P5[i])

        print("-------------------------------")
        self.P = P5
        self.Vn = Vn
        self.Vt = Vt
        print("Final grammar\nVn =", self.Vn, "\nVt=", self.Vt, "\nP=")
        for i in self.P:
            print(i ,":",self.P[i])

    def eliminate_empty(self, P):
        P1 = P
        empty_set = ["empty"]

        self.find_empty(P1, empty_set)

        for k, v in P1.items():
            for trans in v:
                if len(trans) >= 2: self.substitute_empty(empty_set[1:], k, trans, P1)

        return P1

    def find_empty(self, P, empty_set):
        em = 0
        while em < len(empty_set):
            for k, v in P.items():
                if (empty_set[em] in v) and (k not in empty_set):
                    empty_set.append(k)
                if "empty" in v:
                    P[k].remove(empty_set[em])
               
            em += 1
    
    def substitute_empty(self, empty_set, k, trans, P):
        for i in range(len(trans)):
            if trans[i] in empty_set:
                if i == (len(trans) -1): tmp = trans[:-1] 
                else: tmp = trans[:i] + trans[(i + 1):]
                if tmp not in P[k]: P[k].append(tmp)
    
    def eliminate_renaming(self, P):
        P2 = P.copy()
        for k, v in P2.items():
            P2[k].extend(self.check_unit_transition(P2, k, v))
            P2[k] = list(set(P2[k]))
        
        return P2

    def check_unit_transition(self, P2, k, v):
        unit = []
        transitions = []
        
        for trans in v:
            if trans in self.Vn: 
                unit.append(trans)
                P2[k].remove(trans)
        
        for u in unit:
            transitions.extend(P2[u])
            transitions.extend(self.check_unit_transition(P2, u, P2[u]))
        
        return transitions
        
    def eliminate_inaccessible(self, P):
        P3 = {}

        access_vn = ["S"]
        access_tn = []

        i = 0
        while i < len(access_vn):
            tmp = str(P[access_vn[i]])
            P3[access_vn[i]] = P[access_vn[i]]
            for v in self.Vn:
                if v in tmp and v not in access_vn:
                    access_vn.append(v)
            for v in self.Vt:
                if v in tmp and v not in access_tn:
                    access_tn.append(v)
            i+=1

        return P3, access_vn, access_tn

    def eliminate_non_productive(self, P, Vn, Vt):
        P4 = P.copy()
        productive = []
        non_prod = Vn.copy()
        no_change_flag = False

        while not no_change_flag:
            tmp = productive.copy()
            for v in non_prod:
                tmp.extend(self.find_productive(P4, Vt, non_prod, v)) 
            
            if len(tmp) == len(productive) or len(tmp) == len(Vn): 
                no_change_flag = True
            productive = tmp
            
        if len(productive) == len(Vn) : return P4, Vn

        for np in non_prod:
            self.delete_non_productive(P4, np)
        
        return P4, productive

    def find_productive(self, P, Vt, non_prod, v):
        direct_prod = list(filter(lambda x: x in Vt, P[v]))
        if len(direct_prod) > 0:
            non_prod.remove(v)
            return [v]
        else:
            for trans in P[v]:
                indirect_prod = list(filter(lambda x: x in non_prod, trans))
                if len(indirect_prod) == 0:
                    non_prod.remove(v)
                    return [v]
        return []

    def delete_non_productive(self, P, np):
        P.pop(np)
        for k, v in P.items():
            for trans in v:
                if np in trans: P[k].remove(trans)

    def bring_to_chomsky(self, P, Vn, Vt):
        P5 = {}
        self.aux = {}
        self.y = 0

        self.create_X(Vt)

        for k, v in P.items():
            P5[k] = []
            for trans in v:
                if trans in Vt:
                    P5[k].append(trans)
                else:
                    tmp = self.prepare_transition(trans, Vt, Vn)
                    if len(tmp) > 4: tmp = tmp[:2] + self.convert_transition(tmp[2:])
                    try: P5[k].append(tmp.replace(" ", ""))
                    except: P5[k].append(tmp)

        for k, v in self.aux.items():
            lst = []
            try: lst.append(k.replace(" ", ""))
            except: lst.append(k)
            P5[v] = lst                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        Vn.extend(list(self.aux.values()))
        return P5, Vn

    def create_X(self, Vt):
        for i in range(len(Vt)):
            self.aux[Vt[i]] = ("X" + str(i))

    def create_Y(self, trans):
        self.aux[trans] = "Y" + str(self.y)
        self.y += 1
          
    def prepare_transition(self, trans, Vt, Vn):
        transition = trans
        for i in Vt:
            if i in transition: 
                transition = transition.replace(i, self.aux[i])
        for i in Vn:
            if i in transition: 
                transition = transition.replace(i , i + " ")
        return transition

    def convert_transition(self, trans): 
        if len(trans) <= 4:
            if trans not in self.aux.keys():
                self.create_Y(trans)
            return self.aux[trans]
        else:
            return self.convert_transition(trans[0:2] + self.convert_transition(trans[2:]))

grammar = Chomsky(Vn, Vt, Prod)
grammar.normalize_grammar()