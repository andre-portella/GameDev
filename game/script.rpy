# Remover e inserir em 'screens.rpy'
init python:
    style.my_custom_window = Style(style.window)
    style.my_custom_window.background = Frame("gui/textbox.png", 12, 12)

    image_timer = 4.0 # Inicialmente 4s

    def blink(trans, st, at):
        global image_timer

        if st >= image_timer:
            image_timer = 2.0 # Atualizar a cada 2s
            return None
        else:
            return 0

define fade_out = Fade(0.5, 0, 0.5)
define fade_in = Fade(0.5, 0, 1.5, color="#000000")

define jogador = Character("Jogador", window_style="my_custom_window")
define ship = Character("Shipman Harold",  color="#FF0000", window_style="my_custom_window")
define ed = Character("Ed Newgate", color="#0000FF", window_style="my_custom_window")

image bg room = "room.png"
image bg janela = "janela.png"
image bg conves = "conves.png"
    
image backgrounds:
    "room.png"
    function blink
    "conves.png"
    function blink
    repeat

# The game starts here.
label start:

    scene backgrounds with fade_in

    ed "Você se encontra deitado em um pequeno barco, balançando suavemente nas águas escuras em um mar desconhecido.\
        Você pisca, tentando orientar seus olhos na claridade repentina. As suas mãos se contorcem de dor, os músculos \
        contraídos e as articulações inchadas, você não pode continuar dormindo nesse estado, pode?" with dissolve


    ed "Agora, nesse barco à deriva, o som insistente de algo sendo preenchido ecoa do fundo da embarcação e um sentimento\
        de urgência te preenche. Você levanta abruptamente, olhando ao redor, com os sentidos em alerta máximo. Você escuta\
        um som distante de um barril sendo preenchido, um ruído incômodo e persistente." with dissolve

    ship "As suas mãos latejam, uma lembrança dolorosa do que você fez. Talvez seja melhor você se deitar novamente, tentar\
          esquecer o que aconteceu. Não há sentido em investigar esse som estranho, é apenas mais um problema esperando por você.\
          É melhor que você simplesmente feche os olhos e tente esquecer. Deixe que o sono o leve, deixe que as águas escuras o acalmem." with dissolve

# Definindo a variável persistente como False no início do jogo
default op_exp3_unlocked = False

label explorar:

    menu:
        "{b}Que merda está acontecendo? \[Opção Exploratória\]{b}":
            jump op_exp1

        "{b}Como vocês descrevem o que eu faço ou sinto? \[Opção Exploratória\]{b}":
            jump op_exp2
            
        "{b}Eu conheço vocês. Isso não aconteceu antes? \[Opção Exploratória\]{b}" if op_exp3_unlocked:
            jump op_exp3

        "{b}Acho que devo voltar a dormir mesmo.{b}":
            jump voltar_dormir

        "{b}Tenho que descobrir o que é esse barulho.{b}":
            jump descobrir_barulho

############################################################
############################################################
label op_exp1:

    jogador "Estou completamente perdido. O que está acontecendo? quem são vocês?" with dissolve

    ed "Sabemos que pode ser desconcertante sentir-se perdido nesse mar de incertezas. Mas estamos aqui para ser seus guias." with dissolve

    ship "Você está envolto numa escuridão, olhe ao redor e veja por si mesmo. Certamente, o céu poderia trazer alguma iluminação\
          mesmo à noite, mas não há sinal da Lua, nem mesmo das estrelas. Suas mãos doem, suas mãos pedem por alívio, e um som perturbador\
          ecoa. Um barril sendo preenchido é certamente algum tipo de mal presságio." with dissolve

    jogador "Isso é estranho... Não me lembro de como vim parar aqui. E esse som... O que poderia ser?" with dissolve

    ed "A memória é uma faca de dois gumes. Às vezes, é melhor deixar as lembranças adormecidas, pois podem revelar verdades que preferimos deixar\
        enterradas. Quanto ao som, você está prestes a descobrir. Siga o som, será quase como algo instintivo, como algo que você já fez antes." with dissolve

    jump explorar

