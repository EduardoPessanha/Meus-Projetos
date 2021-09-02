# _Interface Gráfica no Python_ - TKinter

<center>

## Usando Tkinter (biblioteca nativa do Python)

[imagem]:Tkinter.png "Usando Tkinter"
![img][imagem]

<!-- Ou desta forma ==>  <img src=Tkinter.png> -->

</center>   

link para aula 57: <https://www.youtube.com/watch?v=gcpy2syshXA>  
link para aula 58: <https://www.youtube.com/watch?v=IjouwdFwsg0>  
link para aula 59: <https://www.youtube.com/watch?v=GsKbhAxL4SM>  
link para aula 60: <https://www.youtube.com/watch?v=kXj4CDBJyYY>  
link para aula 61: <https://www.youtube.com/watch?v=MK6e3Tj8dS4>


Outras bibliotecas para criar interface gráfica no Python:  

  -  Qtcreator
  -  PySimpleGUI

<center>

#  **TKinter**

</center>


TKinter é uma biblioteca na linguagem python que permite ao desenvolvedor criar e implementar interfaces gráficas aos programas desenvolvidos na linguagem Python.
TKinter é uma linguagem que já vem instalada na maioria das distribuições Python, e pode ser facilmente incorporada em códigos executáveis.

-  **Widgets** --> é utilizado para referenciar um objeto gráfico, como botões de comando, caixas de texto, labels, e assim como para todos os objetos gráfico.

-  **Evento** --> é toda uma ação iniciada, como um click de um mouse, o pressionar de um botão, o liberar de uma tecla, são exemplo de eventos.

A programação do TKinter é toda baseada em **_eventos_**.

## Estrutura básica de um programa TKinter

## Montando a interface (Formulário):

```py
Import tkinter *  # para importar a biblioteca gráfica do Python.
```
## Criar um objeto de classe TK para configurar o formulário:
```py
menu = TK()
```
## Configurando a janela (formulário / interface gráfica) da aplicação:  

-  Título da janela --> **menu.title**("Título da Janela")

```py
menu.tile("Menu Principal")
```
## Configurando as dimensões do formulário:

- **menu.geometry**( "l x h"), onde l = largura e h = altura

```py
menu.geometry("800 x 600")
```

## Configurando a cor de fundo do formulário:

- **menu.configure**(background = "#xxxxxx"), onde #xxxxxx --> código da cor em hexadecimal

```py
menu.configure(background = "#000008")
```
## Configurando Labels:

-  Sintaxe:  

    -  **label**("formulário", text = "texto do label", background = "#xxxxxx", foreground = "#yyyyyy")

```py
lbl1 = Label(menu, text = "Interface Gráfica", background = "#ffffff", foreground = "#000000")
```
## Posicionando o Labels no formulário:

-  Sintaxe:  

    -  **place**(x = "a", y = "b", width = "l", height = "h"), onde:  [o **place** é um gerenciador de posição]

        -  a = distância da lateral esquerda do formulário até a caixa do label.
        -  b = distância da lateral superior do formulário até a caixa do label.
        -  l = comprimento da caixa do label.
        -  h = altura da caixa do label,

```py
lbl1.place(x=20, y=20, width=100, height=20) 
```

## Outra forma de configurar a posição do Label: 
 
-  ## método **pack** (melhor aplicável para o posicionamento de containers):

 o **plack** também é um gerenciador de posição

-  Sintaxe:  

    -  **pack**(ipadx = "a", ipady = "b", padx= "c", pady = "d", side ="top, bottom, rigth ou left", fill "[x]/[y]/[both]", expand = "True/False"), onde:
    
        -  ipadx = especifica o espaço horizontal interno em torno das laterais horizontais do objeto. Valor padrão 0
        -  ipady = especifica o espaço vertical interno em torno das laterais verticais do objeto. Valor padrão 0
        -  padx = especifica o espaço horizontal em cada lado do objeto. Pode ser uma lista de dois valores especificando o espaço à esquerda e o espaço à direita separadamente. Valor padrão (0,0).
        -  pady = especifica o espaço vertical em cada lado do objeto. Pode ser uma lista de dois valores especificando o espaço a cima e em baixo separadamente. Valor padrão (0,0).
        -  side = especifica qual lado do mestre irá ser apresentado o objeto. Pode assumir os valores left (esquerda), right (direita), top (cima) e bottom (baixo). O valor padrão é top (cima).
        -  fill [none] = (padrão) Dá ao objeto suas dimensões solicitadas pelo mesmo MAIS o espaço especificado em padx ou pady
        -  fill [x] = Estende o objeto horizontalmente para preencher toda a largura do espeço disponível, menos o espaço em padx.
        -  fill [y] = Estende o objeto verticalmente para preencher toda a largura do espeço disponível, menos o espaço em pady.
        -  fill [both] = Estende o objeto tanto vertical como horizontalmente até preencher todo o espaço disponível.
        -  expand = especifica se o objeto irá se expandir para ocupar todo o espaço disponibilizado pelo mestre, valor booleano pode ser 1(True) ou 0(False). VAlor padrão é 0(False).

