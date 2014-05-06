main.
formula --> opening, vp, closing.

opening --> bracket.
opening --> negp, bracket.
opening --> bracket, vp, closing.
opening --> negp, bracket, vp, closing.

vp --> negp, symbol.
vp --> symbol.
vp --> symbol, conn, symbol.
vp --> negp, symbol, conn, symbol.
vp --> negp, symbol, conn, negp, symbol.
vp --> symbol, conn, negp, symbol.
vp --> symbol, conn, opening.

negp --> [~].
negp --> [~], opening.

closing --> [")"].

symbol --> ["P"].
symbol --> ["Q"].
symbol --> ["R"].
symbol --> ["S"].

conn --> [v].
conn --> [^].

bracket --> ["("].

?- phrase(formula, ["(", ~, "P",v, ~, "Q", ")"]).
