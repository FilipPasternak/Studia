function blad = ident(X0)
load obiekt.mat
k = X0(1);
T = X0(2);
theta = X0(3);

t = 1:1:60;

obiektA = tf([0 k], [T 1]);
set(obiektA, 'outputDelay', theta);
y_sym = step(obiektA, t);

e = y - y_sym;
blad = sum(e.^2) / length(e); 