############################################################
############################################################
label op_exp2:

    jogador "Eu não sei exatamente como vocês fazem isso, mas me assusta como vocês descrevem o que faço, penso e sinto." with dissolve

    ed "Não se assuste, o que temos é uma espécie de conexão empática contigo. Nós sentimos suas emoções, suas dores e suas\
        incertezas. Estamos aqui para ajudá-lo." with dissolve

    jogador "Ainda assim, é estranho... Como se eu estivesse sendo observado de dentro da minha própria mente." with dissolve

    ship "Dito isso, você parece exausto. Talvez seja hora de permitir que o sono o envolva novamente. Feche os olhos e poderá esquecer isso tudo." with dissolve

    jump explorar

############################################################
############################################################
label op_exp3:
    jogador "Eu conheço vocês, isso não aconteceu antes?" with dissolve

    ed "É compreensível que você possa sentir uma familiaridade\
        estranha conosco, mas é só uma coincidência. Não se preocupe, concentre-se no que está diante de você agora." with dissolve

    ship "Sim, concordo, talvez seja apenas uma sensação passageira. Uma ilusão de uma mente confusa e cansada." with dissolve

    jump explorar

############################################################
############################################################



label voltar_dormir:

    ship "Você fez a melhor escolha!" with dissolve

    ed "Não!! Essa é uma pés..." with dissolve

    ship "Olha, eu sei que tudo parece muito enigmático e está tudo bem… Você sabe no que essa escolha vai levar, certo?\
          Já podemos escutar um ruído de algo sendo preenchido lá embaixo... Confie em mim, essa é a melhor escolha e, na\
          verdade, sua única. Afinal, não há nada a ser feito." with dissolve

    ship "Seus olhos estão pesados e a sua alma, bastante abalada, pede por descanso." with dissolve

    jogador "hmmm... Tudo bem, tanto faz... estou meio cansado de qualquer forma." with dissolve

    ship "Seus olhos estão pesados e a escuridão parece convidativa…" with dissolve

    ship "Um pouco de paz, finalmente…" with dissolve

    # Continuação após o escurecimento

    # Muda a cena para 'bg room' enquanto a tela está escura
    scene bg janela with fade_out and fade_in

    #continuação
    ship "O interior do quarto está quase vazio. O ar é pesado e tanto o chão quanto as paredes estão manchados de sangue. A única\
        peça de mobília é uma cama simples, manchada de vermelho e coberta por lençóis ensanguentados. Ao lado da cama, uma faca\
        repousa com sua lâmina reluzindo." with dissolve

    ship "Você reconhece essa faca. Já a utilizou algumas vezes.\n\nVai precisar dela para fazer o que é preciso." with dissolve

    label examinar_faca:

        $ op_exp3_unlocked = True

        menu:
            "{b}Examinar faca \[Opção Exploratória\]{b}":
                jump op_exp4
            "{b}Prosseguir{b}":
                jump prosseguir

    label prosseguir:

        #jogador pega a faca
        ship "Alguns tentam se iludir, mas você não. A morte é, e deve ser, a sua única saída." with dissolve

        jogador "O que eu fiz? Por que estou aqui?" with dissolve

        ship "Você sabe o que fez. E eu já lhe disse que essa faca é familiar. Quer mesmo relembrar todas as suas tragédias?" with dissolve

        ship "Por favor, vamos poupar explicações... Aliás, por que questiona o seu destino? Tudo aqui se deve a suas próprias decisões." with dissolve

        ship "Você precisa fazer o que é preciso." with dissolve

        jogador "Não há outra opção? O que vai acontecer comigo?" with dissolve

        ship "O seu tempo já se esgotou. Você teve toda uma vida para refletir. Em nenhum momento mostrou arrependimento \
            e agora pergunta sobre suas opções?" with dissolve

        ship "Vamos logo! Estamos apenas adiando o irrevogável!" with dissolve

        ship "Você empunha a faca e aponta para o pescoço..." with dissolve

        jump start


    label op_exp4:

        ship "Você não se lembra? Você teve tanto cuidado para escolhê-la. Foi muita procura até chegar nessa faca. A lâmina\
              precisamente afiada, o brilho quase hipnotizante…" with dissolve

        ship "Agora, depois de usá-la, você simplesmente esqueceu tudo? Foi tão traumático assim?" with dissolve

        jogador "Pare de falar como se tudo aqui tivesse significado, como se você pudesse me entender. Essa é uma faca qualquer, nada mais." with dissolve

        jump prosseguir

    

        
############################################################
############################################################
label descobrir_barulho:

    $ op_exp3_unlocked = True

    jump explorar

return
