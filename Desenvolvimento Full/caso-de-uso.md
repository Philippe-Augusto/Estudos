# Caso de Uso: Manter Calendário

| <div style="width:290px">Versão</div> | Atividade | Autor | Data |
|:--|:--|:--|:--|
| 1.0 | Versão Inicial do Arquivo | Hamze Jihad | 09/06/2024 |
| 1.1 | Versão revisada do Arquivo com atualização dos IDs das RN | Afonso Ueslei da Fonseca | 10/06/2024 |
| 1.2 | Atualização Revisão Fábrica | Matheus de Azevedo | 17/06/2024 |
| 1.3 | Adição dos protótipos | Flavimar da Silva Almeida | 14/10/2024 |

## **Descrição**
Este caso de uso permite que todos os usuários verifiquem os prazos da Unidade Acadêmica para processos acadêmicos por semestre. Os prazos incluem datas de início e fim para diversos processos acadêmicos. Usuários com perfil de Vice-Diretor também podem criar, editar e excluir calendários acadêmicos.

## **Ator(es)**
Todos os usuários no sistema, com permissões adicionais para Vice-Diretor.

## **Caminho para Acesso à Funcionalidade**
Login >> Calendário

## **Pré-condições**
O usuário deve estar autenticado no sistema com uma conta válida.

## Descrição da(s) Tela(s)

### Tela 1 - Visualizar Calendário

