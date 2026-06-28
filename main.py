# %%
def check_even_odd(num: int):
    if num % 2 == 0:
        return 'Cüt'
    else:
        return 'Tək'

# Funksiyanı sınaqdan keçirmək
test_number = 37
result = check_even_odd(test_number)
print(f"{test_number} ədədi {result}-dir")

# %% md
# while Dövrü
# %%
i = 1

while i <= 5:
    print(i)
    i += 1

# %% md
# 2. while Dövrü ilə Toplama
# %%
def sum_upto_n(n):
    if n < 0:
        return ('ERROR!!! İnput value must be positive number or zero!!!')

    x = 0
    cem = 0

    while x <= n:
        cem = cem + x
        x = x + 1
    return cem

# Test
test_values = [5, 10, -3, 0]
for val in test_values:
    print(f"sum_upto_n({val}) = {sum_upto_n(val)}")

# %% md
# 3. FizzBuzz
# %%
def fizz_buzz(n):
    for x in range (1, n + 1):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x)

fizz_buzz(15)

# %% md
# 4. Saitlərin Sayını Tapmaq
# %%
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

# %% md
# 5. Sətiri Tərsinə Çevirmək
# %%
def reverse_string(text: str):
    return text[::-1]

# Test
test_words = ["Python", "Colab", "Function", "12345"]
for w in test_words:
    print(f"{w} sətirinin tərsi -> {reverse_string(w)}")