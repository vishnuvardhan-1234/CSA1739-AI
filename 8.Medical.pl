symptom(ravi, fever).
symptom(ravi, cough).
symptom(ravi, headache).

symptom(raju, fever).
symptom(raju, sneezing).

disease(X, flu) :-
    symptom(X, fever),
    symptom(X, cough).

disease(X, cold) :-
    symptom(X, sneezing),
    symptom(X, fever).

disease(X, unknown) :-
    \+ disease(X, flu),
    \+ disease(X, cold).