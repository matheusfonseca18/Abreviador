<h1 align="center" style="font-weight: bold;">Abreviador ✂️</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"/>
</p>


<p align="center">
 <a href="#tech">Technologies</a> • 
 <a href="#abaout">Sobre</a> • 
  <a href="#use">Como usar</a> •
  <a href="#regras">Regras</a> •
</p>

<h2 id="tech">💻 Technologias</h2>

- Python
- Biblioteca UnicodeData
- CustomTKinter

<h2 id="abaout">📌 Sobre</h2>

<h3>O que faz</h3>

O Abreviador é uma aplicação feita em **Python** para auxiliar na formatação de textos de **Anunciantes, Marcas e Versões**.  

O programa aplica <a href="#regras">regras</a> específicas de abreviação, remoção de acentos, espaços e caracteres especiais, deixando o texto pronto para uso imediato (já copiado para a área de transferência).

<h3>Qual problema resolve?</h3>

Temos uma base onde diariamente são injetados diversos dados cadastrados por diversas pessoas, esses dados podem ser **anunciante, marca ou versão**.

São pessoas cadastrando esses dados, que devem seguir um padrão para não serem duplicados. Porém abre precedente para interpretações, e isso acaba duplicando os dados na base. O foco do programa é acabar com essas interpretações.

<h4>Exemplo:</h4>

Seguindo as <a href="#regras">regras</a> o dado pode ter até 30 caracteres, contado com os espaços. Então o dado é **"Chapeuzinho Vermelho e o Lobo Bibi Ferreira"**, que possui 43 caracteres. Cada interpretação pode gerar um abreviação diferente, **"Chap Verm Lobo Bibi Ferreira"** ou **"Chapeuzin Vermel Lob Bibi Fer"**.

O programa terá apenas uma interpretação desse exemplo, **"Chapeuzinho V Lobo Bibi Ferr"**.

<h2 id="use">❓ Como usar</h2>

O programa possui 3 entradas de dados, Anunciante, Marca e Versão. Cada entrada tem suas <a href="#regras">regras</a> distintas.

Digite ou cole seu dado no campo correto, clique no botão "Formatar", e pronto!

Seu dado já estará no formato correto, aparecerá no campo abaixo da entrada, “Seu texto aparecerá aqui“ e no seu **CTRL + V**.

<h2 id="regras">📋 Regras</h2>

<h3>Funcionam em todos os campos</h3>

- Remove espaços excedentes, começo, meio e fim
- Remove todos os acentos
- Remove todos os caracteres especiais

<h3>Campo de Anunciante</h3>

- Formata a frase, primeira letra de cada palavra em maiúscula
- Não possui limite de caracteres

<h3>Campo de Marca</h3>

- Limite de 30 caracteres
- Abreviação sempre termina em consoante
- Formata a frase em maiúsculo
- Remove preposições
- Busca manter a marca principal (primeira palavra) integra, abrevia apenas se for necessário

<h3>Campo de Versão</h3>

- Limite de 30 caracteres
- Abreviação sempre termina em consoante
- Formata a frase em maiúsculo
- Não abrevia palavras “blindadas”, até o momento são elas:  
  - `GLOBO`, `SBT`, `RECORD`, `REDETV`, `BAND`, `CULTURA`,  
    `ESPN`, `SPORTV`, `TNT`, `MAT`, `VES`, `NOT`, `MAD`, `FUT`, `BOLETIM`

<h2 id="colab">🤝 Criado por</h2>

<table>
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/mfonse/">
        <img src="https://avatars.githubusercontent.com/u/129181986?v=4" width="100px;" alt="Matheus Fonseca Profile Picture"/><br>
        <sub>
          <b>Matheus Fonseca</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<h3>Documentações que podem ser úteis</h3>

[📖 Documentação simples](https://github.com/matheusfonseca18/Abreviador/blob/main/Documenta%C3%A7%C3%A3o%20Abreviador.pdf)

<!-- [📝 Documentação técnica](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716) -->
