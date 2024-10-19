

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
    item_desperdicado = False #variavel para o trigger de quando o item eh desperdicado
    item_pego = False
    janela_consertada = False

    #Não entrar no quarto proibido ate o jogador decidir se abre a porta ou não
    porta_trancada = True #//%Variavel que define quando a porta esta trancada ou nao. Ela fica trancada ate o jogador desperdicar o item, isso eh feito para corrigir um erro
    # do roteiro, faltava uma possibilidade de evento e fazer isso corrige o probelma
    style.my_custom_window = Style(style.window)
    style.my_custom_window.background = Frame("gui/textbox.png", 12, 12)



transform blur_image:
        blur 10.0  # O valor indica a quantidade de desfoque


define fade_out = Fade(0.5, 0, 0.5)
define fade_in = Fade(0.5, 0, 1.5, color="#000000")

define jogador = Character("Jogador", window_style="my_custom_window")
define ship = Character("Shipman Harold",  color="#FF0000", window_style="my_custom_window")
define ed = Character("Ed Newgate", color="#0000FF", window_style="my_custom_window")

define unk = Character("????", color="#FFFFFF", window_style="my_custom_window")
define maria = Character("Maria", color="#FFC0CB", window_style="my_custom_window")

image porta = "porta.png"
image rachadura = "rachadura.png"
image rachadura_consertada = "janela_consertada.png"
image conves = "conves.png"
image barco_mar = "barco_mar.png"
image corredor = 'corredor.png'

image black = "black.png"
image quarto_probido_entrada = "quarto.png"
image corpo_mulher_morta = "corpo.png"
image vista_mar = "imagem_provisoria_barco_mar.png"
image vermelho = "img_vermelho_1.jpg"


#------- IMAGENS NÃO FEITAS AINDA --------------
# image bg corredor = "corredor.png"
#-----------------------------------------------

image corredor = 'corredor.png'


image quarto_distorcido = im.Blur('quarto.png', 3)
image porta_blur = im.Blur('porta.png', 5)

image porta_midwarp = At("porta.png", midwarp)
image conves_distortion = At("conves.png", distortion)

image porta_strongwarp = At("porta.png", strongwarp)

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
label start:

    scene conves_distortion with fade_in

    jump rota_raiva

    # pause 0.5 #pausa a leitura dos códigos por 0.5 segundos

    # play sound "door-slam-172171.mp3"

    # scene corredor

    # pause 0.5

    # scene quarto_probido_entrada


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

    scene quarto_distorcido with fade_out and fade_in

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
    scene corredor with fade_out and fade_in #essa parte esta correta?



    ed "Determinado a descobrir a origem do som, você se levanta com dificuldade, ignorando a dor latejante nas suas mãos. O som do vazamento torna-se mais alto e mais insistente, guiando-o para um corredor estreito que se estende a sua frente. A inclinação causada pelas ondas do mar dificulta ainda mais o caminhar." with dissolve

    ship "Um cheiro de madeira molhada e sal preenche o ar. O corredor, com suas portas distribuídas pelos dois lados, se apresenta iluminado apenas por uma luz que atravessa algumas janelas espalhadas ao longo das paredes." with dissolve

    ship "No canto do corredor, você percebe uma poça de água crescente, acumulando-se devido a uma rachadura visível em uma das janelas. O som que te despertou vem precisamente dessa rachadura, onde a água do mar está se infiltrando lentamente, ameaçando encher o corredor por completo." with dissolve

    ed "No canto oposto ao vazamento, algo chama sua atenção. Uma pequena quantidade de resina, provavelmente usada para reparos, está convenientemente armazenada em um recipiente. A resina parece ser a sua melhor chance de vedar a rachadura e impedir que mais água entre." with dissolve

    ed "A situação exige uma ação rápida. Você sente a urgência de agir enquanto observa o corredor inclinado, a água subindo lentamente e o som do vazamento continuando incessante. Você sabe que precisa usar a resina para selar a rachadura antes que seja tarde demais." with dissolve

    jogador "Essa situação é bem estranha, porque me manipula a fazer algo que é óbvio que deve ser feito?" with dissolve


    ship "Apesar do sentimento de urgência, você se encontra indeciso. Certamente passa pela sua mente como o corredor se mantém inclinado de um lado, apesar dos movimentos constantes da maré sobre o barco. Você também questiona a origem desse vazamento, que deve ser recente, dado o volume de água presente. Entretanto, você não está sozinho?" with dissolve


    menu menu_descobrir_barulho:

        "{b}Zoom-in do item\[Opção Exploratória\]{b}":
            jump zoom_in_item

        "{b}Zoom-in da rachadura\[Opção Exploratória\]{b}":
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
                    jump corredor
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
            jump rota_tristeza

    label voltar_corredor:
        jogador "Preciso vedar logo essa rachadura." with dissolve

        jump descobrir_barulho


    label op_exp5:

        jogador "Por que está tudo tão distorcido? Não estou entendendo nada… são alucinações?" with dissolve
        
        ship "O que você vê não são meras alucinações, mas o seu próprio passado, distorcido pelos entorpecentes que outrora foram seu refúgio. Cada contorno borrado, cada sensação incompreendida, ecoando em sua mente são vestígios de uma vida marcada pela dependência." with dissolve

        jump menu_desistir_conserto


# label desistir_conserto:

#     jump Quarto_proibido_jogador_chega_proximo_da_porta_e_narradores_tentam_impedir_isso_de_alguma_forma

