print('-' * 50)
nivel = str(input('''
Escolhe seu tipo de Quiz:
[1] - Conhecimentos Gerais
[2] - Revolução Russa
[3] - Grandes Guerras Mundiais
''')).strip()
print('-' * 50)
if nivel == '1':
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
elif nivel == '2':
  print('Quiz sobre Revolução Russa')
  perguntas = {
    'Pergunta 1': {
      'pergunta': 'Em que ano aconteceu a Revolução Russa? ',
      'respostas': {
        'a': '1917',
        'b': '1916',
        'c': '1910',
        'd': '1920',
      },
      'resposta_certa': 'a',
    },
    'Pergunta 2': {
      'pergunta': 'O que foi a Revolução Russa? ',
      'respostas': {
        'a': 'Foi uma guerra entre Russos',
        'b': 'Foi uma série de conflitos Russos',
        'c': 'Foi uma série de eventos políticos na Rússia',
        'd': 'Foi a revolução industrial que ocorreu na Rússia',
      },
      'resposta_certa': 'c',
    },
    'Pergunta 3': {
      'pergunta': 'O que resultou no estabelecimento do poder soviético sob o controle do partido bolchevique? ',
      'respostas': {
        'a': 'Uma série de conclitos na Rússia',
        'b': 'A eliminação da autocracia russa e depois do Governo Provisório (Ruma)',
        'c': 'Uma série de guerras na Rússia, que, após a aadoção da autocracia russa e depois do Governo Provisório (Duma)',
        'd': 'Uma série de eventos políticos na Rússia, que, após a eliminação da autocracia russa e depois do Governo Provisório (Duma)',
      },
      'resposta_certa': 'd',
    },
     'Pergunta 4': {
      'pergunta': 'De que formar o Czar governa a Rússia? ',
      'respostas': {
        'a': 'Absolutista',
        'b': 'Democrática',
        'c': 'Capitalista',
        'd': 'Socialista',
      },
      'resposta_certa': 'a',
    },
    'Pergunta 5': {
      'pergunta': 'Como ficou conhecido dia em que Nicolau II mandou seu exército fuzilar milhares de manifestantes? ',
      'respostas': {
        'a': 'Dia de todos os mortos',
        'b': 'Domingo Sangrento',
        'c': 'Sábado Sangrento',
        'd': 'Domingo de Sangue',
      },
      'resposta_certa': 'b',
    },
    'Pergunta 6': {
      'pergunta': 'A revolução Russa compreendeu em duas fases, quais são elas? ',
      'respostas': {
        'a': 'A Revolução de Fevereiro de 1917 (março de 1917, pelo calendário ocidental, e a Revolução de Outubro (novembro de 1917, pelo calendário ocidental)',
        'b': 'A Revolução de Fevereiro de 1917 (março de 1917, pelo calendário oriental) e a Revolução de Outubro (novembro de 1917, pelo calendário ocidental)',
        'c': 'A Revolução de Fevereiro de 1917 (maio de 1917, pelo calendário oriental) e a Revolução de Outubro (setembro de 1917, pelo calendário ocidental)',
        'd': 'A Revolução de Outubro de 1917 (março de 1917, pelo calendário oriental) e a Revolução de Outubro (novembro de 1917, pelo calendário ocidental)',
      },
      'resposta_certa': 'a',
    },
    'Pergunta 7': {
      'pergunta': 'Quem liderou os bolcheviques? ',
      'respostas': {
        'a': 'Lenin',
        'b': 'Lemin',
        'c': 'Czar',
        'd': 'Llitch',
      },
      'resposta_certa': 'a',
    },
    'Pergunta 8': {
      'pergunta': 'Quem liderou os Mencheviques? ',
      'respostas': {
        'a': 'Mussolini',
        'b': 'Stalin',
        'c': 'Plekhanov',
        'd': 'Hitler',
      },
      'resposta_certa': 'c',
    },
    'Pergunta 9': {
      'pergunta': 'O que os bolcheviques defendiam? ',
      'respostas': {
        'a': 'Defendiam a ideia revolucionária da guerra armada para chegar ao poder',
        'b': 'Defendiam a ideia revolucionária da luta desarmada para chegar ao poder',
        'c': 'Defendiam a ideia evolucionista de se chegar ao poder através de vias normais e pacíficas como, por exemplo, as eleições',
        'd': 'Defendiam a ideia revolucionária da luta armada para chegar ao poder',
      },
      'resposta_certa': 'd',
    },
    'Pergunta 10': {
      'pergunta': 'O que foi o Tratado de Brest-Litovsk? ',
      'respostas': {
        'a': 'Foi um tratado de paz assinado entre a Rússia (já governada pelos bolcheviques) e as chamadas Potências Centrais (Alemanha, Áustria-Hungria, Bulgária e Império Otomano)',
        'b': 'Foi um tratado comercial',
        'c': 'Foi um tratado de paz assinado entre a Rússia (já governada pelos bolcheviques) e a Inglaterra',
        'd': 'Foi um tratado de paz assinado entre a Rússia (já governada pelos bolcheviques)e alemanha',
      },
      'resposta_certa': 'a',
    },
  }
