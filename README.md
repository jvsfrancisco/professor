# Como utilizar

No diretório imediatamente acima do seu módulo, execute:

`git clone https://github.com/jvsfrancisco/professor`

Depois você pode utilizar as funções de turma com o import:

```Python
from .. import aluno

turma.get_professor(2)
```

**OBS:** Para utilizar imports relativos, seu módulo também precisa fazer parte de um package, ou seja, o diretório do módulo deve possuir um arquivo `__init__.py` assim como o nosso.

Alternativamente, se o diretório acima do seu módulo também for um repositório, como o principal, você pode adicionar turma como submódulo:

`git submodule add https://github.com/jvsfrancisco/professor`

## Dependências

Python 3.9+

# Documentação adicional

## get_professor

Recebe o id de um professor e retorna uma tupla com o código da operação e os dados do professor. Caso o professor não seja encontrado, retorna um erro.

```Python
professor.get_professor(1)

#Retorno
(0, {
    "id": 1,
    "nome": "João",
    "filiais": ["Centro", "Tijuca"],
    "horarios": [8,12]
    "cursos": ['matematica', 'fisica']
})

```

## add_professor

Adiciona um professor à lista de professores. Retorna uma tupla com o código da operação e os dados do Professor Adicionado.


```Python
professor.add_professor("João", 
["Centro", "Tijuca"], [8,12], 
['matematica', 'fisica'])

```

## add_curso

Recebe o id de um professor e um curso.
Adiciona o curso à lista de cursos do professor se o curso não existir na lista.
Caso o curso já exista, retorna um erro.

```Python
professor.add_curso(1, "quimica")

```

## del_curso

Recebe o id de um professor e um curso.
Remove o curso da lista de cursos do professor se o curso existir na lista.
Caso o curso não exista, retorna um erro.

```Python
professor.del_curso(1, "fisica")

```

## set_horario

Recebe o id de um professor e um horário de início e fim.
Atualiza o horário do professor com o horário passado.

```Python
professor.set_horario(1, 10, 14)

```

## add_filial

Adiciona uma filial à lista de filiais do professor.
Caso a filial já exista na lista, retorna FILIAL_JA_ADICIONADA.

```Python
professor.add_filial(1, "Barra")

```

## del_filial

Remove a filial da lista de filiais do professor, caso ela exista.
Caso a filial não exista, retorna um erro.

```Python
professor.del_filial(1, "Tijuca")

```

## get_professores

Retorna uma cópia da lista de professores

```Python
professor.get_professores()

#Retorno
[
    {
        "id": 1,
        "nome": "João",
        "filiais": ["Centro", "Tijuca"],
        "horarios": [8,12]
        "cursos": ['matematica', 'fisica']
    },
    {
        "id": 2,
        "nome": "Maria",
        "filiais": ["Barra", "Tijuca"],
        "horarios": [10,14]
        "cursos": ['quimica', 'fisica']
    }
]

```