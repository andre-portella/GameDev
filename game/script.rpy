

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
    renpy.music.register_channel("sfx2", "sfx", loop=False)

    #canal de audio criado
    # renpy.music.register_channel("layer1", "sfx", synchro_start=True)

    item_desperdicado = False #variavel para o trigger de quando o item eh desperdicado
    item_pego = False
    janela_consertada = False

    olhou_retrato_mulher = False

    max_tentativas = 3

    contador_esperanca = 0

    entrar_quarto = False

    inicio = True

    #Não entrar no quarto proibido ate o jogador decidir se abre a porta ou não
    porta_trancada = True #//%Variavel que define quando a porta esta trancada ou nao. Ela fica trancada ate o jogador desperdicar o item, isso eh feito para corrigir um erro
    # do roteiro, faltava uma possibilidade de evento e fazer isso corrige o probelma
    style.my_custom_window = Style(style.window)
    style.my_custom_window.background = Frame("gui/textbox.png", 12, 12)

init 2 python:  # A prioridade '2' garante que o estilo padrão esteja carregado
    # Baseado no estilo padrão da namebox
    style.my_namebox_style = Style(style.default)  
    style.my_namebox_style.xalign = 1.0           # Alinha horizontalmente à direita
    style.my_namebox_style.margin = (0, 0, 465, 0) # Adiciona margem para afastar da borda direita
    style.my_namebox_style.padding = (10, 5)      # Ajusta o espaçamento interno


transform blur_image:
        blur 10.0  # O valor indica a quantidade de desfoque


define fade_out = Fade(0.5, 0, 0.5)
define fade_in = Fade(0.5, 0, 1.5, color="#000000")

define jogador = Character("Caronte", window_style="my_custom_window",  what_slow_cps=40)
define ship = Character("Shipman Harold",  color="#FF0000", window_style="my_custom_window",  what_slow_cps=40)
define ed = Character("Ed Newgate", color="#0000FF", window_style="my_custom_window",  what_slow_cps=40, namebox_style="my_namebox_style")



define unk = Character(" ", color="#FFFFFF", what_slow_cps=40, window_style="my_custom_window")
define maria = Character("Maria", color="#FFC0CB", what_slow_cps=40, window_style="my_custom_window")

#mudar a cor do texto da fala para vermelho dps
define figura = Character(" ", color="#FFFFFF", what_slow_cps=40, window_style="my_custom_window")

image porta = "porta.png"
image rachadura = "rachadura.png"
image rachadura_consertada = "janela_consertada.png"
image conves = "conves.png"
image barco_mar = "barco_mar.png"
image corredor = 'corredor.png'
image banheiro = 'banero.png'
image banheiro_remedio = 'baneroaber.png'
image maria_morta = 'baneromorto.png'
image maria_balada = 'Bar.png'
image escadaria_super_longa = 'escada.png'
image silhueta2 = 'Silhueta2.png'
image silhueta3 = 'Silhueta3.png'
# image tres_portas

image black = "black.png"
image quarto_probido_entrada = "quarto.png"
image corpo_mulher_morta = "corpo.png"
image vista_mar = "imagem_provisoria_barco_mar.png"
image vermelho = "img_vermelho_1.jpg"


#------- IMAGENS NÃO FEITAS AINDA --------------
# image bg corredor = "corredor.png"
#-----------------------------------------------

image corredor = 'corredor.png'
define fade = Fade(0.5, 1.0, 0.0, color="#000")

image quarto_distorcido = im.Blur('quarto.png', 3)
image porta_blur = im.Blur('porta.png', 5)

image porta_midwarp = At("porta.png", midwarp)
image conves_distortion = At("conves.png", distortion)

image porta_strongwarp = At("porta.png", strongwarp)


define text_cps_sound = "typewriter.wav"

# ---------- Variaveis Auxiliares ----------------#
# Variaveis que definem coisas auxiliares como qual trigger para a rota foi acionado ou desacionado, variaveis para dar efeito de alguma coisa etc.
define auxiliar = Character(" ", color="#FFFFFF", window_style="my_custom_window")

#--------------------------

# transição entre planos de fundo
# image backgrounds:
#     "conves.png"
#     function blink
#     "conves.png"
#     function blink
#     repeat

# The game starts here.

label tela_inicial:

    show screen titulo_jogo  # Exibe a tela do título

label start:
    play music "<from 10.0>rough-sea-mar-bravo-23670.mp3"

    show screen titulo_jogo  # Exibe a tela do título    

    # Aguarda 2 segundos para esconder a tela de título
    $ renpy.pause(2.0)


    hide screen titulo_jogo  # Garante que a tela de título seja escondida antes de prosseguir

    scene conves_distortion with fade_in

    ed "Você se encontra deitado em um pequeno barco, balançando suavemente nas águas escuras em um mar desconhecido.\
        Você pisca, tentando orientar seus olhos na claridade repentina. As suas mãos se contorcem de dor, os músculos \
        contraídos e as articulações inchadas, você não pode continuar dormindo nesse estado, pode?" with dissolve
    
    ed "Agora, nesse barco à deriva, o som insistente de algo sendo preenchido ecoa do fundo da embarcação e um sentimento\
        de urgência te preenche." with dissolve

    ed "Você levanta abruptamente, olhando ao redor, com os sentidos em alerta máximo. Você escuta\
        um som distante de um barril sendo preenchido, um ruído incômodo e persistente." with dissolve


    voice "start/ship_label_start1.mp3"
    ship "As suas mãos latejam, uma lembrança dolorosa do que você fez. Talvez seja melhor você se deitar novamente, tentar\
        esquecer o que aconteceu. " with dissolve

    voice "start/ship_label_start2.mp3"
    ship "Não há sentido em investigar esse som estranho, é apenas mais um problema esperando por você.\
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

    jogador "Estou completamente perdido. O que está acontecendo? Quem são vocês?" with dissolve

    ed "Sabemos que pode ser desconcertante sentir-se perdido nesse mar de incertezas. Mas estamos aqui para ser seus guias." with dissolve

    voice "exploratorias/ship_label_op_exp1.mp3"
    ship "Você está envolto numa escuridão, olhe ao redor e veja por si mesmo. Certamente, o céu poderia trazer alguma iluminação\
        mesmo à noite, mas não há sinal da Lua, nem mesmo das estrelas." with dissolve

    voice "exploratorias/ship_label_op_exp1_2.mp3"
    ship "Um som perturbador ecoa, como se um barril fosse preenchido - o que é certamente algum tipo de mau presságio." with dissolve

    jogador "Isso é estranho... Não me lembro de como vim parar aqui. E esse som... O que poderia ser?" with dissolve

    ed "A memória é uma faca de dois gumes. Às vezes, é melhor deixar as lembranças adormecidas, pois podem revelar verdades que preferimos deixar\
        enterradas." with dissolve
    
    ed "Quanto ao som, você está prestes a descobrir. Siga o som, será quase como algo instintivo, como algo que você já fez antes." with dissolve

    jump explorar

############################################################
############################################################
label op_exp2:

    jogador "Eu não sei exatamente como vocês fazem isso, mas me assusta como vocês descrevem o que faço, penso e sinto." with dissolve

    ed "Não se assuste, o que temos é uma espécie de conexão empática contigo. Nós sentimos suas emoções, suas dores e suas\
        incertezas. Estamos aqui para ajudá-lo." with dissolve

    jogador "Ainda assim, é estranho... É como se eu estivesse sendo observado de dentro da minha própria mente." with dissolve

    voice "exploratorias/ship_label_op_exp2.mp3"
    ship "Dito isso, você parece exausto. Talvez seja hora de permitir que o sono o envolva novamente. Feche os olhos e poderá esquecer isso tudo." with dissolve

    jump explorar

############################################################
############################################################
label op_exp3:
    jogador "Eu conheço vocês, isso não aconteceu antes?" with dissolve

    ed "É compreensível que você possa sentir uma familiaridade\
        estranha conosco, mas é só uma coincidência. Não se preocupe, concentre-se no que está diante de você agora." with dissolve

    voice "exploratorias/ship_label_op_exp3.mp3"
    ship "Sim, concordo, talvez seja apenas uma sensação passageira. Uma ilusão de uma mente confusa e cansada." with dissolve

    jump explorar

############################################################
############################################################

label voltar_dormir:

    voice "voltar_dormir/ship_label_voltar_dormir.mp3"
    ship "Você fez a melhor escolha!" with dissolve

    ed "Não! Essa é uma pés-" with dissolve

    voice "voltar_dormir/ship_label_voltar_dormir_2.mp3"
    ship "Olha, eu sei que tudo parece muito enigmático e está tudo bem… Você sabe no que essa escolha vai levar, certo?\
        Já podemos escutar um ruído de algo sendo preenchido lá embaixo..." with dissolve

    voice "voltar_dormir/ship_label_voltar_dormir_3.mp3"
    ship "Confie em mim, essa é a melhor escolha e, na verdade, sua única. Afinal, não há nada a ser feito." with dissolve

    voice "voltar_dormir/ship_label_voltar_dormir_4.mp3"
    ship "Seus olhos estão pesados, eles pedem por descanso." with dissolve

    jogador "Hmmm... Tudo bem, tanto faz... estou meio cansado de qualquer forma." with dissolve

    voice "voltar_dormir/ship_label_voltar_dormir_5.mp3"
    ship "Um pouco de paz, finalmente…" with dissolve

    # Continuação após o escurecimento

    stop music

    scene quarto_distorcido with fade_out and fade_in

    # Continuação

    voice "voltar_dormir/ship_label_voltar_dormir_6.mp3"
    ship "O interior do quarto está quase vazio. O ar é pesado e tanto o chão quanto as paredes estão manchados de sangue. A única\
        peça de mobília é uma cama simples, manchada de vermelho e coberta por lençóis ensanguentados. Ao lado da cama, uma faca\
        repousa com sua lâmina reluzindo." with dissolve


    voice "voltar_dormir/ship_label_voltar_dormir_7.mp3"
    ship "Você reconhece essa faca. Já a utilizou algumas vezes. \nVai precisar dela para fazer o que é preciso." with dissolve

    label examinar_faca:

        $ op_exp3_unlocked = True

        menu:
            "{b}Examinar faca \[Opção Exploratória\]{b}":
                jump op_exp4
            "{b}Prosseguir{b}":
                jump prosseguir

    label prosseguir:

        #jogador pega a faca

        voice "prosseguir/ship_label_prosseguir.mp3"
        ship "Alguns tentam se iludir, mas você não. Poderíamos apenas seguir pelo caminho mais fácil." with dissolve
        
        jogador "O que eu fiz? Por que estou aqui?" with dissolve

        voice "prosseguir/ship_label_prosseguir_2.mp3"
        ship "Você sabe o que fez. E eu já lhe disse que essa faca é familiar. Quer mesmo relembrar o seu passado?" with dissolve

        voice "prosseguir/ship_label_prosseguir_3.mp3"
        ship "Por favor, vamos poupar explicações... Aliás, por que questiona o seu destino? Tudo aqui se deve a suas próprias decisões." with dissolve

        voice "prosseguir/ship_label_prosseguir_4.mp3"
        ship "Você precisa fazer o que é preciso." with dissolve

        jogador "Não há outra opção? O que vai acontecer comigo?" with dissolve

        voice "prosseguir/ship_label_prosseguir_5.mp3"
        ship "O seu tempo já se esgotou. Você teve toda uma vida para refletir. Em nenhum momento mostrou arrependimento e agora pergunta sobre suas opções?" with dissolve

        voice "prosseguir/ship_label_prosseguir_6.mp3"
        ship "Vamos logo! Estamos apenas adiando o irrevogável!" with dissolve

        voice "prosseguir/ship_label_prosseguir_7.mp3"
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
    scene corredor with fade_out and fade_in #essa parte esta correta?



    ed "Determinado a descobrir a origem do som, você se levanta com dificuldade, ignorando a dor latejante nas suas mãos." with dissolve
    
    ed "O som do vazamento torna-se mais alto e mais insistente, guiando-o para um corredor estreito que se estende a sua frente. A inclinação causada pelas ondas do mar dificulta ainda mais o caminhar." with dissolve

    ship "Um cheiro de madeira molhada e sal preenche o ar. O corredor, com suas portas distribuídas pelos dois lados, se apresenta iluminado apenas por uma luz que atravessa algumas janelas espalhadas ao longo das paredes." with dissolve

    ship "No canto do corredor, você percebe uma poça de água crescente, acumulando-se devido a uma rachadura visível em uma das janelas." with dissolve

    ship "O som que te despertou vem precisamente dessa rachadura, onde a água do mar está se infiltrando lentamente, ameaçando encher o corredor por completo." with dissolve

    ed "No canto oposto ao vazamento, algo chama sua atenção. Uma pequena quantidade de resina, provavelmente usada para reparos, está convenientemente armazenada em um recipiente." with dissolve 

    ed "A resina parece ser a sua melhor chance de vedar a rachadura e impedir que mais água entre." with dissolve

    ed "A situação exige uma ação rápida. Você sente a urgência de agir enquanto observa o corredor inclinado, a água subindo lentamente e o som do vazamento continuando incessante." with dissolve
    
    ed "Você sabe que precisa usar a resina para selar a rachadura antes que seja tarde demais." with dissolve

    jogador "Essa situação é bem estranha, porque me manipula a fazer algo que é óbvio que deve ser feito?" with dissolve


    ship "Apesar do sentimento de urgência, você se encontra indeciso. Certamente passa pela sua mente como o corredor se mantém inclinado de um lado, apesar dos movimentos constantes da maré sobre o barco." with dissolve
    
    ship "Você também questiona a origem desse vazamento, que deve ser recente, dado o volume de água presente. Entretanto, você não está sozinho?" with dissolve


    menu menu_descobrir_barulho:

        "{b}Olhar item\[Opção Exploratória\]{b}":
            jump zoom_in_item

        "{b}Olhar rachadura\[Opção Exploratória\]{b}":
            jump zoom_in_rachadura

        "{b}Ir em direção à porta?{b}":
            if porta_trancada:
                jump aproximar_porta
            else:
                jump aproximar_porta_item_desperdicado

        "{b}Desistir de consertar vazamento.{b}":
            jump desistir_conserto

    jump zoom_in_rachadura


label zoom_in_rachadura:

    if janela_consertada == False:
        scene rachadura with fade_in
        jogador "Por que a rachadura tem esse formato? O que aconteceu aqui?" with dissolve

        ship "Já lhe contamos que a rachadura tem um formato de punho. Me parece um tanto óbvio o que se passou aqui. Mas, vejo que está um pouco confuso. Nesse caso, acho melhor o Ed relembrar a história." with dissolve

        ed "Não podemos afirmar nada, na verdade. É uma rachadura com um formato bastante irregular. Não há muito o que se discutir." with dissolve

        ship "O quê? Está querendo enganar quem? Deixe que eu mesmo conto: em mais um de seus momentos de loucura, você desceu as escadas, foi até o fim do corredor e quebrou essa janela com as próprias mãos. A rachadura, que agora sela o destino desse barco, tem as suas impressões." with dissolve

        ship "Como bem conheço, você não se lembra de nada. Parece que todos os seus erros e traumas são apagados da sua mente. Que coisa fantástica, não?" with dissolve

        ship "Não há o que se lamentar. Sempre foram suas escolhas, tomadas em momentos conscientes ou não, conduzindo seu futuro." with dissolve
    
        if item_pego == True:
            menu consertar_rachadura_1:
                "{b}Consertar rachadura{b}" if janela_consertada == False:
                    $ janela_consertada = True
                    scene rachadura_consertada with fade_in
                    jump rota_esperanca
                "{b}Sair{b}":
                    scene corredor with fade_out and fade_in
                    jump menu_descobrir_barulho

        scene corredor with fade_out and fade_in

        jump menu_descobrir_barulho
    else:
        scene rachadura_consertada with fade_in
        if item_pego == True:
            menu consertar_rachadura:
                "{b}Consertar rachadura{b}" if janela_consertada == False:
                    $ janela_consertada = True
                    scene rachadura_consertada with fade_in
                    jump corredor
                "{b}Sair{b}":
                    scene corredor with fade_out and fade_in
                    jump menu_descobrir_barulho
                



