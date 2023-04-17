# New and trending on GitHub :star:

This Python script retrieves and displays the top 10 new and trending repositories on GitHub in the last specified number of days. It uses the GitHub REST API to fetch the repositories and the `colorama` library to add color, icons, and emojis to the output in the terminal.

## Prerequisites

- Python 3.x installed on your local machine. If you don't have Python installed, you can download it from the official Python website: https://www.python.org/downloads/
- Install the required dependencies using pip:
```pip install -r requirements.txt```

The requirements.txt file contains the `colorama` library which is used for adding color to the output.

## How to Use

- Clone the repository.
- Open a terminal and navigate to the directory where the script is located.
- Run the script using the following command:

```python
python new_and_trending.py -d [days] -l [language]
```

Replace [days] with the number of days you want to retrieve repositories from. If you don't provide any argument for days, it will use 7 as the default value.
Replace [language] with the language you want to filter the repositories by. If you don't provide any argument for language, it will fetch repositories without any language filter.

## License

This project is open-source and available under the MIT License.