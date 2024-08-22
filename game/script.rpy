

default flash = Fade(.25, 0, .75, color="#fff") # usa isso aq pra dar um flash branco na imagem

transform screenshake:
    linear 0.15 xoffset -5 yoffset -5
    linear 0.1 xoffset 10 yoffset 7
    linear 0.13 xoffset 2 yoffset -2
    linear 0.05 xoffset -1 yoffset 1
    linear 0.13 xoffset -8 yoffset -1
    linear 0.09 xoffset 3 yoffset 1
    linear 0.07 xoffset -2 yoffset -10
    linear 0.1 xoffset 6 yoffset 3
    linear 0.11 xoffset -5 yoffset 2
    linear 0.08 xoffset 5 yoffset -4
    linear 0.05 xoffset -6 yoffset -5
    linear 0.14 xoffset 5 yoffset 3
    linear 0.06 xoffset 1 yoffset -9
    linear 0.1 xoffset 10 yoffset 7
    repeat

transform shaketiny:
    linear 0.05 xoffset -1 yoffset 1
    linear 0.13 xoffset -8 yoffset -1
    linear 0.09 xoffset 3 yoffset 1
    linear 0.07 xoffset -2 yoffset -10
    linear 0.1 xoffset 6 yoffset 3


transform shakeshort:
    linear 0.15 xoffset -5 yoffset -5
    linear 0.1 xoffset 10 yoffset 7
    linear 0.13 xoffset 2 yoffset -2
    linear 0.05 xoffset -1 yoffset 1
    linear 0.13 xoffset -8 yoffset -1
    linear 0.09 xoffset 3 yoffset 1
    linear 0.07 xoffset -2 yoffset -10
    linear 0.1 xoffset 6 yoffset 3
    linear 0.11 xoffset -5 yoffset 2
    linear 0.08 xoffset 5 yoffset -4
    linear 0.05 xoffset -6 yoffset -5
    linear 0.14 xoffset 5 yoffset 3
    linear 0.06 xoffset 1 yoffset -9
    linear 0.1 xoffset 10 yoffset 7
    linear 0.1 xoffset 0 yoffset 0

transform sway:
    linear 2.0 xoffset -10
    linear 2.5 xoffset 15
    repeat

transform swayblur:
    linear 1.0 blur 16 xoffset -10
    linear 2.5 blur 5 xoffset 15
    repeat

transform collapse:
    easein .15 yoffset -110
    easein 0.05 yoffset -100

transform rise:
    easein .15 yoffset 10
    easein 0.05 yoffset 0

transform chin:
    easein .15 yoffset -5

transform bigchin:
    easein .15 yoffset -20

transform up:
    easein .15 yoffset 60
    easein 0.05 yoffset 50

transform distortion:
    shader "distortion_perlin"
    u_frame(4.)
    u_speed(0.15)
    u_distortion(0.0002)
    u_distortion2(0.0005)
    u_scale(1.5)
    u_scale2(200.0)
    u_interlacing(0.00010)
    u_interlacing_y(512.0)
    u_vignette(0.5)
    u_static(0.075)
    # u_debug(1.0 if shader_debug_mode else 0.0)
    u_debug(0.0)

transform distortion_personagem:
    shader "distortion_perlin"
    u_frame(4.)
    u_speed(0.15)
    u_distortion(0.0002)
    u_distortion2(0.0005)
    u_scale(1.5)
    u_scale2(200.0)
    u_interlacing(0.00010)
    u_interlacing_y(128.0)
    u_vignette(0.5)
    u_static(0.075)
    u_debug(0.0)
    # u_debug(1.0 if shader_debug_mode else 0.0)

transform distortion_back:
    shader "distortion_perlin"
    u_frame(4.)
    u_speed(0.15)
    u_distortion(0.0002)
    u_distortion2(0.0005)
    u_scale(1.5)
    u_scale2(200.0)
    u_interlacing(0.00010)
    u_interlacing_y(512.0)
    u_vignette(0.5)
    u_static(0.075)
    # u_debug(1.0 if shader_debug_mode else 0.0)
    u_debug(0.0)

transform distortion_fore:
    shader "distortion_perlin"
    u_frame(4.)
    u_speed(1.15)
    u_distortion(0.0006)
    u_distortion2(0.0010)
    u_scale(5.0)
    u_scale2(100.0)
    u_interlacing(0.00065)
    u_interlacing_y(64.0)
    u_vignette(0.5)
    u_static(0.075)
    #u_debug(1.0 if shader_debug_mode else 0.0)
    u_debug(0.0)

transform strongwarp:
    shader "distortion_perlin"
    u_frame(4.)
    u_speed(1.15)
    u_distortion(0.0006)
    u_distortion2(0.0010)
    u_scale(5.0)
    u_scale2(100.0)
    u_interlacing(0.00065)
    u_interlacing_y(64.0)
    u_vignette(0.5)
    u_static(0.075)
    #u_debug(1.0 if shader_debug_mode else 0.0)
    u_debug(0.0)

