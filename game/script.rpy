init python:
    style.my_custom_window = Style(style.window)
    style.my_custom_window.ysize = 350  # Altura da caixa de texto
    style.my_custom_window.background = Frame("gui/textbox.png", 12, 12)


define fade_out = Fade(0.5, 0, 0.5)  # Escurece a tela em 0.5 segundo
define fade_in = Fade(0.5, 0, 1.5, color="#000000")  # Clareia a tela em 0.5 segundo
# Definindo a transição dissolve

define jogador = Character("Jogador", window_style="my_custom_window")
define ship = Character("Shipman Harold",  color="#FF0000", window_style="my_custom_window")
define ed = Character("Ed Newgate", color="#0000FF", window_style="my_custom_window")

image bg room = "room.png"
image bg janela = "janela.png"
image bg conves = "conves.png"

# The game starts here.

label start:

    #scene bg conves with dissolve
    scene bg conves with fade_in

    # These display lines of dialogue.

    ed "Você se encontra deitado em um pequeno barco, balançando suavemente nas águas escuras em um mar desconhecido.\
        Você pisca, tentando orientar seus olhos na claridade repentina. As suas mãos se contorcem de dor, os músculos \
        contraídos e as articulações inchadas, você não pode continuar dormindo nesse estado, pode?" with dissolve


    ed "Agora, nesse barco à deriva, o som insistente de algo sendo preenchido ecoa do fundo da embarcação e um sentimento\
        de urgência te preenche. Você levanta abruptamente, olhando ao redor, com os sentidos em alerta máximo. Você escuta\
        um som distante de um barril sendo preenchido, um ruído incômodo e persistente."

    ship "As suas mãos latejam, uma lembrança dolorosa do que você fez. Talvez seja melhor você se deitar novamente, tentar\
          esquecer o que aconteceu. Não há sentido em investigar esse som estranho, é apenas mais um problema esperando por você.\
          É melhor que você simplesmente feche os olhos e tente esquecer. Deixe que o sono o leve, deixe que as águas escuras o acalmem."

# Definindo a variável persistente como False no início do jogo
default op_exp3_unlocked = False

label explorar:

    menu:
        "Que merda está acontecendo? \[Opção Exploratória\]":
            jump op_exp1

        " Como vocês descrevem o que eu faço ou sinto? \[Opção Exploratória\]":
            jump op_exp2
            
        "Eu conheço vocês. Isso não aconteceu antes? \[Opção Exploratória\]" if op_exp3_unlocked:
            jump op_exp3

        "Acho que devo voltar a dormir mesmo.":
            jump voltar_dormir

        "Tenho que descobrir o que é esse barulho.":
            jump descobrir_barulho

############################################################
############################################################
label op_exp1:

    jogador "Estou completamente perdido. O que está acontecendo? quem são vocês?"

    ed "Sabemos que pode ser desconcertante sentir-se perdido nesse mar de incertezas. Mas estamos aqui para ser seus guias."

    ship "Você está envolto numa escuridão, olhe ao redor e veja por si mesmo. Certamente, o céu poderia trazer alguma iluminação\
          mesmo à noite, mas não há sinal da Lua, nem mesmo das estrelas. Suas mãos doem, suas mãos pedem por alívio, e um som perturbador\
          ecoa. Um barril sendo preenchido é certamente algum tipo de mal presságio."

    jogador "Isso é estranho... Não me lembro de como vim parar aqui. E esse som... O que poderia ser?"

    ed "A memória é uma faca de dois gumes. Às vezes, é melhor deixar as lembranças adormecidas, pois podem revelar verdades que preferimos deixar\
        enterradas. Quanto ao som, você está prestes a descobrir. Siga o som, será quase como algo instintivo, como algo que você já fez antes."

    $ op_exp3_unlocked = True
    jump explorar