![1](https://github.com/user-attachments/assets/789934fc-f2da-4bc6-a785-c2a89934cee1)

| Nome do Atributo | Preench. Obrigatório | Preench. Automático | Tipo | Máscara | Observações | Regra de Interface |
|:--------------|:----------------:|:--------------:|:--------------|:----------------|:--------------|:----------------|
| Ano/Semestre | x | Sim | Seleção única	  | | Permite filtrar por anos/semestres anteriores	 | [RI01](#regras-de-interface) |
| Data de Início do Semestre Letivo	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Fim do Semestre Letivo		 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Início da Matriz de Demanda de Cursos		 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Fim da Matriz de Demanda de Cursos		 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Início da Matriz de Demanda de Serviços | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Fim da Matriz de Demanda de Serviços	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Início da Matriz de Demanda Global	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Fim da Matriz de Demanda Global	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Início da Matriz de Oferta de Cursos	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Fim da Matriz de Oferta de Cursos	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Início para ajustes na Matriz de Oferta de Cursos	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Fim para ajustes na Matriz de Oferta de Cursos	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Início da Matriz de Oferta de Serviços	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Fim da Matriz de Oferta de Serviços	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Início para ajustes na Matriz de Oferta de Serviços	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Fim para ajustes na Matriz de Oferta de Serviços	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Início da Matriz de Oferta Global	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Fim da Matriz de Oferta Global	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Início para Manifestação de Intenção de Ministrar Componente Curricular	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Fim para Manifestação de Intenção de Ministrar Componente Curricular	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Início para Resolução de Conflitos e Anomalias nas Ofertas de Componentes Curriculares	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Fim para Resolução de Conflitos e Anomalias nas Ofertas de Componentes Curriculares	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Início para Consolidação da Matriz de Demanda Global da Unidade Acadêmica	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Fim para Consolidação da Matriz de Demanda Global da Unidade Acadêmica	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Início para Oferta de Turma no SIGAA	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |
| Data de Fim para Oferta de Turma no SIGAA	 | x | Sim | Data  | | 	 | [RI02](#regras-de-interface)  |

### Tela 2 - Visualizar Calendário (vice-diretor) 

![2](https://github.com/user-attachments/assets/073c2eca-6b71-4f02-931d-84274253cdb6)

| Nome do Atributo | Preench. Obrigatório | Preench. Automático | Tipo | Máscara | Observações | Regra de Interface |
|:--------------|:----------------:|:--------------:|:--------------|:----------------|:--------------|:----------------|
| Cadastrar	 |  |  | Botão  | | 	Somente para Vice-Diretor e Secretário Acadêmico	 | [RI03](#regras-de-interface)  |
| Editar	 |  |  | Botão  | | 	Somente para Vice-Diretor e Secretário Acadêmico	 | [RI03](#regras-de-interface)  |
| Excluir	 |  |  | Botão  | | 	Somente para Vice-Diretor e Secretário Acadêmico	 | [RI03](#regras-de-interface)  |


### Tela 3 - Cadastrar Calendário

![3](https://github.com/user-attachments/assets/6cfa14bf-8d1e-4218-b548-8ad23f2d342a)


| Nome do Atributo | Preench. Obrigatório | Preench. Automático | Tipo | Máscara | Observações | Regra de Interface |
|:--------------|:----------------:|:--------------:|:--------------|:----------------|:--------------|:----------------|
| Ano/Semestre | x | Sim | Seleção única	  | | Permite filtrar por anos/semestres anteriores	 | [RI01](#regras-de-interface) |
| Prazo do Semestre Letivo	 | x | Sim | Intervalo de Data  | | 	 | [RI02](#regras-de-interface)  |
| Prazo da Matriz de Demanda de Cursos		 | x | Sim | Intervalo de Data  | | 	 | [RI02](#regras-de-interface)  |
| Prazo da Matriz de Demanda de Serviços | x | Sim | Intervalo de Data  | | 	 | [RI02](#regras-de-interface)  |
| Prazo da Matriz de Demanda Global	 | x | Sim | Intervalo de Data  | | 	 | [RI02](#regras-de-interface)  |
| Prazo da Matriz de Oferta de Cursos	 | x | Sim | Intervalo de Data  | | 	 | [RI02](#regras-de-interface)  |
| Prazo para ajustes na Matriz de Oferta de Cursos	 | x | Sim | Intervalo de Data  | | 	 | [RI02](#regras-de-interface)  |
| Prazo da Matriz de Oferta de Serviços	 | x | Sim | Intervalo de Data  | | 	 | [RI02](#regras-de-interface)  |
| Prazo para ajustes na Matriz de Oferta de Serviços	 | x | Sim | Intervalo de Data  | | 	 | [RI02](#regras-de-interface)  |
| Prazo da Matriz de Oferta Global	 | x | Sim | Intervalo de Data  | | 	 | [RI02](#regras-de-interface)  |
| Prazo para Manifestação de Intenção de Ministrar Componente Curricular	 | x | Sim | Intervalo de Data  | | 	 | [RI02](#regras-de-interface)  |
| Prazo para Resolução de Conflitos e Anomalias nas Ofertas de Componentes Curriculares	 | x | Sim | DaIntervalo de Datata  | | 	 | [RI02](#regras-de-interface)  |
| Prazo para Consolidação da Matriz de Demanda Global da Unidade Acadêmica	 | x | Sim | Intervalo de Data  | | 	 | [RI02](#regras-de-interface)  |
| Prazo para Oferta de Turma no SIGAA	 | x | Sim | Intervalo de Data  | | 	 | [RI02](#regras-de-interface)  |
| Cadastrar	 |  |  | Botão  | | 	Somente para Vice-Diretor e Secretário Acadêmico	 | [RI04](#regras-de-interface) [RI03](#regras-de-interface)  |


### Tela 4 - Cadastrar Calendário DataPicker colapsado

![4](https://github.com/user-attachments/assets/70246f63-9ee0-4858-b5da-1f2a7ef0ba5f)

| Nome do Atributo | Preench. Obrigatório | Preench. Automático | Tipo | Máscara | Observações | Regra de Interface |
|:--------------|:----------------:|:--------------:|:--------------|:----------------|:--------------|:----------------|


### Tela 5 - Cadastrar Calendário Sucesso

![5](https://github.com/user-attachments/assets/745e0076-92ae-495e-bfe4-bbcd7559cdd0)


| Nome do Atributo | Preench. Obrigatório| Preench. Automático | Tipo | Máscara | Observações | Regra de Interface |
|:--------------|:----------------:|:--------------:|:--------------|:----------------|:--------------|:----------------|
| Mensagem de Sucesso	 |  |  | Alerta  | | 	Somente para Vice-Diretor e Secretário Acadêmico	 | [RI03](#regras-de-interface)  |


### Tela 6 - Editar Calendário

![6](https://github.com/user-attachments/assets/7f32db4d-f0b9-4327-9c52-c37ed4417912)


| Nome do Atributo | Preench. Obrigatório | Preench. Automático | Tipo               | Máscara | Observações | Regra de Interface |
|:--------------|:----------------:|:--------------:|:-------------------|:----------------|:--------------|:----------------|

### Tela 7 - Editar Calendário Sucesso

![7](https://github.com/user-attachments/assets/990bdaa3-fcf0-4b65-b2d6-80ba114f4f8e)


| Nome do Atributo | Preench. Obrigatório | Preench. Automático | Tipo | Máscara | Observações | Regra de Interface |
|:--------------|:----------------:|:--------------:|:--------------|:----------------|:--------------|:----------------|
| Mensagem de Sucesso	 |  |  | Alerta  | | 	Somente para Vice-Diretor e Secretário Acadêmico	 | [RI03](#regras-de-interface)  |

### Tela 8 - Editar ou Cadastrar Calendário Fluxo de exceção

![8](https://github.com/user-attachments/assets/5616077f-0792-4f6d-a504-9e9a2280aeab)


| Nome do Atributo | Preench. Obrigatório | Preench. Automático | Tipo | Máscara | Observações | Regra de Interface |
|:--------------|:----------------:|:--------------:|:--------------|:----------------|:--------------|:----------------|
| Mensagem de erro	 |  |  | Alerta  | | 	Somente para Vice-Diretor e Secretário Acadêmico	 | [RI03](#regras-de-interface)  |


### Tela 9 - Remover Calendário Confirmação

![9](https://github.com/user-attachments/assets/11955edc-7745-4f33-aa19-8c02c1e4169b)


| Nome do Atributo | Preench. Obrigatório | Preench. Automático | Tipo | Máscara | Observações | Regra de Interface |
|:--------------|:----------------:|:--------------:|:--------------|:----------------|:--------------|:----------------|
| Modal de confirmação	 |  |  | Modal  | | 	Somente para Vice-Diretor e Secretário Acadêmico	 | [RI03](#regras-de-interface)  |

 
### Tela 10 - Remover Calendário Sucesso

![10](https://github.com/user-attachments/assets/f001bf52-3809-4445-85a6-4a7525744d5f)


| Nome do Atributo | Preench. Obrigatório | Preench. Automático | Tipo | Máscara | Observações | Regra de Interface |
|:--------------|:----------------:|:--------------:|:--------------|:----------------|:--------------|:----------------|
| Mensagem de Sucesso	 |  |  | Alerta  | | 	Somente para Vice-Diretor e Secretário Acadêmico	 | [RI03](#regras-de-interface)  |

### Tela 11 - Tentativa de Exclusão de Calendário com Datas Definidas

![11](https://github.com/user-attachments/assets/5d721a31-2e02-4461-b133-7cb94580db97)


| Nome do Atributo | Preench. Obrigatório | Preench. Automático | Tipo | Máscara | Observações | Regra de Interface |
|:--------------|:----------------:|:--------------:|:--------------|:----------------|:--------------|:----------------|
| Mensagem de Erro	 |  |  | Alerta  | | 	Somente para Vice-Diretor e Secretário Acadêmico	 | [RI03](#regras-de-interface)  |

* Tipos: Inteiro, Numérico, Alfanumérico, Data, Intervalo de Data , Hora, Botão, Seleção única, Seleção múltipla, Lista

## **Fluxo Principal**
### FP - Visualizar calendário acadêmico atual

| ID | Passo | Fluxo | Regra de Negócio | Tela |
|:--------------|:----------------|:--------------|:----------------|:--------------|
| 1 | O usuário acessa o item 'Calendário'	 |  | | |
| 2 | O sistema exibe as datas de início e fim para os processos acadêmicos do calendário atual	| [FA01](#fa01---criar-calendário-somente-para-vice-diretor) [FA02](#fa02---editar-calendário-somente-para-vice-diretor) [FA03](#fa03---excluir-calendário-somente-para-vice-diretor) | | [1](#tela-1---visualizar-calendário) ou [2](#tela-2---visualizar-calendário-vice-diretor) |
| 3 | O usuário pode filtrar os prazos por anos/semestres anteriores, se necessário		|  | | |


## **Fluxo Alternativo**

### FA01 - Criar Calendário (Somente para Vice-Diretor)

| ID | Passo | Fluxo | Regra de Negócio | Tela |
|:--------------|:----------------|:--------------|:----------------|:--------------|
| 1 | O Vice-Diretor ou Secretário Acadêmico clica no botão 'Criar'	 |  | | |
| 2 | O sistema exibe o formulário para criação de um novo calendário acadêmico		 |  | | [3](#tela-3---cadastrar-calendário)|
| 3 | O Vice-Diretor ou Secretário Acadêmico preenche as datas necessárias		 |  |[RN41](#regras-de-negócio) | |
| 4 | O Vice-Diretor ou Secretário Acadêmico confirma a criação do novo calendário		 | [FEX02](#fex02----cadastro-de-calendário-com-dados-incorretos)  | | |
| 5 | O sistema salva o novo calendário e redireciona a listagem do calendário criado exibindo uma mensagem de sucesso		 |  | |[5](#tela-5---cadastrar-calendário-sucesso) |

### FA02 - Editar Calendário (Somente para Vice-Diretor)

| ID | Passo | Fluxo | Regra de Negócio | Tela |
|:--------------|:----------------|:--------------|:----------------|:--------------|
| 1 | O Vice-Diretor clica no botão 'Editar'	 |  | | |
| 2 | O sistema exibe o formulário de edição do calendário acadêmico selecionado			 |  | | [6](#tela-6---editar-calendário)|
| 3 | O Vice-Diretor faz as alterações necessárias nas datas		 |  | | |
| 4 | O Vice-Diretor confirma as alterações			 | [FEX03](#fex03----edição-de-calendário-com-dados-incorretos) | | |
| 5 | O sistema salva as alterações e edireciona a listagem do calendário criado exibindo uma mensagem de sucesso			 |  | | [7](#tela-7---editar-calendário-sucesso)|

### FA03 - Excluir Calendário (Somente para Vice-Diretor)

| ID | Passo | Fluxo | Regra de Negócio | Tela |
|:--------------|:----------------|:--------------|:----------------|:--------------|
| 1 | O Vice-Diretor clica no botão 'Excluir'		 |  | | |
| 2 | O sistema verifica se o calendário selecionado possui datas definidas				 | [FEX01](#fex01---tentativa-de-exclusão-de-calendário-com-datas-definidas) |[RN40](#regras-de-negócio) | |
| 3 | Se não houver datas definidas, o sistema exibe uma mensagem de confirmação de exclusão			 |  | |[9](#tela-9---remover-calendário-confirmação) |
| 4 | O Vice-Diretor confirma as alterações			 |  | | |
| 5 | O sistema exclui o calendário e exibe uma mensagem de sucesso				 |  | | [10](#tela-10---remover-calendário-sucesso)|

Obs: O fluxo acima nunca irá ocorrer

## **Fluxo Extensão**
### FE01 - Não se aplica

## **Fluxo Exceção**
### FEX01 - Tentativa de Exclusão de Calendário com Datas Definidas

| ID | Passo | Fluxo | Regra de Negócio | Tela |
|:--------------|:----------------|:--------------|:----------------|:--------------|
| 1 | O sistema verifica se o calendário selecionado possui datas definidas	 |  | [RN40](#regras-de-negócio) | | |
| 2 | Como há datas definidas, o sistema exibe uma mensagem de erro informando que a exclusão não é permitida		 |  | |[11](#tela-11---tentativa-de-exclusão-de-calendário-com-datas-definidas)|
| 3 | O Vice-Diretor retorna à lista de calendários		 |  | | |

### FEX02 -  Cadastro de calendário com dados incorretos

| ID | Passo | Fluxo | Regra de Negócio | Tela |
|:--------------|:----------------|:--------------|:----------------|:--------------|
| 1 | O sistema verifica se as datas estão de acordo com as restrições	 |  | [RN42](#regras-de-negócio) | | |
| 2 | Como não está de acordo, o sistema exibe uma mensagem de erro informando que não foi possivel cadastrar o calendário		 |  | |[8](#tela-8---editar-ou-cadastrar-calendário-fluxo-de-exceção)|
| 3 | O Vice-Diretor retorna à lista de calendários		 |  | | |


### FEX03 -  Edição de calendário com dados incorretos

| ID | Passo | Fluxo | Regra de Negócio | Tela |
|:--------------|:----------------|:--------------|:----------------|:--------------|
| 1 | O sistema verifica se as datas estão de acordo com as restrições	 |  | [RN42](#regras-de-negócio) | | |
| 2 |Como não está de acord, o sistema exibe uma mensagem de erro informando que não foi possivel editar o calendário		 |  | |[8](#tela-8---editar-ou-cadastrar-calendário-fluxo-de-exceção)|
| 3 | O Vice-Diretor retorna à lista de calendários		 |  | | |



## Regras de Negócio

| ID | Descrição da Regra |
|:--|:--|
| **RN40** | Um calendário acadêmico não pode ser excluído se houver datas definidas nele. |
| **RN41** | Um calendário acadêmico deve ter datas definidas para todos os processos acadêmicos listados. |
| **RN42** | Os prazos de Matriz de Demanda de Cursos, Matriz de Demanda de Serviços e Matriz de Demanda Global devem ser anteriores aos prazos de Matriz de Oferta de Cursos, Matriz de Oferta de Serviços e Matriz de Oferta Global respectivamente. |

<a name="RI"></a>
## Regras de Interface 

| ID | Descrição da Regra |
|:--|:--|
| **RI01** | Campos não editáveis devem ser exibidos com um fundo cinza claro ou outra indicação visual de que não podem ser modificados. |
| **RI02** | Mensagens de erro devem ser exibidas em vermelho abaixo do campo relevante. |
| **RI03** | A mensagem de confirmação deve ser exibida em verde na parte superior da tela após uma atualização bem-sucedida. |
| **RI04** | O botão 'Cadastrar' deve ser desabilitado até que todas as mudanças obrigatórias sejam feitas. |
