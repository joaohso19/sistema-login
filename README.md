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
