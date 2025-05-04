default pressed_key = None

screen wait_key(message, keys):
    frame:
        align (0.5, 0.1)
        text message size 56 color "#ffffff" outlines [(2, "#000000")]

    for k in keys:
        key k action SetVariable("pressed_key", k)

define r = Character('Robi', color="#828282")
define e1 = Character('Estudante', color="#9367a3")
define e2 = Character('Estudante', color="#4ebfa5")
define e3 = Character('Estudante', color="#f2dc91")
define e4 = Character('Estudante', color="#0c0d1f")
define e5 = Character('Estudante', color="#586156")
define e6 = Character('Estudante', color="#47837c")
define e7 = Character('Estudante', color="#e57252")
define e8 = Character('Estudante', color="#f9c498")

label start:

    # mod00

    scene bg hist00 mod00 cena00

    "Do distante planeta Xylos, a unidade de observação Robi partiu em missão especial: entender as diferentes expressões de emoção de seres de outros planetas."

    scene bg hist00 mod00 cena01

    "Sua jornada o levou até a Terra, onde Robi encontrou padrões emocionais tão complexos que nem mesmo a tecnologia avançada de Xylos consegue compreender completamente."

    scene bg hist00 mod00 cena02
    scene bg hist00 mod00 cena03

    "Escolheu a Universidade de São Paulo como seu ponto de estudo. Mas Robi não consegue entender as emoções humanas sozinho, então agora ele precisa da sua ajuda!"

    scene bg hist00 mod00 cena04

    r "Minha programação me permite analisar dados complexos e catalogar fenômenos diversos. No entanto, ao chegar a este fascinante planeta Terra, deparei-me com algo... intrigante: as suas emoções."
    r "Esses estados internos que vocês manifestam através de expressões faciais, tons de voz e comportamentos... eles não se encaixam facilmente em meus algoritmos de análise padronizados. Confesso que estou tendo alguma dificuldade em 'decifrá-los'."
    r "Por isso, preciso da sua ajuda. Você, como ser humano, entende essas emoções de um jeito que eu ainda não consigo."
    r "Juntos, observaremos as diversas situações emocionais que ocorrem neste local, a Universidade de São Paulo. Sua percepção será fundamental para me ajudar a entender a alegria, o medo, a tristeza, o nojo e a raiva. Você aceita ser meu guia neste estudo?"

    scene bg hist00 mod01 cena00
    with squares

    e1 "Meu Deus, eu não acredito! Fomos aprovados!"
    e2 "Que demais! Todo o nosso esforço valeu a pena!"
    e3 "A melhor notícia do dia! Vamos comemorar!"

    scene bg hist00 mod01 cena01

    r "{i}(As expressões faciais deles mudaram drasticamente. Os cantos de suas bocas estão curvados para cima e seus olhos parecem mais brilhantes. Seus corpos estão em movimento constante... Parece que essa experiência é intensamente positiva.){/i}"

    show screen wait_key("Qual emoção eles estão sentindo? Alegria, Medo, Tristeza, Nojo ou Raiva?\nClique no botão da respectiva emoção!", ["K_a", "K_m", "K_t", "K_n", "K_r"])
    while pressed_key is None:
        $ renpy.pause(0.1)
    if pressed_key == "K_a":
        $ acerto()
    else:
        $ erro()
    hide screen wait_key
    $ pressed_key = None

    "O dia passa na USP, e, sem Robi perceber, o céu começa a escurecer na Cidade Universitária..."

    scene bg hist00 mod02 cena00

    e4 "Que barulho foi esse?! Melhor eu ir mais rápido..."

    scene bg hist00 mod02 cena01

    r "{i}(O ritmo dos movimentos dele mudou repentinamente e seus olhos estão bem abertos. Parece que algo o deixou... alerta e desconfortável.){/i}"

    show screen wait_key("Qual emoção o aluno parece estar sentindo? Alegria, Medo, Tristeza, Nojo ou Raiva?\nClique no botão da respectiva emoção!", ["K_a", "K_m", "K_t", "K_n", "K_r"])
    while pressed_key is None:
        $ renpy.pause(0.1)
    if pressed_key == "K_m":
        $ acerto()
    else:
        $ erro()
    hide screen wait_key
    $ pressed_key = None

    "O dia amanhece, e os alunos estão ansiosos para receber o resultado da prova de cálculo que fizeram. Todos parecem ter ido bem, com uma exceção apenas..."

    scene bg hist00 mod03 cena00

    e5 "Eu não consigo acreditar que isso aconteceu...Como eu posso estudar tantas horas cálculo e ainda ir mal na prova?"

    scene bg hist00 mod03 cena01

    r "{i}(Ele está imóvel e parece... encolhido. Seus olhos parecem mais úmidos que o normal. Parece que ela está passando por uma experiência emocionalmente negativa.){/i}"

    show screen wait_key("Qual emoção o aluno parece estar sentindo? Alegria, Medo, Tristeza, Nojo ou Raiva?\nClique no botão da respectiva emoção!", ["K_a", "K_m", "K_t", "K_n", "K_r"])
    while pressed_key is None:
        $ renpy.pause(0.1)
    if pressed_key == "K_t":
        $ acerto()
    else:
        $ erro()
    hide screen wait_key
    $ pressed_key = None

    "Chegou a hora do almoço, e os universitários estão indo comer. Estão esfomeados!"

    scene bg hist00 mod04 cena00

    e6 "Eca! O que é isso? É {b}ALFACE, TOMATE E LIMÃO?!{/b} Eu odeio isso, é muito estranho, sem falar que não parece nada bom..."

    scene bg hist00 mod04 cena01

    r "{i}(A forma do rosto dele mudou e ele parece estar se afastando daquela comida. Parece que ele teve uma reação muito negativa a algo que percebeu através dos seus sentidos.){/i}"

    show screen wait_key("Qual emoção a aluna parece estar sentindo? Alegria, Medo, Tristeza, Nojo ou Raiva?\nClique no botão da respectiva emoção!", ["K_a", "K_m", "K_t", "K_n", "K_r"])
    while pressed_key is None:
        $ renpy.pause(0.1)
    if pressed_key == "K_n":
        $ acerto()
    else:
        $ erro()
    hide screen wait_key
    $ pressed_key = None

    "Voltando à sala de aula para dar continuidade a sua pesquisa sobre o comportamento humano, Robi se depara com uma situação estranha que se estabelece entre dois estudantes."

    scene bg hist00 mod05 cena00

    e7 "Eu estou {b}completamente revoltado!{/b} Você não fez {b}nada{/b} que eu lhe pedi do trabalho!"
    e8 "Eu tive problemas, não é justo você falar assim!"

    scene bg hist00 mod05 cena01

    r "{i}(As vozes deles estão mais altas e o tom parece... carregado. O rosto de um deles está com uma cor diferente e seus braços estão tensos. Parece haver um conflito emocional intenso entre eles.){/i}"

    show screen wait_key("Qual emoção o aluno da esquerda parece estar sentindo? Alegria, Medo, Tristeza, Nojo ou Raiva?\nClique no botão da respectiva emoção!", ["K_a", "K_m", "K_t", "K_n", "K_r"])
    while pressed_key is None:
        $ renpy.pause(0.1)
    if pressed_key == "K_r":
        $ acerto()
    else:
        $ erro()
    hide screen wait_key
    $ pressed_key = None

    scene bg hist00 mod00 cena02

    r "Hoje, o nosso dia foi cheio de emoção!"
    r "Conseguimos experimentar várias delas em diversos contextos!"
    r "Mas acho que meu {i}hardware{/i} está saturado por hoje..."

    "Robi, então, se prepara para retornar a seu planeta natal, satisfeito com sua pesquisa."
    "Daqui a algumas poucas horas, já decola rumo a Xylos."

    r "Adorei essa espécie humana! Não vejo a hora de voltar aqui!"

    "Veja quantas emoções você acertou dos cinco desafios propostos! Confira o número no {i}display{/i}!"

    return

init python:
    import os

    def acerto():
        with open("gpio_control.txt", "w") as f:
            f.write("ACERTO")

    def erro():
        with open("gpio_control.txt", "w") as f:
            f.write("ERRO")
