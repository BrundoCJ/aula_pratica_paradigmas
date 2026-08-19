# Respostas — Capítulo 2 de Sebesta

> Baseado em **Conceitos de Linguagens de Programação — 11ª edição**, Robert W. Sebesta.  
> As respostas abaixo foram elaboradas a partir do conteúdo do Capítulo 2 do PDF fornecido.

## 1. A genealogia das linguagens não é uma escada de progresso

A genealogia das linguagens não representa uma sequência em que cada linguagem nova torna a anterior obsoleta. O Sebesta apresenta a evolução como uma história de influências, adaptações e objetivos diferentes, em que linguagens podem continuar existindo porque atendem bem a determinados domínios.

Dois fatores históricos explicam por que uma linguagem pode influenciar outra sem substituí-la:

1. **Investimento existente e ecossistema.** Uma linguagem já utilizada possui programas, usuários, compiladores, treinamento e experiência acumulada. Isso cria um custo de migração. O caso de ALGOL 58 é ilustrativo: IBM e SHARE chegaram a abandonar a linguagem depois das despesas para desenvolver compiladores, utilizar a nova tecnologia e treinar os usuários, mantendo Fortran como linguagem científica para as máquinas IBM 700.

2. **Especialização por domínio.** Uma linguagem pode continuar sendo adequada ao seu campo mesmo que outra introduza recursos mais sofisticados. COBOL, por exemplo, permaneceu amplamente utilizada por décadas porque atendia bem às necessidades das aplicações empresariais e porque houve pouco incentivo para criar novas linguagens de negócios para substituí-la.

Portanto, uma linguagem pode **influenciar o projeto de outra** e, ao mesmo tempo, continuar sendo usada por razões econômicas, históricas, técnicas e de domínio.

## 2. Plankalkül

Plankalkül é relevante porque foi projetada por Konrad Zuse em **1945**, mas nunca foi implementada e sua descrição só foi publicada em **1972**. Como poucas pessoas conheciam o projeto, várias de suas ideias só apareceram em outras linguagens muitos anos depois.

Três recursos antecipados pelo projeto foram:

1. **Vetores e registros**, inclusive registros aninhados.
2. **Estruturas de repetição**, semelhantes ao `for` moderno.
3. **Expressões que descreviam relações que deveriam permanecer verdadeiras durante a execução**, semelhantes às asserções atuais.

Também havia recursos bastante avançados para a época, como programas para ordenação de vetores, conectividade de grafos, análise sintática e algoritmos de xadrez.

Um recurso particularmente valioso é a ideia de **asserções**. Zuse podia expressar condições que deveriam ser verdadeiras em determinados pontos do programa. Isso antecipa uma preocupação que posteriormente aparece na verificação e no raciocínio sobre a correção de programas.

## 3. Short Code, Speedcoding e A-0/A-1/A-2

| Sistema | Problema principal | Estratégia |
|---|---|---|
| **Short Code** | Tornar a programação matemática menos tediosa que o código de máquina | Usava uma representação codificada de expressões matemáticas e as **interpretava diretamente** |
| **Speedcoding** | Falta de operações de ponto flutuante e limitações do IBM 701 | Criava uma **máquina virtual** com pseudoinstruções para operações matemáticas |
| **A-0/A-1/A-2** | Reduzir a quantidade de código de máquina que precisava ser escrito | Expandiam pseudocódigo em **subprogramas previamente existentes em código de máquina** |

Short Code não era compilada para código de máquina. Era interpretada, simplificando a programação, mas com um custo enorme de execução: aproximadamente **50 vezes mais lenta** que código de máquina.

Speedcoding, de John Backus, transformava conceitualmente o IBM 701 em uma calculadora virtual de ponto flutuante de três endereços, fornecendo operações como raiz quadrada, seno, logaritmo e exponenciação.

Já A-0, A-1 e A-2, desenvolvidos por uma equipe liderada por Grace Hopper, expandiam pseudocódigo em chamadas a subprogramas em código de máquina, de maneira semelhante à expansão de macros em assembly.

Chamá-los simplesmente de **compiladores modernos** seria impreciso porque seus mecanismos eram muito mais limitados. Eles não correspondiam ao modelo completo de um compilador moderno com análise da linguagem, verificação e geração sistemática de código para construções gerais. Eram principalmente mecanismos de **interpretação, virtualização ou expansão de rotinas**.

## 4. Por que Fortran precisou provar que o código traduzido poderia competir com código manual?

Porque o principal concorrente de Fortran não era outra linguagem de alto nível: era o **código de máquina ou assembly escrito à mão**.