label desistir_conserto:

    ed "Como pode desistir? Não vai ao menos tentar? Você pode consertar o vazamento. Tem uma resina bem ali" with dissolve

    jogador "Não vale a pena. Vocês já me falaram que estamos adiando o inevitável. Por que lutar?" with dissolve

    ship "Um pouco de sensatez, finalmente." with dissolve

    ed "Essa decisão é trágica. Mas não se engane, cada escolha tem seu preço. O perdão não é garantido." with dissolve

    ship "Ele já tomou sua decisão! Seus discursos são inúteis, apenas lamentações indistinguíveis. Deixe-o agir com um propósito maior do que si mesmo. Somente assim, depois de tantos anos, ele poderá ter a paz que tanto buscou." with dissolve

    ship "As névoas tomam conta do seu destino, nada mais parece manter a forma. O ar é denso, como se cada respiração fosse um mergulho em águas turvas. Você tateia o espaço ao seu redor, mas os contornos se desvanecem, com tudo escapando entre seus dedos." with dissolve

    scene corredor at blur_image with dissolve

    menu menu_desistir_conserto:
        "{b}O que está acontecendo? \[Opção Exploratória\]{b}":
            jump op_exp5

        "{b}Eu não posso deixar esse vazamento continuar.{b}":
            jump voltar_corredor

        "{b}Desistir.{b}":
            jump rota_tristeza_desistencia

    label voltar_corredor:
        jogador "Preciso vedar logo essa rachadura." with dissolve

        jump descobrir_barulho


    label op_exp5:

        play audio "<from 38.0 to 42.0>zumbido_orelha.mp3"

        # play audio "<from 38.0 to 42.0>zumbido_orelha.mp3"

        jogador "Por que está tudo tão distorcido? Não estou entendendo nada… são alucinações?" with dissolve
        
        ship "O que você vê não são meras alucinações, mas o seu próprio passado, distorcido pelos entorpecentes que outrora foram seu refúgio. Cada contorno borrado, cada sensação incompreendida, ecoando em sua mente são vestígios de uma vida marcada pela dependência." with dissolve

        jump menu_desistir_conserto


# label desistir_conserto:

#     jump Quarto_proibido_jogador_chega_proximo_da_porta_e_narradores_tentam_impedir_isso_de_alguma_forma

###########################
# Wilker
label aproximar_porta_item_desperdicado:
    scene porta_midwarp with fade_in

    jogador "Olhando em volta, noto uma porta que os narradores não mencionaram. Ela está meio escondida na penumbra, diferente das outras. Algo sobre ela parece... importante. Dou um passo em  sua direção." with dissolve

    ed "Espere! Há outras prioridades agora. A gente precisa sair daqui antes que o barco se encha de água. Concentre-se no  vazamento!" with dissolve

    jogador "Ignorando a advertência, aproximo-me mais da porta. Por que vocês não mencionaram essa porta antes? Parece que estão tentando me esconder algo." with dissolve

    ed "Essa porta não é relevante para o que está acontecendo agora. Seu foco deve ser resolver o problema do vazamento. Você não quer que o barco afunde, certo?" with dissolve

    jogador "Se não é relevante, por que tanta insistência em me afastar dela? Algo não está certo. Vou abrir essa  porta." with dissolve

    ed "Não! Você está cometendo um erro! O tempo está contra você, e a água continua a entrar. Se você insistir, pode ser tarde demais para salvar o barco." with dissolve

    ed "Faça o que é necessário para se salvar. Esqueça essa  porta." with dissolve

    ed "Você não entende o que está em jogo! Abrir essa porta pode trazer consequências que você não está preparado para enfrentar!" with dissolve

    ship "Ou talvez devesse...?" with dissolve

    jogador "Quê?!" with dissolve

    ed "Quê?! Não, com certeza não, essa é uma péssima idéia, por que o Harold continua aqui na verdade, não é mesmo? Você deveria desaparecer e deixar a mente dele em paz, acho que seria a melhor coisa para todos  nós." with dissolve

    ship "Na verdade, do outro lado dessa porta se esconde  toda..." with dissolve

    ed "QUIETO! AGORA! Não tem nada atrás dessa porta, não escute ele! Você conhece a dor, você lembra dela, por que fazer algo tão estúpido? HÃ?!" with dissolve

    ship "Ok, de fato, você está certo. Talvez seja uma ideia ruim." with dissolve

    jogador "Você iria dizer o que sobre a porta? O que ela esconde? Eu quero  saber." with dissolve

    ship "Hmmm... Que situação lastimosa, não é mesmo?" with dissolve

    jogador "Quê?" with dissolve

    ship "Hmmm... Que situação lastimosa, não é" with dissolve

    ship "Hmmm... Que situação lastimosa, não é" with dissolve


    ed "Nada, não tem nada aí. A porta com certeza está emperrada. Não vale a pena o esforço de tentar entrar aí, acredite. Vamos para outro lugar…" with dissolve
    
    jump menu_aproximar_porta

    # menu menu_aproximar_porta:
    #     # [Opção exploratória 1] Ideia ⇒ tem um corpo morto dentro do quarto, então provavelmente tem um cheiro pútrido saindo e sons de moscas
    #     "{b}Colocar o ouvido na porta \[Opção Exploratória\]{b}":
    #         jump op_exp_ouvir_porta
    #     # [Opção voltar corredor]: 
    #     "{b}Não entrar.{b}":
    #         jump corredor
    #     "{b}Entrar no quarto{b}":
    #         jump Entrar_quarto_proibido


#Neste momento o jogador está no corredor, ele vê a porta e decide ir em direção a ela.
label aproximar_porta:

    scene porta_midwarp with fade_in

    jogador "Olhando em volta, noto uma porta que os narradores não mencionaram. Ela está meio escondida na penumbra, diferente das outras. Algo sobre ela parece... importante. Dou um passo em direção a ela." with dissolve

    ed "Espere! Há outras prioridades agora. A rachadura precisa ser vedada antes que o barco se encha de água. Concentre-se no  vazamento!" with dissolve

    jogador "Ignorando a advertência, aproximo-me mais da porta. - Por que vocês não mencionaram essa porta antes? Parece que estão tentando me esconder algo." with dissolve

    ed "Essa porta não é relevante para o que está acontecendo agora. Seu foco deve ser resolver o problema do vazamento. Você não quer que o barco afunde,  certo?" with dissolve

    jogador "Se não é relevante, por que tanta insistência em me afastar dela? Algo não está certo. Vou abrir essa  porta." with dissolve

    ed "Não! Você está cometendo um erro! O tempo está contra você, e a água continua a entrar. Se você insistir, pode ser tarde demais para salvar o  barco." with dissolve

    ed "A resina está ali, pronta para uso. Faça o que é necessário para se salvar. Esqueça essa  porta." with dissolve

    ed "Num último esforço - Você não entende o que está em jogo! Abrir essa porta pode trazer consequências que você não está preparado para  enfrentar!" with dissolve

    ship "Ou talvez  devesse...?" with dissolve

    jogador "Quê?!" with dissolve

    ed "Quê?! Não, com certeza não, essa é uma péssima idéia, por que o Harold continua aqui na verdade, não é mesmo? Você deveria desaparecer e deixar a mente dele em paz, acho que seria a melhor coisa para todos  nós." with dissolve

    ship "Na verdade, do outro lado dessa porta se esconde  toda..." with dissolve

    ed "Quieto! Agora! Não tem nada atrás dessa porta, não escute ele! Você lembra dessa angústia! Por que fazer algo tão estúpido agora? Hã ?!" with dissolve 

    ship "Ok, de fato, você está certo. Talvez seja uma ideia ruim." with dissolve

    jogador "Você iria dizer o que sobre a porta? O que ela esconde? Eu quero  saber." with dissolve

    ed "Nada, não tem nada aí. A porta com certeza está emperrada. Não vale a pena o esforço de tentar entrar aí, acredite, vamos para outro  lugar…" with dissolve
    
    menu menu_aproximar_porta:
        # [Opção exploratória 1] Ideia ⇒ tem um corpo morto dentro do quarto, então provavelmente tem um cheiro pútrido saindo e sons de moscas
        "{b}Colocar o ouvido na porta \[Opção Exploratória\]{b}":
            jump op_exp_ouvir_porta
        # [Opção voltar corredor]: 
        "{b}Não entrar.{b}":
            jump corredor
        "{b}Entrar no quarto{b}":
            jump Entrar_quarto_proibido
    

label op_exp_ouvir_porta:
    jogador "Espera, que barulho é esse? Está vindo de dentro do quarto..." with dissolve

    ship "Hmm, são..." with dissolve

    ed "Bom, tal ceticismo e audição são louváveis. Contudo, creio que há coisas mais importantes para fazer no barco..." with dissolve

    jogador "Estranho... está fazendo um... bzzz..." with dissolve

    jump menu_aproximar_porta

#não acontece nada os narradores ficam aliviados
label voltar_corredor_b:
    jogador "Certo. Por agora, não vou entrar então... "

    ed "Excelente decisão, de fato a correta."

    ship "Talvez... você.... Nada, esquece. Talvez seja uma boa decisão."

    jump corredor

label corredor:
    scene corredor with fade_out and fade_in
    jump menu_descobrir_barulho
    
label Entrar_quarto_proibido:
    jogador "Consequências piores do que deixar o barco afundar? Vamos descobrir." with dissolve
    if porta_trancada == False:
        ship "Determinado, você nos ignora e estende a mão para a maçaneta da porta. Com a mão nela, você lentamente abre a porta, preparado-se para o que vier." with dissolve

        ed "Não, de novo isso! Outra decisão terrível, Caronte?!" with dissolve

        ship "Quer saber, o Caronte está certo. Ela esconde a verdade. Ela esconde o fato de você ser uma completa aberração, Caronte!" with dissolve

        ship "Lentamente, a porta se abre, rangendo enquanto cede ao impulso de sua mão até se abrir completamente." with dissolve

        # (mostra uma tela preta ou alguma coisa que crie um suspense, talvez até a imagem da porta semi aberta tampando a visão de dentro)
        scene black

        #fazer a frase aparecer mais devagar
        jogador "{cps=2}Qu-{/cps} {cps=13}QuE POrrA É EsSa?!!{/cps}"

        play sound "moscas_quarto.mp3" volume 1.5
    # dead-zone-166005
        play music "dead-zone-166005.mp3" volume 0.4
    # the-hourglass-24435


        #(mostra a cena do quarto cheio de sangue)
        scene quarto_probido_entrada with fade_in

        ship "Veja, Caronte, contemple a sua desgraça! Veja esse sangue, as paredes, a cama, o chão, cada centímetro desse inferno coberto com sangue." with dissolve

        #Voz tremendo, quase chorando
        ed "Não! Não! Eu não quero lembrar. Por favor, feche essa porta, ainda dá tempo!" with dissolve

        ship "Não fecha! Olha o que você fez! Lembra do que fez? Esse maldito cheiro de carne podre ainda me enoja. Esse cheiro de ferro, do sangue, me enoja. Você me enoja." with dissolve

        jogador "Que merda é essa! Que porra aconteceu aqui?!" with dissolve

        ed "Não! Não! Por favor, não! Me tira daqui!" with dissolve

        ship "Sim! Sim! Eu tenho que saber, a gente quer saber, a gente quer lembrar, não é? Então, olhe no canto do quarto, o que a gente vê?!" with dissolve

        scene corpo_mulher_morta

        jogador "Quem é aquela pessoa? Que porra tá acontecendo aqui? Eu não vou mais ficar aqui!" with dissolve

        ship "Consternado, você nada pode fazer perante essa situação. Mesmo desejando, o reconhecimento do que fez lhe mantém paralisado. Você olha meticulosamente para o corpo e percebe quem você matou." with dissolve

        jogador "Quê? Por que...? Por que... parece comigo? Eu... matei uma pessoa? O que eu fiz?" with dissolve

        ship "Não! Não! Você ainda não lembra? Daria para reconhecer melhor se desse para ver o rosto, mas você ficou tão nervoso, tão irritado. Você não se contentou em bater uma, duas, nem dez vezes, você queria mais, queria que pagasse pelo que fez." with dissolve

        jogador "Eu fiz o quê?! Do que você está falando? Eu não quero ficar mais aqui." with dissolve

        ed "Você não suporta mais permanecer nesse quarto. Afetado e confuso pelas lembranças, você recua subitamente, saindo do quarto e voltando ao corredor." with dissolve

        menu menu_escolhas_entrar_quarto_proibido:
            "{b}Sair desse maldito lugar!{b}":
                jump rota_raiva

    else: #porta está trancada
        auxiliar "tec tec tec"

        jogador "Quê? Está trancada?"

        ed "Ufff...."

        ship "Hmm, claro... Está trancada...."

        jogador "Espera, isso não é conveniente demais? Isso é algum truque ou coisa assim?"

        ship "Olha, infe-"

        ship "Não, não é um truque nosso..."

        ed "Truque nosso? A gente não fez nenhum truque em nenhum momento..."

        jogador "Hmm... Certo..."

        $ entrar_quarto = True

        jump corredor

# label voltar_corredor_c:
#     ed "Entra Rota da Raiva"
#     jump rota_raiva

#Diálogo exploratório:
label zoom_in_item:
    ed "Veja, é isso que usaremos para consertar a rachadura no vidro. Pegue, passe a pasta na rachadura e problema resolvido. Poderemos pensar em como sair daqui finalmente." with dissolve

    ship "Não teria tanta certeza. Como uma pasta iria segurar um vazamento? Esta coisa provavelmente é inútil. Seria melhor continuar procurando algo que faça sentido. Não temos tempo para desperdiçar com idiotices." with dissolve

    jogador "É isso? Não dá para ler a embalagem, está tudo apagado." with dissolve

    menu menu_escolhas_zoom_in_item:
        "{b}Quanto tempo falta?\[Opção Exploratória\]{b}":
            jump op_exp_quanto_tempo_falta
        # [Opção pegar item correto]:
        "{b}Pegar item{b}" if item_desperdicado == False and item_pego == False:
            jump pegar_item_correto 
        "{b}Desperdiçar item{b}" if item_desperdicado == False:
            jump desperdicar_item 
        "{b}Sair{b}":
            jump corredor 
        
label op_exp_quanto_tempo_falta:
    jogador "Espera, tenho tempo de procurar outra coisa ou não?" with dissolve

    ed "Não! Essa pasta vai funcionar. Ela é feita para isso." with dissolve

    ship "Escute Caronte, a resina vai dissolver quando entrar em contato com a água. Jogue isso fora, não tem utilidade." with dissolve

    ed "Não, não vai. Se a embalagem não estivesse tão danificada, daria para ler que ela é feita para isso. Caronte, me escute, eu lembro de quando compramos isso, confie em mim." with dissolve

    jump menu_escolhas_zoom_in_item
    
label pegar_item_correto:
    ed "Excelente escolha! Vamos usar isso para fechar essa rachadura e descobrir como sair desse lugar." with dissolve

    ship "Bem, se quiser tentar, não sou contra. Mas acho que isso vai ser um desperdício precioso do nosso tempo." with dissolve

    $ item_pego = True

    jump menu_escolhas_zoom_in_item

