bird(parrot).
bird(pigeon).
bird(sparrow).
bird(ostrich).
bird(penguin).

cannot_fly(ostrich).
cannot_fly(penguin).

can_fly(X) :-
    bird(X),
    \+ cannot_fly(X).