elif nivel == '3':
  print('Quiz sobre Grandes Guerras Mundiais')
  perguntas = {
    'Pergunta 1': {
      'pergunta': 'Com relação à Primeira Guerra Mundial, é CORRETO afirmar: ',
      'respostas': {
        'a': 'Ela envolveu exclusivamente países europeus, portanto foi mais uma Guerra Civil Européia do que propriamente um conflito mundial',
        'b': 'Uma das suas principais causas foi a Revolução Russa, que colocou em risco a ordem liberal euroéia',
        'c': 'Como consequência houve uma redefinição do mapa europeu, inclusive com o estabelecimento de novos países',
      },
      'resposta_certa': 'c',
    },
    'Pergunta 2': {
      'pergunta': 'A Primeira Guerra Mundial, que enfraqueceu a Europa em população e importância econômica: ',
      'respostas': {
        'a': 'Acarretou a criação da Liga Pan Germânica encarregada de efetivar Anschluss',
        'b': 'Acarretou a difusão das ideias que apontavam as contradições do liberalismo',
        'c': 'Contribuiu para a formação, dentro da Sérvia, de sociedades secretas, tais como a Mão Negra, fundada em 1922',
      },
      'resposta_certa': 'b',
    },
    'Pergunta 3': {
      'pergunta': 'Dentre os fatores que conduzem a Primeira Guerra Mundial, destacamos: ',
      'respostas': {
        'a': 'Nacionalismo eslavo aliado à desagregação do Império Turco',
        'b': 'Acordo militar anglo-germânico visando à partilha da África',
        'c': 'Desequilíbrio internacional provocado pela aliança da Rússia com o Império Austro-Húngaro',
      },
      'resposta_certa': 'a',
    },
    'Pergunta 4': {
      'pergunta': 'Sobre os fatores responsáveis pela Grande Guerra, pode-se afirmar que: ',
      'respostas': {
        'a': 'A crise econômica do início do século reduziu o mercado consumidor de todas as nações capitalistas. Esse declínio enfraqueceu a democracia e estimulou o nacionalismo político e militar que desembocou na Guerra',
        'b': 'Os tratados de paz estabelecidos pelas potências européias solapavam a soberania dos novos Estados do Leste Europeu, o que criou condições de conflitos entre diferentes povos reunidos em um mesmo Estado',
        'c': 'As rivalidades imperialistas contribuíram para que a indústria bélica se desenvolvesse consideravelmente além de, associadas à corrida armamentista, dividir a Europa em dois blocos',
      },
      'resposta_certa': 'c',
    },
    'Pergunta 5': {
      'pergunta': 'Como consequências da Primeira Guerra Mundial, Áustria-Hungria r Alemanha tiveram que suportar tratados que foram antes imposições. Assim, desmembrando o Império A.-H. e mutilando territorialmente a Alemanha, foram impostos respectivamente pelos vencedores, os tratados de:',
      'respostas': {
        'a': 'Saint-Germain e Versalhes',
        'b': 'Trianon e Sèvres',
        'c': 'Lausanne e Versalhes',
      },
      'resposta_certa': 'a',
    },
    'Pergunta 6': {
      'pergunta': 'Dentre os fatores que desencadearam a Grande Guerra, não se pode citar:',
      'respostas': {
        'a': 'O colapso de diplomacia de Bismarck, baseada em acordos internacionais que visavam a manutenção do equilíbrio europeu, e sua substituição por uma política de poder mundial, adotada pela Alemanha guilhermina',
        'b': 'Os sistemas de alianças antagônicos e potencialmente conflitantes: de um lado a Tríplice Entente, e de outro os Impérios Centrais',
        'c': 'A desestabilização do status quo europeu provocada pelos EUA e França, visando a despertar os sentimentos nacionalistas das inúmeras nacionalidades submetidas ao jugo dos velhos impérios',
      },
      'resposta_certa': 'c',
    },
    'Pergunta 7': {
      'pergunta': 'Todos os fatores políticos destacados abaixo estão relacionados a eclosão da Grande Guerra, exceto:',
      'respostas': {
        'a': 'O conflito entre grandes potências frente às pretensões autonomistas de pequenos países',
        'b': 'A pressão das minorias nacionais, oprimidas pelos grandes impérios',
        'c': 'A estruturação da sociedade das Nações, decorrente da rivalidade e hostilidade que envolvia a Europa',
      },
      'resposta_certa': 'b',
    },
    'Pergunta 8': {
      'pergunta': 'Pode-se afirmar que a principal razão do conflito mundial em 1914 foi:',
      'respostas': {
        'a': 'O choque dos imperialismos, de raízes econômicas, mas que se expressou de forma política e militar',
        'b': 'A crise econômica que afetou significativamente os campos político e social das nações europeias',
        'c': 'O revanchismo nacionalista, de origem étnica, mas que se expressou através da expansão colonialista',
      },
      'resposta_certa': 'a',
    },
    'Pergunta 9': {
      'pergunta': 'O neocolonialismo relaciona-se com a eclosão da Primeira Guerra Mundial porque:',
      'respostas': {
        'a': 'A disputa por colônias entre as potências europeias acirrou as rivalidades já existentes',
        'b': 'A partilha Afro-Asiática satisfez as potências surgidas com as unificações italiana e alemã',
        'c': 'O imperialismo norte-americano foi eliminado no Pacífico, desenvolvendo o Japão',
      },
      'resposta_certa': 'a',
    },
    'Pergunta 10': {
      'pergunta': 'Impérios Alemão, Austro-Húngaro, Turco-Otomano e Itália. Inglaterra, França, Rússia, EUA, Itália, Sérvia. Quais são as tríplices respectivamente?',
      'respostas': {
        'a': 'Aliança e Entente',
        'b': 'Triplice Coroa e Coroado',
        'c': 'União Cara e Coroa',
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