# Static Code Analysis – Issue Documentation

## 1. Bandit Issues

| Issue | Severity | Problem | Fix applied |
|---|---|---|---|
| B403 | Low | Potential security risks from importing pickle | Replaced pickle-based storage with JSON. |
| B301 | Medium | Unsafe deserialization using pickle.load() | Used json.load() instead. |
| B605 | High | Possible command injection through os.system() | Removed the unused printing function that invoked the shell. |
| B311 | Low | Standard random generator used for lucky draw | Replaced random.choice() with secrets.choice(). |

## 2. Pylint Issues

| Issue | Problem | Fix applied |
|---|---|---|
| C0114 | Missing module docstring | Added a module docstring. |
| C0116 | Missing function docstrings | Added docstrings to functions. |
| C0103 | Names did not follow snake_case | Renamed functions and arguments using snake_case. |
| W0102 | Mutable list used as a default argument | Changed the default to None and initialized the list inside the function. |
| R1705 | Unnecessary else after return | Removed the unnecessary else branch. |
| W0613 | Unused sortOrder argument | Implemented sorting behavior using sort_order. |

## 3. Flake8 Issues

| Issue | Problem | Fix applied |
|---|---|---|
| E231 | Missing whitespace after comma | Added the required space. |
| E225 | Missing whitespace around operator | Added spaces around the operator. |
| E261 | Incorrect spacing before inline comment | Corrected comment spacing. |
| E305 | Insufficient blank lines after a function definition | Added the required blank lines. |
| E501 | Line exceeded 79 characters | Shortened the module docstring. |

## 4. Final Verification

- Pylint score: 10.00/10
- Bandit: No issues identified
- Flake8: No issues reported

The code was executed successfully after the fixes. Event creation, guest registration, seat counting, event status, lucky-draw selection, and JSON saving and loading were verified.