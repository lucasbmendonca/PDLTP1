import	ply.lex as lex
import subprocess
from utils import slurp

from tkinter import Tk
from tkinter.filedialog import askopenfilename

n_tests = 0 #quantidade total de testes
n_ok_tests = 0 #quantidade total de ok testes
n_nok_tests = 0 #quantidade total de not ok testes

n_subtests = 0 #quantidade total de subtestes
n_ok_subtests = 0 #quantidade total de ok subtestes
n_nok_subtests = 0 #quantidade total de not ok subtestes

tokens = ('N_TESTS', 'OK_TEST', 'NOK_TEST', 'N_SUBTESTS', 'OK_SUBTEST', 'NOK_SUBTEST', 'COMMENT')

t_ignore = "\n"

def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT(t):
    r"-\s.*"
    t.value = t.value.replace("- ","")
    return t

def t_N_TESTS(t):
    r"[0-9]\.\.[0-9]"
    global n_tests 
    n_tests += int(t.value[3])
    return t

def t_N_SUBTESTS(t):
    r"\s[0-9]\.\.[0-9]"
    global n_subtests 
    n_subtests += int(t.value.strip()[3])
    return t

def t_OK_TEST(t):
    r"(ok)\s[0-9]+\s"
    global n_ok_tests
    n_ok_tests += 1
    return t

def t_OK_SUBTEST(t):
    r"\s+(ok)\s[0-9]+\s"
    global n_ok_subtests
    n_ok_subtests += 1
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

#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)

lexer.input(slurp("inputs/teste3.t"))


for token in iter(lexer.token, None):
    print(token)

print("Total testes: %d " % n_tests)
print("OK testes: %d" % n_ok_tests)
print("NOT OK testes: %d" % n_nok_tests)

print("Total subtestes: %d " % n_subtests)
print("OK subtestes: %d" % n_ok_subtests)
print("NOT OK subtestes: %d" % n_nok_subtests)