label desperdicar_item:
    jogador "Eu não ligo. Vou ver o quão longe consigo arremessar essa resina no mar." with dissolve

    ed "Quê?!" with dissolve

    ship "Quê?!" with dissolve

    jogador "Estou indo para o convés, vou ter uma visão melhor de lá." with dissolve

    ed "Não! Caronte? O que...?" with dissolve

    ship "Desafio você a arremesar essa resina tão longe, a ponto de ela sumir antes de cair no mar." with dissolve

    ed "Não Caronte, não faz isso. Essa é a única solução, não tem como arrumar a rachadura sem isso. Vamos todos morrer!" with dissolve

    ship "Não acredito que seja a única. Nem olhamos o barco todo e temos bastante tempo ainda. A água está entrando bem devagar." with dissolve

    scene conves

    jogador "Aqui estamos." with dissolve

    ed "Caronte, não!" with dissolve

    #colocar uma cena que mostra o Caronte olhando para o mar.
    scene barco_mar

    ship "Vemos claramente que não conseguimos ver nada daqui de cima. O céu, a água, tudo está muito escuro. O cheiro salgado do mar, as ondas batendo... Excelente clima para um arremesso." with dissolve

    jogador "Você me desafiou, então aqui vai." with dissolve

    ship "Seu braço direito está um pouco dolorido, principalmente a mão, impedindo de levá-lo para muito atrás das costas. Você gira o tronco, sentindo uma leve dor na região das costelas." with dissolve

    ship "Ao colocar o pé esquerdo para frente, garantindo um melhor arremesso, você percebe que seu corpo está muito pesado. De repente, você está realmente cansado e notou isso melhor agora." with dissolve

    ship "Ao girar o tronco e carregar o braço para frente com o restante de força que ainda tem, você escuta um barulho estridente: " with dissolve

    unk 'VUFF' with dissolve

    ship "A resina quebra o vento tão rápido que é difícil não escutar o barulho. Em menos de dois segundos o composto branco se perde na escuridão para muito, muito longe." with dissolve

    ship "Você fica surpreso com o próprio desempenho físico." with dissolve

    #colocar efeito sonoro de um objeto voando e rasgando o ar
    #play sound effect

    jogador "WOW! Não esperava por isso. Eu sou bem forte." with dissolve

    ship "Oh, Caronte, você não faz ideia." with dissolve

    # jogador "Hm? Não acho que eu seja capaz de fazer algo assim." with dissolve

    # ship "Eu meio que estava exagerando, não se preocupe." with dissolve

    # obs. "talvez colocar mais indignação nessa fala do Ed."
    ed "É... lá se vai nossa solução... Ok, talvez tenha uma alternativa em algum lugar." with dissolve

    ed "Sentindo a leva brisa do mar, você fica determinado a procurar uma outra solução. Então, volta em direção ao corredor." with dissolve

    #linhas auxiliares para resolver aquele problema do roteiro

    play sound "<from 0.2 to 0.8>destranca_porta.mp3"
    auxiliar "Trec..." with dissolve

    jogador "Hm? Eu ouvi algo? Tipo uma trava...?" with dissolve

    $ item_desperdicado = True
    $ porta_trancada = False

    #volta para o corredor sem dizerem nada.

    if (item_desperdicado and entrar_quarto == False):
        jump rota_tristeza_desperdicio

    else:
        jump corredor


##################### INICIO ROTA ESPERANÇA FELIPE ############################################################
label rota_esperanca:

    scene rachadura

    ship "Você se ajoelha próximo à rachadura, resina em mãos. Seus dedos tremem enquanto tenta aplicá-la. A água que continua a entrar, fria, zomba dos seus esforços. Tanta pressa, tanto zelo... Será que, no fundo, você acredita que isso fará diferença?" with dissolve

    jogador" Claro que faz! Se eu não vedar isso, o barco vai afundar!" with dissolve

    # (Efeito sonoro)

    ship "Ouviu isso? O som do inevitável. Mesmo que vede essa rachadura, quem garante que o barco inteiro não está prestes a ceder"
    
    ship "Ao concluir o reparo e perceber que o vazamento persiste, você percebe a água entrando por outras fissuras menores ao redor."

    jogador" Não pode ser... Acabei de consertar isso!"

    ed "Você tapou um buraco em um navio que infelizmente já está condenado. Foi um esforço admirável, mas é como usar um curativo em uma ferida fatal."

    ship "Veja como a água continua entrando. É engraçado, não é? O barco sempre esteve contra você."

    jogador "Vocês me guiaram até aqui, prometeram que tudo isso acabaria se eu fechasse essa rachadura. Mentirosos!"

    ship "A água começa a alcançar seus pés. O som do vazamento torna-se um rugido que preenche todo o ambiente. Você está parado diante da rachadura na parede. O som da água que antes parecia um sussurro distante agora cresce, reverberando nas paredes como um rugido vivo." 
    
    ship "A rachadura então pulsa como se tivesse vida própria, e através dela você vê algo brilhando – um reflexo? Uma memória?"

    ed "Ao seu redor, o cenário parece se distorcer; sombras oscilam, e você sente como se estivesse sendo observado. Nós, muito além de narrar pensamentos, surgimos refletidos na rachadura. Nossas vozes agora emanam diretamente de nossas figuras, que parecem um reflexo de você mesmo."

    ship "Você sabe que este barco não afunda apenas pela rachadura, não sabe? Ele sempre afundará, seja pela água ou pelo peso que carrega."

    ed "Sempre tento ajudar em todas as escolhas, mas ainda sou tido como mentiroso, não? De qualquer forma parece que não há muita solução aqui, não é mesmo? Afinal, você fez tudo que sugeri, mas nada mudou." 

    ed "Talvez seja mais produtivo parar de pensar numa solução e só aceitar as coisas do jeito que elas são. Afinal, nesse exato momento a água começa a alcançar seus joelhos."

    ship "Interessante como ele encara essa rachadura como se fosse a origem de todos os problemas. E se, no fundo, ela for apenas mais um reflexo do desastre que ele carrega?"

    ed "Harold, deixe-o decidir. A rachadura é um caminho, sim. Toque-a. Ela pode te mostrar algo que realmente importa."

    jogador "Você quer que eu toque nela? Depois de tudo isso? Suas palavras nunca ajudaram! Não confio em você."

    ed "Ah, desconfiança... justo. Mas diga-me, o que você realmente tem a perder? A água já tomou o navio, e, francamente, correr não parece uma saída muito convincente."

    ship "Você pode tentar tocar a rachadura, sim, mas onde isso te levará? Você sempre faz isso, não faz? Toca, tenta corrigir, mas nada muda. Sempre o mesmo ciclo... Uma tentativa desesperada de se enganar."

    ship "A água, os sons, a rachadura... tudo apenas parte de uma grande farsa. Por favor, ignore esse charlatão. Ele adora vender respostas fáceis, mas não há atalhos para o inevitável. Corra para seu quarto. Lá, pelo menos, você pode encontrar algum controle – uma pequena ilusão de escolha."

#    menu menu_escolhas_zoom_in_item:
#         "{b}Quanto tempo falta?\[Opção Exploratória\]{b}":
#             jump op_exp_quanto_tempo_falta
#         # [Opção pegar item correto]:
#         "{b}Pegar item{b}" if item_desperdicado == False and item_pego == False:
#             jump pegar_item_correto 
#         "{b}Desperdiçar item{b}" if item_desperdicado == False:
#             jump desperdicar_item 
#         "{b}Sair{b}":
#             jump corredor 

    # ---------------------------------------------------------------
    menu escolha_1_esperanca:
        "{b}Tocar a Rachadura{b}":
            jump tocar_rachadura

        "{b}Correr para o Quarto{b}":
            jump correr_para_quarto


label acabou_tempo_esperanca:
    scene boneco_distorcido

    pause 2.0

    jump start

label tocar_rachadura:
    ed "Sabia que você faria isso. Às vezes, a tentação de encarar a verdade é maior que a dor de viver na mentira. O ambiente a sua volta pulsa, e a rachadura parece chamá-lo, como uma promessa de algo maior ou talvez perturbador. Você estende a mão, hesitante, e o reflexo de Ed te empurra para frente."

    ship "Mas será que a verdade vai te salvar? Olhe para você. Você já está perdido, marinheiro. O que você acha que encontrará tocando isso?"

    ship "De qualquer forma, seu dedo toca a rachadura, e ela imediatamente se expande, engolindo sua mão. O som da água se torna um rugido ensurdecedor, e você é puxado para dentro. Em um instante, tudo se distorce ao seu redor."

    scene quarto_probido_entrada

    ed "E aqui estamos. Você é lançado de volta ao seu quarto. Nada parece ter mudado, mas, assim que entra, algo estranho acontece. As paredes estão molhadas, os móveis são os mesmos, mas há uma sensação de repetição no ar."

    ed "Você sente como se já tivesse estado ali antes. Como se cada movimento fosse uma repetição de algo que já aconteceu, mesmo que tenha escolhido ignorar seu quarto completamente."

    ship "Ah, a velha ilusão de que algo pode ser diferente. O que você achou que encontraria tocando aquela rachadura? A verdade? Ela sempre esteve aqui. Apenas você não quis enxergar."

    # Continuação a partir da escolha 1:

    ed "Você está de volta ao quarto. O espaço é o mesmo de antes, mas algo mudou. Os detalhes chamam sua atenção, como se o próprio quarto tivesse algo a dizer."

    ed "A luz fraca da janela circular projeta um brilho sobre os móveis destruídos. Uma cadeira caída e uma cama ensanguentada dominam o centro da sala. As paredes molhadas parecem absorver o som, tornando o ambiente pesado e claustrofóbico."

    ed "Na parede esquerda, um retrato emoldurado o encara, mesmo que o rosto pintado esteja indistinguível. Na parede oposta, uma segunda moldura apresenta uma família. A imagem está manchada, mas parece transmitir algo... como um apelo mudo."

    ship "Isso não é um quarto. É uma cova, construída lentamente pela sua própria mente. Mas vá em frente, inspecione cada canto. Talvez você encontre o que procura. Ou, mais provavelmente, não encontrará nada." 
    
    ship "Você percebe que, embora o quarto pareça se repetir, há algo diferente agora: detalhes antes ignorados clamam pela sua atenção."

    jogador "Sinto uma estranha sensação tomando conta de mim. Pela primeira vez estou livre do determinismo dos narradores e os cômodos do navio passam por minha mente como opções em um cardápio. As escolhas se alinham diante de mim:"

    # ------------------------------------------------------------------------------------------
    menu minigame_esperanca:
        # Quarto -  #

        "{b}Inspecionar os móveis destruídos{b}":
            $ contador_esperanca = contador_esperanca + 1
            if contador_esperanca == max_tentativas:
                jump acabou_tempo_esperanca

            unk "Você se ajoelha próximo aos móveis destruídos. Um pedaço de madeira parece ter sido arrancado com violência, deixando farpas que apontam como lanças. Há algo estranho na forma como o sangue seco mancha o material, quase como se formasse palavras... mas, ao tocar, tudo desaparece como poeira."

            unk "Não é o que você procura."

            jump minigame_esperanca
        "{b}Inspecionar os retratos a direita{b}":
            $ contador_esperanca = contador_esperanca + 1
            if contador_esperanca == max_tentativas:
                jump acabou_tempo_esperanca

            unk "O retrato da família o encara com uma intensidade silenciosa. Os rostos, embora manchados e indistintos, parecem mudar ligeiramente de expressão toda vez que você desvia o olhar. Há algo perturbadoramente familiar neles. Você sente uma conexão, mas não consegue definir o motivo."

            unk "Não é o que você procura."

            jump minigame_esperanca
        "{b}Inspecionar o sangue que mancha o chão{b}":
            $ contador_esperanca = contador_esperanca + 1
            if contador_esperanca == max_tentativas:
                jump acabou_tempo_esperanca

            unk "Você se aproxima da mancha no chão. O sangue não está seco como deveria; ele brilha, viscoso, refletindo uma luz que não existe no ambiente. Quanto mais você olha, mais parece que está se movendo, como se tentasse formar algo vivo. Quando tenta tocar, a mancha simplesmente se dissolve em nada."
            
            unk "Não é o que você procura."
        
            jump minigame_esperanca
        
        "{b}Inspecionar o retrato a esquerda{b}": #
            $ contador_esperanca = contador_esperanca + 1
            if contador_esperanca == max_tentativas:
                jump acabou_tempo_esperanca

            if olhou_retrato_mulher == False:
                $ olhou_retrato_mulher = True
                unk "O retrato o observa com um olhar vazio, mas há algo familiar nele. Ao chegar mais perto, você percebe que o rosto no quadro... é o seu. Mas há algo errado: os olhos estão completamente pretos, e o sorriso que ele ostenta é de puro escárnio. Quando tenta tocá-lo, o quadro parece se desfazer em uma névoa."
                
                unk "Não é o que você procura."
                jump minigame_esperanca
            
            if olhou_retrato_mulher == True:
                jump olhar_retrato_mulher_2_vez
                

        "{b}Voltar para o corredor{b}": #
            jump corredor_esperanca


label corredor_esperanca:
    scene corredor

    menu escolhas_corredor_esperanca:
        "{b}Inspecionar a janela quebrada{b}":
            $ contador_esperanca = contador_esperanca + 1
            if contador_esperanca == max_tentativas:
                jump acabou_tempo_esperanca

            unk "Você olha pela janela, mas a escuridão do mar não revela nada além de um vazio avassalador. A água que entra tem um cheiro de ferrugem e podridão. Tentar olhar mais fundo causa uma leve vertigem, e você decide desviar o olhar."
            
            unk "Não é o que você procura."
            jump corredor_esperanca

        "{b}Inspecionar as portas laterais{b}":
            $ contador_esperanca = contador_esperanca + 1
            if contador_esperanca == max_tentativas:
                jump acabou_tempo_esperanca

            unk "Cada porta do corredor parece idêntica, mas, ao tocá-las, você sente resistência. Algumas estão trancadas, outras parecem apenas ilusões; seus dedos passam direto através delas. O som de algo se arrastando pode ser ouvido, mas nunca fica claro de onde vem."
            
            unk "Não é o que você procura."
            jump corredor_esperanca

        "{b}Inspecionar a porta central{b}":
            $ contador_esperanca = contador_esperanca + 1
            if contador_esperanca == max_tentativas:
                jump acabou_tempo_esperanca

            unk "As fechaduras enferrujadas emitem um leve calor, um contraste com o frio do corredor. Cada uma parece pulsar, como se estivesse viva. Você tenta forçar a porta, mas ela não cede. Um som estranho escapa das fechaduras, como um sussurro."
            
            unk "Não é o que você procura."
            jump corredor_esperanca

        "{b}Voltar para o quarto{b}":
            scene quarto_probido_entrada
            jump minigame_esperanca

        "{b}Voltar para o Convés{b}":
            jump conves_esperanca

label conves_esperanca:
    scene conves

    menu escolhas_conves_esperanca:
        "{b}Inspecionar as marcas no chão{b}":
            $ contador_esperanca = contador_esperanca + 1
            if contador_esperanca == max_tentativas:
                jump acabou_tempo_esperanca

            unk "As marcas parecem aleatórias à primeira vista, mas, ao observá-las mais de perto, você percebe padrões. Palavras como 'fuga', 'ciclo' e 'mentira' aparecem, mas estão incompletas. Quando você tenta seguir o padrão, elas desaparecem."

            unk "Não é o que você procura."

            jump escolhas_conves_esperanca

        "{b}Inspecionar os mastros{b}":
            $ contador_esperanca = contador_esperanca + 1
            if contador_esperanca == max_tentativas:
                jump acabou_tempo_esperanca

            unk "Os mastros do convés parecem altos demais, como se tocassem algo além do céu. Há cordas penduradas, balançando lentamente, mesmo sem vento. Uma sensação de desconforto cresce conforme você olha para eles, mas não há nada que você possa alcançar."
            
            unk "Não é o que você procura."

            jump escolhas_conves_esperanca

        "{b}Inspecionar o horizonte{b}":
            $ contador_esperanca = contador_esperanca + 1
            if contador_esperanca == max_tentativas:
                jump acabou_tempo_esperanca

            unk "Você olha para o horizonte e percebe algo estranho: ele não se move. Não importa o quanto o navio balance, o horizonte permanece fixo, como uma pintura malfeita. Sua mente começa a vagar e uma vertigem toma conta de você."
            
            unk "Não é o que você procura."

            jump escolhas_conves_esperanca

        "{b}Voltar para o corredor{b}":
            jump corredor_esperanca

        "{b}Voltar para a Cabine{b}":
            jump cabine_esperanca


label cabine_esperanca:
    scene cabine_com_figura
    
    menu escolhas_cabine_esperanca:
        "{b}Inspecionar a figura bizarra{b}":
            $ contador_esperanca = contador_esperanca + 1
            if contador_esperanca == max_tentativas:
                jump acabou_tempo_esperanca

            unk "Você se aproxima da figura. Seus traços são indistinguíveis, como se alguém tivesse tentado desenhá-la e apagado várias vezes. Ao se aproximar, ela se mantém imóvel."
            
            figura "Quem é você?"

            # em vermelho, leitura não imediata de preferencia )
            figura "Você sou eu&UUU&uuQ&**&QYO&######@@@@@!!!¨¨*"

            scene cabine_sem_figura with fade_in
            
            unk "O som reverbera pela sala antes da estátua desaparecer como poeira ao vento."

            unk "Não é o que você procura."

            jump escolhas_cabine_esperanca

        "{b}Inspecionar os mapas na mesa{b}":
            $ contador_esperanca = contador_esperanca + 1
            if contador_esperanca == max_tentativas:
                jump acabou_tempo_esperanca

            unk "Você olha para os mapas, mas eles não fazem sentido. Os traços parecem formar rotas impossíveis, que terminam em círculos ou espirais. Alguns pontos marcados com 'X' parecem se mover enquanto você observa."
            
            unk "Não é o que você procura."

            jump escolhas_cabine_esperanca

        "{b}Inspecionar o diário no chão{b}":
            $ contador_esperanca = contador_esperanca + 1
            if contador_esperanca == max_tentativas:
                jump acabou_tempo_esperanca

            unk "Um diário velho e rasgado está no chão. Quando você o abre, não há palavras; apenas páginas encharcadas que escorrem água entre os dedos. O som da água ecoa pela sala."
            
            unk "Não é o que você procura."
    
            jump escolhas_cabine_esperanca

        "{b}Voltar para o Convés{b}":
            jump conves_esperanca

    # ----------------------------------------------------------------------------------------- Obs: se contador bater cena de body horror e game over

