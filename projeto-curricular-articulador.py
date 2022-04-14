print()
print('Quiz de Conhecimentos Gerais')
print()
perguntas = {
  'Pergunta 1': {
    'pergunta': 'Quantos fusos horários existem na Rússia? ',
    'respostas': {
       'a': '09',
       'b': '11',
       'c': '08',
       'd': '13',
    },
    'resposta_certa': 'b',
  },
  'Pergunta 2': {
    'pergunta': 'Quantas tiras há na bandeira dos Estados Unidos? ',
    'respostas': {
       'a': '13',
       'b': '12',
       'c': '10',
       'd': '11',
    },
    'resposta_certa': 'a',
  },
  'Pergunta 3': {
    'pergunta': 'Quantos dias são necessários para a Terra orbitar o sol? ',
    'respostas': {
       'a': '360',
       'b': '369',
       'c': '365',
       'd': '361',
    },
    'resposta_certa': 'c',
  },
}
print()
respostas_certas = 0
respostas_erradas = 0
for pk, pv in perguntas.items():
  print(f'{pk}: {pv["pergunta"]}')
  print()
  print('Escolha uma das opções abaixo:')
  print()
  for rk, rv in pv['respostas'].items():
    print(f'{rk}: {rv}')
  resposta_usuario = str(input('Sua Resposta: ')).lower().strip()
  print()
  if resposta_usuario == pv['resposta_certa']:
    respostas_certas += 1
  else:
    respostas_erradas += 1

qtd_perguntas = len(perguntas)
porcent_acerto = respostas_certas / qtd_perguntas * 100
porcent_erro = respostas_erradas / qtd_perguntas * 100

if porcent_acerto > 70:
  print('Você acertou {}  e errou {}.'.format(respostas_certas, respostas_erradas))
  print('Com {}% de acerto, uau, você arrasou!'.format(porcent_acerto))
elif porcent_acerto < 30:
  print('Você acertou {}  e errou {}.'.format(respostas_certas, respostas_erradas))
  print('Com {}% de acerto, você não foi tão bem.'.format(porcent_acerto))
elif porcent_acerto <= 69 and porcent_acerto >= 31:
  print('Você acertou {}  e errou {}.'.format(respostas_certas, respostas_erradas))
  print('Com {}% de acerto, ficou na média.'.format(porcent_acerto))