# Wilker
label aproximar_porta_item_desperdicado:
    scene porta_midwarp with fade_in

    jogador "Olhando em volta, noto uma porta que os narradores não mencionaram. Ela está meio escondida na penumbra, diferente das outras. Algo sobre ela parece... importante. Dou um passo em direção a ela." with dissolve

    ed "Espere! Há outras prioridades agora. A gente precisa sair daqui antes que o barco se encha de água. Concentre-se no  vazamento!" with dissolve

    jogador "Ignorando a advertência, aproximo-me mais da porta. - Por que vocês não mencionaram essa porta antes? Parece que estão tentando me esconder algo." with dissolve

    ed "Essa porta não é relevante para o que está acontecendo agora. Seu foco deve ser resolver o problema do vazamento. Você não quer que o barco afunde, certo?" with dissolve

    jogador "Se não é relevante, por que tanta insistência em me afastar dela? Algo não está certo. Vou abrir essa  porta." with dissolve

    ed "Não! Você está cometendo um erro! O tempo está contra você, e a água continua a entrar. Se você insistir, pode ser tarde demais para salvar o barco." with dissolve

    ed "Faça o que é necessário para se salvar. Esqueça essa  porta." with dissolve

    ed "Você não entende o que está em jogo! Abrir essa porta pode trazer consequências que você não está preparado para enfrentar!" with dissolve

    ship "Ou talvez devesse...?" with dissolve

    jogador "Quê?!" with dissolve

    ed "Quê?! Não, com certeza não, essa é uma péssima idéia, por que o Harold continua aqui na verdade, não é mesmo? Você deveria desaparecer e deixar a mente dele em paz, acho que seria a melhor coisa para todos  nós." with dissolve

    ship "Na verdade, do outro lado dessa porta se esconde  toda..." with dissolve

    ed "Quieto! Agora! Não tem nada atrás dessa porta, não escute ele! Você lembra dessa angústia! Por que fazer algo tão estúpido agora? Hã ?!" with dissolve 

    ship "Ok, de fato, você está certo. Talvez seja uma ideia ruim." with dissolve

    jogador "Você iria dizer o que sobre a porta? O que ela esconde? Eu quero  saber." with dissolve

    ed "Nada, não tem nada aí. A porta com certeza está emperrada. Não vale a pena o esforço de tentar entrar aí, acredite, vamos para outro lugar…" with dissolve
    
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
    
    ed "test"

label op_exp_ouvir_porta:
    jogador "Espera, que barulho é esse? Está vindo de dentro do quarto..." with dissolve

    ship "Hmm, são..." with dissolve

    ed "Bom, tal ceticismo e audição são louváveis, contudo, creio que há coisas mais importantes para fazer no barco..." with dissolve

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
        ship "Determinado, você nos ignora e estende a mão para a maçaneta da porta. Com a mão na maçaneta, você levemente abre a porta, preparado para o que vier." with dissolve

        ed "Não! De novo isso, outra decisão terrível, Caronte?!" with dissolve

        ship " Quer saber, o Caronte está certo. Ela esconde a verdade, ela esconde toda a verdade. Ela esconde o fato de você ser uma aberração que deveria morrer!" with dissolve

        ship "Lentamente a porta se abre, rangendo enquanto cede ao impulso de sua mão até se abrir completamente." with dissolve

        # (mostra uma tela preta ou alguma coisa que crie um suspense, talvez até a imagem da porta semi aberta tampando a visão de dentro)
        scene black

        #fazer a frase aparecer mais devagar
        jogador "{cps=2}Qu-{/cps} {cps=13}QuE POrrA É EsSa?!!{/cps}"

        #(mostra a cena do quarto cheio de sangue)
        scene quarto_probido_entrada with fade_in

        ship "Contemple a sua obra, aberração! Veja esse sangue, as paredes, a cama, o chão, cada centímetro desse inferno coberto com sangue." with dissolve

        ed "Não! Não! Eu não quero lembrar. Por favor, feche essa porta, ainda dá tempo!" with dissolve

        ship "Não fecha! Olha o que você fez! Lembra do que fez? Esse maldito cheiro de carne apodrecendo (podre) ainda me enoja. Esse cheiro de ferro, do sangue, me enoja. Você me enoja." with dissolve

        jogador "Que porra é essa! Que porra aconteceu aqui?!" with dissolve

        ed "Não! Não! Por favor, não! me tira daqui!" with dissolve

        ship "Sim! Sim! Eu tenho que saber, a gente quer saber, a gente quer lembrar, né? Então, olha no canto do quarto, o que a gente vê?!" with dissolve

        scene corpo_mulher_morta

        jogador "Que porra é essa? Quem é aquela pessoa? Que porra tá acontecendo aqui? Eu não vou mais ficar aqui!" with dissolve

        ship "Consternado, você nada pode fazer perante essa situação. Mesmo desejando, o reconhecimento do que fez lhe mantém paralisado. Você olha meticulosamente para o corpo, e percebe quem você matou, seu psicótico desgraçado." with dissolve

        jogador "Quê? Por que...? Por que... parece comigo? Eu... matei uma pessoa? O que eu fiz?" with dissolve

        ship "Não! Não! Você ainda não lembra? Daria para reconhecer melhor se desse para ver o rosto, mas você ficou tão nervoso, tão irritado. Você não se contentou em bater uma, duas, nem dez vezes, você queria mais, queria que pagasse pelo que fez." with dissolve

        jogador "Eu fiz o quê?! Do que você está falando? Eu não quero ficar mais aqui." with dissolve

        ed "Você não suporta mais permanecer nesse quarto. Afetado e confuso pelas lembranças, você recua subitamente, saindo do quarto e voltando ao corredor." with dissolve

        menu menu_escolhas_entrar_quarto_proibido:
            "{b}Sair desse maldito lugar!{b}":
                jump rota_raiva

    else: #porta está trancada
        auxiliar "tec tec tec"

        jogador "Que? Está trancada?"

        ed "ufff...."

        ship "Hmm, claro... Está trancada...."

        jogador "Espera, isso não é conveniente demais? Isso é algum truque ou coisa assim?"

        ship "Olha, infe-"

        ship "Não, não é um truque nosso..."

        ed "Truque nosso? A gente não fez nenhum truque em nenhum momento..."

        jogador "Hmm... Certo..."

        jump corredor

# label voltar_corredor_c:
#     ed "Entra Rota da Raiva"
#     jump rota_raiva

#Diálogo exploratório:
label zoom_in_item:
    ed "Veja, é isso que usaremos para consertar a rachadura no vidro, pegue-o, passe a pasta na rachadura e problema resolvido, poderemos pensar em como sair daqui finalmente." with dissolve

    ship "Não teria tanta certeza, como uma pasta iria segurar um vazamento? Esta coisa provavelmente é inútil. Seria melhor continuar procurando algo que faça sentido, não temos tempo para desperdiçar com soluções inválidas." with dissolve

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

    ed "Não, essa pasta vai funcionar, ela é feita para isso." with dissolve

    ship "Escuta, Caronte, a resina vai dissolver quando entrar em contato com a água, joga isso fora, não tem utilidade." with dissolve

    ed "Não, não vai. Se a embalagem não estivesse tão danificada daria para ler que ela é feita para isso. Caronte, me escute, eu lembro de quando compramos isso, confie em mim." with dissolve

    jump menu_escolhas_zoom_in_item
    