label olhar_retrato_mulher_2_vez:
    # Inspecionando o Retrato da Mulher (Segunda Vez)

    jogador "Algo naquele retrato... Não consigo tirar da cabeça. Preciso vê-lo novamente."

    ed "Você se aproxima do retrato à esquerda mais uma vez. Desta vez, a sensação é diferente. A moldura parece pulsar suavemente e o olhar da mulher não é mais vazio. Há algo mais profundo ali, algo que te chama."

    ship "Ah, de volta ao mesmo lugar. Você achou que um olhar mais atento revelaria algo novo? Você é previsível. Sempre voltando às suas culpas. Você toca a moldura do retrato e imediatamente sente uma onda de calor percorrer sua mão. A superfície do quadro parece se dissolver e uma visão toma conta de sua mente."

    ed "Não há mais o que fazer. Tenha cuidado, porque a verdade nunca vem sem um preço. O que você vê agora é o que você sempre soube... e sempre temeu."

    ed "Você está parado no convés. Enquanto uma tempestade cai, diante de você se apresenta a mulher do retrato, seus olhos cheios de lágrimas e medo."

    ed "Ela grita algo, mas o som é abafado pelo vento. Você sente o peso do metal em sua mão – um objeto que só pode ser descrito como um instrumento de morte."

    ship "Você lembra agora, não é? Foi você que a trouxe aqui, você que segurou a arma e decidiu seu destino. Você vê a si mesmo empurrando a mulher para trás. Ela tropeça, seu corpo batendo contra o convés."

    ship "A tempestade consome tudo, mas você ouve o som claro de algo quebrando. Você grita – não por arrependimento, mas por raiva. O momento congela, e o cenário se desfaz como vidro estilhaçado."

    ship "De volta ao retrato, você percebe que ele agora está vazio. A mulher se foi, deixando apenas um pedaço de papel dobrado na moldura. Você o pega."

    ed "Ah, então você encontrou um fragmento da realidade. Um fragmento que confirma aquilo que você já sabia, mas fingiu esquecer. O sangue naquele convés, o silêncio neste navio... tudo isso é sua criação."

    ed "O papel tem apenas três palavras escritas: 'Eu perdoo você.' Mas, ao ler, o papel desintegra-se em pó, como se nunca tivesse existido."

    ed "Ah, ele começa a entender. Mas será que já percebeu quem realmente está conduzindo esse ciclo?"

    ed "E aí está você. As escolhas que você tanto procura... sempre foi uma ilusão. O que você não entende é que o navio já está afundando desde o começo. Tudo o que você fez, todas as tentativas, levaram você de volta ao mesmo ponto."

    ed "A rachadura, a mulher, o barco afundando... Não há saída, nunca houve. Você nunca quis saber quem quebrou a janela? Quem deixou a água entrar? Mas, ei, talvez isso não importe mais. Afinal, o barco afundará, com ou sem rachaduras."

    ship "Pobre Ed. Sempre tentando levar os outros ao 'entendimento'. Mas é engraçado... o ciclo não é escolha dele, nem sua. É escolha de algo maior. Talvez você descubra isso... na próxima vez."

    ship "Outra tentativa. Outro fracasso. Mas, como sempre, ele tentará de novo."

    ed "E, talvez, um dia, ele veja o reflexo completo."

    unk "O ciclo continua."
    
    jump start

    # ========================================================================================
label correr_para_quarto:
    ed "Você decide correr para o seu quarto, deixando a rachadura e a água para trás. Seus passos ecoam no corredor alagado do barco, o som da água se intensificando a cada pisada. Há algo de urgente em sua corrida, como se estivesse fugindo de algo maior que você mesmo, mas, ao mesmo tempo, você sente uma estranha calmaria, como se fosse a última coisa que pudesse fazer."

    ship "Você corre, mas a cada passo sente que o corredor está se esticando. Ele parece nunca terminar, cada porta e cada janela surgem mais distantes, como se o espaço estivesse sendo distorcido, afastando o objetivo cada vez mais. O som da água atrás de você ecoa mais alto, mas algo está estranho. Você não está indo a lugar algum. Olha o que acontece quando você tenta: o corredor se estica, se alonga, e a porta nunca chega."

    ed "Você olha para frente e vê duas opções. Seguir adiante para a porta, cada vez ficando mais imperceptível, e o reflexo do vidro quebrado, que reflete sua figura distorcida."
    
    menu escolha_esperanca_2:
        "{b}Voltar a escolha 1{b}":
            jump escolha_1_esperanca

        "{b}Continuar Correndo para o Quarto{b}":
            ed "Você decide seguir em frente. Cada passo agora parece ser uma tentativa desesperada de continuar, mas o corredor nunca acaba. Você sente o peso da água subindo pelas suas pernas, seu corpo ficando mais pesado, mas ainda assim não para de correr. O corredor nunca termina, e você nunca vai chegar aonde quer. Você está apenas adiando o inevitável."

            ship "Corra, corra até não poder mais. O corredor continua a se esticar, e você sente o peso da água aumentar enquanto corre. A cada passo, você afunda mais, e o som da água se mistura com sua respiração ofegante. Mas algo está acontecendo: a água começa a envolver seu corpo, sua respiração fica mais pesada, e você percebe que está sendo arrastado pela correnteza."

            jogador" ahgh...?"

            ship "Você tenta gritar, mas a água invade sua boca. A visão começa a turvar, e a sensação de afogamento se torna imersiva. O corredor se estende ainda mais enquanto você, incapaz de se mover, é finalmente consumido pela água. O som da água é tudo o que resta, e você percebe que nunca realmente escapou. Você morre afogado, e o ciclo, como sempre, reinicia. A água está à sua volta novamente, o navio sempre afundando, sempre repetindo. Mas algo em seu peito parece saber que nada disso vai mudar."

    jump start


#########################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------
# ROTA TRISTEZA #

label rota_tristeza_desistencia:

    #Caminho: Desistência de vedar vazamento

    ship "Agora, você deita no chão, com as costas viradas para o piso. Olhe para o teto do corredor e ouça o barulho da água tomando o barco."

    #Mudança de cenário para o protagonista ficar flutuando no  fundo do mar.
    ship "Eu sei o que se passa na sua mente. Sei de todas as falhas que tomam seus pensamentos nesse momento."

    ship "Minha sugestão é permanecer parado. É só aguardar."

    jump start

label rota_tristeza_desperdicio:

    scene barco_mar at blur_image with dissolve

    jogador "O que podemos fazer agora? Tem algum outro item pelo barco?"

    ed "Devo dizer que não há."

    jogador "Ok… bem, o que faremos agora?"

    ed "\Caronte, você não deveria ter feito isso, mas está tudo bem. Poderemos resolver isso. Acho que tem uma canoa em algum lugar por aqui. Podemos usar ela para fugir desse barco, apesar de ser arriscado."

    ship "Fugir para quê? Sabemos que isso não é a solução dos seus problemas, Caronte. Eu já te disse isso antes."

    ed "Não escute ele, Caronte. Confie em mim, você tem uma vida maravilhosa pela frente! Na verdade, eu vou fazer melhor, vou te mostrar."

    ed "Surge a imagem de uma linda moça na sua frente. Pele morena, cabelos escuros. O coração palpita forte."

    ed "Você vê sua família, vocês estão... em uma igreja. Seus pais, tios e tias estão ali, todos te olhando, sorrindo, te amando tanto que você não consegue imaginar. A moça bonita está ao seu lado, ela sorri timidamente."

    ed "Você está feliz! Você sorri imaginando esta cena junto de mim. Não é amável, Caronte? Não é um futuro perfeito? O que mais um homem poderia querer?"

    ship "Isso não existe! Uma vida feliz para você?"

    ship "Estamos condenados nesse barco por um motivo. E pode ter certeza que não é por uma vida maravilhosa que você levava."
    #(uma sombra preta toma a cena ou rabiscos pretos em toda parte)"

    ship "A verdade é: você está jogado em uma sarjeta, com vômito escorrendo pelas suas calças. É uma figura asquerosa que definha, como um vira-lata atropelado e esquecido para morrer. Esta é a verdade, isso é o que aconteceu com você."

    jogador "Que?! Que merda é essa? Por que diabos você está falando isso?"

    ed "Não, não escute ele, Caronte. Ele está apenas distorcendo o que aconteceu. Tentando te manipular!"

    ship "Eu? É ele quem está mentindo, ocultado a realidade para parecer algo belo. Você é um viciado, Caronte. Você tem problemas graves e não tem nada que possa te ajudar. É por isso que deve morrer."

    ship "Mais tarde, sua esposa, esta “morena bonita de cabelos escuros” te encontra e começa a chorar. Você fica profundamente perturbado! E eu não quero passar por isso de novo! Eu não vou passar por isso de novo!"

    ed "\Caronte, ele está mentindo. Deixa eu te mostrar outra..."

    ship "Não, eu ainda não terminei! Depois disso, ela tentou te levantar, te levar para casa e cuidar de você. Ela tentou enxergar em você uma pessoa digna, mas não conseguia. Ela não tinha força para te levantar e você mal se aguentava em pé."

    ship "Ela chorava não só por ver o amor dela nessa situação lastimável, mas também porque você quebrou a promessa que fizeram. Você prometeu, a gente prometeu que não iria fazer mais essa merda mas, no fim, a gente fez!" with dissolve

    ship "E fizemos de novo, e de novo... Nenhum ser humano em sã consciência aguentaria essa tortura, Caronte… Confie em mim, eu não estou mentindo!" with dissolve

    ed "Esquece isso! Pense neste outro caso, esta outra possibilidade." with dissolve

    jogador "O quê? Eu… eu realmente fiz isso? Por…" with dissolve

    ed "Esqueça isso, Caronte. Me escute, pense nos seus filhos!" with dissolve

    ed "Você está sentado em uma cadeira, segurando a mão da moça bonita. Na sua frente um menino e uma menina correm e brincam nas areias cristalinas da praia. O mar está no mais perfeito tom de azul, com o Sol aquecendo-o tão suavemente." with dissolve

    ed "A vida parece tão calma, com uma leve brisa passando pelas árvores e as fazendo ressoar. Mais distante, pássaros tomam o horizonte, colorindo o céu." with dissolve

    jogador "Sim, tudo isso parece tão bom! Por que minha vida não pode ser assim?" with dissolve

    ship "Porque você foi condenado por Deus a ser essa criatura repugnante!" with dissolve

    ship "Mentiras e mais mentiras! Isso nunca aconteceu, você tratava os seus filhos como se fossem lixo!" with dissolve

    jogador "Espera, eu tenho filhos?" with dissolve

    ship "Você NUNCA deu um pingo de amor para eles! Não ouse tentar se convencer de que, em algum momento da sua vida, você foi bom ou deu qualquer tipo de alegria para aquelas crianças!" with dissolve

    jogador "Crianças? Mas co…" with dissolve

    ship "Tudo que você sabia fazer com aquelas crianças era gritar e xingar. Toda vez que elas te pediam alguma coisa, toda vez que elas te pediam qualquer forma de carinho ou amor, você as assustava. Isso quando não batia nelas!" with dissolve

    jogador "Meu Deus! Eu não fiz isso! Eu não lembro de nada." with dissolve

    ship "Até quando elas estavam tendo problemas nas escolas com os outros meninos, você nunca, nunca ajudou! Seu miserável!" with dissolve

    ship "Então, não ouse acreditar nas mentiras que o Ed te conta." with dissolve

    ed "Caronte, não acredite no que ele diz! É tudo mentira, você não é assim, você tem chance de mudar, chance de ser uma pessoa melhor. Acredite em mim, por favor. Acredite em nós dois." with dissolve

    jogador "Não… Eu acho que… eu entendo agora…" with dissolve

    jogador "Esse peso no meu corpo, essa desolação em minha cabeça, como se… algo muito ruim estivesse guardado aqui dentro… na verdade… eu acho que tudo faz sentido na realidade… Eu sou de fato horrível, não sou?" with dissolve

    ed "Não, Caronte. Você não é, você…" with dissolve

    ship "Sim! você é!" with dissolve

    jogador "Entendo… Realmente sou um maldito que apenas inferniza e destrói a vida das pessoas ao meu redor…." with dissolve

    ship "Você está ficando ainda mais cansado, Caronte. Você sente algo sumindo do seu corpo… Sua esperança se esvaindo." with dissolve

    #Ed Newgate desaparecendo
    jogador "Ed, não resta muito para nós aqui."

    ed "Espere!"

    ship "Não interrompa! Sabemos que ele já se decidiu. Nós podemos sentir... "

    jogador "Eu sinto muito, Ed…"

    play sound "agua_splash.mp3"

    ship "O corpo dele já se encontra nas águas. E as preocupações que tanto nos assombraram foram esquecidas."



    jump start

#---------------------------------------------------------------------------------------------------------------------------------
# ROTA RAIVA #

label fugir_barco_raiva:
    # (Fugir de Barco):
    ed "Excelente, escolha, amigo!"

    ed "Você se levanta do chão e sai do quarto." 
    
    scene corredor

    # sound effect porta batendo
    play sound "door-slam-172171"

    ed "Abruptamente, a porta fecha atrás de você... Estranho, temos a impressão de que ela nunca mais vai abrir... nunquinha."

    ed "Você segue até as escadas que te levam até a proa e as sobe. O clima está gelado, tem uma certa neblina no mar escuro, a única coisa mais ou menos visível no meio dessa obscuridade toda. "

    ed "Ao explorar os arredores, você vê uma pequena canoa de resgate, pairando por cordas sobre o mar. Tem um remo dentro dela e você, felizmente, sente que, se subir ali, sua vida vai ficar melhor e melhor a cada dia. "

    ed "Ao dar o primeiro passo, surge a imagem de uma linda moça na sua frente. Pele morena, cabelos escuros. Nosso coração palpita forte."

    ed "No segundo passo, você vê sua família, vocês estão... em uma igreja. Seus pais, tios e tias estão ali, todos te olhando, sorrindo, te amando, tanto que você não consegue imaginar. A moça bonita está do seu lado, ela sorri timidamente"

    ed "No terceiro passo, você está sentado em uma cadeira, segurando a mão da moça bonita, na sua frente um menino e uma menina correm e brincam nas areais cristalinas da praia. O mar está no tom mais azul possível, o Sol o aquece tão amigavelmente. "

    ed "Você chega nessa canoa e entra nela."

    ed "Tudo é perfeito!"

    jump start



label encerrar_vida_raiva:
# (Encerrar a própria vida)

    ship "Esta é a melhor escolha, Caronte."

    ship "Você se levanta e sai do quarto. Sentindo-se aliviado, como se tivesse se livrado de um pesadelo horrível. Ao sair, você escuta um estrondo atrás de você. A porta se fecha para nunca mais abrir... nunca mais"

    ship "Você caminha pelo navio uma última vez... mas não dura muito tempo, você quer se livrar logo destas emoções ruins e ser, portanto, verdadeiramente livre. Logo, corre para o início de tudo, para o local em que acordou."

    ship "Lá está uma faca, uma arma que para muitos soa perigosa, para nós é a verdade, não somos idiotas, sabemos que não tem outra forma, estamos nos livrando do verdadeiro sofrimento. Esta é a única forma."

    ship "Você se ajoelha, pega a faca e a encosta contra a barriga."

    ship "Você olha para os lados uma última vez... não vai sentir saudade desse lugar maldito."

    ship "Você enfia a faca na barriga..."

    ship "E se sente aliviado. Sente seu corpo ficando leve, sua alma está flutuando, a dor,o cansaço, eles estão desaparecendo. O mundo está de lado agora, uma das últimas sensações que tem é algo molhado se espalhando pelo corpo."

    ship "Com a leveza de espirito que sente, inevitavelmente, nós sorrimos. É o fim. Estamos em paz"

    ship "Tudo é paz."

    jump start




