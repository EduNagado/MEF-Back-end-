# MEF Back-end
Um sistema interativo que gerencia contas de usuários, cadastro de veículos e oferece suporte por meio de um assistente virtual para relatar problemas. Criado em Python, o projeto utiliza validações robustas para garantir a segurança e consistência dos dados.

## Funcionalidades

- **Gerenciamento de Contas**:
  - Criar conta com validação de nome, e-mail e senha.
  - Login utilizando nome completo ou e-mail.
  - Exibição de contas cadastradas.

- **Gerenciamento de Veículos**:
  - Adicionar, modificar, remover e exibir veículos com informações detalhadas.

- **Assistente Virtual**:
  - Relatar problemas.
  - Interagir com perguntas ao assistente (em desenvolvimento).

## Estrutura do Menu

### Menu Principal
1. Criar uma conta.
2. Entrar na conta.
3. Relatar um problema ou conversar com o assistente.
4. Exibir contas.
5. Sair.

### Menu Secundário (Acessível após login)
1. Adicionar veículo.
2. Modificar veículo.
3. Remover veículo.
4. Exibir veículos.
5. Voltar ao menu principal.

## Validações Implementadas
- **E-mail**: Formato padrão com domínio e extensão válidos.
- **Nome**: Apenas caracteres alfabéticos, incluindo acentos e espaços.
- **Senha**: Mínimo de 8 caracteres, contendo pelo menos uma letra maiúscula, uma letra minúscula e um número.

## Tecnologias Utilizadas
- Linguagem: Python.
- Validações com Expressões Regulares (`re`).
- Entrada e saída de dados interativa no terminal.

## Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/vehicle-assistant.git
   cd vehicle-assistant
