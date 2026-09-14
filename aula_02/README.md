# Atividade - Aula 02

[← Voltar ao índice](../README.md)

Questões sobre a **evolução das principais linguagens de programação**, com
base no capítulo 2 de *Conceitos de Linguagens de Programação*, de Robert W.
Sebesta.

## 1. Por que linguagens antigas continuam em uso?

Uma linguagem nova nem sempre substitui a anterior. Sistemas já implantados,
bibliotecas, profissionais treinados e custos de migração mantêm linguagens
como Fortran e COBOL relevantes. Além disso, algumas continuam eficientes no
domínio para o qual foram projetadas.

## 2. Qual é a importância de Plankalkül?

Konrad Zuse projetou Plankalkül nos anos 1940, antes de existirem ferramentas
adequadas para implementá-la. Ela antecipou ideias como estruturas de dados,
arranjos, atribuições e expressões lógicas, mostrando que uma linguagem podia
ser pensada em nível mais abstrato que o código de máquina.

## 3. O que Short Code, Speedcoding e A-0 buscavam resolver?

Todos tentavam reduzir a dificuldade de programar diretamente em linguagem de
máquina. Short Code e Speedcoding interpretavam notações mais convenientes. O
sistema A-0, de Grace Hopper, reunia rotinas previamente escritas. Ainda não
eram compiladores modernos completos, mas prepararam o caminho para eles.

## 4. Por que o primeiro compilador Fortran precisava gerar código eficiente?

Computadores eram caros e programadores desconfiavam que uma tradução
automática pudesse competir com código manual. O compilador precisava produzir
código rápido para que o ganho de produtividade na escrita não fosse anulado
por um grande custo de execução.

## 5. Como Fortran e Lisp refletem domínios diferentes?

| Aspecto | Fortran | Lisp |
|---|---|---|
| Domínio original | cálculo científico | inteligência artificial e símbolos |
| Dados principais | números, vetores e matrizes | listas e símbolos |
| Estilo favorecido | imperativo e iterativo | funcional e recursivo |

## 6. Quais foram as principais contribuições de ALGOL 60?

ALGOL 60 difundiu blocos, escopo léxico, estruturas de controle e uma forma
rigorosa de descrever sintaxe. Mesmo sem dominar o mercado, influenciou Pascal,
C e muitas linguagens posteriores.

## 7. Como o domínio comercial influenciou COBOL?

COBOL adotou comandos próximos do inglês e registros hierárquicos para ser
compreensível também por pessoas da área de negócios. FLOW-MATIC, de Grace
Hopper, foi uma influência direta nessa busca por legibilidade e processamento
de arquivos comerciais.

## 8. Que compromissos aparecem em BASIC e PL/I?

BASIC priorizou facilidade de aprendizagem e acesso interativo, sacrificando
parte da estrutura. PL/I tentou servir tanto à computação científica quanto à
comercial, ganhando muitos recursos, mas também maior complexidade.

## 9. O que APL, SNOBOL e SIMULA 67 trouxeram de novo?

- **APL:** notação compacta e operações sobre vetores e matrizes;
- **SNOBOL:** processamento de textos e casamento de padrões;
- **SIMULA 67:** classes, objetos, herança e simulação de entidades.

Cada uma avançou a linguagem em um domínio específico. SIMULA 67 teve impacto
especial por estabelecer fundamentos da orientação a objetos.

## 10. O que significa ortogonalidade em ALGOL 68?

Ortogonalidade é a possibilidade de combinar recursos da linguagem de maneira
regular, com poucas exceções. ALGOL 68 buscou tipos e construções muito
combináveis. Isso aumentou o poder expressivo, embora a especificação tenha se
tornado difícil de aprender e implementar.

## 11. Como Pascal e C herdaram ideias de ALGOL? E como Prolog se diferencia?

Pascal e C conservaram blocos, procedimentos, expressões e controle imperativo
derivados da família ALGOL. Prolog segue o paradigma lógico: o programa declara
fatos e regras, e o sistema procura uma prova para a consulta, em vez de
receber uma sequência detalhada de comandos.

