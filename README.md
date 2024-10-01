# Sistema Bancário Simples

## Descrição

Este é um sistema bancário simples implementado em Python. O programa simula operações bancárias básicas como depósitos, saques e visualização de extrato. É uma aplicação de console interativa que permite ao usuário realizar múltiplas operações em uma única sessão.

## Funcionalidades

- **Depósito**: Adiciona fundos à conta do usuário.
- **Saque**: Retira fundos da conta do usuário, respeitando o saldo disponível e limites estabelecidos.
- **Extrato**: Exibe um resumo das transações realizadas e o saldo atual.
- **Menu Interativo**: Interface de usuário simples e intuitiva via console.

## Requisitos

- Python 3.6 ou superior

## Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/sistema-bancario-simples.git
   ```
2. Navegue até o diretório do projeto:
   ```
   cd sistema-bancario-simples
   ```

## Como Usar

Execute o script Python no terminal:

```
python sistema_bancario.py
```

Siga as instruções no menu interativo para realizar operações:

- Digite 'd' para Depositar
- Digite 's' para Sacar
- Digite 'e' para ver o Extrato
- Digite 'q' para Sair do programa

## Detalhes de Implementação

### Variáveis Globais

- `saldo`: Armazena o saldo atual da conta.
- `limite`: Define o limite máximo para cada saque (R$ 500,00).
- `extrato`: String que mantém o histórico de transações.
- `numero_saques`: Contador de saques realizados.
- `LIMITE_SAQUES`: Constante que define o número máximo de saques permitidos (3).

### Funções

#### `depositar(saldo, extrato)`

Realiza um depósito na conta.

- Parâmetros:
  - `saldo`: Saldo atual da conta.
  - `extrato`: String contendo o histórico de transações.
- Retorna:
  - Novo saldo e extrato atualizado.

#### `sacar(saldo, extrato, limite, numero_saques, limite_saques)`

Realiza um saque da conta.

- Parâmetros:
  - `saldo`: Saldo atual da conta.
  - `extrato`: String contendo o histórico de transações.
  - `limite`: Valor máximo permitido por saque.
  - `numero_saques`: Número de saques já realizados.
  - `limite_saques`: Número máximo de saques permitidos.
- Retorna:
  - Novo saldo, extrato atualizado e número de saques atualizado.

#### `exibir_extrato(saldo, extrato)`

Exibe o extrato das transações e o saldo atual.

- Parâmetros:
  - `saldo`: Saldo atual da conta.
  - `extrato`: String contendo o histórico de transações.

#### `menu()`

Retorna um dicionário com as opções do menu e suas respectivas funções.

## Limitações e Regras

- O sistema não possui persistência de dados. Todos os dados são perdidos ao encerrar o programa.
- Cada saque está limitado a R$ 500,00.
- São permitidos no máximo 3 saques por sessão.
- Não são permitidos saques ou depósitos de valores negativos ou zero.

## Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.
