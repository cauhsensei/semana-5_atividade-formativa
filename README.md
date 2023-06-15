# Atividade realizada por: Cauane Cardoso da Rosa
## Curso: Análise e Desenvolvimento de Sistemas

## Desenvolvimento da Atividade Formativa referente a Semana 5.

### Proposta da Atividade:

- Ao incluir, listar ou editar um estudante, as seguintes informações devem ser utilizadas:
  - Código do estudante (Número inteiro).
  - Nome do estudante (String).
  - CPF do estudante (String).

- Os dados do estudante devem ser armazenados em um dicionário ou tupla, que por sua vez, devem ser adicionados à uma lista.

    - ANTES: lista de nomes de estudantes, onde cada posição da lista é uma string equivalente ao nome do estudante
      ```
      ["Lucas", "Pedro"]
      ```

    - AGORA: lista de estudantes, onde cada posição da lista é um dicionário ou uma tupla, representando os dados do estudante (e exemplo abaixo utiliza dicionário)
      ```
      [ 
        {"codigo": 1, "nome": "Lucas", "cpf": "999"}, 
        {"codigo": 2, "nome": "Pedro", "cpf": "555"} 
      ]
      ```

- Desenvolver a funcionalidade de excluir um estudante, onde deve ser perguntado ao usuário qual o código do estudante que ele deseja excluir, para então remover o estudante correspondente da lista. Lembre-se que você deve percorrer a lista e encontrar uma tupla ou dicionário que contenha o código igual ao informado, e então excluir esta estrutura da lista.

- Desenvolver a funcionalidade de editar um estudante, onde deve ser perguntado ao usuário o código do estudante que se deseja editar, e então realizar a entrada dos dados correspondentes a todos dados do estudante (código, nome e cpf). Após isso, estes dados devem ser atualizados no dicionário ou tupla correspondente dentro da lista de estudantes.
