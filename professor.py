__all__ = ['inicializar', 'finalizar', 'get_professor', 'add_professor', 'add_curso', 'del_curso', 'set_horario', 'add_filial', 'del_filial', 'get_professores']

import json, copy, atexit

# Professor:
#   id: int,
#   nome: str,
#   filiais: list[int],
#   horario: tup[ini: int, fim: int]
#   cursos: list[str]

# Variáveis globais
_NEXT_ID = 1
_JSON_FILE_PATH = 'data/professor.json'
professores = []

# Códigos de erro
OPERACAO_REALIZADA_COM_SUCESSO = 0
ARQUIVO_NAO_ENCONTRADO = 30
ARQUIVO_EM_FORMATO_INVALIDO = 31
ERRO_NA_ESCRITA_DO_ARQUIVO = 32
PROFESSOR_NAO_ENCONTRADO = 17
FILIAL_JA_ADICIONADA = 18
FILIAL_NAO_EXISTENTE = 19
CURSO_JA_ADICIONADO = 20
CURSO_NAO_EXISTENTE = 21
HORARIO_INVALIDO = 22



def inicializar() -> int:
    '''
    Inicializa a lista de professores com os dados do arquivo JSON.
    '''
    global professores

    try:
        with open(_JSON_FILE_PATH, 'r') as arquivo:
            try:
                professores = json.load(arquivo)
            except json.JSONDecodeError:
                return ARQUIVO_EM_FORMATO_INVALIDO
    except FileNotFoundError:
        return ARQUIVO_NAO_ENCONTRADO

    return OPERACAO_REALIZADA_COM_SUCESSO

def finalizar() -> int:
    '''
    Faz um dump da lista de professores em um arquivo JSON.
    '''
    try:
        with open(_JSON_FILE_PATH, 'w') as arquivo:
            json.dump(obj=professores, fp=arquivo, indent=2)
    except OSError:
        return ERRO_NA_ESCRITA_DO_ARQUIVO

    return OPERACAO_REALIZADA_COM_SUCESSO

def get_professor(id_professor: int) -> tuple[int, dict]:
    '''
    Recebe o id de um professor e retorna uma tupla com o código da operação e os dados do professor.
    Caso o professor não seja encontrado, retorna um erro.
    '''
    for professor in professores:
        if professor['id'] == id_professor:
            return OPERACAO_REALIZADA_COM_SUCESSO, copy.deepcopy(professor)

    return PROFESSOR_NAO_ENCONTRADO, None  # Professor não encontrado

def add_professor(nome: str, filiais: list[str], horario: tuple[str, str], cursos: list[str]) -> tuple[int, int]:
    '''
    Adiciona um professor à lista de professores.
    Retorna uma tupla com o código da operação e os dados do Professor Adicionado.

    '''

    id = _gerar_id()

    professores.append({
        'id': id,
        'nome': nome,
        'filiais': filiais,  
        'horario': horario,
        'cursos': cursos,
    })

    return OPERACAO_REALIZADA_COM_SUCESSO, get_professor(id)[1]

def _gerar_id() -> int:
    global _NEXT_ID
    id_atual = _NEXT_ID
    _NEXT_ID += 1
    return id_atual

def add_curso(id_professor: int, curso: str) -> tuple[int, dict]:
    '''
    Recebe o id de um professor e um curso.
    Adiciona o curso à lista de cursos do professor se o curso não existir na lista.
    Caso o curso já exista, retorna um erro.
    '''
    professor = get_professor(id_professor)
    if professor[0] != OPERACAO_REALIZADA_COM_SUCESSO:
        return professor
    if curso in professor[1]['cursos']:
        return CURSO_JA_ADICIONADO, 'O curso já existe na lista de cursos do professor.'
    professor[1]['cursos'].append(curso)
    return OPERACAO_REALIZADA_COM_SUCESSO, copy.deepcopy(professor[1])

def del_curso(id_professor: int, curso: str) -> tuple[int, dict]:
    '''
    Recebe o id de um professor e um curso.
    Remove o curso da lista de cursos do professor se o curso existir na lista.
    Caso o curso não exista, retorna um erro.
    '''
    professor = get_professor(id_professor)
    if professor[0] != OPERACAO_REALIZADA_COM_SUCESSO:
        return professor[0]
    if curso not in professor[1]['cursos']:
        return CURSO_NAO_EXISTENTE, 'Não é possível realiza a operação pois o curso não existe na lista de cursos do professor.'
    professor[1]['cursos'].remove(curso)
    return OPERACAO_REALIZADA_COM_SUCESSO, copy.deepcopy(professor[1])

def set_horario(id_professor: int, ini: int, fim: int) -> tuple[int, dict]:
    '''
    Recebe o id de um professor e um horário de início e fim.
    Atualiza o horário do professor com o horário passado.
    '''
    professor = get_professor(id_professor)
    if professor[0] != OPERACAO_REALIZADA_COM_SUCESSO:
        return professor[0]
    if ini >= fim:
        return HORARIO_INVALIDO, 'O horário de início deve ser menor que o horário de fim.'
    if ini[:2] < 0 or ini > 24[:2] or fim[:2] < 0 or fim[:2] > 24:
        return HORARIO_INVALIDO, 'O horário de início e fim deve estar entre 0 e 24.'
    if ini[2:] < 0 or ini[2:] > 59 or fim[2:] < 0 or fim[2:] > 59:
        return HORARIO_INVALIDO, 'Os minutos devem estar entre 0 e 59.'
    professor[1]['horario'] = ini, fim
    return OPERACAO_REALIZADA_COM_SUCESSO, copy.deepcopy(professor[1])

def add_filial(id_professor: int, filial: str) -> tuple[int, dict]:
    '''
    Adiciona uma filial à lista de filiais do professor.
    Caso a filial já exista na lista, retorna FILIAL_JA_ADICIONADA.

    '''
    professor = get_professor(id_professor)
    if professor[0] != OPERACAO_REALIZADA_COM_SUCESSO:
        return professor[0]
    if filial in professor[1]['filiais']:
        return FILIAL_JA_ADICIONADA, 'A filial já existe na lista de filiais do professor.'
    professor[1]['filiais'].append(filial)
    return OPERACAO_REALIZADA_COM_SUCESSO, copy.deepcopy(professor[1])

def del_filial(id_professor: int, filial: str) -> tuple[int, dict]:
    '''
    Remove a filial da lista de filiais do professor, caso ela exista.
    Caso a filial não exista, retorna um erro.
    
    '''
    professor = get_professor(id_professor)
    if professor[0] != OPERACAO_REALIZADA_COM_SUCESSO:
        return professor[0]
    if filial not in professor[1]['filiais']:
        return FILIAL_NAO_EXISTENTE, 'Não é possível realiza a operação pois a filial não existe na lista de filiais do professor.'
    professor[1]['filiais'].remove(filial)
    return OPERACAO_REALIZADA_COM_SUCESSO, copy.deepcopy(professor[1])

def get_professores() -> tuple[int, list[dict]]:
    '''
    Retorna uma cópia da lista de professores.
    '''
    return OPERACAO_REALIZADA_COM_SUCESSO, copy.deepcopy(professores)

inicializar()
atexit.register(finalizar)
