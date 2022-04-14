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
  'Pergunta 4': {
    'pergunta': 'Quantas teclas há em um piano clássico? ',
    'respostas': {
       'a': '80',
       'b': '69',
       'c': '76',
       'd': '88',
    },
    'resposta_certa': 'd',
  },
  'Pergunta 5': {
    'pergunta': 'Quando foi a primeira publicação da Vogue? ',
    'respostas': {
       'a': '1960',
       'b': '1994',
       'c': '2000',
       'd': '1892',
    },
    'resposta_certa': 'd',
  },
  'Pergunta 6': {
    'pergunta': 'De onde é Billie Eilish? ',
    'respostas': {
       'a': 'Los Angeles',
       'b': 'Miami',
       'c': 'San Francisco',
       'd': 'Chicago',
    },
    'resposta_certa': 'a',
  },
  'Pergunta 7': {
    'pergunta': 'Quando a Netflix foi fundada? ',
    'respostas': {
       'a': '2001',
       'b': '2009',
       'c': '1997',
       'd': '2015',
    },
    'resposta_certa': 'c',
  },
  'Pergunta 8': {
    'pergunta': 'Em que ano Flamengo se tornou Bi campeão da Libertadores? ',
    'respostas': {
       'a': '2017',
       'b': '2010',
       'c': '2019',
       'd': '1999',
    },
    'resposta_certa': 'c',
  },
  'Pergunta 9': {
    'pergunta': 'Qual time de futebol é conhecido como “The Red Devils”? ',
    'respostas': {
       'a': 'Chelsea',
       'b': 'Manchester United',
       'c': 'Liverpool',
       'd': 'Manchester City',
    },
    'resposta_certa': 'b',
  },
  'Pergunta 10': {
    'pergunta': 'Como a Nike era chamada inicialmente? ',
    'respostas': {
       'a': 'Blue Ribbon Sports',
       'b': 'Total 90',
       'c': 'Wearing Sport',
       'd': 'Total Clothing',
    },
    'resposta_certa': 'a',
  },
}
print('-' * 50)
certas = 0
erradas = 0
for perg_key, perg_value in perguntas.items():
  print(f'{perg_key}: {perg_value["pergunta"]}')
  print('Escolha uma das opções abaixo:')
  print('-' * 50)
  for resposta_key, resposta_value in perg_value['respostas'].items():
    print(f'{resposta_key}: {resposta_value}')
  resposta_usuario = str(input('Sua Resposta: ')).lower().strip()
  print('-' * 50)
  if resposta_usuario == perg_value['resposta_certa']:
    certas += 1
  else:
    erradas += 1

num_perg = len(perguntas)
porcent_acerto = certas / num_perg * 100
porcent_erro = erradas / num_perg * 100

if porcent_acerto > 70:
  print(f'Você acertou {certas}  e errou {erradas}.')
  print(f'Você teve {porcent_acerto:.0f}% de acerto. Parabéns, você arrasou!')
elif porcent_acerto < 30:
  print(f'Você acertou {certas}  e errou {erradas}.')
  print(f'Você teve {porcent_acerto:.0f}% de acerto. Tenho certeza que na próxima você vai se sair melhor.')
elif porcent_acerto <= 69 and porcent_acerto >= 31:
  print(f'Você acertou {certas}  e errou {erradas}.')
  print(f'Você teve {porcent_acerto:.0f}% de acerto. Você ficou na média.')