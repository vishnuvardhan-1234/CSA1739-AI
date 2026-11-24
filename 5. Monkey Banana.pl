at(monkey, door).
at(box, window).
at(banana, middle).

can_reach :-
    at(monkey, door),
    at(box, window),
    at(banana, middle),
    write('Monkey moves to box'), nl,
    write('Monkey pushes box to middle'), nl,
    write('Monkey climbs box'), nl,
    write('Monkey gets banana'), nl.