label pegar_item_correto:
    ed "Excelente escolha, vamos usar isso para fechar essa rachadura e descobrir como sair desse lugar." with dissolve

    ship "Bem, se quiser tentar não sou contra, mas acho que isso vai ser um desperdício precioso do nosso tempo." with dissolve

    $ item_pego = True

    jump menu_escolhas_zoom_in_item

label desperdicar_item:
    jogador "Eu não ligo, vou ver o quão longe consigo arremessar essa resina no mar." with dissolve

    ed "Quê?!" with dissolve

    ship "Quê?!" with dissolve

    jogador "Estou indo para o convés vou ter uma visão melhor de lá." with dissolve

    ed "Não. Caronte? O que...?" with dissolve

    ship "Desafio você fazer essa resina sumir de vista enquanto ela estiver no ar." with dissolve

    ed "Não, Caronte, não faz isso. Essa é a única solução, não tem como arrumar o vidro sem isso, vamos todos morrer!" with dissolve

    ship "Não acredito que seja a única. Nem olhamos o barco todo ainda e temos bastante tempo ainda. A água está entrando bem devagar." with dissolve

    scene conves

    jogador "Aqui estamos e aqui vamos." with dissolve

    ed "Caronte, não!" with dissolve

    #colocar uma cena que mostra o Caronte olhando para o mar.
    scene barco_mar

    ship "Vemos claramente que não conseguimos ver nada daqui de cima, o céu, a água, está tudo bem escuro. O cheiro salgado do mar, as ondas se batendo... Excelente clima para um arremesso." with dissolve

    jogador "Você me desafiou, então aqui vai." with dissolve

    ship "Seu braço direito está um pouco dolorido, impedindo de carregá-los para muito atrás das costas. Você gira o tronco, sentindo uma leve dor na região das costelas." with dissolve

    ship "Ao colocar o pé esquerdo para frente, garantindo um melhor arremesso, você percebe que seu corpo está muito pesado e, de repente, você está realmente cansado e notou isso melhor agora." with dissolve

    ship "Ao se girar o tronco novamente e carregar o braço para frente com todo o resto de força que tem, escuta-se um barulho estridente 'VUFF', a resina quebra o vento tão rápido que é difícil não escutar o barulho, em menos de 2 segundo o composto branco se perde na escuridão  para muito, muito  longe, enquanto está no ar." with dissolve

    ship "Você fica surpreso com o próprio desempenho físico." with dissolve

    #colocar efeito sonoro de um objeto voando e rasgando o ar
    #play sound effect

    jogador "WOW! Não esperava por isso. Eu sou bem forte." with dissolve

    ship "Oh, Caronte, você não faz ideia. Forte como um urso, o suficiente para levantar um motor de um avião ou até destruir o crânio de um adulto bem desenvolvido." with dissolve

    jogador "Hm? Não acho que eu consiga fazer qualquer um dessas coisas." with dissolve

    ship "Eu meio que estava exagerando, não se preocupe." with dissolve

    # obs. "talvez colocar mais indignação nessa fala do Ed."
    ed "É... lá se vai nossa solução... Ok, talvez tenha alguma outra solução em algum lugar." with dissolve

    jogador "Ok, vamos voltar lá para baixo." with dissolve

    #linhas auxiliares para resolver aquele problema do roteiro

    auxiliar "Trec..." with dissolve

    jogador "Hm? Eu ouvi algo? Tipo uma trava...?" with dissolve

    $ item_desperdicado = True
    $ porta_trancada = False

    #volta para o corredor sem dizerem nada.
    jump corredor


label rota_esperanca:

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

    ship "Você se levanta e sair do quarto. Sentindo-se aliviado, como se tivesse se livrado de um pesadelo horrível. Ao sair, você escuta um estrondo atrás de você. A porta se fecha para nunca mais abrir... nunca mais"

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

    ship "Por Deus que merda de idéia é essa? Meu Deus do céu como dói!!! Ahhhr"

    jogador "Vai logo, tem alguma porra de sedativo nessa merda desse quarto?"

    ship "Que merda você tem na cabeça?! O que você acha que vai acontecer agora, hã?"

    jogador "O que? Você sabe muito bem, ou a gente para essa merda agora ou eu vou ferrar ainda mais com vocês, entendeu?"

    ed "Não, caronte, não é assim, na verdade, tem alguma coisa de estranha, no seu corpo. Você está deixando de se sentir, está ficando leve. Algo de errado está acontecendo, voc...."

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

    jogador "Hmm.... entendo. Maldito seja o meu mundo. Eu já vivi de tudo e nenhuma funcionou...."

    jump start


