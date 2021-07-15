# Alterando a transparência do painel

Como tornar o painel transparente: (https://plus.diolinux.com.br/t/resolvido-transparencia-no-painel-do-cinnamon/57)


Oi Jedi, eu consegui fazer a mudança, e realmente, tirando temas e extensões, é possível alterar o CSS do Cinnamon. Então vai exigir, não diria conhecimentos de programação, mas uma boa percepção ao menos.


Recomendo pegar o tema que você gosta mais e criar uma cópia. Por exemplo, eu fui até:

**/usr/share/themes**


La eu copiei a pasta do tema Mint-Y-Aqua-Dark e colei ele pra dentro da minha pasta **./themes** dentro da minha home e alterei o nome dela para 'Mint Y Aqua Dark modificado", só para poder diferenciar do original. Então nas configurações de temas eu coloquei ele para que quando eu fizesse as modificações eu pudesse perceber as diferenças.


_Agora o negócio é editar o CSS mesmo, vá até a pasta do tema que você vai modificar, no meu caso o “Mint Y Aqua Dark modificado” e nela você vai encontrar uma pasta com o nome de **_Cinnamon_** e dentro dela um arquivo **_cinnamon.css_**_


**/home/$USER/.themes/Mint-Y-Dark-Aqua-Customizado/cinnamon/cinnamon.css**


Você pode abrir ele com qualquer editor de texto de sua preferência, o próprio xed que o Mint traz serve para isso.


Com ele aberto você vai dar um “Ctrl+F” para pesquisar pela palavra “panel”


Navegando pelas sessões você encontrará um trecho mais ou menos assim:

```css
**.panel-top, .panel-bottom, .panel-left, .panel-right {
color: #ffffff;
border: none;
background-color: rgba(47, 47, 47, 0.99);
font-size: 1em;
padding: 0px; }**
```

Repare na sessão “background-color: rgba(47, 47, 47, 0.99);”, essa sessão é que contem as informações de cores e transparências do painel do cinnamon.


Mais especificamente o número “0,99” no final da linha indica o canal alpha, por consequência, a transparência. Altere para 0.10 por exemplo, ficando mais ou menos assim:

```css
.panel-top, .panel-bottom, .panel-left, .panel-right {
color: #ffffff;
border: none;
background-color: rgba(47, 47, 47, 0.10);
font-size: 1em;
padding: 0px; }
```

Salve o arquivo e reinicie o Cinnamon, você pode fazer isso clicando com o botão direito na barra de tarefas>>resolução de problemas>>Reiniciar o Cinnamon, ou então pressionar Alt+F2 escrever a letra “r” e reiniciar o Cinnamon, ou ainda pressionar “Ctrl+Shift+Esc”. Se você estiver usando o tema que está editando, vai perceber a diferença na hora. Recomendo colocar um papel de parede colorido para a diferença ficar mais evidente ainda.


Se você for explorar, tanto no arquivo cinnamon.css quanto no gtk.css, dentro da outra pasta, você também consegue alterar as cores principais do tema, basta um pouco de paciência, porém, atente-se que alguns elementos do tema são imagens, e não arquivos de texto, por isso seria preciso editá-las com um editor de imagens como o GIMP ou o Inkscape, dependendo do que você queira fazer.


Se for só a transparência que você quer, acho que esse ajuste já é o suficiente. Lembrando que isso é para um tema em específico, se você quiser essa característica em outro tema, terá de repetir o processo.


Dica: Desative a extensão “transparent panels” para fazer a modificação, se ela estiver ativada pode acabar interferindo na sua customização.

Abraços!