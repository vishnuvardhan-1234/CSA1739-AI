hanoi(1, S, D, _) :-
    write('Move disk from '), write(S),
    write(' to '), write(D), nl.

hanoi(N, S, D, A) :-
    N > 1,
    M is N - 1,
    hanoi(M, S, A, D),
    hanoi(1, S, D, A),
    hanoi(M, A, D, S).