```py
lbl2 = Lavel(menu, text = "Menu Tinker", bg = "#0000f0", fg = "#000000")

lbl2.pack(ipadx=5,ipady = 5,padx = 20,pady = 40,side = 'top',fill = 'y',expand = True)
```

## Exibindo o formulário:

-  mainloop() --> executa o objeto da classe TK() e exibe o formulário na tela, é o elemento finbal da classe TK()

```py
menu1.mainloop()
```

<center>

#  Resumo das configurações do Label TTK:

</center>

**anchor** - Se o texto e/ou imagem forem menores que a largura especificada, você pode usar a opção anchor para especificar onde posicioná-los: tk.W, tk.CENTER ou tk.E para alinhamento à esquerda, centralizado ou direito, respectivamente. Você também pode especificar esta opção usando um estilo.

**background** - Use esta opção para definir a cor de fundo. Você também pode especificar esta opção usando um estilo.

**borderwidth** - Para adicionar uma borda ao redor do Label, defina esta opção para a dimensão de largura. Você também pode especificar esta opção usando um estilo.

**compound** - Especifica se o widget deve exibir texto e bitmaps/imagens ao mesmo tempo, e se sim, onde o bitmap/imagem deve ser colocado em relação ao texto. Deve ser um dos valores tk.NONE, tk.BOTTOM, tk.TOP, tk.LEFT, tk.RIGHT, ou tk.CENTER. Por exemplo, o valor tk.NONE nenhum especifica que o bitmap ou imagem deve (se definido) será  exibido em vez do texto, o valor à esquerda especifica que o bitmap ou imagem deve ser exibido à esquerda do texto, e o valor central especifica que o bitmap ou imagem deve ser exibido em cima do texto.r

**cursor** - Use esta opção para especificar a aparência do cursor do mouse quando ele estiver sobre o widget; O valor padrão (uma string vazia) especifica que o cursor é herdado do widget pai.

**font** - Use esta opção para especificar o estilo da fonte para o texto exibido. Você também pode especificar esta opção usando um estilo.

**foreground** - Use esta opção para especificar a cor do texto exibido. Você também pode especificar esta opção usando um estilo.

**image** - Esta opção especifica uma imagem ou imagens a serem exibidas em adição ou ao invés de texto. Veja na opção compound acima o que acontece quando você fornece tanto a imagem quanto o texto.

**justify** - Se o texto que você fornecer contém novos caracteres de linha (‘\n’), esta opção especifica como cada linha será posicionada horizontalmente: tk.LEFT para esquerda-justifica; tk.CENTER para centro; ou tk.RIGHT para direita-justifica cada linha. Você também pode especificar esta opção usando um estilo.

**padding** - Para adicionar mais espaço nos quatro lados do texto e/ou imagem, defina esta opção para a dimensão desejada. Você também pode especificar esta opção usando um estilo.

**relief** - Defina esta opção para criar um efeito 3-d. Você precisará aumentar a largura da borda para fazer este efeito aparecer. Você também pode especificar esta opção usando um estilo.

**style** - Use esta opção para especificar um nome de widget personalizado

**takefocus** - Use esta opção para especificar se o widget é visitado durante a travessia do foco; Especifique takefocus=True se você quiser que a visita aceite o foco; especifique takefocus=False se o widget não deve aceitar o foco.
O valor padrão é uma string vazia; por padrão, ttk.Label widgets não recebem foco.

**text** - Uma sequência de texto a ser exibida no widget.

**textvariable** - Uma instância StringVar. o texto exibido no widget será o seu valor. Se ambos texto e textvariable forem especificados, a opção de texto será ignorada

**underline** - Você pode solicitar que uma das letras da seqüência de texto seja sublinhada, definindo esta opção para a posição daquela letra. Por exemplo, as opções text=’Quit’ e underline=0 sublinhariam o Q.

O uso desta opção não altera nada funcionalmente. Se você quiser que a aplicação reaja à tecla Q ou alguma variação como control-shift-Q, você precisará configurar os bindings usando o sistema de eventos.

**width** - Para especificar uma largura fixa, defina esta opção para o número de caracteres. Para especificar uma largura mínima, defina esta opção para menos o número de caracteres. Se você não especificar esta opção, o tamanho da área da etiqueta será apenas o suficiente para acomodar o texto e/ou imagem atual.

Para texto exibido em uma fonte proporcional, a largura real do widget será baseada na largura média de um caractere na fonte, e não em um número específico de caracteres.

