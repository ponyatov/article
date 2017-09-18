human(socrates).                % (unary) fact
mortal(X) :- human(X).          % rule

% SWI Prolog specific syntax
:- initialization
    mortal(X),                  % query 
    writeln(X),halt(0).