O projeto de Fortran prometia duas coisas aparentemente difíceis de conciliar: a facilidade de programação dos sistemas de pseudocódigo e uma eficiência próxima à do código produzido manualmente.

Isso era fundamental naquele período porque:

- os computadores eram caros;
- tinham pouca memória e eram relativamente lentos;
- as aplicações eram principalmente científicas;
- o tempo de execução tinha grande importância.

Por isso, os programadores desconfiavam de uma linguagem de alto nível. A equipe chegou a afirmar que o código produzido pelo compilador poderia ter cerca de metade da eficiência do código manual. Essa afirmação gerou bastante ceticismo. Grande parte do esforço de desenvolvimento do primeiro compilador foi dedicada à otimização, e a equipe quase atingiu a meta de desempenho.

O resultado foi decisivo para a adoção: em abril de 1958, apenas um ano depois do lançamento, aproximadamente **metade do código escrito para o IBM 704 já era Fortran**.

Assim, Fortran venceu porque tornou o **custo de programação menor** sem sacrificar demasiadamente o **desempenho da execução**. Esse equilíbrio foi fundamental para sua aceitação.

## 5. Fortran × Lisp

As duas linguagens surgiram para problemas muito diferentes.

### Fortran

Fortran foi projetada principalmente para **computação científica**, em um contexto dominado por cálculos numéricos. O desempenho do código era uma preocupação central.

Suas primeiras versões trabalhavam com estruturas relativamente simples e com armazenamento e tipos definidos antes da execução, favorecendo compiladores altamente otimizados.

Seu estilo é essencialmente **imperativo**: variáveis, atribuições e estruturas de repetição.

### Lisp

Lisp surgiu para **computação simbólica e inteligência artificial**. McCarthy estudava, por exemplo, diferenciação simbólica e precisava de recursão, expressões condicionais e listas encadeadas alocadas dinamicamente, recursos ausentes em Fortran I.

Lisp pura possui principalmente **átomos e listas**, sendo as listas representadas como estruturas encadeadas.

Seu modelo de computação é **funcional**: os cálculos são realizados pela aplicação de funções a argumentos, e a repetição pode ser expressa por recursão em vez de laços.

**Em resumo:** Fortran prioriza **números, eficiência e computação imperativa**; Lisp prioriza **símbolos, listas e computação funcional**.

## 15. Java e a mudança de contexto

Java não nasceu para a Web. Seu impulso inicial veio dos **dispositivos eletrônicos para consumidores**. A equipe da Sun considerou C e C++ inadequadas para esse propósito por questões de orientação a objetos, complexidade e confiabilidade.

Entretanto, os primeiros produtos em que Java foi usada não chegaram ao mercado. A partir de 1993, com a expansão da World Wide Web e o aparecimento dos navegadores gráficos, percebeu-se que Java era adequada para a Web. Os applets, executados dentro dos navegadores, tornaram-se populares na segunda metade dos anos 1990.

O caso mostra que **uma linguagem não precisa mudar completamente para encontrar um novo domínio**. O que mudou foi o contexto. Características que haviam sido pensadas para dispositivos de consumo — simplicidade, confiabilidade e execução independente da plataforma — passaram a ser úteis em um ambiente Web emergente.

A história de Java mostra, portanto, que a importância de uma linguagem depende não apenas de seu projeto, mas também de **quando, onde e em qual ecossistema ela é aplicada**.

## 16. Perl, JavaScript, PHP, Python, Ruby e Lua

Serem chamadas de *scripting* não significa que sejam equivalentes.

| Linguagem | Domínio inicial | Estruturas de dados | Estratégia de implementação |
|---|---|---|---|
| **Perl** | Unix, processamento de texto e administração de sistemas | vetores dinâmicos/esparsos e hashes | compilada para uma linguagem intermediária |
| **JavaScript** | Web no navegador | strings e vetores dinâmicos, objetos | interpretada pelo navegador |
| **PHP** | páginas pessoais e posteriormente Web no servidor | vetores normais e associativos | interpretada no servidor |
| **Python** | administração de sistemas, CGI e tarefas menores | listas, tuplas e dicionários | interpretada |
| **Ruby** | linguagem geral com forte orientação a objetos | coleções/dicionários e objetos dinâmicos | foco em dinamismo e extensibilidade |
| **Lua** | extensão de aplicações e scripting embutido | uma estrutura principal: **tabelas** | traduzida para código intermediário e interpretada |

### Perl

Perl nasceu como combinação de **sh e awk**, sendo inicialmente usada para processamento de arquivos e administração de sistemas Unix. Apesar do rótulo de scripting, Sebesta observa que ela se aproxima de uma linguagem imperativa tradicional e é compilada pelo menos para linguagem intermediária antes da execução.