**wraplength** - Se você definir esta opção para alguma dimensão, todo o texto será cortado em linhas não mais longas do que esta dimensão. Esta opção também pode ser especificada através de um estilo.

<center>

# Resumo das configurações do Label Tk:

</center>

**activebackground** - Que cor de fundo usar quando o Label está ativo (definida com a opção de estado). O padrão é específico da plataforma.

**activeforeground** - Qual cor de primeiro plano usar quando o rótulo está ativo. O padrão é específico da plataforma.

**anchor** - Controla onde no Label o texto (ou imagem) deve estar localizado. Use um dos seguintes controles: N, NE, E, SE, S, SW, W, NW, ou CENTER. O padrão é CENTER.

**background** - A cor de fundo. O padrão é específico da plataforma.

**bg** - Mesmo que background.

**bitmap** - O bitmap a ser exibido no widget. Se a opção de imagem for dada, esta opção é ignorada.

**borderwidth** - A largura da borda do Label. O padrão é específico do sistema, mas normalmente é de um ou dois pixels.

**bd** - Mesmo que borderwidth.

**compound** - Controla como combinar texto e imagem no rótulo. Por padrão, se uma imagem ou bitmap é dada, ela é desenhada ao invés do texto. Se esta opção estiver definida como CENTER, o texto é desenhado em cima da imagem. Se esta opção estiver definida como BOTTOM, LEFT, RIGHT ou TOP, a imagem é desenhada além do texto (use BOTTOM para desenhar a imagem sob o texto, etc.). O padrão é NENHUMA.

**cursor** - Que cursor mostrar quando o mouse é movido sobre a etiqueta. O padrão é usar o cursor padrão.

**disabledforeground** - Qual cor de primeiro plano usar quando o rótulo estiver desativado. O padrão é específico do sistema.

**font** - A fonte a ser utilizada no rótulo. O rótulo só pode conter texto em fonte única. O padrão é específico do sistema.

**foreground** - A cor do Label, utilizada para Labels de texto e bitmap. O padrão é específico do sistema.

**fg** - Mesmo que foreground.

**height** - A altura do Label. Quando  o Label exibe texto, o tamanho é dado em unidades de texto. Quando exibe  uma imagem, o tamanho é dado em pixels (ou unidades de tela). Se fizermos width igual 0 (zero), ou omitido, ele é calculado com base no conteúdo do Label.

**highlightbackground** - Que cor usar para a borda de destaque quando o widget não tem foco. O padrão é específico do sistema, mas normalmente é o mesmo que a cor de fundo padrão.

**highlightcolor** - Que cor usar para a borda de destaque quando o widget tem foco. O padrão é específico do sistema.

**highlightthickness** - A largura da borda de destaque. O padrão é 0 (sem borda de destaque).

**image** - A imagem a ser exibida no widget. O valor deve ser uma PhotoImage, BitmapImage, ou um objeto compatível. Se especificado, isto tem precedência sobre o texto e opções de bitmap.

**justify** - Define como alinhar múltiplas linhas de texto. Use LEFT, RIGHT ou CENTER. Note que para posicionar o texto dentro do widget, use a opção anchor. O padrão é CENTER.

**padx** - Espaço horizontal extra para adicionar ao redor do texto. O padrão é 1 pixel.

**pady** - Espaço vertical extra para adicionar ao redor do texto. O padrão é 1 pixel.

**relief** - Decoração de bordas. O padrão é FLAT. Outros valores possíveis são SUNKEN, RAISED, GROOVE, e RIDGE.

**state** - Estado do Label. Esta opção controla como o Label é renderizado. O padrão é NORMAL. Outros valores possíveis são ACTIVE e DISABLED.

**takefocus** - Se for verdade, o widget aceita foco de entrada. O padrão é falso.

**text** - O texto a ser exibido no Label. O texto pode conter várias linhas. Se as opções de bitmap ou imagem forem usadas, esta opção é ignorada.

**textvariable** - Associa uma variável Tkinter (geralmente uma StringVar) com o Label. Se a variável for alterada, o texto do Label é atualizado.

**underline** - Utilizado com a opção de texto para indicar que um caractere deve ser sublinhado (por exemplo, para atalhos de teclado). O padrão é -1 (sem sublinhado).

**width** - Define a largura do texto.  Na situação em que o Label exibe texto, width (largura)  é dado em unidades de texto.  Quando  o Label exibe uma imagem, o tamanho é dado em pixels (ou unidades de tela). Quando definimos width como 0 (zero), ou omitido, ele é calculado com base no conteúdo do Label.

**wraplength** - Determina quando o texto de um Label deve ser embalado em várias linhas. Isto é dado em unidades de tela. O padrão é 0 (sem invólucro).