label ficar_quarto_final:
    # (Investigar o quarto)

    jogador "Bom, eu cheguei até aqui... vou descobrir o que aconteceu de uma vez por todas..."

    ship "Vamos até o fim nesse inferno, certo? Acho que você já entendeu, a gente não vai deixar você fazer isso."

    ed "Ele está certo, acho que você já entendeu que somos e por que existimos, nada mais natural do que irmos nesse caminho juntos."

    jogador "Hmm, eles voltaram... Ok.... Mas a pergunta é, como eu saio daqui?..."

    jogador "Ei, vocês sabem se tem algum kit de primeiros socorros nesse quarto? Eu digo, no quarto de verdade, nã nesse que vocês fizeram...."

    ed "Hm? É sério isso? Você sabe que nossas mentes estão conectadas, certo? Eu sei o que você pensou e não, não vai funcionar, é loucura na verdade."

    ship "Oh, sim, excelente idéia na verdade, bom tem um no banheiro, é só sair pela porta"

    jogador "Ahr... é sério isso? Ainda nesse brincadeira? Bom acho que vou ter que fazer as coisas por conta própria."

    jogador "Sendo eu um louco ou não ainda tenho certeza, sou humano, portanto, estou preso às correntes que a humanidade enrolou em si mesma para ajudar nesse processo."

    ed "Caronte, caronte! Estou te avisando está é uma pés...."

    jogador "Por Deus, Ed, você é muito insistente.... Desapareçam vocês dois logo."

    jogador "Eu me levanto e caminho até a faca a poucos passos da minha vista. Estando em cima dela, eu me ajoelho e a pego com as duas mãos. "

    jogador "Agora, onde eu devo enfiar isso? "

    ship "No coração, rapaz. É a melhor forma."

    jogador "Alguma outra sugestão?"

    ship "Coração, garganta ou barriga, são as opções mais rápidas, apesar de que o nível de dor não ser tão confortável, é o que temos no momento."

    jogador "Certo... "

    ship "Mas você não vai fazer nenhuma dessas escolhas não é mesmo? Eu não vou mais conseguir te parar, não é mesmo?"

    jogador "Sim... sinto muito, mas eu quero lembrar da verdade, mesmo que isso me mate... ou faça eu querer me matar..."

    ship "Ok, vamos fazer um acordo, você vai querer se matar depois disso, eu te garanto... e acho que você já deduziu isso por conta própria também. Se você enfiar a faca na barriga, eu prometo que eu limpo a minha parte e solto as memórias. Temos um acordo?"

    jogador "E como eu posso confiar em você?"

    ship "Me diz você, como pode não confiar em si mesmo?"

    jogador "Hmm, esquece. Eu vou fazer do meu jeito."

    jogador "Eu coloco a faca em minha boca, a lâmina fica virada em direção a minha bochecha... Penso comigo mesmo 'Merda, isso vai doer muito... mas deve ser o suficiente'."

    ship "O que? Está louco? Isso não vai te matar! Só vai te causar uma dor inimaginável!"

    jogador "Essa é a idéia... E eu puxo a faca para o lado"

# (Som de corte e tela pisca vermelho)

    jogador "AHHRHR. Sangue espirra no chão, minha boca queima, está molhada, com gosto de ferro, alguns dentes meus dentes caem no chão. Meu Deeus, como Dói"

    jogador "Deus, Deus eu preciso de ajudar, eu preciso de alguma forma de parar essa dor logo... AHHHRR, MERDA, MERDA, MERDA!"

    ed "Merda, Porra, Porraa!!! Que MERDA você fez seu maníaco?!"

    ship "Por Deus que droga de idéia é essa? Meu Deus do céu como dói!!! Ahhhr"

    jogador "Vai logo, tem alguma porra de sedativo nessa merda desse quarto?"

    ship "Que merda você tem na cabeça?! O que você acha que vai acontecer agora, hã?"

    jogador "O que? Você sabe muito bem: ou a gente para com isso agora ou vamos sentir ainda mais dor, entendeu?"

    ed "Não, Caronte, não é assim, na verdade, tem alguma coisa de estranha, no seu corpo. Você está deixando de se sentir, está ficando leve. Algo de errado está acontecendo, voc...."

    jogador "Eu largo a mão esquerda da faca e enfio no corte e pressiono os buracos que ficavam meus dentes."

    ed "AAAAHHHHRRRR, PORRRAAA! SOLTA, SEU DESGRAÇADO! PARA COM ISSO!"

    ship "HMMMRRR, DEUS DO CÉU, COMO PODE DOER TANTO!!"

    jogador "Eu retiro a mão da minha boca. Suspirando e suando, minha mão está cheia de sangue, lágrimas de dor saem dos meus olhos, eu estou tremendo... "

    jogador "E-Eu já falei para vocês... ou vocês me mostram a merda do quarto ou eu vou fazer a gente implorar pela morte!"

    ship "Não!"

    ed "Não vamos fazer isso! Não importa o que você faça!"

    jogador "Com um último suspiro, eu penso: sempre do jeito difícil não é mesmo?"

    jogador "Com a mão direita que segura a faca, eu a encosto ela nas raizes do meus dentes da frente...."

    jogador "E, finalmente acontece, o mundo escuro começa a tremer. Eu enfio a lâmina que corta meus dentes e minha gengiva, eu até os sinto na minha língua e pela minha descendo pela minha garganta. "

    jogador "AHHHR, AAHHAARR. Eu começo a chorar, lágrimas e mais lágrimas escorrem dos meus olhos se misturando com o sangue em minhas mãos. Eu nunca senti tanta dor e desespero na minha vida. Minhas mãos tremendo, meu corpo inteiro treme, implorando para eu parar, mas acho que sou louco demais para isso."

    jogador "Juntos, Harold e Ed gritam o mais alto que conseguem e, ao mesmo tempo, eu minhas orelhas que antes escorriam sangue e a sensação de desesperança em meu corpo desaparecem. Quase que em mesma sintonia eu sinto o mundo ganhando cor, saindo do vazio que antes estava."

    jogador "O quarto se revela, mas a única coisa que eu consigo pensar agora é que eu preciso de alguma coisa para parar essa dor, pelo amor de Deus. alguém faz isso parar."

    jogador "Com esforço, eu tento me levantar, tento recuperar o foco. ' O corpo, Caronte, a gente precisa ver o corpo...' "

    jogador "Minha cabeça dói, tem alguma coisa vindo? Eu sinto meus braços e perna ficando cada vez mais fracos, eu estou indo, eu não vou aguentar... é impossível... eles... eles estavam enganando a realidade, minha condição é bem pior."

    jogador "Rápido! Rápido, o corpo, Caronte! Caronte? Eu me chamo.... ? Não importa, está em nossa frente, olhe com atenção, vamos logo, não temos tempo!"

    jogador "Estranhamente, sinto um aperto no meu peito, minha cabeça começa a doer mais e mais... elas estão vindo, cada vez mais perto, as memórias! Eu me aproximo, cada vez mais perto, eu estou indo, meu corpo cada vez mais, eu estou indo."

    jogador "Essa pessoa? Sou eu... Caronte? O rosto dela  uma mulher eu estou num quarto elas estão borbulhando cada vez mais... cada vez mais fraco... Quem sou eu? Esse não é meu nome essa mulher eu não... conheço ela não ela não ela me olha estou preocupado estou preocupada contigo você tem que ser melhor que isso por favor"

    jogador "Raiva Raiva RAIVA RAIVA RAIVA RAIVA RAIVA MORRE MORRE MORRE MORRE MORRE MORRE "

    unk "EU ESTOU BEM EU SOU PERFEITO VOCÊ NÃO ME CRIOU VOCÊ NÃO ME CONHECE NINGUÉM ME CONHECE ESSE NÃO É MEU NOME NEM HAROLD SHIPMAN NEM EDWARD NEWGATE NINGUÉM"

    unk "De lado, o mundo está... girando... mais fraco.... cansado... eu me odeio... por que... por que Deus me fez assim? Ela... me desculpa..."

    unk "M-... você n-... devia ter acreditado.... em mim."

    unk "Mãe, Eu.... t- am..........................................................................................."

    jump  start

label fim_raiva:
    # (Tanto faz, certo?)

    jogador "Hmm... entendo. Maldito seja o meu mundo. Eu já vivi de tudo e nenhuma funcionou..."

    jump start


label ficar_quarto_8:
    # (Morrer)

    jogador "AHHR, EU NÃO AGUENTO MAIS!!" with dissolve

    ed "Inferno! Está doendo muito!" with dissolve

    ship "..." with dissolve

    jogador "Eu coloco as mãos sobre minha barriga." with dissolve

    jogador "Eu vou arrancar essa merda de mim, seja lá o que for!" with dissolve

    ed "Não é um bicho, Caronte. Eu já te disse. Você está tendo um surto. Foi isso que levou a gente até aqui,  é a mesma coisa. A gente precisa sair daqui." with dissolve

    ship "Não... não tem mais jeito. Ele escolheu a morte... que assim seja." with dissolve

    jogador "Com as mãos em minha barriga, eu não sinto nada. De fato, não tem nada se mexendo dentro de mim." with dissolve

    ship "Você vai perdendo as forças, alguma coisa vai surgindo dentro de você, uma... ira... uma raiva." with dissolve

    jogador "Eu puxo a pele do meu estômago, tentando abri-la." with dissolve

    ed "Não puxe com tanta força, você vai rasgar a própria pele desse jeito." with dissolve

    jogador "Eu puxo e puxo, cada vez mais forte." with dissolve

    ship "..." with dissolve

    ed "Caronte, pare com isso! Você está indo longe demais." with dissolve

    jogador "Mas meus braços não conseguem puxar mais. Desesperado, olho a minha volta e algo muito estranho me acontece." with dissolve

    jogador "Em um momento rápido, eu vejo a realidade. Um quarto, uma cama... um corpo." with dissolve

    jogador "Uma faca aparece logo a minha frente, um pouco antes da cama. E tudo some novamente, mas a faca... continua ali... por quê?" with dissolve

    ship "Merda! Chega disso, chega de tudo isso! Por quê? Por que você insiste tanto em ficar aqui dentro?! Eu já te disse isso só vai te trazer mais dor." with dissolve

    ed "Não importa o que a gente faça, você não sai daqui. Você prefere morrer do que sair aqui." with dissolve

    jogador "Hã, que droga está acontecendo aqui? Eu consegui ver a realidade por um segundo... mas depois ela se foi. Era óbvio, eu estava no quarto este tempo todo, mas por que eu não consigo enxergar?" with dissolve

    ship "Eu... não sei mais o que fazer."

    jogador "Eu estou sentindo o Harold chorando... Ele está com muito medo."

    jogador "Hã? Algo molhado escorre dos meus olhos... Estou... chorando?"

    ed "Eu... só não quero passar por isso de novo."

    jogador "Algo molhado escorre de minhas orelhas... Isso é sangue... Edward está ficando mais fraco... eu sinto que estou... perdendo a esperança em mim."

    jogador "..."

    jogador "Entendi... eles só querem me proteger... na verdade... Eu quero me proteger." with dissolve 

    jogador "Eu criei esse mundo falso e obscuro, para me impedir de sofrer, me impedir de encarar aquilo que me pôs contra mim mesmo. Agora eu entendo."

    jogador "Então... acho que para ver a realidade, eu tenho que forçar meu corpo a precisar enxergá-la. Se eu sair tudo vai ser o que era antes... Eu vou poder fugir deste barco ou encerrar minha vida aqui, de uma vez por todas."

    jogador "Se eu ficar... eu não sei o que vai acontecer comigo... Eu preciso me forçar a me deixar enxergar a realidade, certo? Provavelmente esta faca na minha frente vai ser a saída para isso."

    jogador "Será que não tem mesmo saída? Tanto Ed quanto Harold estavam dizendo a verdade? Será que eu vou conseguir viver com as outras pessoas se eu sair daqui? Estou eu mesmo em um barco ou em um hospício? Eu ao menos estou vivo?"

    jogador "Seja qual for a verdade... nunca terei de fato certeza. Ao olhar para cima, procuro uma resposta, uma saída desse mundo de loucuras... Eu vejo estrelas..."

    jogador "Elas formam tudo no céu, todas as combinações e todas as possibilidades. Elas são todos os desenhos, todos os momentos que o universo viveu, tudo que se tem disponível..."

    jogador "Mas elas ainda estão presas neste mundo... Estamos juntos aqui..."

    jogador "Estranho... por que elas me lembram de mim...?"

    menu escolhas_sair_ficar_9:
        "{b}Tanto faz, certo?{b}":
            jump fim_raiva  



label ficar_quarto_7:
    # (Ficar aqui e morrer)

    jogador "Eu não ligo, eu não vou sair daqui!!"

    ed "Por quê?! O que você tem na cabeça?! Você prefere morrer e perder tudo do que confiar na gente só dessa vez?!"

    ship "Por que você nos odeia tanto? Por que faz a gente sofrer tanto?"

    menu escolhas_sair_ficar_8:
        "{b}Viver{b}":
            jump sair_do_quarto_34567
        "{b}Morrer{b}":
            jump ficar_quarto_8  



label ficar_quarto_6:
    # (Ficar onde está)
    jogador "Não!! ARRHHH, MERDA!! "

    ship "Caronte, isso é questão de vida ou morte, inferno. Não tem brincadeira nisso. VOCÊ VAI SURTAR DE NOVO, IGUAL DA ÚLTIMA VEZ!"

    ed "Vai logo para o banheiro pegar seus remédios. Depois você volta aqui!"

    menu escolhas_sair_ficar_7:
        "{b}Pegar remédios no banheiro e viver{b}":
            jump sair_do_quarto_34567
        "{b}Ficar aqui e morrer{b}":
            jump ficar_quarto_7


#Falta: Colocar mais efeitos de dor e tontura e barulhos e tals
label ficar_quarto_5:
    # (Ficar aqui e mas sofrer muita dor)

    jogador "Não, eu vou ficAHR, MER...DA! Que drog..."

    ship "Alguma coisa começa a se mexer dentro da sua barriga, você sente uma criatura viva dentro de você. Ela está te rasgando de dentro para fora."

    ed "A gente tem que tirar esse bicho daí de dentro, Caronte. Ele vai matar a gente! Não pode terminar assim!"

    jogador "Como diabos eu tiro esse negócio de dentro de mim?! Porra, essa merda tá apertando meus pulmões!!"

    ed "Eu lembro disso, já aconteceu antes. Não é um bicho, você precisa tomar seus remédios, Caronte."
    
    ed "Eles devem estar no banheiro do quarto também. Rápido, senão esse 'bicho' vai realmente abrir sua barriga!"

    #Colocar um efeito de luz na porta, destacando ela ainda mais dando mais imponência e poder para ela
    #Como se a própria porta chamasse o Caronte

    menu escolhas_sair_ficar_6:
        "{b}Pegar remédios no banheiro{b}":
            jump sair_do_quarto_34567
        "{b}Continuar aqui (É sério, vamos morrer assim!){b}":
            jump ficar_quarto_6



#FALTA: colocar efeitos de dor e distorção (tontura), barulhos de bicho na barriga
label ficar_quarto_4:
    # (Ficar onde está)

    jogador "Não, dane-se eu vou ficar aqui. Merda... que sensação é essa?!"

    ed "Droga, Caronte, não é hora de picuinha, eu acho que tem alguma coisa dentro da nossa barriga, porra!"

    ship "Ahr! Minha cabeça vai explodir, merda!"

    menu escolhas_sair_ficar_5:
        "{b}Rapido, para o banheiro, logo!{b}":
            jump sair_do_quarto_34567
        "{b}Ficar aqui e sofrer muita dor{b}":
            jump ficar_quarto_5



