t1 = (input('Insira o nome do time da casa: ')).upper()
t2 = (input('Insira o nome do time visitante: ')).upper()
print('-'*40)
print('Insira o total de cantos gerais dos últimos 10 jogos do time da casa:')
a = [int(i) for i in input().split(' ')]
print('-'*40)
print('Insira o total de cantos gerais dos últimos 10 jogos do time de fora:')
b =  [int(i) for i in input().split(' ')]
print('-'*40)
print('Quantos cantos o time da casa marcou nos últimos 10 jogos:')
m = [int(i) for i in input().split(' ')]
print('-'*40)
print('Quantos cantos o time da casa levou nos últimos 10 jogos:')
n = [int(i) for i in input().split(' ')]
print('-'*40)
print('Quantos cantos o time de fora marcou nos últimos 10 jogos:')
o = [int(i) for i in input().split(' ')]
print('-'*40)
print('Quantos cantos o time de fora levou nos últimos 10 jogos:')
p = [int(i) for i in input().split(' ')]
mediagerala = sum(a)/10
mediageralb = sum(b)/10
mediageral = (mediagerala + mediageralb)/2
cm = sum(m)/10
cl = sum(n)/10
fm = sum(o)/10
fl = sum(p)/10
print('_'*40)
print(t1 +' x '+ t2)
print('A média de cantos gerais para este embate é', float(mediageral))
print('O {} costuma marcar {} cantos e levar {}'.format(t1,cm,cl))
print('O {} costuma marcar {} cantos e levar {}'.format(t2,fm,fl))