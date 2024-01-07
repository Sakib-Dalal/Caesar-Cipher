# Caesar Cipher

## Overview

This Python script implements a simple Caesar Cipher encryption and decryption tool. The program prompts the user to input a message and a shift value, allowing them to either encrypt or decrypt the message using the Caesar Cipher algorithm. The user can choose to repeat the process or exit the program.

## Author

This code is authored by Sakib Dalal.

## Usage

1. Run the `main.py` script.
2. Choose whether to encode or decode a message.
3. Enter the message you want to process.
4. Specify the shift value for encryption or decryption.
5. Review the result.

The program uses a circular alphabet, and any non-alphabetic characters in the input message remain unchanged.

## Art

The ASCII art logo is stored in `art.py` and is displayed at the beginning of the program. The visual representation enhances the user experience.

```python
# art.py
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
```

## How to Run

1. Clone the repository to your local machine:

    ```bash
    git clone git@github.com:Sakib-Dalal/Caesar-Cipher.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Caesar-Cipher
    ```

3. Run the main script:

    ```bash
    python main.py
    ```

## License

This project is licensed under the [MIT License](LICENSE).

---

*This project is developed by Sakib Dalal. For more details, please visit the [GitHub repository](git@github.com:Sakib-Dalal/Caesar-Cipher.git).*
