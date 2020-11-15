import	ply.lex as lex
from utils import slurp
from treelib import Node, Tree
import json

class Tests(dict):
    def __init__(self, testNo, parentNo, status = "", comment = ""):
        dict.__init__(self, testNo=testNo, parentNo=parentNo, status=status, comment = comment)
        self.testNo = testNo
        self.parentNo = parentNo
        self.status = status
        self.comment = comment
        self.teste = str(testNo) + " " + str(parentNo) + " " + str(status) + " " + str(comment)

tree_aux = None
n_tests = 0 #quantidade total de testes
n_ok_tests = 0 #quantidade total de ok testes
n_nok_tests = 0 #quantidade total de not ok testes

n_subtests = 0 #quantidade total de subtestes
n_ok_subtests = 0 #quantidade total de ok subtestes
n_nok_subtests = 0 #quantidade total de not ok subtestes

tokens = ('N_TESTS', 'OK_TEST', 'NOK_TEST', 'N_SUBTESTS', 'OK_SUBTEST', 'NOK_SUBTEST', 'COMMENT')

t_ignore = "\n"

resultTree = Tree()
node_root = resultTree.create_node(tag = "Root", identifier= "root")

def getNivel(s):
    return int((len(s) - len(s.lstrip()))/4)

def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT(t):
    r"-\s.*"
    t.value = t.value.replace("- ","")
    return t

def t_N_TESTS(t):
    r"[0-9]\.\.[0-9]+"
    global n_tests 
    n_tests += int(t.value[3:])
    return t

def t_N_SUBTESTS(t):
    r"\s[0-9]\.\.[0-9]+"
    global n_subtests 
    n_subtests += int(t.value.strip()[3:])
    return t

def t_OK_TEST(t):
    r"(ok)\s[0-9]+\s"
    global n_ok_tests
    global nodes, node, tree_aux
    nodes = [None] * 100

    if tree_aux != None:
        node = resultTree.create_node(t.value, t.value, parent= node_root, data = Tests(1, 0, "OK", t.value))
        resultTree.merge(t.value, tree_aux)
    else:
        resultTree.create_node(t.value, t.value, parent= node_root, data = Tests(1, 0, "OK", t.value)) 
    n_ok_tests += 1
    return t

def t_OK_SUBTEST(t):
    r"\s+(ok)\s[0-9]+\s"
    global n_ok_subtests, tree_aux
    n_ok_subtests += 1
    node = None
    n = getNivel(t.value) 
    if n == 1:
        if tree_aux != None:
            node = tree_aux.get_node("aux")
        if node == None:
            tree_aux = Tree()
            nodes[n-1] = tree_aux.create_node("aux", "aux", data = Tests(1, 0, "OK", "aux"))
    nodes[n] = tree_aux.create_node(t.value, t.value, parent=nodes[n-1], data = Tests(1, 0, "OK", t.value)) 
    return t

def t_NOK_TEST(t):
    r"(not\sok)\s[0-9]+"
    global n_nok_tests
    n_nok_tests += 1
    return t

def t_NOK_SUBTEST(t):
    r"\s+(not\sok)\s[0-9]+"
    global n_nok_subtests
    n_nok_subtests += 1
    return t    

lexer = lex.lex()

lexer.input(slurp("inputs/teste3.t"))

for token in iter(lexer.token, None):
    print(token)

print("Total testes: %d " % n_tests)
print("OK testes: %d" % n_ok_tests)
print("NOT OK testes: %d" % n_nok_tests)

print("Total subtestes: %d " % n_subtests)
print("OK subtestes: %d" % n_ok_subtests)
print("NOT OK subtestes: %d" % n_nok_subtests)

resultTree.show(line_type="ascii-em")
#resultTree.save2file('tree.txt')
print(resultTree.to_json(with_data=True))

data = resultTree.to_json(with_data=True)

with open('data.json', 'w') as outfile:
    outfile.write(data)