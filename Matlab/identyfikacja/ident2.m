function blad = ident2(X0)
load obiekt.mat
k = X0(1);
T1 = X0(2);
T2 = X0(3);
theta = X0(4);

t = 1:1:60;

obiektB = tf([0 0 k], conv([T1 1], [T2 1]));
set(obiektB, 'outputDelay', theta);

y_sym = step(obiektB, t);
e = y - y_sym;
blad = sum(e.^2) / length(e); 