#FALTA: aplicar efeito distorção, 1 imagem quarto escuro banheiro
label ficar_quarto_3:
    # (Ficar no quarto)

    jogador "Hmm... Espera... Estranho, vocês dois... só estão relatando o que eu estou sentindo, certo? Nada mais... apenas o que eu realmente sinto..."

    ship "Sim, de fato... por que esse tom estranho? Alguma coisa errada?"

    jogador "Esse tempo todo foi assim? Desde o início vocês me diziam o que eu estava vendo, ouvindo e sentindo, não?"

    ed "Estávamos apenas relatando o que estava acontecendo, Caronte. Não é como se a gente tivesse inventado qualquer coisa."

    ship "Nós somos você, uma parte de você. Estamos conectados, você sabe disso."

    jogador "Hm, entendo. Então, eventos estranhos não poderiam ser causados por vocês, certo?"

    ed "Bem... você sabe que nossa mente nos prega peças, Caronte, então..."

    ship "Na verdade, coisas estranhas podem acontecer a qualquer momento."

    jogador "Tipo isso?"

    ed "Você continua no quarto, olhando para o nada..."

    jogador "..."

    ship "O tempo passa... nada acontece. Você não se mexe e o quarto continua vazio..."

    ed "Você então vai ficando mais lento, letárgico... As coisas vão ficando mais lentas..."

    scene black

    pause 0.3

    scene quarto_escuro

    ed "Você começa a perceber seus olhos piscando à medida que tudo vai ficando instantaneamente preto."

    scene black

    pause 0.3

    scene quarto_escuro

    pause 1

    scene black

    pause 0.6

    scene quarto_escuro

    ship "Você continua no quarto, parado, percebendo as piscadas que insiste em fazer."

    scene black

    pause 0.6

    scene quarto_escuro

    pause 2
    
    scene black

    pause 0.6

    scene quarto_escuro

    pause 1

    scene black

    pause 1
    
    scene corredor

    jogador "Espera! O quê?!"

    jogador "Ei! O que é isso? O que aconteceu aqui? Onde eu estou?"

    ed "O que você está falando?"

    ship "Loucuras que podem acontecer a qualquer momento, Caronte."

    ed "A gente te disse que você não bate muito bem da cabeça."

    jogador "Não, não. Isso está errado. Eu estava no quarto agora mesmo. Agora estou no corredor, de novo?!"

    ed "Bem... Sim... Não pergunte para a gente, aconteceu a mesma coisa para nós."

    ship "É meio complicado ser você, Caronte - ser a gente. Essas coisas acontecem com mais frequência do que você imagina."

    jogador "E vocês não tem envolvimento nenhum com isso?"

    ed "Como teríamos? Você acha que a gente consegue teletransportar pessoas?"

    jogador "Ótimo, então eu vou voltar para o quarto! De novo."

    ship "Então, você se vira para entrar no quarto. Você sabe que a porta está atrás de você, não? É só virar e entrar... simples assim."

    scene tres_portas with fade_in

    jogador "..."

    jogador "Era óbvio, né?"

    ship "Por algum motivo, agora aparecem três portas ao invés de uma."

    jogador "É só mais uma maluquice minha também?"

    ed "Bem... talvez?"

    jogador "Bom, dane-se, eu vou entrar."

    jump cena_tres_portas

#começa com todo mundo ficando confuso, se o jogador erra a porta, ele sai do quarto se ele acerta, eles mandam um bicho pegar ele
# mas pq eles colocariam a porta correta? E se eles "teletransportassem" o jogador para fora do quarto e o jogador tentasse entrar de novo?

# colocar as portas no inicio implica que o jogador não vai estranhar o que está acontecendo e quebra a lógica que aparece no futuro

#colocar as portas no futuro é estranho, pq os narradores fariam isso
# Resposta: para tirar o jogador de dentro do quarto muahahahaha

##############


label cena_tres_portas:
    #primeiro, fazer o jogador entender o sistema de portas
    ed "Você escolhe a segunda porta, gira a maçaneta e não tem nada ali, é um lugar escuro qualquer." with dissolve

    scene black

    ed "Ao entrar nesse lugar escuro, nada acontece por alguns segundos..." with dissolve

    ship "A porta está atrás de você. A luz do corredor não adentra o lugar, é meio confuso... Depois de alguns segundos, algo estranho acontece: você está de novo no corredor." with dissolve

    scene tres_portas

    jogador "Espera, o quê? Que droga que está acontecendo nesse lugar?" with dissolve

    ed "A gente não sabe, tente de novo se quiser." with dissolve

    ship "Ou só desista de uma vez e vamos embora daqui, não? Quanto mais a gente tentar entrar no quarto, mais estranho as coisas ficam." with dissolve

    ed "É eu reparei nisso também, não estou gostando nada." with dissolve

    jogador "Não, eu já decidi: eu vou entrar. E também são só umas portas, não tem nada de perigoso aqui." with dissolve

    jogador "Se eu não quiser mais é só eu sair pela porta que eu entrei, não? Isso se eu sair do corredor." with dissolve

    ed "Você faz a mesma coisa para a segunda porta e a mesma coisa acontece. Estamos aqui de novo, no corredor." with dissolve

    jogador "... De novo?" with dissolve

    ship "É... parece que sempre que você entrar nessa porta aí, a gente vai voltar aqui?" with dissolve

    ed "Caronte faz isso com a segunda porta e obtém o mesmo resultado."

    jogador "É, acho que é realmente isso."

    ship "Vai para a primeira se quiser... ou vamos embora."

    ed "Você abre a primeira porta, a escuridão aparece. Você abre a terceira porta, apenas para olhar também, e é a mesma escuridão das outras duas."

    ship "Entramos na terceira e o mesmo acontece: voltamos para o corredor."
    
    ship "Por que você não foi na primeira, Caronte?"

    jogador "Hm? Por que eu iria?"

    ship "Porque é a primeira. É o que todo mundo escolheria, não?"

    jogador "Do que você está falando? Inclusive..."

    ed "Ele tem razão, é meio estranho você não ter entrado na primeira porta."

    ship "'Inclusive'?"

    jogador "Tem algo estranho aqui, não? Eu me senti meio estranho com aquela primeira porta."

    jogador "Tem alguma coisa acontecendo no geral, mas não consigo entender direito... Algo me diz que eu não deveria passar por ela."

    ed "Hm? Por que você diz isso? Não faz muito sentido."

    ship "Sim, realmente não faz muito. Deve ser alguma estranheza sua, rapaz."

    jogador "Tá, talvez isso seja estranho, mas tenho a impressão de que eu estou apenas sobrevivendo aqui."

    ship "Caronte, a gente está aqui, no corredor, fora do quarto. Se você quiser entrar no quarto tem que escolher a porta correta, não?"

    ed "Sim, a porta do quarto não deve ter desaparecido do nada. Uma destas deve ser a correta, não?"

    jogador "Hm... Só uma delas é a correta... mas a única que eu não quis entrar me levaria aonde eu quero?"

    ship "É... é meio estranho, mas enfim, se você entrar nela você vai conseguir o que queria... o quarto escuro sem nada dentro."

    jogador "É... sei."

    jump minigame_porta1

label minigame_porta1:
    ed "Bem... então, Caronte, escolhe a primeira porta, não?"

    menu escolha_minigame_porta1:
        "{b}Entrar na porta 1{b}":
            jump sair_minigame
        "{b}Entrar na porta 2{b}":
            jump ficar_minigame1
        "{b}Entrar na porta 3{b}":
            jump ficar_minigame1
        # "{b}Ficar parado{b}": #Colocar isso daqui? Expandir para ir embora e encotrar e sair realmente do quarto
        #     jump ficar_minigame1





    #agora, ele já entendeu, então inicia o minigame
    #o ship e o ed irão dar a dica para escolher a porta errada, qualquer uma das outras duas portas leva para o lugar certo
    
label ficar_minigame1:
    play audio "<from 0.4 to 1.9>door_handle.mpeg" volume 2.0
    
    jogador "Na verdade, prefiro vir por aqui."

    ed "Hm? Por quê? Estamos no corredor de novo, Caronte."

    ship "O que deu em você, Caronte? Por que está escolhendo a porta errada? Você sabe que ela vai te fazer voltar para cá."

    jogador "Não é nada. Só queria testar uma coisa."

    ed "...Ok, então acho que agora podemos ir pela porta certa, pode ser?"
    
    menu escolher_porta_1:
        "{b}Entrar na porta 1{b}":
            jump sair_minigame
        "{b}Entrar na porta 2{b}":
            jump ficar_minigame2
        "{b}Entrar na porta 3{b}":
            jump ficar_minigame2
        # "{b}Ficar parado{b}": #Colocar isso daqui? Expandir para ir embora e encotrar e sair realmente do quarto
        #     jump ficar_minigame1

label ficar_minigame2:
    play audio "<from 0.4 to 1.9>door_handle.mpeg" volume 2.0
    
    ship "Você passa pela porta e volta para o corredor, de novo."

    ed "Caronte? Você está tendo algum problema com a gente?"

    ship "Por que diabos você não vai na porta certa? Só por que a gente está dizendo para ir nela?"

    jogador "Claro que não. Só estava vendo uma coisa."

    ed "Isso não faz o menor sentido. Você não quer ir para a porta que é diferente apenas por que a gente está dizendo para ir nela."

    jogador "Na verdade, a pergunta é por que vocês estão pedindo para eu ir nessa porta? Tudo isso na verdade é bem estranho, não acham?"

    ship "Hm? Sim, é claramente estranho."

    ed "Tudo bem."

    scene black

    pause 0.2

    scene tres_portas

    jogador "Hm? O que foi isso?"

    ed "Faz sentido o que você disse, Caronte. Esquece essa primeira porta. Se ainda quiser entrar em alguma dessas portas, sinta-se à vontade."

    ship "Hm, ok... Mas você ainda pode ir embora se quiser - esquece esse quarto. Esse anda-anda sem rumo está me irritando."

    menu escolher_porta_2:
        "{b}Entrar na porta 1{b}":
            jump ficar_minigame3
        "{b}Entrar na porta 2{b}":
            jump sair_minigame
        "{b}Entrar na porta 3{b}":
            jump ficar_minigame3
        # "{b}Ficar parado{b}": #Colocar isso daqui? Expandir para ir embora e encotrar e sair realmente do quarto
        #     jump ficar_minigame1    

label ficar_minigame3:
    play audio "<from 0.4 to 1.9>door_handle.mpeg" volume 3.0

    ed "Agora você escolhe a primeira porta?"

    ship "Que droga, Caronte, qual é o seu problema?"

    jogador "Nada. Vocês que são estranhos. Isso tudo é confuso. Por que vocês querem que eu entre no quarto?"

    ed "Você pode fazer o que você quiser, mas a gente ainda não apoia essa ideia. Não tem nada lá dentro, por que nos importaríamos?"

    ship "Toda porta que a gente mandar você entrar, você vai negar? É isso?"

    jogador "Não se preocupe, eu vou ir à certa agora. Qual eu deveria entrar?"

    ship "É.... claro... Entra na terceira porta, então."

    scene black

    pause 0.2

    scene tres_portas

    menu escolher_porta_3:
        "{b}Entrar porta 1{b}":
            jump sair_minigame
        "{b}Entrar porta 2{b}":
            jump ficar_minigame4
        "{b}Entrar porta 3{b}":
            jump ficar_minigame4
        # "{b}Ficar parado{b}": #Colocar isso daqui? Expandir para ir embora e encotrar e sair realmente do quarto
        #     jump ficar_minigame1    

label ficar_minigame4:
    play audio "<from 0.4 to 1.9>door_handle.mpeg" volume 3.0

    ed "Agora ele escolhe a porta que a gente mandou..."

    ship "Chega dessa merda, qual seu problema, Caronte? Escolhe a maldita porta certa e entra nesse maldito quarto."

    jogador "Não se preocupe, Harold. Já deu para entender o que está acontecendo."

    ship "Do que você está falando?"

    jogador "Em um momento vocês não querem que eu entre no quarto de jeito nenhum. Depois, o quarto inteiro desaparece e vocês dizem que é 'só uma brincadeira da minha mente ou sei lá o quê'."

    jogador "Agora eu 'desapareço do quarto' e fico preso em um ciclo de portas infinitas. E claramente tem algo de errado com uma dessas portas, que fica mudando. Algo assim."

    ed "Hm... Você não disse nada na verdade. Não tem nada em sua linha de raciocínio que diga que a gente está te trocando de lugar, não tem nem como fazermos isso."

    ship "Escolhe uma porta, Caronte!"

    jogador "Parece que vocês tem mais poder sobre mim do que eu realmente entendo."

    ship "Escolha. Uma. Porta Caronte!"

    menu escolher_porta_4:
        "{b}Entrar porta 1{b}":
            jump sair_minigame
        "{b}Entrar porta 2{b}":
            jump ficar_minigame5
        "{b}Entrar porta 3{b}":
            jump ficar_minigame5
        "{b}Ficar parado{b}":
            jump ficar_minigame5

label ficar_minigame5:
    play audio "<from 0.4 to 1.9>door_handle.mpeg" volume 3.0

    ship "Maldita criança inútil"

    ed "Chega disso. A gente não vai chegar a lugar nenhum e o barco ainda está afundando." with dissolve

    ed "Você se levanta e escolhe a terceira porta. Lá você fica no quarto escuro por um tempo. Depois nada acontece." with dissolve

    scene quarto_escuro

    ed "Estamos no quarto escuro de novo." with dissolve

    jogador "Hm... Olha só, parece que funcionou, não?" with dissolve

    jump parte_da_dor_fim_minigame_volta_para_quarto_escuro

label parte_da_dor_fim_minigame_volta_para_quarto_escuro:
    play audio "<from 0.4 to 1.9>door_handle.mpeg" volume 3.0

    ship "Feliz, agora, garoto? Estamos todos irritados e de volta nesse quarto."

    ed "Já chega, Harold... Estamos aqui, querendo ou não." with dissolve

    jogador "Mas vocês não se importam com isso, certo? Vocês não gostam, mas não vão tentar ir contra a minha vontade... né?" with dissolve

    ed "Sim. Exato... Na verdade, essa caminhada toda me deu um pouco de cansaço... nossas pernas estão meio machucadas." with dissolve

    ship "Claro... Não está relacionado com o fato de estarmos destruídos desde o início dessa 'aventura' toda." with dissolve

    jogador "Bom... então ainda é um quarto escuro, certo?" with dissolve

    ed "Sim... não há nada aqui ainda." with dissolve

    jogador "Entendo. Vou caminhar por ele, então..." with dissolve

    ship "Ok... como quiser." with dissolve

    ed "Na verdade... vocês não estão sentindo isso? Harold? Caronte?" with dissolve

    # ship "Por um segundo, você sente algo... não parece que é só cansaço mais... tem alguma outra coisa... não?"

    # jogador "Hmm... O que foi agora? Estou me sentindo...."

    # jogador "Hmm... Espera... Estranho, vocês dois... só estão relatando o que eu estou sentindo, certo? Nada mais... apenas o que eu realmente sinto..."

    # ship "Sim, de fato... por que esse tom estranho? Alguma coisa errada?"

    # jogador "Esse tempo todo foi assim? Desde o início vocês me diziam o que eu estava vendo, ouvindo e sentindo, não?"

## VOLTA PARA O QUE ERA ANTES
    
    ed "Nós estamos nos sentindo estranhos."

    ship "O que é isso? O que está acontecendo?"

    jogador "Hã?"

    ed "Estamos nos sentindo... atordoados..."
    
    #aplicar efeito de distorção que eles usam na porta, mas agr no quarto escuro

    ed "O mundo parece estar girando.... O que é isso?"

    ship "Sua cabeça começa a ficar mais leve..."
    
    ed "Seu corpo também, como se a gente estivesse flutuando. Um embrulho no estômago toma a gente - tem alguma coisa na nossa barriga que precisa sair."

    ed "Caronte, acho melhor a gente usar o banheiro. Tem alguma coisa de errado com o nosso corpo."

    jogador "O quê? Droga, minha cabeça... Ah... Merda, eu sinto que vou vomitar! Onde tem um banheiro?"

    #FALTA TERMINAR
    scene quarto_escuro_banheiro

    ed "Dentro deste quarto tem um. Ali, a sua esquerda tem um banheiro."

# (colocar a imagem de uma porta em uma tela toda preta)

    ship "Fica ali, passando pela porta. Vamos logo, eu não estou aguentando mais!!"

    jogador "Que droga de sensação é essa?!"

    menu escolhas_sair_ficar_4:
        "{b}Ir ao banheiro{b}":
            jump sair_do_quarto_34567
        "{b}Ficar aqui parado (vai ser ruim){b}":
            jump ficar_quarto_4

