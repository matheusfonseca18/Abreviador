<h1 align="center" style="font-weight: bold;">Abreviador ✂️</h1>

<p align="center">
   <a href="./README.pt-br.md">🇧🇷 Versão em Português (Brasil)</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"/>
</p>

<p align="center">
 <a href="#tech">Technologies</a> • 
 <a href="#about">About</a> • 
 <a href="#use">How to Use</a> •
 <a href="#rules">Rules</a> •
</p>

<h2 id="tech">💻 Technologies</h2>

- Python  
- UnicodeData Library  
- CustomTKinter  

<h2 id="about">📌 About</h2>

<h3>What it does</h3>

**Abreviador** is a Python application designed to assist in formatting text for **Advertisers, Brands, and Versions**.  

The program applies specific <a href="#rules">rules</a> for abbreviation, removal of accents, spaces, and special characters, leaving the text ready for immediate use (already copied to the clipboard).

<h3>What problem does it solve?</h3>

We have a database where data such as **advertiser, brand, or version** are entered daily by several people.  

Since these entries should follow a specific pattern to avoid duplicates, human interpretation can lead to inconsistencies and duplicated data.  
The goal of this program is to eliminate those variations by enforcing a single standard.

<h4>Example:</h4>

Following the <a href="#rules">rules</a>, data can have a maximum of 30 characters (including spaces).  
For instance, the entry **"Chapeuzinho Vermelho e o Lobo Bibi Ferreira"** has 43 characters.  
Each person might abbreviate it differently, e.g. **"Chap Verm Lobo Bibi Ferreira"** or **"Chapeuzin Vermel Lob Bibi Fer"**.  

However, the program provides only one standardized interpretation:  
**"Chapeuzinho V Lobo Bibi Ferr"**.

<h2 id="use">❓ How to Use</h2>

The program has three input fields: **Anunciante (Advertiser)**, **Marca (Brand)**, and **Versão (Version)**. Each has its own <a href="#rules">rules</a>.

Type or paste your text in the correct field, click **"Formatar"**, and that’s it!  
Your formatted result will appear below in the “Your text will appear here” field — and it will also be available on your **clipboard (CTRL + V)**.

<h2 id="rules">📋 Rules</h2>

<h3>Apply to all fields</h3>

- Removes extra spaces (beginning, middle, and end)  
- Removes all accents  
- Removes all special characters  

<h3>Advertiser Field</h3>

- Capitalizes the first letter of each word  
- No character limit  

<h3>Brand Field</h3>

- 30-character limit  
- Abbreviation always ends with a consonant  
- Converts the entire phrase to uppercase  
- Removes prepositions  
- Keeps the main brand (first word) intact whenever possible, abbreviating only when necessary  

<h3>Version Field</h3>

- 30-character limit  
- Abbreviation always ends with a consonant  
- Converts the entire phrase to uppercase  
- Does not abbreviate “protected” words, which currently include:  
  - `GLOBO`, `SBT`, `RECORD`, `REDETV`, `BAND`, `CULTURA`,  
    `ESPN`, `SPORTV`, `TNT`, `MAT`, `VES`, `NOT`, `MAD`, `FUT`, `BOLETIM`

<h2 id="colab">🤝 Created by</h2>

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

<h3>Useful Documentation</h3>

[📖 Simple Documentation (PDF)](https://github.com/matheusfonseca18/Abreviador/blob/main/Documenta%C3%A7%C3%A3o%20Abreviador.pdf)
