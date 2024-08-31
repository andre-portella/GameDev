

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

image porta = "porta.png"
image rachadura = "rachadura.png"
image conves = "conves.png"
image corredor = 'corredor.png'

image black = "black.png"
image quarto_probido_entrada = "quarto.png"
image corpo_mulher_morta = "corpo.png"
image vista_mar = "imagem_provisoria_barco_mar.png"


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
    scene corredor with fade_out and fade_in



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
            jump aproximar_porta

        "{b}Desistir de consertar vazamento.{b}":
            jump desistir_conserto

    jump zoom_in_rachadura


label zoom_in_rachadura:

    scene rachadura with fade_in

    jogador "Por que a rachadura tem esse formato? O que aconteceu aqui?" with dissolve

    ship "Já lhe contamos que a rachadura tem um formato de punho. Me parece um tanto óbvio o que se passou aqui. Mas, vejo que está um pouco confuso. Nesse caso, acho melhor o Ed relembrar a história." with dissolve

    ed "Não podemos afirmar nada, na verdade. É uma rachadura com um formato bastante irregular. Não há muito o que se discutir." with dissolve

    ship "O quê? Está querendo enganar quem? Deixe que eu mesmo conto: em mais um de seus momentos de loucura, você desceu as escadas, foi até o fim do corredor e quebrou essa janela com as próprias mãos. A rachadura, que agora sela o destino desse barco, tem as suas impressões." with dissolve

    ship "Como bem conheço, você não se lembra de nada. Parece que todos os seus erros e traumas são apagados da sua mente. Que coisa fantástica, não?" with dissolve

    ship "Não há o que se lamentar. Sempre foram suas escolhas, tomadas em momentos conscientes ou não, conduzindo seu futuro." with dissolve

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

#Neste momento o jogador está no corredor, ele vê a porta e decide ir em direção a ela.
label aproximar_porta:

    scene porta_midwarp with fade_in

    jogador "Olhando em volta, noto uma porta que os narradores não mencionaram. Ela está meio escondida na penumbra, diferente das outras. Algo sobre ela parece... importante. Dou um passo em direção a ela." with dissolve

    ed "Espere! Há outras prioridades agora. A rachadura precisa ser vedada antes que o barco se encha de água. Concentre-se no  vazamento!" with dissolve

    jogador "Ignorando a advertência, aproximo-me mais da porta. - Por que vocês não mencionaram essa porta antes? Parece que estão tentando me esconder algo." with dissolve

    ed "Essa porta não é relevante para o que está acontecendo agora. Seu foco deve ser resolver o problema do vazamento. Você não quer que o barco afunde,  certo?" with dissolve

    jogador "Se não é relevante, por que tanta insistência em me afastar dela? Algo não está certo. Vou abrir essa  porta." with dissolve

    ed "Mais desesperado - Não! Você está cometendo um erro! O tempo está contra você, e a água continua a entrar. Se você insistir, pode ser tarde demais para salvar o  barco." with dissolve

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
            jump voltar_corredor_b
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
    ed "falta implementar: corredor"



label Entrar_quarto_proibido:
    jogador "Consequências piores do que deixar o barco afundar? Vamos descobrir." with dissolve

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
            jump voltar_corredor_c

label voltar_corredor_c:
    ed "teste voltar ao corredor c"
    jump rota_raiva

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
    scene vista_mar

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
    jump voltar_corredor_c




label rota_tristeza:

    jump start


return