### JavaScript

Foi criada para atender à necessidade de tornar documentos HTML dinâmicos. O código é incorporado ao HTML e interpretado pelo navegador; seus usos principais incluem validação de formulários e criação dinâmica de páginas.

### PHP

Começou como uma ferramenta pessoal de Rasmus Lerdorf e foi transformada em uma linguagem de scripting **do lado servidor**, embutida em HTML. O código PHP é processado no servidor e normalmente gera HTML. Seus vetores combinam características de vetores de JavaScript e hashes de Perl.

### Python

É uma linguagem de scripting orientada a objetos e interpretada, usada inicialmente para administração de sistemas, CGI e tarefas menores. Em vez de vetores tradicionais, utiliza **listas, tuplas e dicionários**.

### Ruby

Foi criada por Yukihiro Matsumoto a partir de sua insatisfação com Perl e Python. Sua característica marcante é ser **puramente orientada a objetos**: cada valor é um objeto e as operações são realizadas por métodos. Classes e objetos também podem ser modificados dinamicamente.

### Lua

Lua foi criada no Brasil e tinha como objetivo central a **extensibilidade**. É procedural e funcional, possui tipagem dinâmica e utiliza tabelas como sua principal estrutura de dados. As tabelas podem funcionar como vetores, hashes ou registros. Lua é traduzida para código intermediário e interpretada, o que facilita seu uso embutido em outros sistemas.

Portanto, "scripting" descreve uma **família histórica de usos e ambientes de execução**, não um único modelo de linguagem.

## 17. Decisões de C# comparadas com Java e C++

Duas decisões interessantes são:

### 1. Delegates em vez de ponteiros de função

C++ possui ponteiros para funções, mas eles carregam problemas de segurança de tipos. C# introduziu os **delegates**, que são referências a subprogramas orientadas a objetos e verificadas quanto aos tipos. Eles são usados, entre outras coisas, para eventos, callbacks e controle de threads. Em Java, callbacks são obtidos principalmente por meio de interfaces.

**Problema resolvido:** oferecer o poder de passar referências a métodos sem expor diretamente a insegurança dos ponteiros de função de C++.

### 2. Enums mais seguros

C++ e Java possuem sistemas distintos para tipos primitivos e objetos, e C++ permite características como enumerações com conversões implícitas. C# decidiu manter alguns desses recursos de C++, mas modificá-los para aumentar a segurança. Em C#, valores de `enum` não são implicitamente convertidos para inteiros.

**Problema resolvido:** evitar conversões automáticas que podem mascarar erros de tipos e tornar o programa menos seguro.

Essas decisões mostram a posição histórica de C#: ela não simplesmente copia Java ou C++; procura combinar características de C++ e Java com mecanismos que, segundo Sebesta, melhoram segurança e produtividade.

## 18. XSLT × JSP

### XSLT

**Entrada:** um documento de dados XML + um documento XSLT, também escrito em XML.  
**Processamento:** o processador encontra padrões nos dados XML e aplica os *templates* e instruções de transformação correspondentes.  
**Saída:** outro documento, podendo ser XML, HTML ou texto.

### JSP

**Entrada:** uma página normalmente formada por **HTML + Java**, podendo conter elementos JSTL.  
**Processamento:** o processador JSP transforma o documento em um servlet; o código Java é copiado para o servlet e o HTML é transformado em instruções de impressão Java. Depois, o servlet é executado pelo *servlet container*.

**Saída:** um documento HTML enviado para o navegador. Os elementos JSTL podem determinar quais partes do HTML serão incluídas e permitir iteração e seleção.

As duas são chamadas de **linguagens híbridas de marcação-programação** porque combinam a estrutura de uma linguagem de marcação com elementos capazes de realizar operações de programação, como controle de fluxo e computação.

A diferença central é:

**XSLT = transforma dados XML em outro documento.**  
**JSP = gera conteúdo Web dinâmico a partir de uma página processada no servidor.**

## 19. Linha do tempo com oito linguagens e quatro paradigmas

Uma forma interessante de representar a evolução é:

```text
1957 ─ Fortran
        │
        │ influência: computação científica + estrutura imperativa
        ▼
1960 ─ ALGOL 60
        │
        │ influência: estrutura de blocos, controle estruturado
        ▼
1967 ─ Simula 67
        │
        │ influência: classes + herança → orientação a objetos
        ▼
1983 ─ C++
        │
        │ influência: POO sobre base imperativa de C
        ▼
1995 ─ Java
        │
        │ influência: POO de C++ com simplificação e maior confiabilidade
        ▼
1990s ─ Ruby
        │
        └── influência: ideias e recursos de Perl/Python
```

