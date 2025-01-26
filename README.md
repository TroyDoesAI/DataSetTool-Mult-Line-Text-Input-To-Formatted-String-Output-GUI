# LLM DataSmith

**LLM DataSmith** is a lightweight PyQt application designed to help you craft custom datasets for training large language models. Paste or type any text snippet, then instantly convert it into a properly escaped Python string. This speeds up the manual creation of training data, making it simpler to integrate text snippets into your code or dataset pipeline.

## Features

- **Paste-friendly editor:** Easily paste or manually type your text into a multi-line input field.  
- **Instant conversion:** Click a button to convert the text into a Python string with correct line breaks `\n` and tabs `\t`.  
- **Simple copying:** Copy the transformed text at the click of a button for quick use in your code.  
- **Straightforward UI:** A minimal interface built with PyQt for a fuss-free experience.

## Installation

1. Clone this repository or download the source files.
2. Install the required dependencies (primarily `PyQt5`):
   ```bash
   pip install PyQt5
   ```
3. Run the Python script:
   ```bash
   python LLM_DataSmith.py
   ```

*(You can rename `LLM_DataSmith.py` to whatever script name you’re using.)*

## Usage

1. Launch **LLM DataSmith**:
   ```bash
   python LLM_DataSmith.py
   ```
2. Paste or type your text into the top box.
3. Click **Convert** to generate the Python-formatted string.
4. Copy the output from the lower box via **Copy Output**.
5. Use the formatted string in your dataset creation scripts or anywhere you need properly escaped text.

## Contributing

Contributions are welcome! If you have suggestions for improving the tool’s functionality or user interface, feel free to open an issue or submit a pull request.

## License

This project is released under the [MIT License](LICENSE). Feel free to use it and modify it as you like. 

---  

Have any questions, feature requests, or feedback? Please open an issue in this repository. Happy dataset crafting!