label sair_minigame:
    ed "Você esta no corredor. Você vira e as três portas não estão mais ali, tem apenas uma."

    jogador "O que? Algo mudou."

    # play sound porta_fechada

    ship "Você tenta abrir essa porta de novo e ela nao abre, a macaneta sequer gira. Não importa o quanto você tente essa porta nunca mais vai abrir."

    #trocar por jump menu tal escolhas_principais_raiva_2
    menu escolhas_principais_raiva_3:
        "{b}Fugir do navio{b}":
            jump fugir_do_navio_raiva
        "{b}Encerrar sofrimento{b}":
            jump encerrar_sofrimento


label sair_do_quarto_34567:
    ed "Merda! Finalmente."

    ship "Você corre em direção ao banheiro, desesperadamente, querendo resolver essa merda logo."

    #Colocar esse som?
    # play sound "porta_banheiro-batendo.mp3"
    scene banheiro_remedio
    
    ed "Vai logo, Caronte. O armário está aberto e parece que ainda tem um pouco do remédio."

    play sound "door-slam-172171.mp3"

    ed "Você finalmente entra, mas isso não importa agora."

    ed "Olhe para o armário que está a sua frente e pegue os remédios."

    jogador "Quando passo pela porta, escuto um barulho bem alto. Algo me diz que ela nunca mais vai abrir... nunca. Aqui é o banheiro?"

    ship "Caronte, foco. Pegue os remédios de uma vez e tome-os."

    jogador "Argh, merda! Quantos, quantos eu pego?"

    ed "Apenas dois, é o su-"

    ship "Todos, Caronte, pegue todos é o-"

    ed "O quê?! Sério isso? Agora?"

    ship "Não seja idiota! Olhe a droga que está acontecendo com ele. Um só não vai parar!"

    ed "Caronte, não seja burro! É obvio que isso não faz sentido."

    ship "Se você não tomar o suficiente, você morre aqui mesmo."

    ed "Se ele tomar muito, ele vai ter uma overdose, seu imbecil. Só dois já é o suficiente."

    menu escolha_morte_ou_vida:
        "{b}Tomar duas pílulas{b}":
            jump escolha_morte_ou_vida_vida
        "{b}Tomar todas as quatro pílulas{b}":
            jump escolha_morte_ou_vida_morte
        "{b}Tomar apenas três pílulas{b}":
            jump escolha_morte_ou_vida_morte #ou criar uma morte lenta?
        "{b}Tomar três ou quatro pílulas vai te matar, não escolhe essa{b}":
            jump escolha_morte_ou_vida
        "{b}Não vai não, se você estiver com dúvida, escolha a do meio, não?{b}":
            jump escolha_morte_ou_vida
        "{b}Não! A opção do meio vai te matar, não seja burro!{b}":
            jump escolha_morte_ou_vida
        "{b}Não! Tomar apenas duas pílulas COM CERTEZA vai te matar{b}":
            jump escolha_morte_ou_vida

label escolha_morte_ou_vida_vida:
    ed "Excelente, Caronte. Graças a Deus, realmente achei que você cometeria alguma estupidez agora." with dissolve

    jogador "Hm? Está... sumindo?" with dissolve

    ed "É claro que está sumindo. Eu tinha esquecido que a gente tinha essa coisa, maldita cabeça minha... nossa." with dissolve

    jogador "Haha, não se preocupe, Edward. Todo mundo comete essas bobices de vez em quando, não?" with dissolve

    ed "É... claro." with dissolve

    jogador "Então, meu caro. O que iremos fazer agora? Sair do barco, certo? Tudo bem deve ter algum outro jeito." with dissolve

    ed "Sim! Claro... Enfim, vamos... vamos sair dessa droga de lugar de uma vez, por Cristo... Estamos a sós agora." with dissolve

    jogador "Hm? Perfeito, meu amigo. Huhu. Eu caminho para fora desse quarto feio." with dissolve

    jogador "Espera, a porta está fechada! Hahaha, me esqueci disso." with dissolve

    ed "Não, não está não." with dissolve

    scene corredor

    jogador "Hm? Espera, o que foi isso? Haha."

    ed "Nada, a gente está do lado de fora já, só sair agora."

    jogador "Cara, tudo é tão estranho aqui hahahaha. Ok, eu só vou ir embora."

    ed "Você caminha pelo corredor, chega até o convés e procura alguma forma de sair daqui. Um tempo depois, você acha um pequeno barco abandonado na lateral do navio."

    ed "Ótimo, finalmente. Usaremos esse botezinho para sair desse lugar e finalmente ter uma vida decente, sem mais erros."

    unk "..."

    jogador "Certo... claro."

    scene black

    ed "Descemos o bote, entramos nele e remamos até terra firme. Não é a forma mais segura, contudo, não vai acontecer nada com a gente, acredite."

    ed "Quando chegarmos em terra firme, a gente vai para casa. Você vai tomar um bom banho e descansar."

    ed "A gente vai arranjar um emprego qualquer, ter uma vida normal. Iremos conseguir uma esposa, talvez, ou viver sozinho, não tem problema."

    ed "Aproveitaremos a vida como deve ser feito. Revisitaremos nossos familiares, eles com certeza estão com saudade de nós."

    unk "...."

    ed "Faz tempo que a gente não se vê..."

    ed "Finalmente, Caronte, finalmente acabamos com esse ciclo maldito. Esse é o nosso verdadeiro final!"

    scene estrelas

    pause 2.0

    #começa a tocar a musica originalmente aqui
    # play music "musica_feliz_violao_mais_outras_coisas.mp3" volume 0.7
    # teto quarto

    # label aqui

    scene teto_balada with fade_in

    play music "musica_feliz_violao_mais_outras_coisas.mp3" volume 0.1

    voice "<from 0.8>maria_oi.mp3"
    maria "Oi."

    stop audio
    jogador "...."

    voice "<from 0.6>maria-oi-td-bem2.mp3"
    maria "Oi? Tudo bem?"

    jogador "Hm?"

    scene maria_balada 

    jogador "Ahn, oi. Tudo bem?"

    voice "<from 0.8>maria-haha-luzes3.mp3"
    maria "Haha, ficou encantado com a luzes, é?"

    jogador "Hm, é... na verdade... Onde estou?"

    voice "<from 0.9>maria-wow-alguem-bebeu4.mp3"
    maria "Wow! Hahaha, acho que alguém bebeu mais do que deveria, não?"

    ed "Caronte, estamos numa balada, bar ou sei lá o quê. Só não estraga as coisas, ok?"

    jogador "Que? Ah, não, não se preocupe, estou bem. Só... meio tonto..."

    voice "maria-hahah-engracado5.mp3"
    maria "Haha, é, eu imagino. Você é engraçado, gostei."

    jogador "É... obrigado, me chamo Caronte."

    voice "maria-prazer-conhecer-viaj6.mp3"
    maria "Me chamo Maria, prazer te conhecer viajante."

    jogador "Viajante? Ah, sim, haha, por causa das histórias mitológicas, né?"

    voice "maria-caronte-o-barqueiro7.mp3"
    maria "Uai, seu nome não é por causa do 'Caronte, o barqueiro'? O cara que fica vagando entre os mundos em um barco, levando as pessoas para o inferno?"

    voice "maria-n-lembro-da-historia8.mp3"
    maria "Não sei, acho que é algo assim. Não lembro da história direito."

    jogador "Sim, na verdade acho que é algo próximo disso. Apesar de que não sei o motivo de eu ter esse nome na verdade... Não lembro de nada que aconteceu comigo."

    jogador "Caronte...? Esse nome... é meu... né?"

    voice "maria-parar-de-beber9.mp3"
    maria "Cara, você está muito mal, ahahha. Você precisa parar de beber urgente."

    jogador "Haha, acho que sim..."

    voice "maria-beber-em-outro-lugar10.mp3"
    maria "Ou então... a gente pode continuar a beber em outro lugar, não acha?"

    ed "Se você falar que não, eu te mato."
    
    jogador "Hm, claro, por que não."

    jogador "Ela se levanta e estende a mão para mim. Eu sei que eu não estou bêbado, nem nada... então... por que as coisas estão tão confusas?"

    jogador "Eu me levanto segurando a mão dela."

    ed "E é assim que começa a nossa nova vida, haha."

    # pause music "musica_feliz_violao_mais_outras_coisas.mp3"

    scene black with fade_in

    #tirar musica da balada e colocar silêncio

    stop music

    # coracao_batendo_tensao_terror_maria.mp3
    # terror_percepcao_maria_morta.mp3
    # musica_feliz_violao_mais_outras_coisas.mp3
    # musica_bizarra_terror_maria_morta.mp3


    unk ". . . . . . . . . . . . . . . . . . . . . . . . . ."

    unk ". . . . . não . . . . . . . . . "

    #OBS.: Os efeitos estão muito estranhos, principalmente o da policia

    #estilo blood do kloud
    # play music "morte_maria.mp3"

    #respiração pesada do caronte.
    play sound "respiracao_masculina_pesada1.mp3"
    #Colocar efeitos de coração batendo e aquele zumbido

    # play sound na outra faixa "coracao_batendo.mp3"
    # play sound em outra faixa "zumbido.mp3"
    #Com isso vai ficar os tres sons ao mesmo tempo

    #colocar musica tensa, horripilante

    jogador "Que..."

    pause 2.0

    #colocar som de BOM

    window hide

    play sound "<from 1.7>terror_percepcao_maria_morta.mp3"

    #Colocar ou não essa ficta?
    # play sfx2 "coracao_batendo_tensao_terror_maria.mp3"

    scene maria_morta

    play music "musica_bizarra_terror_maria_morta.mp3"

    #colocar um som de zumbido, tipo, atordoado?

    pause 7.0

    window show

    jogador "Qu- porra...?"

    ed "Não! Não! Não! Não! Não! Não!"

    # play sound "sirene_policia.mp3"

    #Trocar frase? "Você entendeu agora, né?"
    ship "Aberração..."

    stop sound

    scene black with fade_in

    jump start



#Falta cenas, efeitos sonoros
label escolha_morte_ou_vida_morte:
    ship "Isso, exato. Agora, com calma, Caronte, vai ficar tudo bem."

    # aplicar distorção
    # play banheiro_distortion

    jogador "Hmm? O qu... Estou ficand..."

    ship "Está tudo bem, rapaz. Se deixe levar. Você está ficando com sono. Deite no chão e tudo vai passar."

    # scene deitado_chao_banheiro

    ship "O mundo se distorce ao nosso redor. Os sons e as imagens, elas não são o que são. Nosso corpo fica cada vez mais leve e os olhos pesados."

    ship "Lembra, Caronte? Quando éramos pequenos, apenas um garotinho que comia meleca e tinha medo do escuro?"

    ship "Ficamos deitados assim na grama do parque municipal uma vez... não muito longe de casa."

    #colocar som de passáros, vento, coisas felizes em um parque
    play sound "passaros.mp3" loop

    #colocar cena parque municipal
    # scene parque_municipal

    ship "Era manhã, o sol não queimava muito. Os passáros cantavam e o vento nos empurrava, tentando levantar a gente gentilmente... Haha... sinto falta daquela época."

    # scene mulher_parque_municipal

    ship "Ela estava lá ainda, Caronte..."

    #pausa som de passaros

    play sound "suspiro_masculino.mp3"

    ship "Maldito seja a gente, Caronte... Por que Deus odeia tanto a gente?"

    jump start


label ficar_quarto_2:
    # (Ficar no quarto)

    jogador "Deve ter alguma coisa de errado aqui. É como se... o mundo tivesse mudado... para eu não ver aquilo de novo?"

    ship "Hahahaha. 'Como se o mundo tivesse mudado' não seja burro, Caronte! isso não é um mundo de fadas, você só teve uma alucinação devido aos seus danos mentais."
    
    ship "Não tem nada aqui."

    ed "Ele está certo. Você é histérico demais, rapaz."

    jogador "Essas paredes escuras. Elas são falsas, eu vou arrancá-las."

# (aqui eu tento fazer uma manipulação das informações que chegam ao jogador, como os narradores que dizem para o jogador o que ele sente e vê, eles estão mentindo o que o jogador sente de verdade e vê de verdade para tentar tirar o jogador do quarto)

    ed "Não são não! Mas eu te disse, estou ao seu lado. Você se aproxima das paredes escuras, as toca e sente: gelado e concreto. Igual a uma parede normal."

    jogador "Eu sinto a parede gelada... Igual a uma parede normal. Entendi."

    ed "Exato, percebe? Eu te avisei que era apenas uma ilusão."
    
    ed "Você se sente preenchido, satisfeito, como se suas dúvidas desaparecessem. Não há mais nada para fazer aqui."

    menu escolhas_sair_ficar_3:
        "{b}Sair do quarto{b}":
            jogador "Sim, vocês estão certos, são só impressões falsas minhas. Não tenho mais dúvidas sobre isso"
            jump sair_do_quarto_12
        "{b}Ficar no quarto vazio{b}":
            jump ficar_quarto_3

label ficar_quarto_1:
    # (Explorar quarto vazio)

    jogador "Vocês estão de sacanagem? Eu sei o que eu vi."

    ed "Então, você insiste em entrar no quarto vazio? Tudo bem. Você é um homem livre e pode fazer o que quiser. Eu não vou mais tentar te impedir."

    ship "Mas o que você vai fazer agora? Você entrou mais fundo no quarto vazio e encontrou o que esperava. O vazio."

    menu escolhas_sair_ficar_2:
        "{b}Sair do quarto{b}":
            jogador "Droga de lugar bizarro. Ok, eu vou sair logo daqui"
            jump sair_do_quarto_12
        "{b}Ficar e não fazer nada{b}":
            jump ficar_quarto_2




#falta achar 1 imagem
label entrar_quarto_dnv:
    # (jogador escolhe entrar no quarto e vem essa cena):

    ship "Então vai ser assim? Tem certeza disso?"

    ed "Você se vira rapidamente e coloca sua mão sobre a maçaneta da porta mais uma vez, contudo... Você está com medo, encarando a maçaneta com os olhos arregalados, repensando consigo mesmo se vale a pena fazer isso."
    
    ed "Seu corpo está transpirando, mesmo estando gelado. Por que sua mão está tremendo tanto?"
    
    ed "Você não quer isso realmente. Você está em dúvida. Eu tenho a resposta de sua dúvida: volte."

    jogador "Danem-se vocês."

    #tem que terminar. Colocar esse efeito?
    # play sound "porta_abrindo_macaneta.mp3"

    ship "Você gira a maçaneta e puxa a porta com força..."

    jogador ". . . . . . . . . . . . . . . . Mas o quê?"


    # pausar musica ou colocar musica de vazio?
    # play music "vazio.mp3"

    stop music

#Resultado após o jogador passar da última porta
    #tem que terminar
    scene quarto_escuro

    ship "Apenas para revelar que o quarto que antes aí estava, não existe mais. Apenas para revelar que tudo isso foi apenas uma alucinação."
    
    ship "Dê a volta, Caronte. O que você vê agora é apenas uma sala escura, vazia, sem nada dentro."

    jogador "Espera. O que está acontecendo? Onde está o quarto... O sangue... Onde está tudo?"

    ed "Nada disso jamais existiu, Caronte. Era tudo parte da sua imaginação fértil, somada aos danos neurológicos ao longo da vida."
    
    ed "Faz parte! Isso já aconteceu várias vezes e agora foi só mais uma delas. Dê a volta, vamos embora daqui."

    menu escolhas_sair_ficar_1:
        "{b}Sair do quarto{b}":
            jump sair_do_quarto_12
        "{b}Explorar quarto vazio{b}":
            jump ficar_quarto_1



#Caronte está calmo e estranhando o fato do mundo ter mudado, ele vai ter que decidir se sai do barco ou se irá morrer aqui
label sair_do_quarto_12:

    # play sound "Porta_batendo.mp3"

    scene corredor

    ed "A porta fecha atrás de você com tudo. Bam!!!"

    menu escolhas_principais_raiva_2:
        "{b}Fugir do navio{b}":
            jump fugir_do_navio_raiva
        "{b}Encerrar sofrimento{b}":
            jump encerrar_sofrimento