<center>

# Tkinter -Checkbuttom

</center>

O widget Checkbutton é usado para exibir uma série de opções para um usuário como botões de alternância. O usuário pode então selecionar uma ou mais opções clicando no botão correspondente a cada opção.

Você também pode exibir imagens no lugar de texto.

## Syntax

Aqui está a sintaxe simples para criar este widget -
```py
w = Checkbutton ( master, option, ... )
```
## Parametros

-   **master** - representa a janela principal.

-   **options** - Aqui está a lista das opções mais comumente usadas para este widget. Essas opções podem ser usadas como pares de valores-chave separados por vírgulas.

###  **_Options:_**

**activebackground** - Cor de fundo quando o botão de seleção está sob o cursor.

**activeforeground** - Cor do primeiro plano quando o botão de seleção está sob o cursor.

**bg** - A cor de fundo normal exibida atrás da etiqueta e do indicador.

**bitmap** - Para exibir uma imagem monocromática em um botão.

**bd** - O tamanho da borda ao redor do indicador. O padrão é 2 pixels.

**command** - Um procedimento a ser chamado toda vez que o usuário altera o estado deste botão de verificação.

**cursor** - Se você definir esta opção para um nome de cursor ( arrow, dot etc. ), o cursor do mouse mudará para aquele padrão quando estiver sobre o botão de seleção.

**disabledforeground** - A cor de primeiro plano usada para renderizar o texto de um botão de seleção desativado. O padrão é uma versão pontilhada da cor de primeiro plano padrão.

**font** - A fonte usada para o texto.

**fg** - A cor usada para renderizar o texto.

**height** - O número de linhas de texto no botão de verificação. O padrão é 1.

**highlightcolor** - A cor do foco é realçada quando o botão de seleção tem o foco.

**image** - Para exibir uma imagem gráfica no botão.

**justify** - Se o texto contiver várias linhas, esta opção controla como o texto é justificado: CENTRO, ESQUERDA ou DIREITA.

**offvalue** - Normalmente, a variável de controle associada a um botão de verificação será definida como 0 quando for apagada (desligada). Você pode fornecer um valor alternativo para o estado desligado definindo offvalue para esse valor.

**onvalue** - Normalmente, a variável de controle associada a um botão de verificação será definida como 1 quando for ativada. Você pode fornecer um valor alternativo para o estado ligado, definindo onvalue para esse valor.

**padx** - Quanto espaço deixar à esquerda e à direita do botão de verificação e do texto. O padrão é 1 pixel.

**pady** - Quanto espaço deve ser deixado acima e abaixo do botão de verificação e do texto. O padrão é 1 pixel.

**relief** - Com o valor padrão, relief = FLAT, o botão de seleção não se destaca de seu fundo. Você pode definir esta opção para qualquer um dos outros estilos

**selectcolor** - A cor do botão de verificação quando definido. O padrão é selectcolor = "red".

**selectimage** - Se você definir esta opção para uma imagem, essa imagem aparecerá no botão de seleção quando for definida.

**state** - O padrão é state = NORMAL, mas você pode usar state = DISABLED para tornar o controle cinza e torná-lo sem resposta. Se o cursor estiver atualmente sobre o botão de seleção, o estado é ATIVO.

**text** - O rótulo exibido próximo ao botão de verificação. Use novas linhas ("\ n") para exibir várias linhas de texto.

**underline** - Com o valor padrão de -1, nenhum dos caracteres do rótulo de texto é sublinhado. Defina esta opção para o índice de um caractere no texto (contando de zero) para sublinhar esse caractere.

**variable** - A variável de controle que rastreia o estado atual do botão de verificação. Normalmente, esta variável é um IntVar() , e 0 significa apagado e 1 significa definido, mas consulte as opções offvalue e onvalue acima.

**width** - A largura padrão de um botão de seleção é determinada pelo tamanho da imagem ou texto exibido. Você pode definir esta opção para um número de caracteres e o botão de verificação sempre terá espaço para esse número de caracteres.

**wraplength** - Normalmente, as linhas não são quebradas. Você pode definir esta opção para um número de caracteres e todas as linhas serão quebradas em partes não maiores do que esse número.

###  **_Methods:_**

A seguir estão os métodos comumente usados ​​para este widget

**deselect()** - Limpa (turns off - desliga) o botão de verificação.

**flash()** - O botão de seleção pisca algumas vezes entre suas cores ativas e normais, mas deixa do jeito que começou.

**invoke()** - Você pode chamar esse método para obter as mesmas ações que ocorreriam se o usuário clicasse no botão de seleção para alterar seu estado.

**select()** - Define (turns on - liga) o botão de verificação.

**toggle()** - Limpa o botão de verificação se definido, define-o se desmarcado.