############################################################
############################################################
label op_exp2:

    jogador "Eu não sei exatamente como vocês fazem isso, mas me assusta como vocês descrevem o que faço, penso e sinto."

    ed "Não se assuste, o que temos é uma espécie de conexão empática contigo. Nós sentimos suas emoções, suas dores e suas\
        incertezas. Estamos aqui para ajudá-lo."

    jogador "Ainda assim, é estranho... Como se eu estivesse sendo observado de dentro da minha própria mente."

    ship "Dito isso, você parece exausto. Talvez seja hora de permitir que o sono o envolva novamente. Feche os olhos e poderá esquecer isso tudo."

    $ op_exp3_unlocked = True
    jump explorar

############################################################
############################################################
label op_exp3:
    jogador "Eu conheço vocês, isso não aconteceu antes?"

    ed "É compreensível que você possa sentir uma familiaridade\
        estranha conosco, mas é só uma coincidência. Não se preocupe, concentre-se no que está diante de você agora."

    ship "Sim, concordo, talvez seja apenas uma sensação passageira. Uma ilusão de uma mente confusa e cansada."

    jump explorar

############################################################
############################################################



label voltar_dormir:
    ship "Você fez a melhor escolha!"

    ed "Não!! Essa é uma pés..."

    ship "Olha, eu sei que tudo parece muito enigmático e está tudo bem… Você sabe no que essa escolha vai levar, certo?\
          Já podemos escutar um ruído de algo sendo preenchido lá embaixo... Confie em mim, essa é a melhor escolha e, na\
          verdade, sua única. Afinal, não há nada a ser feito."

    ship "Seus olhos estão pesados e a sua alma, bastante abalada, pede por descanso."

    jogador "hmmm... Tudo bem, tanto faz... estou meio cansado de qualquer forma."

    ship "Seus olhos estão pesados e a escuridão parece convidativa…"

    ship "Um pouco de paz, finalmente…"

    # Continuação após o escurecimento

    # Muda a cena para 'bg room' enquanto a tela está escura
    scene bg janela with fade_out and fade_in

    #continuação
    ship "O interior do quarto está quase vazio. O ar é pesado e tanto o chão quanto as paredes estão manchados de sangue. A única\
        peça de mobília é uma cama simples, manchada de vermelho e coberta por lençóis ensanguentados. Ao lado da cama, uma faca\
        repousa com sua lâmina reluzindo."

    ship "Você reconhece essa faca. Já a utilizou algumas vezes.\n\nVai precisar dela para fazer o que é preciso."

    label examinar_faca:

        menu:
            "Examinar faca \[Opção Exploratória\]":
                jump op_exp4
            "Prosseguir":
                jump prosseguir

    label prosseguir:

        #jogador pega a faca
        ship "Alguns tentam se iludir, mas você não. A morte é, e deve ser, a sua única saída."

        jogador "O que eu fiz? Por que estou aqui?"

        ship "Você sabe o que fez. E eu já lhe disse que essa faca é familiar. Quer mesmo relembrar todas as suas tragédias?"

        ship "Por favor, vamos poupar explicações... Aliás, por que questiona o seu destino? Tudo aqui se deve a suas próprias decisões."

        ship "Você precisa fazer o que é preciso."

        jogador "Não há outra opção? O que vai acontecer comigo?"

        ship "O seu tempo já se esgotou. Você teve toda uma vida para refletir. Em nenhum momento mostrou arrependimento \
            e agora pergunta sobre suas opções?"

        ship "Vamos logo! Estamos apenas adiando o irrevogável!"

        ship "Você empunha a faca e aponta para o pescoço..."

        jump start


    label op_exp4:

        ship "Você não se lembra? Você teve tanto cuidado para escolhê-la. Foi muita procura até chegar nessa faca. A lâmina\
              precisamente afiada, o brilho quase hipnotizante…"

        ship "Agora, depois de usá-la, você simplesmente esqueceu tudo? Foi tão traumático assim?"

        jogador "Pare de falar como se tudo aqui tivesse significado, como se você pudesse me entender. Essa é uma faca qualquer, nada mais."

        jump prosseguir

        
############################################################
############################################################
label descobrir_barulho:
    jump explorar

return
