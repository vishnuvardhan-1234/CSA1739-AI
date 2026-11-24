fact(sunlight).
fact(water).

plant_grows :-
    fact(sunlight),
    fact(water).

flower_blooms :-
    plant_grows.