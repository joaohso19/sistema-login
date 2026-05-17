<h1>SISTEMA DE LOGIN - RELATÓRIO</h1>  

### 1. Criação e Configuração da Máquina Virtual
<img width="367" height="60" alt="image" src="https://github.com/user-attachments/assets/7994715d-af32-4643-a605-32fcc675c24c" />

---

<img width="636" height="304" alt="image" src="https://github.com/user-attachments/assets/1eed4eee-9c31-4739-9fdb-8aa9d80cd235" />

---

### 2. Redirecionamento de Portas (Port Forwarding) no NAT
Para permitir que a máquina real (Host) consiga acessar os serviços internos da VM (Guest) rodando em rede NAT, configurou-se uma regra de redirecionamento:
* **Serviço:** SSH
* **Protocolo:** TCP
* **IP do Hospedeiro:** `127.0.0.1`
* **Porta do Hospedeiro:** `2222`
* **Porta do Convidado:** `22`
<img width="1277" height="801" alt="image" src="https://github.com/user-attachments/assets/55a93a94-5bed-4e62-9e7e-f127190bc4c7" />

---

<img width="636" height="304" alt="image" src="https://github.com/user-attachments/assets/8b6108e8-b773-4409-9503-f67151c70b72" />

---

### 3. Configuração do SSH e Firewall no Ubuntu
Dentro do ambiente Ubuntu, foram executados os seguintes comandos via terminal para atualizar o sistema, instalar o servidor SSH e liberar as portas necessárias no firewall:

Instalação do Servidor OpenSSH:
<img width="489" height="108" alt="image" src="https://github.com/user-attachments/assets/bbb2f8a0-fda6-47ce-abac-c397677baced" />

---

O serviço foi iniciado e o seu estado foi verificado com o utilitário systemctl, confirmando que o SSH estava ativo (active (running)) e a escutar na porta 22.
<img width="487" height="319" alt="image" src="https://github.com/user-attachments/assets/daa27af1-cd49-4eef-9843-f9eb5f10baaf" />

---

Para permitir o tráfego da aplicação Web que seria executada posteriormente, liberou-se a porta 8000/tcp no firewall nativo do Linux (UFW) e o serviço foi ativado:
<img width="815" height="462" alt="image" src="https://github.com/user-attachments/assets/44408345-de9f-408b-84a3-4660fa999594" />

---

### 4. Teste de Conexão SSH via Prompt de Comando (Host)
Para validar se o redirecionamento de portas e o serviço SSH estavam operantes, realizou-se o acesso através do Prompt de Comando do Windows (Host) apontando para a porta configurada (2222):
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/e58bccba-ed17-4d33-afa9-079a88a90b4a" />

---

### 5. Desenvolvimento e Integração com o VS Code (Remote - SSH)

Utilizando a extensão Remote - SSH do Visual Studio Code no Windows, conectou-se diretamente ao ambiente da máquina virtual.

O primeiro passo foi abrir o Visual Studio Code na máquina real (Windows) e usar a extensão Remote - SSH para se conectar à máquina virtual.

    No topo do VS Code, foi inserido o comando de conexão: ssh -p 2222 user@127.0.0.1.

    Esse comando diz ao VS Code para se conectar ao IP local (127.0.0.1) na porta 2222

    O VS Code então inicializou o VS Code Server dentro do Ubuntu. Isso permite que você edite arquivos e rode comandos na VM usando a interface gráfica do seu Windows.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/5f3c39dd-f948-4ffe-92f4-5b0e870503a6" />

---

O **VS Code Server** foi inicializado automaticamente dentro do Ubuntu, permitindo o gerenciamento do sistema de arquivos `/home/user/` de forma gráfica e integrada.
<img width="947" height="1079" alt="image" src="https://github.com/user-attachments/assets/e8135cb3-b83b-4065-85ff-6e9dfaaf9f6e" />

---

A pasta contendo o projeto pré-existente SISTEMA-LOGIN foi transferida diretamente da máquina real para o ambiente virtualizado do Ubuntu através da funcionalidade de arrastar e soltar (drag-and-drop) da interface gráfica do VS Code.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/9868e142-83b7-4ea5-b567-9a464021a22f" />

---

Utilizando o terminal integrado do VS Code (conectado via SSH à VM), navegou-se até à pasta do projeto e instalou-se o framework Flask:
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/ac34b92b-fa1d-4b1b-94c1-b577e2b734d7" />

---

Dentro do diretório do projeto na VM, o script em Python foi colocado em execução, fazendo o acesso do Sistema Login via VM Ubunte
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/f5d1742e-d3e0-4612-9f16-a29a2ad1ad68" />

---

## DESAFIO

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/a2af2496-812b-4120-8ab6-1f7e67a0cae4" />

---

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/f2d0a2fb-0787-4efb-a985-fa9f8fbfa26b" />



