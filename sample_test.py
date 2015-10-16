__author__ = 'Winnie'

from bnetbase import *

## E,B,S,w,G example from sample questions
A = Variable('A', ['a', '-a'])
B = Variable('B', ['b', '-b'])
C = Variable('C', ['c', '-c'])
D = Variable('D', ['d', '-d'])
E = Variable('E', ['e', '-e'])
F = Variable('E', ['f', '-f'])
G = Variable('E', ['g', '-g'])
H = Variable('E', ['h', '-h'])
I = Variable('E', ['i', '-i'])



FA = Factor('P(A)', [A])
FBAH = Factor('P(B|A,H)', [B, A, H])
FCBG = Factor('P(C|B,G)', [C, B, G])
FDCF = Factor('P(D|C,F)', [D, C, F])
FEC = Factor('P(E|C)', [E,C])
FF = Factor('P(F)', [F])
FG= Factor('P(G)', [G])
FH = Factor('P(H)', [H])
FIB = Factor('P(I|B)', [I,B])


FA.add_values([['a',0.9], ['-a', 0.1]])
FBAH.add_values([['b', 'a', 'h', 1], ['-b', 'a', 'h', 0], ['b', 'a', '-h', 0], ['-b', 'a', '-h', 1],
                 ['b', '-a', 'h', .5], ['-b', '-a', 'h', 0.5], ['b', '-a', '-h', .6], ['-b', '-a', '-h', .4]])
FCBG.add_values([['c', 'b', 'g', 0.9], ['-c', 'b', 'g', 0.1], ['c', 'b', '-g', 0.9], ['-c', 'b', '-g', .1],
                 ['c', '-b', 'g', .1], ['-c', '-b', 'g', 0.9], ['c', '-b', '-g', 1], ['c', 'b', 'g', 0]])
FDCF.add_values([['d', 'c', 'f', 0], ['-d', 'c', 'f', 1], ['d', 'c', '-f', 1], ['-d', 'c', '-f', 0],
                 ['d', '-c', 'f', .7], ['-d', '-c', 'f', 0.3], ['d', '-c', '-f', .2], ['-d', '-c', '-f', 0.8]])
FEC.add_values([['e', 'c', 0.2], ['-e', 'c', .8], ['e', '-c', 0.4], ['-e', '-c', 0.6]])
FF.add_values([['f',0.1], ['-f', 0.9]])
FG.add_values([['g',1], ['-g', 0]])
FH.add_values([['h',0.5], ['-h', 0.5]])
FIB.add_values([['i', 'b', 0.3], ['-i', 'b', .7], ['i', '-b', 0.9], ['-i', '-b', 0.1]])


Q3 = BN('SampleQ4', [A, B, C, D, E, F, G, H, I], [FA, FBAH, FCBG, FDCF, FEC, FF, FG, FH, FIB])


if __name__ == '__main__':

    print("Question (a)")
    A.set_evidence('a')
    probs = VE(Q3, B, [A])
    print('P(b|a) = {} P(-b|a) = {}'.format(probs[0], probs[1]))

    print("\nQuestion (b)")
    A.set_evidence('a')
    probs = VE(Q3, C, [A])
    print('P(c|a) = {} P(-c|a)) = {}'.format(probs[0], probs[1]))

    print("\nQuestion (c)")
    A.set_evidence('a')
    E.set_evidence('-e')
    probs = VE(Q3, C, [A, E])
    print('P(c|a,-e) = {} P(-c|a,-e)) = {}'.format(probs[0], probs[1]))

    print("\nQuestion (d)")
    A.set_evidence('a')
    F.set_evidence('-f')
    probs = VE(Q3, C, [A, F])
    print('P(c|a,-f) = {} P(-c|a,-f)) = {}'.format(probs[0], probs[1]))

