
# 🧑‍🎓 Exercício: Implementação de um CRUD para Alunos com FastAPI

Implemente uma API RESTful para gerenciar um cadastro de **alunos** utilizando o FastAPI. A API deve conter todas as operações básicas de CRUD (Create, Read, Update e Delete), com os seguintes requisitos:

#### 📄 Estrutura da Entidade

A entidade **Aluno** deve conter os seguintes campos:

* `id`: int (gerado automaticamente)
* `nome`: str
* `sobrenome`: str
* `cpf`: str
* `data_nascimento`: str ou `datetime` (você pode escolher o tipo, mas seja consistente)

Você deve utilizar `@dataclass` para definir as seguintes classes:

* `Aluno`: representa o aluno completo, incluindo o campo `id`.
* `AlunoCadastro`: usada para receber dados ao cadastrar um novo aluno (sem o campo `id`).
* `AlunoEditar`: usada para editar os dados de um aluno existente (sem o campo `id`).

---

#### 📌 Requisitos da API

##### ✅ `GET /api/alunos`

* Deve retornar uma lista com todos os alunos cadastrados.
* **Status de resposta**: `200 OK`

##### ✅ `GET /api/alunos/{id}`

* Deve retornar o aluno correspondente ao `id` informado.
* Caso o aluno não seja encontrado, retorne um erro.
* **Status de resposta**:

  * `200 OK` se encontrado
  * `404 Not Found` se não encontrado

##### ✅ `POST /api/alunos`

* Deve cadastrar um novo aluno com os dados enviados no corpo da requisição.
* O campo `id` deve ser gerado automaticamente.
* **Status de resposta**: `200 OK`

##### ✅ `PUT /api/alunos/{id}`

* Deve atualizar os dados do aluno com o `id` correspondente, usando os dados enviados no corpo da requisição.
* Utilize um loop (`for`) para localizar o aluno.
* Caso o aluno não seja encontrado, retorne um erro.
* **Status de resposta**:

  * `200 OK` se atualizado com sucesso
  * `404 Not Found` se o aluno não for encontrado

##### ✅ `DELETE /api/alunos/{id}`

* Deve remover o aluno correspondente ao `id` informado.
* Caso o aluno não seja encontrado, retorne um erro.
* **Status de resposta**:

  * `204 No Content` se excluído com sucesso
  * `404 Not Found` se não encontrado


# Outros exercícios

## Enunciado: Cálculo do Total de Venda de um Produto (Sem Validações)

Implemente um endpoint HTTP usando o método **GET** que receba as informações de um produto via query params, calcule o valor total da venda e retorne o resultado em JSON, sem nenhuma validação extra e usando apenas estruturas condicionais (`if`/`else`).

1. **Endpoint**

   ```
   /calcular-total-produto
   ```

2. **Query params**

   * `nome` (string) – nome do produto
   * `quantidade` (inteiro) – número de unidades
   * `preco` (número) – preço unitário em reais

3. **Processamento**

   * Calcule o total:

     ```
     total = quantidade * preco
     ```
   * Arredonde `total` para duas casas decimais.

4. **Resposta**

   * Retornar HTTP **200** com objeto JSON:

     ```json
     {
       "nome": "Caneta Azul",
       "quantidade": 10,
       "precoUnitario": 2.50,
       "total": 25.00
     }
     ```

> **Observação:** não implemente nenhuma verificação de parâmetros — assuma que `nome`, `quantidade` e `preco` sempre serão fornecidos corretamente.


## Enunciado 02: Escolha de Combustível Econômico

Crie um endpoint `/calcular-combustivel` HTTP usando método GET que receba dois parâmetros de consulta (query params):

* `gasolina` (número, preço por litro da gasolina)
* `alcool` (número, preço por litro do álcool)

O endpoint deve:

1. **Validar** que ambos os preços são números positivos; se não, retornar HTTP 400 com mensagem de erro em JSON.
2. **Comparar** o custo‐benefício usando apenas estruturas `if` / `else if` / `else`:

   * Se `alcool <= gasolina * 0.7`, escolher **álcool**.
   * Caso contrário, escolher **gasolina**.
3. **Retornar** um objeto JSON com o formato:

   ```json
   { "abastecer": "<combustível>" }
   ```

   onde `<combustível>` é `"álcool"` ou `"gasolina"`.

**Exemplos de resposta:**

* Para `?gasolina=5.20&alcool=3.50` →

  ```json
  { "abastecer": "álcool" }
  ```
* Para `?gasolina=5.20&alcool=4.00` →

  ```json
  { "abastecer": "gasolina" }
  ```

## Enunciado 03: Calculadora de Média e Status do Aluno

Implemente um endpoint HTTP usando o método **GET** que receba três notas de um aluno via query params, calcule a média aritmética e retorne o status de aprovação em JSON, sem usar nenhum banco de dados e apenas com estruturas condicionais (`if`/`else if`/`else`).

1. **Endpoint**

   ```
   /calcular-media
   ```

2. **Query params**

   * `nota1` (número, de 0 a 100)
   * `nota2` (número, de 0 a 100)
   * `nota3` (número, de 0 a 100)


3. **Cálculo da média**

   * Média simples:

     ```
     media = (nota1 + nota2 + nota3) / 3
     ```
   * Arredonde `media` para duas casas decimais.

4. **Determinação de status**

   * Se `media` ≥ 70 → **“Aprovado”**
   * Se 50 ≤ `media` < 70 → **“Em recuperação”**
   * Se `media` < 50 → **“Reprovado”**

5. **Resposta de sucesso**

   * Retornar HTTP **200** com objeto JSON:

     ```json
     {
       "nota1": 85,
       "nota2": 76,
       "nota3": 90,
       "media": 83.67,
       "status": "Aprovado"
     }
     ```
