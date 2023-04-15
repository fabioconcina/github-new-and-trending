# Most starred on GitHub :star:

This Python script retrieves and displays the top 10 most starred repositories on GitHub in the last specified number of days. It uses the GitHub REST API to fetch the repositories and the `colorama` library to add color, icons, and emojis to the output in the terminal.

## Prerequisites

- Python 3.x installed on your local machine. If you don't have Python installed, you can download it from the official Python website: https://www.python.org/downloads/
- Install the required dependencies using pip:
```pip install -r requirements.txt```

The requirements.txt file contains the `colorama` library which is used for adding color to the output.

## How to Use

- Clone the repository or download the main.py file to your local machine.
- Open a terminal and navigate to the directory where main.py is located.
- Run the script using the following command:

```python
python main.py -d [days] -l [language]
```

Replace [days] with the number of days you want to retrieve repositories from. If you don't provide any argument for days, it will use 7 as the default value.
Replace [language] with the language you want to filter the repositories by. If you don't provide any argument for language, it will fetch repositories without any language filter.

The script will fetch the top 10 most starred repositories on GitHub in the last specified number of days and with the specified language filter, if provided, and display them in the terminal with color, icons, and emojis to make the output visually appealing.

## License

This project is open-source and available under the MIT License.