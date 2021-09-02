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
## Parameters

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