label ficar_quarto_8:
    # (Morrer)

    jogador "AHHR, EU NÃO AGUENTO MAIS!!"

    ed "Inferno! Está doendo muito!"

    ship "..."

    jogador "Eu coloco as mãos sobre minha barriga."

    jogador "Eu vou arrancar essa merda de mim, seja lá o que for!"

    ed "Não é um bicho, Caronte. Eu já te disse. Você está tendo um surto. Foi isso que levou a gente até aqui,  é a mesma coisa. A gente precisa sair daqui."

    ship "Não... não tem mais jeito. Ele escolheu a morte... que assim seja"

    jogador "Com as mãos em minha barriga, eu não sinto nada. De fato, não tem nada se mexendo dentro de mim."

    ship "Você vai perdendo as forças, alguma coisa vai surgindo dentro de você, uma... ira... uma raiva."

    jogador "Eu puxo a pele do meu estômago, tentando abri-la."

    ed "Não puxe com tanta força, você vai rasgar a própria pele desse jeito. "

    jogador "Eu puxo e puxo, cada vez mais forte"

    ship "...."

    ed "Caronte, pare com isso! Você está indo longe demais."

    jogador "Mas meus braços não conseguem puxar mais. Desesperado, olho a minha volta e algo muito estranho me acontece."

    jogador "Em um momento rápido, eu vejo a realidade. Um quarto, uma cama... um corpo."

    jogador "Uma faca aparece logo a minha frente, um pouco antes da cama. E tudo some novamente, mas a faca... continua ali... por que?"

    ship "Merda! Chega disso, chega de tudo isso! Por que? Por que você insiste tanto em ficar aqui dentro?! Eu já te disse isso só vai te trazer mais dor."

    ed "Não importa o que a gente faça, você não sai daqui. Você prefere morrer do que continuar aqui"

    jogador "Hã, que droga está acontecendo aqui? Eu consegui ver a realidade por um segundo... mas depois ela se foi. Era obvio, eu estava no quarto este tempo todo, mas por que eu não 
    consigo enxerga?"

    ship "Eu... não sei mais o que fazer."

    jogador "Eu estou sentindo o Harold chorando... Ele está com muito medo"

    jogador "Hã? Algo molhado escorre dos meus olhos... Estou... chorando?"

    ed "Eu... só não quero passar por isso de novo"

    jogador "Algo molhado escorre de minhas orelhas... Isso é sangue... Ed está ficando mais fraco... eu sinto que estou... perdendo a esperança em mim."

    jogador "Entendi... eles só querem me proteger... na verdade... eu quero me proteger. Eu criei esse mundo falso e obscuro, para que então eu me impeça de me fazer sofrer, me impeça
    de encarar aquilo que me pôs contra mim mesmo. Agora eu entendo."

    jogador "Então... acho que para ver a realidade, eu tenho que forçar meu corpo a precisar enxergar ela. Se eu sair tudo vai ser o que era antes... eu vou poder fugir deste barco 
    ou encerrar minha vida aqui, de uma vez por todas."

    jogador "Se eu ficar... eu não sei o que vai acontecer comigo... eu preciso me forçar a me deixar enxergar a realidade, certo? Provavelmente esta faca na minha frente vai ser 
    a saída para isso."

    jogador "Será que não tem mesmo saída? Tanto Ed quanto Harold estavam dizendo a verdade? Será que eu vou conseguir viver com as outras pessoas se eu sair daqui? Estou eu mesmo
    em um barco ou um hospício? Eu ao menos estou vivo?"

    jogador "Seja qual for a verdade... nunca terei de fato certeza. Ao olhar para cima, procuro uma resposta, uma saída desse mundo de loucuras, eu vejo estrelas.... "

    jogador "elas formam tudo no céu, todas as combinações, todas as possibilidades, todos os desenhos, todos os momentos que o universo viveu, elas são tudo que se tem disponível.... "

    jogador "mas elas ainda estão presas neste mundo... Estamos juntos aqui.... "

    jogador "Estranho... por que elas me lembram de mim?..."

    menu escolhas_sair_ficar_9:
        "{b}Fugir de Barco{b}":
            jump fugir_barco_raiva
        "{b}Encerrar a própria vida{b}":
            jump encerrar_vida_raiva
        "{b}Investigar o quarto{b}":
            jump ficar_quarto_final  
        "{b}Tanto faz, certo?{b}":
            jump fim_raiva  



label ficar_quarto_7:
    # (Ficar aqui e morrer)

    jogador "Eu não ligo, eu não vou sair daqui!!"

    ed "Por que?! O que você tem na cabeça?! Você prefere morrer e perder tudo do que confiar na gente só dessa vez?!"

    ship "Por que você nos odeia tanto? Por que faz a gente sofrer tanto?"

    menu escolhas_sair_ficar_8:
        "{b}Viver{b}":
            jump sair_do_quarto_34567
        "{b}Morrer{b}":
            jump ficar_quarto_8  



label ficar_quarto_6:
    # (Ficar onde está)
    jogador "Não!! ARRHHH, MERDA!! "

    ship "Caronte, isso é questão de vida ou morte, inferno, não tem brincadeira nisso. VOCÊ VAI SURTAR DE NOVO, IGUAL DA ÚLTIMA VEZ!"

    ed "Vai logo para o banheiro pegar seus remédios, depois você volta aqui!"

    menu escolhas_sair_ficar_7:
        "{b}Pegar remédios no banheiro e viver{b}":
            jump sair_do_quarto_34567
        "{b}Ficar aqui e morrer{b}":
            jump ficar_quarto_7


#Falta: Colocar mais efeitos de dor e tontura e barulhos e tals
label ficar_quarto_5:
    # (Ficar aqui e mas sofrer muita dor)

    jogador "Não, eu vou ficAHR, MER...DA! Que drog...."

    ship "Alguma coisa começa a se mexer dentro da sua barriga, você sente uma criatura viva dentro de você. Ela está te rasgando de dentro para fora"

    ed "A gente tem que tirar esse bicho daí de dentro, Caronte. Ele vai matar a gente! Não pode terminar assim!"

    jogador "Como diabos eu tiro esse negócio de dentro de mim?! Porra, essa merda tá apertando meus pulmões!!"

    ship "Exato, ela está te esmagando, rasgando, de dentro para fora. Você precisa de uma faca ou ácido, sei lá. "

    ed "Eu lembro disso, já aconteceu antes, não é um bicho, você precisa tomar seus remédios, Caronte."
    
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

    ed "Nós estamos nos sentindo estranhos."

    ship "O que é isso? O que está acontecendo?"

    jogador "Hã?"

    ed "Estamos nos sentindo... zonzo..."
    
    #aplicar efeito de distorção que eles usam na porta, mas agr no quarto escuro

    ed "O mundo parece estar girando.... O que é isso?"

    ship "Sua cabeça começa a ficar mais leve..."
    
    ed "Seu corpo também, como se a gente estivesse flutuando, um embrulho no estômago toma a gente, tem alguma coisa na nossa barriga que precisa sair"

    ed "Caronte, acho melhor a gente usar o banheiro, tem alguma coisa de errado com o nosso corpo"

    jogador "O que? Droga, minha cabeça... O... Merda, eu sinto que vou vomitar! Onde tem um banheiro?"

    #FALTA TERMINAR
    scene quarto_escuro_banheiro

    ed "Dentro deste quarto tem um, alí, na sua esquerda tem um banheiro"

# (colocar a imagem de uma porta em uma tela toda preta)

    ship "Fica ali, passando pela porta. Vamos logo, eu não estou aguentando mais!!"

    jogador "Que droga de sensação é essa?!"

    menu escolhas_sair_ficar_4:
        "{b}Ir para o banheiro{b}":
            jump sair_do_quarto_34567
        "{b}Ficar aqui parado (vai ser ruim){b}":
            jump ficar_quarto_4


