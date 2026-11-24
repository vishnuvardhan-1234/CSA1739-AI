diet(diabetes, 'Green vegetables').
diet(diabetes, 'Oats').
diet(bp, 'Low salt food').
diet(bp, 'Fruits').
diet(obesity, 'Salad').
diet(obesity, 'Boiled vegetables').
diet(anemia, 'Spinach').
diet(anemia, 'Iron rich food').

suggest(X) :-
    diet(X, Food),
    write(Food), nl.