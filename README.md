# 🔤 NATO Phonetic Alphabet Converter

This is a simple Python project that converts user-input words into the NATO phonetic alphabet using data from a CSV file and a dictionary comprehension.

---

## 📦 Features

- Reads phonetic alphabet data from a CSV file
- Converts words into corresponding NATO phonetic codes
- Handles invalid characters with error handling
- Recursive retry if input contains non-alphabetic characters

---

## 🧠 How It Works

1. Loads `nato_phonetic_alphabet.csv` into a dictionary.
2. Prompts the user to input a word.
3. Converts each letter into its corresponding NATO code.
4. Displays the result as a list.

---

## 📁 File Structure

nato-phonetic-converter/
│
├── main.py # Main Python script
├── nato_phonetic_alphabet.csv # CSV file with NATO codes

How to Run
Make sure Python 3.x is installed.

Install the required library (if not already installed):

pip install pandas
Run the script:

python main.py


Example Usage

Type a word for conversation: hello
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
If the user types invalid characters:


Type a word for conversation: hi123
Sorry, only letters in the alphabet please.



👨‍💻 Author
Nándor Forgó
📧 Email: nfori.coding@gmail.com
