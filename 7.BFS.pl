edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 5).
edge(c, d, 1).

best_first(Start, Goal) :-
    search([Start], Goal).

search([Goal|_], Goal) :-
    write('Goal Found: '), write(Goal).

search([Node|Rest], Goal) :-
    findall(Cost-Next,
        (edge(Node, Next, Cost),
         \+ member(Next, [Node|Rest])),
        Children),
    append(Rest, Children, New),
    sort(New, Sorted),
    search_nodes(Sorted, Goal).

search_nodes([_-Next|Rest], Goal) :-
    search([Next|Rest], Goal).