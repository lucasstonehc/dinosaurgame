# Dinosaur Bot
![Eu sou o dino](https://github.com/lucasstonehc/dinosaurgame/blob/master/images/dinoicon.jpg)

One Paragraph of project description goes here
Here we talk about AI like weakness AI

## Iniciando
O projeto visa construir uma inteligência artificial(IA) fraca, que possa realizar as atividades atribuidas a ela. Iremos nesse rápido e didático projeto criar um ***bot*** em ***Python*** para jogar o game do dinochome. 

**Let´s do it!**

### Pré-requesitos

Para criar nosso projeto com sucesso devemos instalar essas bibliotecas.
```
    pip install PyAutoGUI
    pip install Pillow==5.4 and python 3.7
    pip install numpy
```

### Instalando

**Parte 1.**

Uma boa prática de programação em ***Python*** quando se inicia um projeto, é criar para este projeto um ambiente virtual ou em Inglês ***virtual environments***. Quando se cria um ambiente virtual seu projeto logo estará isolado do sistema de diretórios, permitindo que as bibliotecas que tu instala nesse projeto, altere somente este projeto e não os demais projetos que estão presentes na máquina.

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

https://pt.wikipedia.org/wiki/Pip_(gerenciador_de_pacotes)




## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