label sair_do_quarto_34567:
    ed "Merda! Finalmente"

    ship "Você corre me direção ao banheiro, desesperadamente, querendo resolver essa merda logo"

    #Colocar esse som?
    play sound "door-slam-172171.mp3"

    ed "Você passa finalmente pela porta, mas isso não importa agora. Olha para o armário que está na sua frente e pegue os remédios"

    jogador "Quando passo pela porta, escuto um barulho bem alto. Algo me diz que ela nunca mais vai abrir... nunca. Aqui é o banheiro?"

    ship "Caronte, foco. Pegue os remédios de uma vez e tome eles"

    jogador "Ahr, merda! Quantos, quantos eu pego?"

    ed "Apenas dois, é o su-"

    ship "Todos, Caronte, pegue todos é o"

    ed "O que?! Sério isso? Agora?"

    ship "Não seja idiota, olha a droga que está acontecendo com ele. Um só não vai parar!"

    ed "Caronte, não seja burro, é obvio que não faz sentido isso"

    ship "Se você não tomar o suficiente, essa merda vai te rasgar de dentro para fora e você morre aqui mesmo"

    ed "Se ele tomar muito, ele vai ter uma overdose, seu imbecil. Só dois já é o suficiente"

    menu escolha_morte_ou_vida:
        "{b}Tomar duas pilulas{b}":
            jump escolha_morte_ou_vida_vida
        "{b}Tomar todas as quatro pilulas{b}":
            jump escolha_morte_ou_vida_morte
        "{b}Tomar apenas três{b}":
            jump morte_lenta
        "{b}Tomar três ou quatro pilulas vai te matar, não escolhe essa{b}":
            jump escolha_morte_ou_vida
        "{b}Não vai não, se você estiver com dúvida, escolha a do meio, não?{b}":
            jump escolha_morte_ou_vida
        "{b}Não! Isso vai te matar, não seja burro!{b}":
            jump escolha_morte_ou_vida
        "{b}Não! Tomar apenas duas pilulas COM CERTEZA vai te matar{b}":
            jump escolha_morte_ou_vida

    # ed "entramos no banheiro, pegamos remédios, tem anti-depressivos na banheiro, temos que tomá-lo para evitar que o bicho mate a gente"

    # ed "ed e ship dizem que o jogador tem que tomar o remédio, só que ship diz que você tem que tomar tomas as várias pilulas e o ed não, diz que é só uma"

    # ed "ed e  ship comecam a brigar, se o jogador tomar todas, ele mmorre, se ele tomar uma o ed ganha se ele tomar 5 ele também 
    # morre, é uma tática do ship para enganar o jogador" 

label escolha_morte_ou_vida_vida:
    ed "Excelente, Caronte. Graças a Deus, realmente achei que você cometeria alguma estupidez agora"

    jogador "Hm? Está... sumindo?"

    ed "É claro que está sumindo, eu tinha esquecido que a gente tinha essa coisa, maldita cabeça minha... nossa"

    jogador "Haha, não se preocupe, Edward, todo mundo comete essas bobices de vez em quando, não?"

    ed "É.... claro"

    jogador "Então, meu caro. O que iremos fazer agora? Sair do barco, certo? Tudo bem deve ter algum outro jeito"

    ed "Sim! Claro.... Em fim, vamos, vamos sair dessa droga de lugar de uma vez, por Cristo... Estamos a sós agora"

    jogador "Hm? Perfeito, meu amigo. Huhu. Eu caminho para fora desse quarto feio, espera, a porta está fechada! hahaha, me esqueci disso"

    ed "Não, não está não"

    scene corredor

    jogador "Hm? Espera, o que foi isso? Haha"

    ed "Nada, a gente está do lado de fora já, só sair agora"

    jogador "Cara, tudo é tão estranho aqui hahahaha. Ok, eu só vou ir embora"

    ed "Você caminha pelo corredor, chega até o convés e procura alguma forma de sair daqui. Um tempo depois, você acha um pequeno barco abandonado na lateral do navio"

    ed "Ótimo, finalmente. Usaremos esse botezinho para sair desse lugar e finalmente ter uma vida decente, sem mais erros"

    unk "..."

    jogador "Certo... claro"

    scene black

    ed "Descemos o bote, entramos nele e remamos até terra firme, não é a forma mais segura, contudo não vai acontecer nada com a gente, acredite"

    ed "Quando chegarmos em terra firme, a gente vai para casa. Você vai tomar um bom banho e descansar"

    ed "A gente vai arranjar um emprego qualquer, ter uma vida normal. Conseguir uma esposa talvez ou viver sozinho, não tem problema"

    ed "Aproveitaremos a vida como deveria ser feito. Revisitaremos nossos familiares, eles com certeza estão com saudade de nós"

    unk "...."

    ed "Faz tempo que a gente não se vê..."

    # scene estrelas

    # pause 2.0

    # play music "musica_balada.mp3"

    #teto quarto
    scene teto_balada with fade_in

    maria "Oi"

    jogador "...."

    maria "Oi? Tudo bem?"

    jogador "Hm?"

    scene maria_balada

    jogador "Ahn, oi. Tudo bem?"

    maria "Haha, ficou encantado com a luzes, é?"

    jogador "Hm, é... na verdade... Onde estou?"

    maria "Wow! Hahaha, acho que alguém bebeu mais do que deveria, não?"

    ed "Estamos numa balada ou bar ou sei lá o que Caronte, não estraga as coisas"

    jogador "Que? Ah, não, não se preocupe, estou bem. Só... meio tonto..."

    maria "Haha, é, eu imagino. Você é engraçado, gostei"

    jogador "É... obrigado, me chamo Caronte"

    maria "Me chamo Maria, prazer te conhecer viajante"

    jogador "Viajante? Ah, sim, haha, por causa da mitologia, né?"

    maria "Uai, seu nome não é por causa do Caronte o barqueiro? O cara que fica vagando entre os mundos em um barco, levando as pessoas para o inferno.. meio que em um limbo, não?"

    maria "Não sei, acho que é algo assim, não lembro da história direito"

    jogador "Sim, na verdade acho que é algo próximo disso, apesar de que não sei o motivo de eu ter esse nome na verdade... não lembro de nada o que aconteceu comigo"

    jogador "Caronte...? Esse nome... é meu... né?"

    maria "Cara, você está muito mal, ahahha. Você precisa parar de beber urgente"

    jogador "Haha, acho que sim..."

    maria "Ou então a gente pode continuar a beber em outro lugar, não acha?"

    ed "Se você falar que não eu te mato"
    
    jogador "Hm, claro, por que não"

    jogador "Ela se levanta e estende a mão para mim, eu sei que eu não estou bebado, nem nada... então... por que as coisas estão tão confusas?"

    jogador "Eu me levanto segurando na mão dela"

    ed "E é assim que começa a nossa nova vida, haha"

    scene black with fade_in

    unk "..."

    unk "...não..."

    #OBS.: Os efeitos estão muito estranhos, principalmente o da policia

    #estilo blood do kloud
    # play music "morte_maria.mp3"

    #respiração pesada do caronte.
    play sound "respiracao_masculina_pesada1.mp3"
    #Colocar efeitos de coração batendo e aquele zumbido

    # play sound na outra faixa "coracao_batendo.mp3"
    # play sound em outra faixa "zumbido.mp3"
    #Com isso vai ficar os tres sons ao mesmo tempo


    # scene maria_morta

    #colocar um som de zumbido, tipo, atordoado?

    jogador "Qu- porra?"

    ed "Não! Não! Não! Não! Não! Não!"

    play sound "sirene_policia.mp3"

    #Trocar frase? "Você entendeu agora, né?"
    ship "Você realmente achou que era real?"

    scene black with fade_in

    jump start



