# ForthPy — A Forth-like Stack-Based Interpreter in Python  
> Lightweight • Extensible • Educational

[![MIT License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Built with Love](https://img.shields.io/badge/built%20with-%E2%9D%A4-red)](#)

---

## ✨ What is ForthPy?

ForthPy is a minimal yet powerful interpreter for a Forth-like, stack-based language, built entirely in Python. It offers dynamic data handling, list and string processing, and encourages postfix-style computation — all while being super fun to hack on!

---

## 🚀 Features

- Postfix notation with stack-based evaluation
- Arithmetic: +, -, *, /, %, ^
- Booleans: true, false, and, or, not
- Comparisons: =, !=, <, <=, >, >=
- String Comparisons: s=, s!=, lex<, lex<=, lex>, lex>=
- List Support: list, listn, len, nth, spread
- Stack Ops: dup, drop, swap, over, rot, clear, print
- List-aware operations via optional A parameter
- Clean Error Reporting with contextual feedback

---

## 🧠 Sample Usage

### Basic Arithmetic

from forth_interpreter import interpreter

interpreter("5 3 + print")
# Output: [8]
### Booleans & Comparisons

interpreter("true false and print")
# Output: [False]

interpreter('"apple" "apple" s= print')
# Output: [True]
### Lists & Stack Magic

interpreter("3 4 5 list dup len print spread print")
# Output:
# [3]
# [3, 4, 5]
---

## 🧰 Supported Tokens

| Category         | Tokens |
|------------------|--------|
| Arithmetic   | +, -, *, /, %, ^ |
| Booleans     | true, false, and, or, not |
| Comparisons  | =, !=, <, <=, >, >= |
| String Compare | s=, s!=, lex<, lex<=, lex>, lex>= |
| List Handling| list, listn, len, nth, spread |
| Stack Ops    | dup, drop, swap, over, rot, clear, print |

---

## ⚙️ Architecture

The interpreter follows a clear pipeline:

1. Tokenizer → Breaks input into meaningful tokens  
2. Parser → Converts tokens into typed Python objects  
3. Evaluator → Applies stack-based logic and executes commands  
4. Context-aware Stack → Optional A parameter to manage nested stacks for list-aware operations

---

## 📦 Installation

```git clone https://github.com/WasimKaunain/forthpy.git```


from forth_interpreter import interpreter
interpreter("2 3 * print")
---

## ✍️ Roadmap

- [ ] User-defined procedures (: square dup * ;)
- [ ] Conditionals (if ... else ... endif)
- [ ] Looping (repeat, while)
- [ ] REPL interface
- [ ] Debug mode / Trace stack
- [ ] Web-based interactive playground

---

## 🤝 Contributing

Pull requests, ideas, suggestions, and improvements are welcome!

1. Fork the project
2. Create your feature branch (git checkout -b feature/your-feature)
3. Commit your changes (git commit -am 'Add feature')
4. Push to the branch (git push origin feature/your-feature)
5. Open a Pull Request

---

## ⚖ License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 💬 Final Words

This project is a love letter to stack-based programming, retro language design, and expressive simplicity.  
Perfect for curious minds, compiler explorers, and Forth enthusiasts.

> “Simplicity is the ultimate sophistication.” – *Leonardo da Vinci*

---
