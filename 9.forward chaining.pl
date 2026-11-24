fact(rain).
fact(cold).

rule(wet_ground) :-
    fact(rain).

rule(wear_jacket) :-
    fact(cold).

rule(carry_umbrella) :-
    fact(rain).

forward :-
    (rule(X),
     write('Derived Fact: '), write(X), nl,
     fail);
    true.