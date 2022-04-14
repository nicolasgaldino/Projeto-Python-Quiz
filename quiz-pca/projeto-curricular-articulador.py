print('-' * 50)
print('Quiz de Conhecimentos Gerais')
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
print('-' * 50)
certas = 0
erradas = 0
for pk, pv in perguntas.items():
  print(f'{pk}: {pv["pergunta"]}')
  print('Escolha uma das opções abaixo:')
  print('-' * 50)
  for rk, rv in pv['respostas'].items():
    print(f'{rk}: {rv}')
  resposta_usuario = str(input('Sua Resposta: ')).lower().strip()
  print('-' * 50)
  if resposta_usuario == pv['resposta_certa']:
    certas += 1
  else:
    erradas += 1

num_perg = len(perguntas)
porcent_acerto = certas / num_perg * 100
porcent_erro = erradas / num_perg * 100

if porcent_acerto > 70:
  print(f'Você acertou {certas}  e errou {erradas}.')
  print(f'Com {porcent_acerto:.0f}% de acerto, uau, você arrasou!')
elif porcent_acerto < 30:
  print(f'Você acertou {certas}  e errou {erradas}.')
  print(f'Com {porcent_acerto:.0f}% de acerto, você não foi tão bem.')
elif porcent_acerto <= 69 and porcent_acerto >= 31:
  print(f'Você acertou {certas}  e errou {erradas}.')
  print(f'Com {porcent_acerto:.0f}% de acerto, ficou na média.')