## 12. Como uma base Prolog pode ser entendida em linguagem natural?

```prolog
aluno(pedro).
estuda(pedro, paradigmas).
aprovado(X) :- aluno(X), estuda(X, paradigmas).
```

As duas primeiras linhas afirmam fatos. A regra diz que uma pessoa é aprovada
se for aluna e estudar paradigmas. A consulta `aprovado(pedro).` pode ser
demonstrada a partir desses fatos.

## 13. Por que Ada foi associada a sistemas críticos?

Ada surgiu de requisitos do Departamento de Defesa dos Estados Unidos e deu
ênfase à legibilidade, tipagem forte, modularização, tratamento de exceções e
concorrência. Esses recursos ajudam a detectar erros cedo e tornam a linguagem
adequada a sistemas de alta confiabilidade.

## 14. Como os objetos evoluíram de Smalltalk para C++ e Java?

Smalltalk organizou praticamente toda computação como troca de mensagens entre
objetos. C++ acrescentou orientação a objetos à eficiência e compatibilidade da
família C. Java simplificou alguns pontos de C++, usou uma máquina virtual e
priorizou portabilidade e segurança.

## 15. Como a finalidade de Java mudou?

Java começou ligado a dispositivos eletrônicos, mas ganhou espaço com a Web
pela promessa de executar o mesmo bytecode em diferentes máquinas. Depois,
tornou-se uma plataforma importante para servidores, aplicações corporativas e
Android.

## 16. Qual problema cada linguagem de script procurou resolver?

| Linguagem | Ênfase histórica |
|---|---|
| Perl | texto e administração de sistemas |
| JavaScript | interatividade em páginas Web |
| PHP | geração de páginas no servidor |
| Python | legibilidade e uso geral |
| Ruby | produtividade e orientação a objetos |
| Lua | linguagem pequena e incorporável |

## 17. Como C# se relaciona com Java e C++?

C# conserva a sintaxe familiar de C/C++, mas usa execução gerenciada na
plataforma .NET, coleta de lixo e uma biblioteca extensa. Assim como Java,
busca segurança e portabilidade por meio de uma máquina virtual, embora tenha
evoluído com recursos próprios, como propriedades, delegados e LINQ.

## 18. Qual é a diferença entre XSLT e JSP?

XSLT é declarativa: descreve transformações de documentos XML. JSP combina
conteúdo Web com processamento no servidor e é traduzida para componentes
Java. As duas geram documentos, mas trabalham com modelos e finalidades
diferentes.

## 19. Linha do tempo resumida

| Ano | Linguagem | Contribuição/paradigma |
|---:|---|---|
| 1957 | Fortran | imperativo científico |
| 1958 | Lisp | funcional |
| 1959 | COBOL | processamento comercial |
| 1960 | ALGOL 60 | blocos e sintaxe formal |
| 1967 | SIMULA 67 | orientação a objetos |
| 1972 | Prolog | lógico |
| 1972 | C | programação de sistemas |
| 1995 | Java | objetos e portabilidade |

Essa linha do tempo mostra que paradigmas diferentes surgiram para responder a
problemas diferentes e continuam coexistindo.

## 20. Que linguagem escolher em cada domínio?

- Cálculo científico legado e alto desempenho numérico: **Fortran**;
- Regras e inferência simbólica: **Prolog**;
- Sistema embarcado com forte controle de recursos: **C** ou **Ada**;
- Aplicação corporativa portável: **Java** ou **C#**;
- Automação, dados e prototipação: **Python**;
- Interação no navegador: **JavaScript**.

A escolha deve considerar domínio, ecossistema, desempenho, segurança,
manutenção e experiência da equipe, não apenas a idade ou popularidade da
linguagem.

## Referência

- SEBESTA, Robert W. *Conceitos de Linguagens de Programação*. 11. ed.
  Capítulo 2: Evolução das principais linguagens de programação.