#Falta cenas, efeitos sonoros
label escolha_morte_ou_vida_morte:
    ship "Isso, exato. Agora, com calma, Caronte, vai ficar tudo bem"

    # aplicar distorção
    # play banheiro_distortion

    jogador "Hmm? O qu... Estou ficand..."

    ship "Está tudo bem, rapaz. Se deixe levar. Você está ficando com sono. Deite no chão e tudo vai passar"

    # scene deitado_chao_banheiro

    ship "O mundo se distorce ao nosso redor. Os sons as imagens, elas não são o que são, nosso corpo fica cada vez mais leve e os olhos pesados"

    ship "Lembra, Caronte? Quando eramos pequenos, apenas um garotinho que comia meleca e tinha medo do escuro?"

    ship "Ficamos deitados assim na grama do parque municipal uma vez... não muito longe de casa"

    #colocar som de passáros, vento, coisas felizes em um parque
    play sound "passaros.mp3" loop

    #colocar cena parque municipal
    # scene parque_municipal

    ship "Era manhã, o sol não queimava muito, os passáros cantavam e o vento nos empurrava, tentando levantar a gente gentilmente.... Haha..."

    # scene mulher_parque_municipal

    ship "Ela estava lá ainda, Caronte...."

    #pausa som de passaros

    play sound "suspiro_masculino.mp3"

    ship "*suspiro* ... Maldito seja a gente, Caronte.... Por que Deus odeia tanto a gente?"

    jump start


label ficar_quarto_2:
    # (Ficar no quarto)

    jogador "Deve ter alguma coisa de errado aqui... como se... o mundo tivesse mudado... para eu não ver aquilo de novo?"

    ship "Hahahaha, 'como se o mundo tivesse mudado' não seja burro, Caronte, isso não é um mundo de fadas, você só teve uma alucinação devido aos danos mentais seu"
    
    ship "Não tem nada aqui"

    ed "Ele está certo, você está histérico demais, rapaz"

    jogador "Essas paredes escuras. Elas são falsas, eu vou arrancar elas"

# (aqui eu tento fazer uma manipulação das informações que chegam ao jogador, como os narradores que dizem para o jogador o que ele sente e vê, eles estão mentindo o que o jogador sente de verdade e vê de verdade para tentar tirar o jogador do quarto)

    ed "Não são não, mas eu te disse, estou do seu lado. Você se aproxima das paredes escuras, as toca e sente: gelado e concreto. Igual uma parede normal"

    jogador "Eu sinto a parede gelada e concreta... Igual uma parede normal. Entendi"

    ed "Exato, percebe? Eu te avisei que era apenas uma ilusão"
    
    ed "Você se sente preenchido, satisfeito, como se suas dúvidas desaparececem. Não há mais nada para fazer aqui"

    menu escolhas_sair_ficar_3:
        "{b}Sair do quarto{b}":
            jogador "Sim, vocês estão certos, são só impressões falsas minhas. Não tenho mais dúvidas sobre isso"
            jump sair_do_quarto_12
        "{b}Ficar no quarto vazio{b}":
            jump ficar_quarto_3





label ficar_quarto_1:
    # (Explorar quarto vazio)

    jogador "Vocês estão de sacanagem? Eu sei o que eu vi."

    ed "Então você insiste em entrar no quarto vazio, hâ? Tudo bem. Você é um homem livre e pode fazer o que quiser. Eu não vou mais tentar te impedir."

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

    ed "Você se vira rapidamente e coloca sua mão sobre a maçaneta da porta, mais uma vez, contudo... você está com medo também, você encara a maçaneta com os olhos arregalados, repensando consigo mesmo se vale a pena fazer isso."
    
    ed "Seu corpo está transpirando, mesmo estando gelado. Por que sua mão está tremendo tanto?"
    
    ed "Você não quer isso realmente. Você está em dúvida. Eu tenho a resposta de sua dúvida, 'volte'"

    jogador "Dane-se vocês."

    #tem que terminar. Colocar esse efeito?
    # play sound "porta_abrindo_macaneta.mp3"

    ship "Ele gira a maçaneta e puxa a porta com força...."

    jogador "Mas o que?"

    #tem que terminar
    scene quarto_escuro

    ship "Apenas para revelar que o quarto que antes ai estava, não existe mais, apenas para revelar que tudo isso foi apenas uma alucinação."
    
    ship "Dê a volta, Caronte. O que você vê agora é apenas uma sala escura, vazia, sem nada dentro."

    jogador "Espera. O que está acontecendo? Onde está o quarto.... o sangue e.... o resto, onde está?"

    ed "Nada disso jamais existiu, Caronte. Era tudo parte da sua imaginação fértil, somada com os danos cerebrais ao longo da vida."
    
    ed "Faz parte, isso já aconteceu várias vezes e agora foi só mais uma delas. Dê a volta, vamos embora daqui"

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
    jogador "Não, eu não vou sair daqui sem saber de nada. "

    scene porta

    ship "Que?!"

    ed "Que?! Não, não!"

    jogador "Eu não sou um assassino, eu vou descobrir quem era aquela pessoa e o maldito monstro que fez isso com ela."

    ship "Não Caronte, por favor, tenha piedade. O que eu te disse antes é a infeliz verdade. Isso dói demais, eu não vou aguentar viver aquilo de novo."

    ed "Você não precisa lembrar de nada, eu suplico, confie em nós, não nos faça passar por isso."

    jogador "A verdade? Tudo que você fez até agora foi tentar dizer que eu deveria morrer! Falando merda atrás de merda, como se você soubesse de alguma coisa. Se eu não me lembro de nada, como você deveria? "

    ship "O. Que. Eu. Te. Disse. É. A. Verdade. Eu tenho que soletrar para você entender?"

    jogador "Ha! Dane-se esse cara."
    
    jogador "Se vocês não me conterem o que realmente aconteceu, então eu vou descobrir sozinho... Eu não fiz nada, eu sei disso, vou dar um pouco de dignidade para aquela pobre alma e encerrar essa viagem por aqui. "
    # ("para aquela" está correto ortograficamente?)

    ship "Merda de moleque...."

    ed "Caronte, eu não vou passar por isso de novo... é para o nosso bem."

    jogador "Hm? Você também, Ed? Ok, dane-se vocês dois."