E, paralelamente:

```text
1959 ─ Lisp
        │
        │ influência: computação funcional
        ▼
      família funcional

1970s ─ Prolog
        │
        │ influência: programação lógica/declarativa
        ▼
      família lógica
```

Paradigmas representados:

- **Imperativo:** Fortran, ALGOL 60, C++;
- **Orientado a objetos:** Simula 67, C++, Java, Ruby;
- **Funcional:** Lisp;
- **Lógico/declarativo:** Prolog.

O ponto mais importante não é a cronologia, mas o **tipo de influência**: ALGOL 60 contribui para a evolução de estruturas de programação; Simula 67 é importante para abstração de dados e orientação a objetos; C++ combina recursos imperativos e orientados a objetos; Java parte dessa tradição e simplifica várias decisões; Ruby incorpora ideias de Perl e Python.

## 20. Estudo de caso

Para uma equipe com quatro necessidades muito diferentes, eu escolheria **famílias diferentes**, em vez de tentar usar uma única linguagem para tudo.

| Necessidade | Família sugerida | Justificativa histórica |
|---|---|---|
| **Cálculo científico** | **Fortran** | Foi criada especificamente em um contexto de computação científica e priorizou eficiência |
| **Regras declarativas** | **Prolog** | Trabalha naturalmente com fatos, regras e consultas |
| **Aplicação Web interativa** | **JavaScript / família de scripting Web** | Foi criada para adicionar computação dinâmica aos documentos HTML |
| **Firmware restrito** | **Ada / família de linguagens para sistemas embarcados** | Ada surgiu no contexto do DoD, em que mais da metade das aplicações eram sistemas embarcados |

### Cálculo científico — Fortran

Fortran foi criada para computação científica e seu desenvolvimento foi fortemente influenciado pela necessidade de gerar código eficiente.

**Escolha:** família Fortran.

### Regras declarativas — Prolog

A base de dados de Prolog é formada por **fatos e regras**, e o sistema responde consultas tentando provar seus objetivos. Isso corresponde muito melhor ao problema de regras declarativas que um modelo imperativo tradicional.

O próprio Sebesta, porém, alerta para um trade-off: programação lógica mostrou-se menos eficiente que alternativas imperativas e especialmente útil apenas em determinadas áreas, como IA e certos bancos de dados.

### Web interativa — JavaScript

JavaScript foi criada em resposta à necessidade de computação associada a documentos HTML estáticos. Seu uso mais comum é no navegador, com validação de formulários e criação de documentos HTML dinâmicos.

**Escolha:** família JavaScript/scripting Web.

### Firmware restrito — Ada

Aqui há uma pequena ressalva: o Sebesta fala em **sistemas embarcados**, e não especificamente no termo "firmware". Historicamente, porém, é o enquadramento mais próximo. Em 1974, mais da metade das aplicações do DoD eram sistemas embarcados, e o excesso de linguagens e a dificuldade de reutilização motivaram a criação de Ada.

Ada também trouxe recursos importantes para abstração de dados e tratamento de exceções, coerentes com a preocupação com sistemas confiáveis.

### Dois trade-offs

**Trade-off 1 — desempenho × produtividade.**  
Fortran pode oferecer alto desempenho para cálculo numérico, enquanto linguagens de scripting favorecem rapidez de desenvolvimento. A escolha depende de qual custo é mais importante no projeto.

**Trade-off 2 — especialização × complexidade tecnológica.**  
Escolher a linguagem adequada para cada domínio aumenta o encaixe entre problema e solução, mas cria uma equipe que precisa dominar várias tecnologias. Em outras palavras, ganha-se adequação técnica, mas aumenta-se o custo de treinamento, integração e manutenção.

## Resumo para estudar para a prova

A ideia central do capítulo 2 é que **linguagens evoluem por influência, não simplesmente por substituição**. Fortran representa a busca por eficiência e produtividade na computação científica; Lisp representa a computação simbólica e funcional; ALGOL introduz estruturas que influenciam inúmeras linguagens; Simula leva à orientação a objetos; C++ combina paradigmas; Java reposiciona-se com a Web; linguagens de scripting surgem para automatizar e dinamizar ambientes específicos; C# reorganiza várias ideias de C++ e Java no ecossistema .NET; e XSLT/JSP mostram a integração entre marcação e programação.

A genealogia mostrada pelo Sebesta confirma justamente essa visão: há **vários ramos, cruzamentos e descendências**, e não uma escada na qual cada nova linguagem simplesmente elimina a anterior.