#PRONTO
label Investigar_e_descobrir_a_verdade:
    # ****Investigar e descobrir a verdade:
    jogador "Não, eu não vou sair daqui sem saber de nada." with dissolve

    scene porta

    # narrar protagonista 

    ed "Você, tomado por uma tola curiosidade, caminha em direação à porta." with dissolve

    jogador "Eu não sou um assassino! Eu vou descobrir quem era aquela pessoa e o maldito monstro que fez isso com ela." with dissolve

    ship "Não, Caronte, por favor, tenha piedade. O que eu te disse antes é a infeliz verdade. Isso dói demais, eu não vou aguentar viver aquilo de novo." with dissolve

    ed "Você não precisa lembrar de nada, eu suplico. Confie em nós, não nos faça passar por isso." with dissolve

    jogador "A verdade? Tudo que vocês fizeram foi tentar dizer o que eu deveria fazer! Falando merda atrás de merda, como se você soubesse de alguma coisa. Se eu não me lembro de nada, como você deveria?" with dissolve

    ship "O. Que. Eu. Te. Disse. É. A. Verdade. Eu tenho que soletrar para você entender?" with dissolve

    jogador "Ha! Dane-se esse cara."
    
    jogador "Se vocês não me contarem o que realmente aconteceu, então eu vou descobrir sozinho... Eu não fiz nada, eu sei disso. Vou dar um pouco de dignidade para aquela pobre alma e encerrar essa viagem por aqui. "
    # ("para aquela" está correto ortograficamente?)

    ship "Merda de moleque..."

    ed "Caronte, eu não vou passar por isso de novo... É para o nosso bem."

    jogador "Hm? Você também, Ed? Ok, danem-se vocês dois."

# (aqui na cena de investigação o jogador começa a lutar contra o Harold e o Ed, ou seja, o mundo, a "realidade" vai mudando e o jogador tem que se forçar a mudar a própria mente para encontrar de novo a porta proibida)

    menu menu_escolhas_entra_quarto_dnv:
        "{b}Entrar no quarto{b}":
            jump entrar_quarto_dnv
    # [única opção disponível o jogador entra no barco]
    #  - Entrar no quarto


label rota_raiva:

    play music "<from 10.0>rough-sea-mar-bravo-23670.mp3"

    scene corredor

    ed "Bosta! Inferno! Eu odeio esse lugar, eu odeio toda essa merda!" with dissolve

    ship "Que inferno! Ah, maldito quarto!" with dissolve

    jogador "Por Deus, que merda foi essa?! O que foi isso?"

    ship "A verdade, ou parte dela... Mas ainda tem um poço de memórias que você esqueceu - e que assim seja." with dissolve

    ship "Lembrar disso só vai causar mais dor... E eu não quero mais isso. Por favor, Caronte, liberte a gente - eu já te disse como." with dissolve

    ed "Não, não precisa ser assim. Vamos embora desse barco, a gente não tem nada para fazer aqui. É a melhor forma."

    ship "Isso não vai funcionar, Ed. A gente sabe disso."

    menu escolhas_principais_raiva:
        "{b}Investigar o quarto{b}":
            jump Investigar_e_descobrir_a_verdade
        # [Opção pegar item correto]:
        "{b}Fugir do navio{b}":
            jump fugir_do_navio_raiva #feito, exceto imagens
        "{b}Encerrar sofrimento{b}":
            jump encerrar_sofrimento #feito, exceto imagens



#Falta imagem escadaria e melhorar texto
label fugir_do_navio_raiva:
    # ****Fugir do Navio:
    jogador "Esquece essa merda, esquece toda essa merda! Eu vou sair daqui logo, eu não aguento mais esse maldito lugar!" with dissolve

    ed "Isso! Perfeito, vamos recomeçar e esquecer de tudo de uma vez por todas."

    ship "Hum. Não, não é assim tão fácil. Não dá para esquecer o que nós somos. A verdade sempre volta para cuspir na nossa cara de uma forma ou de outra."
    
    ship "Não dá para fugir! Pelo amor de Deus, me escuta!!"

    jogador "Que se foda. Que merda você sabe sobre isso? Que merda tem de errado com você? Eu cansei desse lugar, nunca mais eu volto aqui!"

    ship "Me escuta, a gente já viveu isso um milhão de vezes. Não dá! Simples assim, NÃO DÁ!"

    ed "Por Cristo, cala essa maldita boca uma vez na sua vida. Ele tomou a decisão dele, não tem mais volta."

    ed "Agora, finalmente, de uma vez por todas, a gente vai sair desse inferno e ter uma vida digna."

    ship "E voltar aqui..."

    ed "E nunca mais voltar aqui. NUNCA. MAIS."

    ed "Vamos em direção às escadas. Podemos sair daqui por um barquinho na lateral do convés e navegar até terra firme. Não é muito longe daqui."

    #melhorar a morte do Harold, queria que ficasse discreta, mas sinistra ao mesmo tempo. Talvez colocar um efeito sonoro ou uma imagem bem rápida?
    ship "Hm... então aqui vamos nós de novo.... mais uma vez.... de novo e de novo...."

    ed "Ao caminhar, você sente uma energia em você Caronte, algo... sumindo... algo ruim está indo embora, um encosto que não irá mais te assombrar. Não se preocupe, ele vai morrer daqui a pouco."

    ed "Me certificarei disso."

    ed "Ao mesmo tempo, você olha para os lados mais detalhadamente, tudo está inundando. Uma água estranha, preta, está entrando, afundando tudo que aqui existe, mas conseguiremos sair se nos apressarmos."

    ed "Ao chegar na ponta da escada, você olha para cima... Estranho, você nunca prestou muita atenção nisso, mas essa escadaria é realmente longa, não?"

    scene escadaria_super_longa

    ed "E escura também.... Caminhamos por ela."

    #audio de madeira sendo pisada
    play sound "<from 3.0 to 6.0>steps-on-wooden-stairs.mp3"

    ed "Subimos as escadas, passo a passo. Cada degrau grita sob seus passos..."
    
    #colocar flashes, gritos e som de coisas batendo em uma pessoa (o som de uma briga com flashes vermelhos) a ideia é que o som das escadas "gritando" lembram a briga que ele teve com a mãe dele
    # o cérebro dele tenta lembrar, mas o ed não deixa.
    ########## flashes e gritos ###########
    # renpy.music.play("soco_sangue_1_edit.mp3", channel="layer1")
    # renpy.music.play("mulher_gritando_1_edit_2.mp3", channel="layer1")
    # renpy.music.play("mulher_gritando_1_edit_2.mp3", channel="layer1")
    # renpy.music.play("choro_mulher_1_edit.mp3", channel="layer1")

    # ed "pause"

    scene vermelho #imagem vermelha (sangue)
    #aumentar volume das coisas?
    play audio "soco_sangue_1_edit.mp3"
    pause 0.1
    scene corredor
    pause 0.1
    play  audio "mulher_gritando_1_edit_2.mp3"
    scene vermelho
    pause 0.1
    scene quarto_probido_entrada
    pause 0.1
    scene corpo_mulher_morta #trocar por foto mulher quadro
    pause 0.1
    play  audio "choro_mulher_1_edit.mp3"
    scene vermelho
    pause 0.1
    #trocar scene corredor por escadaria longa
    scene corredor
    # scene escadaria_super_longa
    pause 0.3
    stop audio

    ################

    ed "Não se preocupe, isso não te lembra de nada. Está tudo bem, Caronte." 
    
    stop audio

    ed "No fim dessas escadas, vemos algo... tem algo ali.... uma... luz? Sim! Isso, é claro... é claro"

    ed "É assim, Caronte, que encerrmos uma passagem para começar outra completamente diferente. É assim que inicia o começo da nossa felicidade eterna, HAHAHA."

    jump start


#Pronto, talvez colocar efeitos de sangue e explosões ou coisa assim
label encerrar_sofrimento:
# ****Encerrar o Sofrimento:
    jogador "Quer saber... Eu estou cansado dessa merda toda... "

    ed "Hm?!"

    jogador "Meu corpo está chorando por descanso, minha cabeça está implorando por paz... e eu nem sei o porquê disso, mas... é como se o mundo estivesse me dizendo...'só... para'."

    ed "Não, NÃO, Caronte! Não-"

    ship "SIM!! Você está escutando, Caronte! Você sente! É como se estivesse alguma coisa adormecida dentro da nossa mente. Algo tão horrível que mesmo selado ainda nos corrói, ainda nos faz sangrar, perder a respiração e as energias."
    
    ship "É uma eterna luta, Caronte. Uma luta sem descanso... uma luta que nunca poderemos ganhar..."

    ed "Não, não escuta ele, a gente ainda tem esperança, Caronte. Dane-se o que o mundo ou esse cara te diz. A gente consegue sair dessa situação, eu consigo te salvar, eu prometo!!!"

    jogador "... Não... me desculpa, Ed... mas eu não... quero mais seguir..., nem ser salvo... De alguma forma, eu sei que não tem outro jeito."

    ship "Você sente alguma coisa mudando dentro de você, Caronte. Como se algo estivesse sumindo."

    ed "N o. Ei, me esc ta, se concentra na minha v z, vai ficar tudo b m, só se conc ntr  em mim e esquece o resto, eu sei que está difícil agora, mas vai tudo m lh rar"

    ship "Vamos logo com isso... Hoje vai ser o dia mais feliz que a gente teve desde aquilo... e o último."

    jogador "Certo... Vamos."

    ed "Não, o qu  eu p ecis  dizer para você mu ar de ideia?"

    ship "Você sente algo mudando em você, como se uma parte sua estivesse sumindo."
    
    ship "Caminhamos para onde tudo começou e, no caminho, você sente que de suas orelhas sai algum líquido vermelho: sangue... e, de certa forma, não é o seu."

    scene conves_distortion

    ed "Car  te! C  ont! M   SC TA! P R FAV R! A GENTE AINDA TEM UMA CHANCE. ENTÃO ME ESCUTA!"

    ship "O sangramento parou."

    menu continuar_escolha_menu:
        "{b}Continuar com sua escolha{b}":
            jump continuar_escolha #feito
        "{b}Fugir do navio{b}":
            jump fugir_navio_encerrar_sofrimento #feito

#Falta terminar
label fugir_navio_encerrar_sofrimento:
    jogador "Merda. Desculpa, Ed. Eu não quero morrer. Meu Deus, me perdoa." with dissolve

    ship "Hm..." with dissolve

    ed "Isso!!! Eu estou vivo!!" with dissolve

    ed "Já ele, nem tanto, né?. Ele nunca mais vai aparecer aqui" with dissolve

    ed "Droga, você me asusstou, Caronte, o que foi aquilo?" with dissolve

    jogador "Desculpa, é que.... Estou tão cansado... tão cansado...." with dissolve

    ed "Entendo, as coisas não tem sido fácil para a gente... nunca foram na verdade... no nascimento Deus nos abandonou e deixou que o mundo fizesse o que queria com nós." with dissolve

    ed "Mas eu não sou Deus ou qualquer outra dessas entidades. Eu não vou te abandonar, Caronte. Eu vou te ajudar a sair dessa merda de uma vez por todas." with dissolve

    jogador "Como? O que eu posso fazer para sair daqui? Estou preso nesse lugar.... de novo?" with dissolve

    ed "Preso nesse lugar?" with dissolve

    ed "Hm..." with dissolve

    # es

    jogador "Tudo parece mais lento... eu, aqui, neste convés. Ao redor, o mar... com as ondas pouco a pouco se distanciando." with dissolve

    ed "E se... você nos matasse para sempre?" with dissolve

    jogador "O quê?"

    ed "Eu tive uma ideia, Caronte... mas não sei se vai dar certo."

    ed "A gente precisa ser rápido. Tem uma canoa aqui em algum lugar. Solte-a na água e vamos para terra firme logo. RÁPIDO!!"

    jogador "Hm, ok. Entendi. Mas qual é o seu plano?"

    ed "Arrume as coisas enquanto vou te explicando."

    jogador "Ok."

    jogador "Eu saio procurando este bote, mas não sei onde está. Se o Ed falou que está por aqui, deve estar certo."

    ed "Sim, estou certo. A explicação é que eu e o Harold estamos na sua cabeça tem muito tempo. Adormecidos ou ativos, estamos aqui."

    jogador "Espera, o quê?"

    ed "E, talvez, só talvez, a gente seja a causa de tudo isso... ou o resultado do efeito que te causa isso. Entende?"

    ed "Se a gente morrer, talvez o seu problema desapareça e você finalmente fique a salvo."

    jogador "Matar vocês? Essas vozes?\nEspera, achei o bote!"

    ed "Perfeito, desça o bote e reme até as docas, após isso..."

    ed "Vamos para um manicômio nos internar à força!"

    jogador "Espera, o quê?! Que merda de ideia é essa?"

    ed "Não pare, vamos logo. Não sei por quanto tempo a gente vai continuar aqui."

    jogador "Do que você está falando? Como assim? Me internar? Tempo?"

    # ?
    play sound "agua_splash.mp3"

    scene black

    ed "Eu sei que sempre te prometi que viveríamos uma vida feliz e alegre, mas preciso que você receba um tratamento logo."

    ed "Somos doentes, Caronte. Precisamos de ajuda..." with dissolve

    jogador "...."

    jogador "Merda... Entendi." with dissolve

    ed "Sim... eu sei... mas é assim que as coisas são... é assim que a gente foi feito, eu acho. Me desculpa." with dissolve

    jogador "...." with dissolve

    jogador "Edward." with dissolve

    ed "Sim?" with dissolve

    jogador "Obrigado." with dissolve

    play sound "mar.mp3"

    jogador "Me internar?" with dissolve

    jogador "É isso que eu sou? Uma pessoa debilitada, doente, ferida?" with dissolve

    jogador "Onde eu estou?" with dissolve

    jogador "Por que não lembro de nada?" with dissolve

    jogador "O Ed não está mais aqui, né?"

    jogador "Ele nunca esteve na verdade."

    scene manicomio

    pause 2.0

    scene black

    # jogador "Eu enxergo alguma coisa na realidade?"

    stop sound

    jump start

    # ed "O seu rosto no lado direito começa a sangrar seu e o olhos estoura em uma chuva de sangue"

    # ed "vamos caronte,  deve ter uma barco aqui em algum lugar, não vai ter como tampar o buraco"

    # ed "Nós iremos ser felizes, Caronte, eu prometo"
    
    # ed "Quando chegarmos na cidade, a primeira coisa que a gente vai fazer vai ser arranjar um esposa de uma vez por todas, isso, uma esposa"
    
    # ed "A gente nunca teve sorte com as mulheres, mas agora, somos pessoas novas, uma vida nova, vai ficar tudo melhor, tudo"

    # ed "Helena? Ela deve estar por ai ainda, vamos até ela, ela vai te consertar de uma vez por todas"

    #colocar algum simbolismo



#Falta imagem estrelas
label continuar_escolha:
    # Continuar Escolha:
    # ou colocar frase?
    jogador "Eu já te disse, Ed... Eu estou cansado disso."

    play sound "sangue_caindo.mp3"

    scene vermelho

    pause 0.1

    queue sound "zumbido_orelha_edit.mp3"

    scene conves_distortion

    ship "Nossas orelhas estouram em sangue e você agora não ouve mais nada. Somos apenas um. A outra parte sua está morta... completamente."

    jogador "Ao acordar, noto convenientemente uma faca no chão, eu me ajoelho e a pego. Com a duas mãos eu a encosto contra minha barriga."
    
    scene estrelas

    jogador "Olhando para cima... eu vejo... estrelas?"

    jogador "Ei... "

    jogador "Que estranho... "

    jogador "Elas me lembram de mim mesmo."

    #achar som de corte de faca
    play sound "corte_faca.mp3"
    # (referência ao jogador e as múltiplas "runs" que tem no jogo)

    scene black with fade_out

    jump start

# 
# Imagens pedir para o Prado:
# - Imagem do céu estrelado, - quarto escuro, - talvez imagem do quadro/mãe do protagonista, - escadaria super longa
# - maria morta, - maria na balada, - teto da balada, - banheiro, - deitado no banheiro, - armário do banheiro
# - deitado parque, - deitado parque vendo mulher do quadro, - manicomio, - 3 portas do minigame, 
# 
#  musicas: muscia ambiente (natural do jogo?) cada rota tem uma música diferente?
#  musica da balada, musica morte da maria
# FIM ROTA RAIVA #
#---------------------------------------------------------------------------------------------------------------------------------