# (aqui na cena de investigação o jogador começa a lutar contra o Harold e o Ed, ou seja, o mundo, a "realidade" vai mudando e o jogador tem que se forçar a mudar a própria mente para encontrar de novo a porta proibida)

    menu menu_escolhas_entra_quarto_dnv:
        "{b}Entrar no quarto{b}":
            jump entrar_quarto_dnv
    # [única opção disponível o jogador entra no barco]
    #  - Entrar no quarto




label rota_raiva:
    scene corredor

    ed "Bosta! inferno! Eu odeio esse lugar, eu odeio toda essa merda!"

    ship "Que inferno! Ahr, maldito quarto!"

    jogador "Por Deus, que merda foi essa?! O que foi isso??    "

    ship "A verdade... ou a face dela, mas ainda tem um poço de memórias que você esqueceu e que assim seja. Lembrar disso só vai causar mais dor... e eu não quero mais isso. Por favor, Caronte, liberte a gente, eu já te disse como."

    ed "Não, não precisa ser assim, vamos embora desse barco, a gente não tem nada para fazer aqui, é a melhor forma."

    ship "Isso não vai funcionar, Ed, a gente sabe disso."

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
    jogador "Esquece essa merda, esquece toda essa merda, eu vou sair daqui logo, eu não aguento mais esse maldito lugar!"

    ed "Isso! Perfeito, vamos recomeçar e esquecer de tudo de uma vez por todas"

    ship "Hum. Não, não é assim tão fácil. Não dá para esquecer o que a gente é, a verdade volta para cuspir na nossa cara de uma forma ou de outra."
    
    ship "Não dá para fugir! Pelo amor de Deus, me escuta!!"

    jogador "Que se foda, que merda você sabe sobre isso? Que merda tem de errado com você? Eu cansei desse lugar, nunca mais eu volto aqui!"

    ship "Me escuta, a gente já viveu isso! Um milhão de vezes, não dá! Simples assim, NÃO DÁ!"

    ed "Por Cristo, cala essa maldita boca uma vez na sua vida. Ele tomou a decisão dele, não tem mais volta"

    ed "Agora, finalmente, de uma vez por todas, a gente vai sair desse inferno e ter uma vida digna"

    ship "E voltar aqui"

    ed "E nunca mais voltar aqui. NUNCA. MAIS"

    ed "Rapidamente, vamos em direção as escadas, podemos sair daqui por um barquinho que irá ter na lateral do convés e navegar até terra firme, não é muito longe daqui"

    #melhorar a morte do Harold, queria que ficasse discreta, mas sinistra ao mesmo tempo. Talvez colocar um efeito sonoro ou uma imagem bem rápida?
    ship "Hm... então aqui vamos nós de novo.... mais uma vez.... de novo e de novo...."

    ed "Ao caminhar, você sente uma energia em você Caronte, algo... sumindo... algo ruim está indo embora, um encosto que não irá mais te assombrar, não se preocupe, ele vai morrer daqui a pouco"

    ed "Me certificarei disso, haha"

    ed "Ao mesmo tempo, você olha para os lados mais detalhadamente, tudo está inundando uma água estranha, preta está entrando, afundando tudo que aqui existe, mas conseguiremos sair se nos apressarmos"

    ed "Ao chegar na ponta da escada, você olha para cima... Estranho, você nunca presotu muita atenção nisso, mas essa escadaria é realmente longa, não?"

    #scene escadaria_super_longa

    ed "E escura também.... Caminhamos por ela"

    #audio de madeira sendo pisada
    play sound "steps-on-wooden-stairs.mp3"

    ed "Subimos as escadas, passo a passo, as escadas gritam sob seus passos..."
    
    #colocar flashes, gritos e som de coisas batendo em uma pessoa (o som de uma briga com flashes vermelhos) a ideia é que o som das escadas "gritando" lembram a briga que ele teve com a mãe dele
    # o cérebro dele tenta lembrar, mas o ed não deixa.
    ########## flashes e gritos ###########
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

    ################

    ed "Não se preocupe, isso não te lembra de nada. Está tudo bem Caronte." 
    
    ed "No fim dessas escadas, vemos algo... tem algo ali.... uma... luz? Sim! Isso, é claro... é claro"

    ed "É assim, Caronte, que encerrmos uma passagem para comçar outra completamente diferente. É assim que inicia o começo da nossa felicidade eterna, HAHAHA."

    jump start


