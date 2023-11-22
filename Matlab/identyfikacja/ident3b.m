function blad = ident3b(X0)
load obiekt.mat
k = X0(1);
T = X0(2);

global n;

t = 1:1:60;

obiektC = zpk([], [-T, -T, -T],k);
y_sym = step(obiektC, t);

e = y - y_sym;
blad = sum(e.^2) / length(e); 