# Python Control Structures & Custom Functions

This repository showcases practical implementations of foundational Python control structures, loop mechanics, and algorithmic problem-solving tasks. The exercises focus on custom functional design, iteration limits, and core string/math logic.

---

## 📌 Project Overview

The project covers **5 essential functional programming tasks**:
* **Parity Validation:** Even/Odd conditional testing using modulo arithmetic.
* **Bounded Iteration:** Aggregating numbers incrementally with structured `while` loops and baseline validation rules.
* **Classical FizzBuzz Algos:** Handling compound logic using chained execution flow constraints (`if-elif-else`).
* **Sequential String Traversal:** Evaluating character profiles dynamically using conditional membership testing (`in`).
* **String Reversal Slicing:** Efficiently altering sequence formats using pythonic index manipulation (`[::-1]`).

---

## 💻 Code Structure & Examples

Here is a quick look at how the code is structured and implemented using core features from the project:
### 1. Functional Conditional Structure
Testing basic input criteria and handling branch flows securely:
```python
def check_even_odd(num: int):
    if num % 2 == 0:
        return 'Cüt'
    return 'Tək'


Finding vowel count

```python
def count_vowels(text: str):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for letter in text:
        if letter in vowels:
            vowel_count = vowel_count + 1
    return vowel_count

# Test
test_strings = ["Hello", "Education", "Rhythm", ""]
for t in test_strings:
    print(f"'{t}' sözündə saitlərin sayı: {count_vowels(t)}")