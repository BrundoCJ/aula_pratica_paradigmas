# Exercício: qual é a saída? (3/3)

Para cada trecho: **(a)** qual é a saída? **(b)** qual conceito da aula explica?

## 5 · Rust

```rust
fn dobra(v: Vec<i32>) -> Vec<i32> {
    v.iter().map(|x| x * 2).collect()
}
let v = vec![1, 2, 3];
let d = dobra(v);
println!("{:?} {:?}", v, d);
```

**(a) Saída**

Não há saída: o programa **não compila**.

```text
error[E0382]: borrow of moved value: `v`
  |
  |     let v = vec![1, 2, 3];
  |         - move occurs because `v` has type `Vec<i32>`, which does not implement the `Copy` trait
  |     let d = dobra(v);
  |                   - value moved here
  |     println!("{:?} {:?}", v, d);
  |                           ^ value borrowed here after move
```

**(b) Conceito: *ownership* e semântica de movimento**

Em Rust, cada valor tem um único dono. Passar `v` por valor para `dobra`
**move** a posse do vetor para o parâmetro da função. Depois disso, a variável
`v` do chamador não pode mais ser usada, e o compilador rejeita o `println!`.
O erro é detectado em tempo de compilação, antes de qualquer execução.

Correção com empréstimo (*borrow*), sem transferir a posse:

```rust
fn dobra(v: &[i32]) -> Vec<i32> {
    v.iter().map(|x| x * 2).collect()
}
let v = vec![1, 2, 3];
let d = dobra(&v);
println!("{:?} {:?}", v, d); // [1, 2, 3] [2, 4, 6]
```

## 6 · Python

```python
total = 0

def adiciona(x):
    total = total + x
    return total

print(adiciona(5))
```

**(a) Saída**

O programa lança uma exceção:

```text
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
```

**(b) Conceito: regras de escopo de Python, onde atribuição torna o nome local**

O escopo de um nome é decidido quando a função é compilada, não linha a linha.
Como `total` recebe uma atribuição dentro de `adiciona`, Python trata `total`
como **variável local em toda a função**, inclusive no lado direito de
`total + x`. Na hora de ler esse valor, a variável local ainda não foi
vinculada a nenhum valor. A variável global `total = 0` fica oculta.

Para alterar a variável global, é preciso declará-la:

```python
def adiciona(x):
    global total
    total = total + x
    return total

print(adiciona(5))  # 5
```
