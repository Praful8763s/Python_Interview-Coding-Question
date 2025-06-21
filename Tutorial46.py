# Here is a comprehensive **guide on pattern questions** using **Python**, complete with **examples, explanations, and solutions**. These are especially helpful for coding interviews, competitive programming, and strengthening logic building.

# ---

# # 🌟 All Pattern Questions in Python (with Solutions)

# ---

# ## ✨ What are Pattern Programs?

# Pattern programs are coding exercises where characters like `*`, numbers, or alphabets are arranged in a specific shape (like triangles, pyramids, diamonds). These help build:

# * Logical thinking
# * Loop mastery
# * Nested structure understanding

# ---

# # 🔁 Basic Structure

# Most pattern programs use **nested loops**:

# ```python
# for i in range(rows):         # Outer loop
#     for j in range(something):  # Inner loop
#         print('*', end=' ')
#     print()
# ```

# ---

# ## ✅ Table of Contents

# 1. Star Patterns
# 2. Number Patterns
# 3. Alphabet Patterns
# 4. Advanced Patterns
# 5. Inverted and Mirrored Patterns
# 6. Tips and Tricks

# ---

# # 🌟 1. STAR PATTERNS

# ---

# ### 1.1 Square Star Pattern

# ```
# *****
# *****
# *****
# *****
# *****
# ```

# ```python
# rows = 5
# for i in range(rows):
#     for j in range(rows):
#         print('*', end=' ')
#     print()
# ```

# ---

# ### 1.2 Right-Angled Triangle

# ```
# *
# * *
# * * *
# * * * *
# * * * * *
# ```

# ```python
# rows = 5
# for i in range(rows):
#     for j in range(i + 1):
#         print('*', end=' ')
#     print()
# ```

# ---

# ### 1.3 Inverted Right Triangle

# ```
# * * * * *
# * * * *
# * * *
# * *
# *
# ```

# ```python
# rows = 5
# for i in range(rows):
#     for j in range(rows - i):
#         print('*', end=' ')
#     print()
# ```

# ---

# ### 1.4 Pyramid Pattern

# ```
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# ```

# ```python
# rows = 5
# for i in range(rows):
#     for j in range(rows - i - 1):
#         print(' ', end=' ')
#     for j in range(i + 1):
#         print('*', end=' ')
#     print()
# # ```

# ---

# ### 1.5 Inverted Pyramid

# ```
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# ```

# ```python
# rows = 5
# for i in range(rows):
#     for j in range(i):
#         print(' ', end=' ')
#     for j in range(rows - i):
#         print('*', end=' ')
#     print()
# ```

# ---

# # 🔢 2. NUMBER PATTERNS

# ---

# ### 2.1 Right Triangle with Numbers

# ```
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# ```

# ```python
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()
# ```

# ---

# ### 2.2 Floyd's Triangle

# ```
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# ```

# ```python
# rows = 4
# num = 1
# for i in range(1, rows + 1):
#     for j in range(i):
#         print(num, end=' ')
#         num += 1
#     print()
# ```

# ---

# ### 2.3 Repeating Row Number

# ```
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# ```

# ```python
# rows = 4
# for i in range(1, rows + 1):
#     for j in range(i):
#         print(i, end=' ')
#     print()
# ```

# ---

# ### 2.4 Inverted Number Triangle

# ```
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# ```

# ```python
# rows = 5
# for i in range(rows, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()
# ```

# ---

# # 🔤 3. ALPHABET PATTERNS

# ---

# ### 3.1 Alphabet Right Triangle

# ```
# A
# A B
# A B C
# A B C D
# ```

# ```python
# rows = 4
# for i in range(rows):
#     for j in range(i + 1):
#         print(chr(65 + j), end=' ')
#     print()
# ```

# ---

# ### 3.2 Repeating Alphabets

# ```
# A
# B B
# C C C
# D D D D
# ```

# ```python
# rows = 4
# for i in range(rows):
#     for j in range(i + 1):
#         print(chr(65 + i), end=' ')
#     print()
# ```

# ---

# # 🧠 4. ADVANCED PATTERNS

# ---

# ### 4.1 Diamond Pattern

# ```
#     *
#    * *
#   * * *
#    * *
#     *
# ```

# ```python
# n = 3
# # Top
# for i in range(n):
#     print(' ' * (n - i - 1) + '* ' * (i + 1))
# # Bottom
# for i in range(n - 2, -1, -1):
#     print(' ' * (n - i - 1) + '* ' * (i + 1))
# ```

# ---

# ### 4.2 Number Pyramid

# ```
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# ```

# ```python
# rows = 4
# for i in range(1, rows + 1):
#     print(' ' * (rows - i), end='')
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()
# ```

# ---

# ### 4.3 Pascal's Triangle

# ```
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
# ```

# ```python
# def factorial(n):
#     return 1 if n == 0 else n * factorial(n - 1)

# rows = 5
# for i in range(rows):
#     for j in range(rows - i + 1):
#         print(' ', end='')

#     for j in range(i + 1):
#         print(factorial(i) // (factorial(j) * factorial(i - j)), end=' ')
#     print()
# ```

# ---

# # 🔁 5. INVERTED / MIRRORED PATTERNS

# ---

# ### 5.1 Mirrored Right Triangle

# ```
#         *
#       * *
#     * * *
#   * * * *
# ```

# ```python
# rows = 4
# for i in range(rows):
#     for j in range(rows - i - 1):
#         print(' ', end=' ')
#     for j in range(i + 1):
#         print('*', end=' ')
#     print()
# ```

# ---

# ### 5.2 Hollow Square Pattern

# ```
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
# ```

# ```python
# rows = 5
# for i in range(rows):
#     for j in range(rows):
#         if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# ```

# ---

# ### 5.3 Hollow Pyramid Pattern

# ```
#     *
#    * *
#   *   *
#  *     *
# *********
# ```

# ```python
rows = 5
for i in range(rows):
    for j in range(rows - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == rows - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
# ```

# ---

# # 🧩 6. Tips and Tricks

# * Use `chr()` to convert ASCII numbers to letters.
# * `print(end=' ')` is used to print in the same line.
# * Reverse patterns? Use `range(rows, 0, -1)`.
# * Always sketch the pattern before writing the code.

# ---

# # 🚀 Challenge Yourself: Practice

# Try solving these:

# 1. Butterfly Pattern
# 2. Zig-Zag Pattern
# 3. Sandglass Pattern
# 4. Hourglass Star Pattern
# 5. Heart Shape Pattern

# ---

# # 💡 Conclusion

# Pattern questions are an **excellent way to master Python loops, logic, and structure**. They may look easy but are often tricky when combined with constraints (e.g., hollow, mirrored, numeric combinations).

# Mastering these helps not only in **interviews** but also in **logical problem solving** for real-world applications like **UI layouts, data formatting, and algorithm visualizations**.

# Would you like a downloadable PDF version of this guide or the complete code in a zip file?
