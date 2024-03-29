# Dinosaur Bot
![Eu sou o dino](https://github.com/lucasstonehc/dinosaurgame/blob/master/images/dinoicon.jpg)


### Inteligência Artificial(IA) fraca.
Este conceito entende que a construção de sistemas são de certa forma “inteligente”, entretanto, não são capazes de raciocinar por si próprios. Não tendo raciocínio nem vontades, pois a máquina se baseia em uma lógica fornecido por um humano.I

## Iniciando
O projeto visa construir uma inteligência artificial(IA) fraca, que possa realizar as atividades atribuidas a ela. Iremos nesse rápido e didático projeto criar um ***bot*** em ***Python*** para jogar o game do dinochome. 

**Let´s do it!**

### Pré-requesitos

Para criar nosso projeto com sucesso devemos instalar essas bibliotecas e o nosso ***Python*** deve ser a versão 3.7
```
    PyAutoGUI
    Pillow==5.4  
    numpy
```

### Instalando

**Parte 1.**

Uma boa prática de programação em ***Python*** quando se inicia um projeto, é criar para este projeto um ambiente virtual ou em Inglês ***virtual environments***. Quando se cria um ambiente virtual seu projeto logo estará isolado do sistema de diretórios, permitindo que as bibliotecas que tu instala nesse projeto, altere somente este projeto e não os demais projetos que estão presentes na máquina.

Para encontrar mais detalhes sobre ambiente virtual, acesse: [Ambiente Virtual](https://docs.python.org/3/library/venv.html) 

Vamos instalar o ***virtual environments*** para nosso projeto. Para isso, abra seu terminal e vá até um diretório que tu queira iniciar o projeto.
Exemplo:

```
C:\Users\stone\Desktop>
```
Após entrar no diretório desejado, tu deve criar seu ***virtual environments***. Digite o comando abaixo seu VENV(***virtual environments***).

```
python -m venv dinosaurgame 
```
Obs: dinosaurgame é o nome do projeto ou nome da pasta ou o que tu quiser chamar, o importante aqui é saber que este será nosso projeto e tu pode atribuir o nome que quiser para este projeto, neste caso escolhemos dinosaurgame.

Caso ocorra tudo certo, tu poderá ver que o projeto foi criado entrando dentro dele. Para isso digite o comando abaixo.
```
cd dinosaurgame
```
Para vereficar quais arquivos foram criados, tu pode digitar o comando abaixo também.
```
dir
```
Caso tu tenha executado este comando, irá perceber que o sistema irá retornar algo semelhante a estrutura abaixo.
```
11/23/2019  01:23 PM    <DIR>          .
11/23/2019  01:23 PM    <DIR>          ..
11/21/2019  08:45 PM    <DIR>          Include
11/21/2019  08:45 PM    <DIR>          Lib
11/21/2019  08:45 PM               120 pyvenv.cfg
11/21/2019  08:51 PM    <DIR>          Scripts
               1 File(s)            120 bytes
               5 Dir(s)  295,931,645,952 bytes free
```

O próximo passo agora é ativar nossa VENV e para isso tu deve navegar até o diretório ***Scripts***. Digite o comando abaixo para realizar esta operação.
```
cd Scripts
```
Após executar o comando tu deve listar os arquivos que estão dentro deste diretório. Digite o comando abaixo.
```
dir
```
Caso tu tenha executado este comando, irá perceber que o sistema irá retornar algo semelhante a estrutura abaixo.
```
11/21/2019  08:51 PM    <DIR>          .
11/21/2019  08:51 PM    <DIR>          ..
11/21/2019  08:45 PM             2,307 activate
11/21/2019  08:45 PM             1,041 activate.bat
11/21/2019  08:45 PM             1,511 Activate.ps1
11/21/2019  08:45 PM               368 deactivate.bat
11/21/2019  08:45 PM            93,065 easy_install-3.7.exe
11/21/2019  08:45 PM            93,065 easy_install.exe
11/21/2019  08:51 PM            93,048 f2py.exe
11/21/2019  08:50 PM            93,052 pip.exe
11/21/2019  08:50 PM            93,052 pip3.7.exe
11/21/2019  08:50 PM            93,052 pip3.exe
11/21/2019  08:45 PM           415,248 python.exe
11/21/2019  08:45 PM           414,736 pythonw.exe
              12 File(s)      1,393,545 bytes
               2 Dir(s)  295,927,517,184 bytes free
```
Aqui temos dois arquivos que iremos utilizar. eles são: ***activate*** e ***deactivate***. O ***activate*** irá iniciar nossa VENV, enquanto o ***deactivate*** irá desativar nossa VENV, bem simples!

Para ativar nossa VENV digite o comando abaixo.
```
activate
```
Caso tudo tenha corrido certo, irá perceber que o sistema irá retornar algo semelhante a estrutura abaixo.
```
(dinosaurgame) C:\Users\stone\Desktop\dinosaurgame\Scripts>
```
Este (dinosaurgame) sinaliza para nós que a VENV está ativa e para finalizar tudo deve voltar para o diretório dinosaurgame. Para isso digite o comando abaixo.
```
cd ..
```

Okay. Se tu compreendeu tudo até aqui, meus PARABÉNS! You´re ROCK!

Agora iremos iniciar a parte 2.

**Parte 2.**

Nessa segunda parte iremos instalar as bibliotecas para nosso projeto, mas antes de iniciar a instalação das bibliotecas vamos atualizar nosso PIP. Digite o comando abaixo para atualizar o PIP.
```
python -m pip install --upgrade pip
```
Tu pode checar a versão do PIP utilizando o comando abaixo.
```
pip --version
```
Uma breve descrição sobre o que PIP. 
Pip é um sistema de gerenciamento de pacotes usado para instalar e gerenciar pacotes de software escritos na linguagem de programação Python. Muitos pacotes podem ser encontrados no Python Package Index (PyPI). 

Fonte: [Descrição PIP](https://pt.wikipedia.org/wiki/Pip_(gerenciador_de_pacotes))

Instalando as bibliotecas ...

A primeira biblioteca que iremos instalar é a **PyAutoGUI**. Essa biblioteca é utilizada para simular interações humana com o computar. interações como: movimento do mouse, click, pressionamento de teclas e entre outros eventos. Caso tu queira saber mais sobre a biblioteca tu pode acessar: [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest)

Digite o comando abaixo para instalar a biblioteca **PyAutoGUI** e lembre-se, sempre instale qualquer biblioteca com sua VENV ativa.

```
pip install PyAutoGUI
```
A segunda biblioteca que iremos instalar é a **Pillow** e a versão dessa biblioteca que iremos utilizar é a 5.4. Esta biblioteca é utilizada para manipular diferentes formatos de imagens. Caso tu queira saber mais sobre a biblioteca tu pode acessar: [Pillow](https://pillow.readthedocs.io/en/stable)


Digite o comando abaixo para instalar a biblioteca **Pillow** e lembre-se, sempre instale qualquer biblioteca com sua VENV ativa.

```
pip install Pillow==5.4
```

A terceira biblioteca que iremos instalar é a **Numpy**. A **Numpy** permite que tu manipule matrizes, realize cálculos e operações  matemáticas avançadas.  Caso tu queira saber mais sobre a biblioteca tu pode acessar: [Numpy](https://numpy.org)

Digite o comando abaixo para instalar a biblioteca **Numpy** e lembre-se, sempre instale qualquer biblioteca com sua VENV ativa.


```
pip install numpy
```

Okay. Se tu compreendeu tudo até aqui, meus PARABÉNS! You´re ROCK!

Agora iremos iniciar a parte 3.

**Parte 3.**

Na terceira parte iremos de fato a começar a construir nosso ***bot***, pois todo nosso projeto já esta configurado e pronto.

Let´s do it. 

Abra seu ***browser*** e acesse o link: ***chrome://dino*** esse será nosso ambiente que iremos mapear para criar nosso ***bot***.
Após executar essa operação, vamos rodar o game até o dino morrer e após sua morte iremos mapear o ambiente.

![Ambiente](https://github.com/lucasstonehc/dinosaurgame/blob/master/images/environments.png)

**Mapeando - Descobrindo a posição do Dino na tela e outros elementos.**
Para descobrir a posição do Dino na tela iremos utilizar a biblioteca ***PyAutoGUI***. A biblioteca possui uma função que chama:
```
pyautogui.displayMousePosition()
```
Vamos construir um mini-script para mapear nosso ambiente. Let´s do it.

Vá até seu terminal e digite o comando abaixo.
```
python
```
A estrutura irá parecer como está abaixo.
```
(dinosaurgame) C:\Users\stone\Desktop\dinosaurgame>python
```
Após executar o comando o sistema irá executar o ***Python*** e estaremos pronto para rodar nosso mini-script.
```
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
O símbolo >>> demonstar que o Python está pronto para receber nossos comandos.

Vamos importar a biblioteca ***PyAutoGUI***. Digite o comando abaixo e execute.

```
import pyautogui 
```
Agora iremos executar a função para retornar para nós coodernadas do mouse na tela. Para isso digite o comando abaixo.
```
pyautogui.displayMousePosition()
```
![Gif do mapeamento](https://github.com/lucasstonehc/dinosaurgame/blob/master/images/pointmouse.gif)

Quando a função é ativada o Gif demonstra como os valores de X e Y mudam de acordo com a movimentação do mouse na tela.

Bom, entendido essa parte, vamos pegar a posição do dino no ambiente e para isso devemos pegar a parte do nariz dele.

![Dino nariz](https://github.com/lucasstonehc/dinosaurgame/blob/master/images/dinonose.png)

Okay, guarde essa informação, pois mais tarde iremos precisar dela.

Vamos criar nossa classe ***Cordenates***. para isso eu aconselho utilizar um IDEA como o **Visual Studio Code**, mas sinta-se livre para escolher qualquer um.

Abra seu editor de preferência e crie o arquivo bot.py.

Digite o ***script*** abaixo para criar a classe.
```
class Cordenates(): 
  
    # coordenatas para encontar o button de restart o game.
    screen_x,screen_y =  pyautogui.size()
    replaybutton = (screen_x/2, screen_y/2) 
    dinosaur = (110, 350) 
```
Pronto acabamos de criar nossa classe ***Cordenates***. Tu lembra das coordenadas do nariz do dino ? então iremos utilizar ela na variável dinosaur. Na classe Cordenates tu encontra a variável com seus valores X e Y setados em 110 e 350 respectivamente.

Com a posição do dino setada. Nós iremos construi uma função para reiniciar o ***game***. Para criar essa fução iremos utilizar as variável ***replaybutton***, pois essa variável já esta setada com as coordenadas para reiniciar o game. Para criar a função digite o ***script*** abaixo.

```
 def restartGame(): 
  
    # Usando pyautogui para criar uma insteração sem nenhum usuário humano.   
    pyautogui.click(Cordenates.replaybutton) 
```

Criando a função de ***Jump***. Nossa função pressSpace tem a função de pressionar a tecla space para que nosso dino pule os obstáculos. Para criar a função digite o ***script*** abaixo.

```
def pressSpace():  

    # pressionando a tecla space
    pyautogui.keyDown('space') 
  
    # aguardando um tempo para liberar 
    time.sleep(0.03)   
  
    # liberando a tecla space  
    pyautogui.keyUp('space')

```

Após realizar todo esse processo, acredito eu que iremos criar uma das funções mais importante do nosso ***bot***. A função ***ImageGrab***. Essa função irá gerar vários screens shoots da tela para nós, e o melhor é que iremos escolher as coordenadas de captura.

A ideia é o seguinte: Vamos capturar um ***box*** pouco a frente do dino e quando houver uma variação de cor na tela iremos fazer com que o dino tome uma ação.

Existe uma frase que fala que uma imagem fala mais que 1000 palavras, então observe a imagem abaixo. O retângulo vermelho é onde nossa função irá atuar.

![Box](https://github.com/lucasstonehc/dinosaurgame/blob/master/images/box.png)

Para criar a função digite o ***script*** abaixo.

```
def imageGrab():  
    # definindo a coordenada do box em frente ao dino 
    box = (Cordenates.dinosaur[0]+30, Cordenates.dinosaur[1], 
           Cordenates.dinosaur[0]+120, Cordenates.dinosaur[1]+30) 
  
    # pegando todos os pixel em forma RGB tupples    
    image = ImageGrab.grab(box) 
  
    # convertendo RGB to Grayscale 
    grayImage = ImageOps.grayscale(image) 
  
    # usando o numpy para somar todos os grayscale pixels  
    a = np.array(grayImage.getcolors()) 
  
    # retornado a soma  
    return a.sum() 
```

Para finalizar nossas funções, nós iremos fazer a função do ***gameOver***. Esta função segue a mesma lógica da função ***imageGrab***.
Para criar a função digite o ***script*** abaixo.

```
def gameOver():
    x = 487
    y = 291
    x2 = 48   
    y2 = 44    

    box = (x, y, x+x2, y+y2)

    image = ImageGrab.grab(box) 
    grayImage = ImageOps.grayscale(image) 
    a = np.array(grayImage.getcolors())
    
    return a.sum()
```
Lembrando que para setar esses valores de x, y, x2 e y2 tu deve utilizar a função ***displayMousePosition*** de ***PyAutoGUI***.

![Restart](https://github.com/lucasstonehc/dinosaurgame/blob/master/images/restart.png)

Percebe que para achar o x2 e y2 tu deve fazer a posição de x2-x1 e então terá x2 final. O mesmo processo se repete para o y2.

Se tu chegou até, Eu gostaria de PARABENIZAR tu novamente.
Para finalizar nosso ***bot***, nós iremos criar nossa função principal. Para criar a função digite o ***script*** abaixo.

```
restartGame() 
while True:  
    if(gameOver() == 2915):
        restartGame() 
    if(imageGrab() != 2955):    
        pressSpace()
        time.sleep(0.1) 
```
Os valores de comparação da função ***gameOver*** e a  função ***imageGrab*** será captura por um rápido comando.
No link abaixo tu encontra o arquivo completo.
[Bot completo em python](https://github.com/lucasstonehc/dinosaurgame/blob/master/dinosaurbot.py)

Para setar os valores vamos, rodar o bot mas iremos colocar alguns prints nas funções.
Para pegar o valor da função ***imageGrab*** altere o ***Script*** principal para e rode o arquivo ***dinosaurbot.py.***
```
restartGame() 
while True:  
    print(imageGrab())    
```

![imageGrab valor](https://github.com/lucasstonehc/dinosaurgame/blob/master/images/imageGrabs.png)

O valor final retornado é quando o ***box*** apresenta valores em escala gray. 
Para pegar o valor da função ***gameOver*** altere o ***Script*** principal para e rode o arquivo ***dinosaurbot.py.***
```
restartGame() 
while True:  
    print(gameOver())    
```
![gameOver valor](https://github.com/lucasstonehc/dinosaurgame/blob/master/images/gameOver.png)

Com esse processo todo, nossa função principal está totalmente setada e nosso bot pronto para rodar. Agora basta tu executar o arquivo ***dinosaurbot.py.*** e ver a mágica acontecendo. 

## Authors

***Junior Stone *** [JS](https://github.com/lucasstonehc)
***Paulo Henrique *** [PH](https://github.com/PauloHenriqueRCS)

## Licença
Fique à vontade para ESTUDAR!

## Agradecimentos

* Agradecemos ao IFMG pelo Ótimo ensino proporcionado aos Alunos.