#Pronto, talvez colocar efeitos de sangue e explosões ou coisa assim
label encerrar_sofrimento:
# ****Encerrar o Sofrimento:
    jogador "Quer saber... Eu estou cansado dessa merda toda... "

    ed "Hm?!"

    jogador "Meu corpo está chorando por descanso, minha cabeça está implorando por paz... e eu nem sei o porquê disso, mas... é como se o mundo estivesse me dizendo... só... para."

    ed "Não, NÃO, Caronte! Não-"

    ship "SIM!! Você está escutando, Caronte! Você sente! É como se estivesse alguma coisa adormecida dentro da nossa mente, tão horrível que mesmo selada ainda nos corrói, ainda nos faz sangrar, perder a respiração e as energias."
    
    ship "É uma eterna luta, Caronte, uma luta sem descanso... uma luta que nunca poderemos ganhar..."

    ed "Não, não escuta ele, a gente ainda tem esperança, Caronte. Dane-se o que o mundo ou esse cara te diz, a gente consegue sair dessa situação, eu consigo te salvar, eu prometo!!!"

    jogador "... Não... me desculpa, Ed... mas eu não... quero mais seguir..., nem ser salvo... De alguma forma, eu sei que não tem outro jeito"

    ship "Você sente alguma coisa mudando dentro de você, Caronte. Como se algo estivesse sumindo."

    ed "N o. Ei, me esc ta, se concentra na minha v z, vai ficar tudo b m, só se conc ntr  em mim e esquece o resto, eu sei que está difícil agora, mas vai tudo m lh rar"

    ship "Vamos logo com isso... Hoje vai ser o dia mais feliz que a gente teve desde aquilo... e o último."

    jogador "Certo... Vamos"

    ed "Não, o qu  eu p ecis  dizer para você mu ar de ideia?"

    ship "Você sente algo mudando em você, como se uma parte sua estivesse sumindo."
    
    ship "Caminhamos para aonde tudo começou e, no caminho, você sente suas orelhas saindo algum tipo de líquido. Sangue... e, de certa forma, não é o seu."

    scene conves_distortion

    ed "Car  te! C  ont! M   SC TA! P R FAV R! A GENTE AINDA TEM UMA CHANCE, ENTÃO SE ESCUTA, PORRA!"

    ship "O sangramento parou"

    menu continuar_escolha_menu:
        "{b}Continuar com sua escolha{b}":
            jump continuar_escolha #feito
        "{b}Fugir do navio{b}":
            jump fugir_navio_encerrar_sofrimento #feito

#Falta terminar
label fugir_navio_encerrar_sofrimento:
    jogador "Merda. Desculpa, Ed. Eu não quero morrer, meu Deus, me perdoa"

    ship "Hm..."

    ed "Isso!!! Eu estou vivo, porra!!"

    ed "Já ele, nem tanto, né? Ha. Ele nunca mais vai aparecer aqui"

    ed "Droga, você me asusstou, Caronte, o que foi aquilo?"

    jogador "Desculpa, é que.... Estou tão cansado... tão cansado...."

    ed "Entendo, as coisas não tem sido fácil para a gente... nunca forma na verdade... no nascimento Deus nos abandonou e deixou que o mundo fizesse o que queria com nós"

    ed "Mas eu não sou Deus ou qualquer outra dessas entidades, eu não vou te abandonar, Caronte. Eu vou te ajudar a sair dessa merda de uma vez por todas"

    jogador "Como? O que eu posso fazer para sair daqui? Estou preso nesse lugar.... de novo?"

    ed "Preso nesse lugar?"

    ed "Hm..."

    jogador "Tudo fica parado por um tempo... Estou aqui, neste convés. Ao redor, o mar.... alguns segundos passam"

    ed "E se... você nos matasse para sempre?"

    jogador "O que?"

    ed "Eu tive uma idéia, Caronte... mas não sei se vai dar certo"

    ed "A gente precisa ser rápido, tem uma canoa aqui em algum lugar, desça ela e vamos para terra firme logo. RÁPIDO!!"

    jogador "Hm, ok. Entendi. Mas qual é o seu plano?"

    ed "Arruma as coisas enquanto vou te explicando."

    jogador "Ok"

    jogador "Eu saio procurando este bote, não sei onde está, mas se o Ed falou que ele está aqui, deve estar certo"

    ed "Sim, esotu certo. A explicação é que eu e o ship estamos na sua cabeça tem muito tempo, adormecidos ou ativos, estamos aqui"

    jogador "Espera, o que?"

    ed "E, talvez, só talvez, a gente seja a causa de tudo isso... ou o resultado do efeito que te causa isso. Entende?"

    ed "Se a gente morrer, talvez o seu problema desapareça e você finalemente fique a salvo"

    jogador "Matar vocês? Essas vozes? Espera, achei!"

    ed "Perfeito, desça o bote e reme até as docas, após isso..."

    ed "Vamos para um manicomio nos internar a força!"

    jogador "Espera, o que?! Que merda de ideia é essa?"

    ed "Não pare, vamos logo, não sei por quanto tempo a gente vai continuar aqui"

    jogador "Do que você está falando? Como assim? Me internar? Tempo?"

    # ?
    play sound "agua_splash.mp3"

    scene black

    ed "Eu sei que sempre te prometi que viveriamos uma vida feliz e alegre, mas tenho que deixar esse objetivo para forçar você a receber um tratamento logo."

    ed "Somos doentes, Caronte, precisamos de ajuda..."

    jogador "...."

    jogador "Merda... porra... Entendi"

    ed "Sim... eu sei... mas é assim que as coisas são... é assim que a gente foi feito, eu acho. Me desculpa"

    jogador "...."

    jogador "Edward"

    ed "Sim?"

    jogador "Obrigado"

    play sound "mar.mp3"

    jogador "Me internar?"

    jogador "É isso que eu sou? Uma pessoa debilitada, doente, ferida"

    jogador "Onde eu estou?"

    jogador "Por que não lembro de nada?"

    jogador "O Ed não está mais aqui, né?"

    jogador "Ele nunca esteve na verdade"

    # scene manicomio

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
    jogador "Eu já te disse, Ed... Eu estou cansado dessa merda."

    play sound "sangue_caindo.mp3"

    scene vermelho

    pause 0.1

    queue sound "zumbido_orelha_edit.mp3"

    scene conves_distortion

    ship "Nossas orelhas estouram em sangue e você agora não ouve mais nada. Somo apenas um. A outra parte sua está morta... completamente."

    jogador "Ao chegar no destino onde acordamos, adequadamente se encontra uma faca no chão, eu a pego e me ajoelho no chão. Com a duas mãos eu a encosto contra minha barriga."
    
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
# - deitado parque, - deitado parque vendo mulher do quadro
# 
#  musicas: muscia ambiente (natural do jogo?) cada rota tem uma música diferente?
#  musica da balada, musica morte da maria
# FIM ROTA RAIVA #
#---------------------------------------------------------------------------------------------------------------------------------


label rota_tristeza:

    jump start


return
