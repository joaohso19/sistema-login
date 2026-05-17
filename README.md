<h1>SISTEMA DE LOGIN - RELATÓRIO</h1>  

### 1. Criação e Configuração da Máquina Virtual
<img width="367" height="60" alt="image" src="https://github.com/user-attachments/assets/7994715d-af32-4643-a605-32fcc675c24c" />
<img width="636" height="304" alt="image" src="https://github.com/user-attachments/assets/1eed4eee-9c31-4739-9fdb-8aa9d80cd235" />

### 2. Redirecionamento de Portas (Port Forwarding) no NAT
Para permitir que a máquina real (Host) consiga acessar os serviços internos da VM (Guest) rodando em rede NAT, configurou-se uma regra de redirecionamento:
* **Serviço:** SSH
* **Protocolo:** TCP
* **IP do Hospedeiro:** `127.0.0.1`
* **Porta do Hospedeiro:** `2222`
* **Porta do Convidado:** `22`
<img width="1277" height="801" alt="image" src="https://github.com/user-attachments/assets/55a93a94-5bed-4e62-9e7e-f127190bc4c7" />
<img width="636" height="304" alt="image" src="https://github.com/user-attachments/assets/8b6108e8-b773-4409-9503-f67151c70b72" />


### 3. Configuração do SSH e Firewall no Ubuntu
Dentro do ambiente Ubuntu, foram executados os seguintes comandos via terminal para atualizar o sistema, instalar o servidor SSH e liberar as portas necessárias no firewall:
<img width="491" height="302" alt="image" src="https://github.com/user-attachments/assets/31262cd0-28c4-424b-b601-3e44fc2b4bb0" />
<img width="489" height="108" alt="image" src="https://github.com/user-attachments/assets/bbb2f8a0-fda6-47ce-abac-c397677baced" />
<img width="487" height="319" alt="image" src="https://github.com/user-attachments/assets/daa27af1-cd49-4eef-9843-f9eb5f10baaf" />
<img width="815" height="462" alt="image" src="https://github.com/user-attachments/assets/44408345-de9f-408b-84a3-4660fa999594" />

### 4. Teste de Conexão SSH via Prompt de Comando (Host)
Para validar se o redirecionamento de portas e o serviço SSH estavam operantes, realizou-se o acesso através do Prompt de Comando do Windows (Host) apontando para a porta configurada (2222):
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/e58bccba-ed17-4d33-afa9-079a88a90b4a" />

### 5. Desenvolvimento e Integração com o VS Code (Remote - SSH)

Utilizando a extensão Remote - SSH do Visual Studio Code no Windows, conectou-se diretamente ao ambiente da máquina virtual.

O primeiro passo foi abrir o Visual Studio Code na sua máquina real (Windows) e usar a extensão Remote - SSH para se conectar à máquina virtual.

    No topo do VS Code, foi inserido o comando de conexão: ssh -p 2222 user@127.0.0.1.

    Esse comando diz ao VS Code para se conectar ao IP local (127.0.0.1) na porta 2222

    O VS Code então inicializou o VS Code Server dentro do Ubuntu. Isso permite que você edite arquivos e rode comandos na VM usando a interface gráfica do seu Windows.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/33045d0d-d322-44dc-9a41-0d4d267bcbb5" />
Navegação no Sistema de Arquivos do Ubuntu

Após autenticar a conexão com a senha do usuário da VM, o VS Code abriu o diretório raiz do usuário do Ubuntu: /home/user/.

    Na interface, foi possível visualizar todas as pastas padrão do Linux (Área de Trabalho, Documentos, Downloads, .ssh, .vscode-server, etc.) diretamente pelo explorador de arquivos do Windows.

    A partir daí, foi criada uma pasta dedicada para o projeto chamada SISTEMA-LOGIN.

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/a0ce29d4-2dde-4501-b493-8c5d49051291" />
Preparação do Ambiente e Instalação do Flask

Com a pasta do projeto criada, você abriu o terminal integrado do VS Code. Esse terminal não é o CMD do Windows, mas sim o próprio Bash do Ubuntu rodando remotamente.

    Dentro da pasta SISTEMA-LOGIN, foi executado o comando para instalar o framework web do Python: sudo apt install python3-flask
    Esse comando preparou a VM com as dependências necessárias para rodar servidores HTTP baseados em Python.

<img width="947" height="1079" alt="image" src="https://github.com/user-attachments/assets/5e6ae146-fa9c-42d4-b05a-fd83893bc0a2" />
Preparação do Ambiente e Instalação do Flask

Com a pasta do projeto criada, você abriu o terminal integrado do VS Code. Esse terminal não é o CMD do Windows, mas sim o próprio Bash do Ubuntu rodando remotamente.

    Dentro da pasta SISTEMA-LOGIN, foi executado o comando para instalar o framework web do Python: sudo apt install python3-flask
    Esse comando preparou a VM com as dependências necessárias para rodar servidores HTTP baseados em Python.

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/7b8a2688-ecb3-4d55-89d6-7ed83935dbdc" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/32bd9f31-7147-40f6-bf1b-fe6f6f059805" />