transform midwarp:
    shader "distortion_perlin"
    u_frame(4.)
    u_speed(1.15)
    u_distortion(0.0005)
    u_distortion2(0.0008)
    u_scale(4.0)
    u_scale2(100.0)
    u_interlacing(0.00065)
    u_interlacing_y(64.0)
    u_vignette(0.5)
    u_static(0.075)
    #u_debug(1.0 if shader_debug_mode else 0.0)
    u_debug(0.0)

transform spectre_small_zoom:
    ease 0.5 zoom 1.05 yoffset 50

transform spectre_small_zoom_instant:
    ease 0.5 zoom 1.05 yoffset 50

transform apoth_zoom_in:
    ease 0.5 zoom 1.1 yoffset 100 xoffset -50

transform apoth_zoom_out:
    ease 0.5 zoom 1.0 yoffset -100 xoffset -200

transform xflip:
    yzoom -1

transform zoom_in:
    ease 0.5 zoom 1.1

transform zoom_instant:
    zoom 1.1

transform big_zoom:
    ease 1.0 zoom 1.2 yoffset 200

transform big_zoom_instant:
    zoom 1.2 yoffset 200

transform small_zoom:
    ease 1.0 zoom 1.1 yoffset 100

transform zoom_pracima1:
    ease 0.5 zoom 1.06 yoffset 10
    ease 0.15 zoom 1.05

transform zoom_pracima2:
    ease 0.5 zoom 1.11 yoffset 20
    ease 0.15 zoom 1.1

transform zoom_pracima3:
    ease 0.5 zoom 1.16
    ease 0.15 zoom 1.15

transform zoom_out:
        ease 0.5 zoom 1.0

transform zoom_out_far:
    ease 0.5 zoom 0.95


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

image bg porta = "porta.png"
image bg janela = "janela.png"
image bg conves = "conves.png"

image bg_porta = At("bg porta", distortion)

image bg porta_desfoque = im.Blur("porta.png", 10)

# transição entre planos de fundo
image backgrounds:
    "conves.png"
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

    # Continuação
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


        # Reinício do jogo
        jump start


    label op_exp4:

        ship "Você não se lembra? Você teve tanto cuidado para escolhê-la. Foi muita procura até chegar nessa faca. A lâmina\
              precisamente afiada, o brilho quase hipnotizante…" with dissolve

        ship "Agora, depois de usá-la, você simplesmente esqueceu tudo? Foi tão traumático assim?" with dissolve

        jogador "Pare de falar como se tudo aqui tivesse significado, como se você pudesse me entender. Essa é uma faca qualquer, nada mais." with dissolve

        jump prosseguir

    

        
############################################################
############################################################

#FELIPE

label descobrir_barulho:

    $ op_exp3_unlocked = True

    ship 'Parte do Felipe.'

    jump desistir_conserto



label desistir_conserto:

    ed "Como pode desistir? Não vai ao menos tentar? Você pode consertar o vazamento. Tem uma resina bem ali" with dissolve

    jogador "Não vale a pena. Vocês já me falaram que estamos adiando o inevitável. Por que lutar?" with dissolve

    ship "Um pouco de sensatez, finalmente." with dissolve

    ed "Essa decisão é trágica. Mas não se engane, cada escolha tem seu preço. O perdão não é garantido." with dissolve

    ship "Ele já tomou sua decisão! Seus discursos são inúteis, apenas lamentações indistinguíveis. Deixe-o agir com um propósito maior do que si mesmo. Somente assim, depois de tantos anos, ele poderá ter a paz que tanto buscou." with dissolve

    ship "As névoas tomam conta do seu destino, nada mais parece manter a forma. O ar é denso, como se cada respiração fosse um mergulho em águas turvas. Você tateia o espaço ao seu redor, mas os contornos se desvanecem, com tudo escapando entre seus dedos." with dissolve

    scene bg_porta 
    menu:
        "{b}O que está acontecendo? \[Opção Exploratória\]{b}":
            jump op_exp5

        "{b}Eu não posso deixar esse vazamento continuar.{b}":
            jump voltar_corredor


    label voltar_corredor:
        jogador "Preciso vedar logo essa rachadura." with dissolve

        jump descobrir_barulho


    label op_exp5:

        scene bg porta

        jogador "Por que está tudo tão distorcido? Não estou entendendo nada… são alucinações?" with dissolve
        
        ship "O que você vê não são meras alucinações, mas o seu próprio passado, distorcido pelos entorpecentes que outrora foram seu refúgio. Cada contorno borrado, cada sensação incompreendida, ecoando em sua mente são vestígios de uma vida marcada pela dependência." with dissolve


    



return
