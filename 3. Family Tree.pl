male(ram).
male(shyam).
male(raj).

female(sita).
female(gita).

parent(ram, shyam).
parent(sita, shyam).
parent(shyam, raj).
parent(gita, raj).

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.