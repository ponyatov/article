human(socrates).                % (unary) facts
human(aristotle).
human(plato).
god(zeus).                      % and who is a god
god(apollo).

mortal(X) :- human(X).          % rule 

% load in SWI Prolog and run (press ; for next)

% mortal(X).                  	% query 
