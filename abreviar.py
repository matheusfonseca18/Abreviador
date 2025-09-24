import unicodedata


# tira os espaços exedentes
def limpar_espacos(frase):
    frase = frase.split()

    return ' '.join(frase)


# tira preposições
def limpar_preposicoes(frase):
    prep = {'A', 'E', 'O', 'AS', 'OS', 'DA', 'DE', 'DO', 'DAS', 'DOS'}
    palavras = frase.split()
    filtrada = []
    for p in palavras:
        if p not in prep:
            filtrada.append(p)

    if not filtrada:
        return ' '.join(palavras)

    return ' '.join(filtrada)


# tira os acentos
def limpar_acento(frase):
    frase_sem_acento = unicodedata.normalize('NFD', frase)
    frase_sem_acento = ''.join(especial for especial in frase_sem_acento
                               if unicodedata.category(especial) != 'Mn')

    return frase_sem_acento.upper()


# tira o caracteres especiais
def limpar_especial(frase):
    frase_limpa = ''

    for c in frase:
        if c.isalnum() or c.isspace():
            frase_limpa += c

    palavras = frase_limpa.split()
    frase_normal = ' '.join(palavras)

    return frase_normal.upper()


# conta os caracteres
def contar(frase):
    separar_Palavras = frase.split()
    quantidade_Palavras = len(separar_Palavras)
    espacos = quantidade_Palavras-1
    total_Caracteres = 0

    for i in range(quantidade_Palavras):
        caracteres = len(separar_Palavras[i])
        total_Caracteres += caracteres

    return total_Caracteres+espacos


# encontra a maior palavra
def maior_palavra(frase):
    palavras = frase.split()
    return max(palavras, key=len)


# verifica se em alguma palavra blindada e encontra a maior palavra
def maior_palavra_versao(frase):
    blindadas = ['GLOBO', 'SBT', 'RECORD', 'REDETV', 'BAND', 'CULTURA',
                 'ESPN', 'SPORTV', 'TNT', 'MAT', 'VES', 'NOT', 'MAD', 'FUT', 'BOLETIM']

    palavras = frase.split()

    palavras_nao_blindadas = [p for p in palavras if p not in blindadas]

    if palavras_nao_blindadas:
        return max(palavras_nao_blindadas, key=len)

    return None


# abrevia a palavra sempre terminando em uma consoante
def abreviar(palavra):
    vogais = "AEIOU"
    n = len(palavra)

    for i in range(n-1, -1, -1):
        letra = palavra[i]
        if letra not in vogais and any(ch in vogais for ch in palavra[i+1:]):
            return palavra[:i+1]

    for i in range(n-2, -1, -1):
        if palavra[i] not in vogais:
            return palavra[:i+1]

    return palavra


# abrevia a marca
def abreviar_marca(frase):
    frase = limpar_espacos(frase)
    frase = limpar_acento(frase)
    frase = limpar_especial(frase)
    tamanho = contar(frase)

    if tamanho > 30:
        nova = limpar_preposicoes(frase)
        if nova != frase:
            frase = nova
            tamanho = contar(frase)

    palavras = frase.split()
    primeira = palavras[0]

    while tamanho > 30:

        palavra = maior_palavra(frase)

        if palavra == primeira and contar(frase) > 30:
            palavas_temp = frase.split()
            candidatas = [p for p in palavas_temp if p != primeira]
            if not candidatas:
                palavra = primeira
            else:
                palavra = max(candidatas, key=len)

        palavra_abrev = abreviar(palavra)
        frase = frase.replace(palavra, palavra_abrev, 1)
        tamanho = contar(frase)

        if palavra_abrev == palavra:
            break

    return frase


 # abrevia a versão
def abreviar_versao(frase):
    frase = limpar_espacos(frase)
    frase = limpar_acento(frase)
    frase = limpar_especial(frase)
    tamanho = contar(frase)

    while tamanho > 30:
        palavra = maior_palavra_versao(frase)

        if not palavra:
            break

        palavra_abrev = abreviar(palavra)

        if palavra_abrev == palavra:
            break

        palavras = frase.split()
        for i, p in enumerate(palavras):
            if p == palavra:
                palavras[i] = palavra_abrev
                break
        frase = ' '.join(palavras)

        tamanho = contar(frase)

        if tamanho > 30:
            palavras = frase.split()
            trocou = False
            for i, p in enumerate(palavras):
                if p == 'BOLETIM':
                    palavras[i] = 'BOL'
                    trocou = True
                    break
            if trocou:
                frase = ' '.join(palavras)

    return frase


# formata o anunciante
def anunciante(frase):
    frase = limpar_espacos(frase)
    frase = limpar_acento(frase)

    return frase.title()
