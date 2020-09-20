/* facts */
male(toha).
male(ilya).
male(nikolay).
male(eugene). 
male(petr).
male(kolya).
male(iorgos).
male(matvey).
male(viktor).
male(mikhail).
male(gregory).
male(son1).

female(w2).
female(tamara).
female(marina).
female(galina).
female(ann_mary).
female(zoya_j).
female(sasha).
female(masha_p).
female(natasha).
female(zoya).
female(manya).
female(valya).
female(nina).
female(olga).
female(natalya).
female(anya).
female(nastya).
female(masha_sh).
female(lyuda).


good(zoya).
bad(valya).
 

/* facts-links */
parent(ilya, toha).
parent(tamara, toha).
/* mom and her siblings */
parent(zoya, tamara).
parent(iorgos, tamara).
parent(zoya, galina).
parent(iorgos, galina).
parent(zoya, nikolay).
parent(iorgos, nikolay).
parent(zoya, marina).
parent(iorgos, marina).

/* cousins */
parent(nikolay, natasha).
parent(natasha, kolya).
parent(marina, ann_mary).
parent(marina, zoya_j).
parent(marina, sasha).
parent(galina, petr).
parent(eugene, petr).
parent(galina, masha_p).
parent(eugene, masha_p).

/* grands */
parent(manya, zoya).
parent(matvey, zoya).
parent(manya, valya).
parent(matvey, valya).
parent(manya, nina).
parent(matvey, nina).


/* valya + victor */
parent(valya, olga).
parent(victor, olga).
parent(valya, natalya).
parent(victor, natalya).

/* children */
parent(olga, anya).
parent(mikhail, anya).
parent(olga, nastya).
parent(mikhail, nastya).
parent(natalya, masha_sh).
parent(gregory, masha_sh).
parent(natalya, lyuda).
parent(gregory, lyuda).
 
parent(w2, son1).
parent(ilya, son1).
 
/* Rules */
father(X,Y):- male(X),
    parent(X,Y).
 
mother(X,Y):- female(X),
    parent(X,Y).

daughter(X,Y):- female(X),
    parent(Y, X).
 
son(X,Y):- male(X),
    parent(Y, X).
 
grandfather(X,Y):- male(X),
    parent(X,Z),
    parent(Z,Y).
 
grandmother(X,Y):- female(X),
    parent(X,Z),
    parent(Z,Y).

siblings(X, Y) :- 
    parent(Z, X), 
    parent(Z, Y),
    X \= Y.
 
sister(X,Y):- female(X),
    siblings(X, Y).

brother(X,Y):- male(X),
    siblings(X, Y).
 
aunt(X,Y):- female(X),
    siblings(X, Z), 
    parent(Z, Y).
 
uncle(X,Y):- male(X),
    siblings(X, Z), 
    parent(Z, Y).

nephew(X, Y):- male(X),
    siblings(Y, Z), 
    parent(Z, X).

niece(X, Y):- female(X),
    siblings(Y, Z), 
    parent(Z, X).

couple(X, Y):-
    parent(X, Z),
    parent(Y, Z).

wife(X, Y):-
    couple(X, Y),
    female(X).

husband(X, Y):-
    couple(X, Y),
    male(X).

mother_in_law(X, Y):-
    wife(Z, Y),
    mother(X, Z).

/* On practise: some strange rules) */
good_mother_in_law(X, Y):-
    mother_in_law(X, Y),
    good(X).

bad_mother_in_law(X, Y):-
    mother_in_law(X, Y),
    bad(X).

matcheha(X, Y):-
    husband(Z, X),
    parent(Z, Y),
    not(parent(X, Y)).
           
           
           
           
           
           
           
           
           
           
