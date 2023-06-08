# Steam Trading Bot

The Steam Trading Bot is a Python bot that uses the Steam and Binance APIs to facilitate TF2 key trades and Bitcoin transactions. The bot can listen for specific commands in Steam chat, accept valid trade offers, and execute corresponding Bitcoin transactions.

The bot requires Python 3.7 or higher. If you don't have Python installed, you can download it from [Python's official website](https://www.python.org/downloads/).

## Creating a Virtual Environment

To create a virtual environment, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the root directory of your project.
3. Run the following command to create a virtual environment:

```shell
python3 -m venv env
```
Replace env with the name you want to give to your virtual environment. You can choose any name you prefer.

    Wait for the process to complete. This will create a new directory called env (or your chosen name) in your project's root directory.

### Activating the Virtual Environment

#### Windows

To activate the virtual environment, follow these steps:
Windows

1. Open the terminal or command prompt.
2. Navigate to the root directory of your project if you're not already there.
3. Run the following command to activate the virtual environment:

```shell
env\Scripts\activate
# or
.\env\Scripts\Activate  
```
Replace env with the name of your virtual environment.

Remember to activate the virtual environment every time you work on your project. When you're done working, you can deactivate the virtual environment by running the following command:

```shell
deactivate
```

## Requirement Installation:
Then, you need to install the necessary Python packages. Open your terminal and navigate to the directory where you have cloned the repository. Once there, you can install the necessary packages by running the following commands:

```bash
# Install steam package with SteamClient dependencies
pip install -U "steam[client]"

# If you want to install directly from the GitHub repository (cutting edge from master)
pip install "git+https://github.com/ValvePython/steam#egg=steam"
```

### Installing from requirements.txt

To install packages from a requirements.txt file, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where your requirements.txt file is located.
3. Run the following command to install the packages listed in the file:

```shell
pip install -r requirements.txt
```

    Wait for the process to complete. Pip will read the requirements.txt file and install all the packages and their dependencies specified in the file.

Make sure you have the necessary permissions to install packages and that you have Python and pip installed on your system before executing the command.

This command is especially useful when you want to quickly install all the required packages for a project without individually specifying each package.

## Environment Variables Setup:

To use the Steam and Binance APIs, you will need to get your API keys and set them as environment variables.

Here's an example of how to set environment variables in .env file:

```
STEAM_USERNAME=your_steam_username
STEAM_PASSWORD=your_steam_password
STEAM_API_KEY=your_steam_api_key
CRYPTO_API_KEY=your_crypto_api_key
CRYPTO_API_SECRET=your_crypto_api_secret
```

Also, please ensure that these environment variables are set before running the bot script.

Important: Never share your API keys or secrets with anyone or commit them to version control. Always keep them private and secure.

## Running the Bot:
Once you've installed the required packages and set the environment variables, you can start the bot by running the bot script in your terminal:

```bash
python main.py
# or
py main.py
```
Remember, the bot is currently in development and not all features are implemented yet. Always test with small amounts first.