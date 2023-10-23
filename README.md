
# Week 7 Mini Project -  Package a Python Script into a Command-Line Tool


## Introduction

Welcome to the Command Line Query Script, a powerful tool for performing various database operations through the command line. This script leverages the SQLite database system to enable you to create tables, insert data, delete records, and query your database effortlessly.

## Getting Started

### Prerequisites

- **Python 3.x**: Make sure you have Python 3.x installed. If not, you can download it from the [official Python website](https://www.python.org/downloads/).

### Installation

1. Clone this repository or download the script to your local machine.

2. Open your command-line terminal and navigate to the directory where the script is located.

3. Install the required `click` library using `pip`:

   ```bash
   pip install click
   ```

## Usage

The Command Line Query Script is simple to use:

1. **Running the Script**: Execute the script by providing the name of your SQLite database as an argument. For example:

   ```bash
   python script.py your_database.db
   ```

   Replace `script.py` with the actual filename of the script and `your_database.db` with the name of your SQLite database file.

2. The script will then create a user table if it doesn't already exist and perform various operations on it.

## Features

- **Create a User Table**: The script will create a user table in your database if it does not already exist. This table has columns for `id` and `username`.

- **Insert Users**: It will insert sample users into the user table: 'rc381', 'ab123', and 'cd567'.

- **Delete Users**: You can remove specific users from the user table. In the example, 'rc381' is deleted.

- **Query Users**: The script performs a query to retrieve and display the usernames of all current users in the user table.

## Example

After running the script as described in the "Usage" section, you will see the following output:

```bash
Creating table...
inserting...
Deleting...
Querying...
current users:
('ab123',)
('cd567',)
Closing connection...
Finished
```

## Support and Feedback

If you encounter any issues or have suggestions for improvement, please feel free to [open an issue](https://github.com/your_username/your_project/issues) on the project's GitHub repository.

Thank you for using the Command Line Query Script!