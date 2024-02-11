# Telegram Reader

This project is designed to read messages from a Telegram channel and store them in a database.

## Features

- Connects to a Telegram channel and retrieves messages.
- Parses the messages and extracts relevant information.
- Stores the messages in a database for further analysis or processing.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/telegram-reader.git`
2. Install the required dependencies: `npm install`

## Configuration

Before running the project, you need to provide the necessary configuration. Create a `.env` file in the root directory of the project and add the following variables:

TELEGRAM_API_ID=       // The API ID provided by Telegram for authentication.
TELEGRAM_API_HASH=     // The API hash provided by Telegram for authentication.
TELEGRAM_SESSION_STRING=   // The session string obtained after authenticating with Telegram.
TELEGRAM_GROUP_ID=     // The ID of the Telegram group or channel from which messages will be retrieved.
DB_USER=               // The username for the database connection.
DB_PASSWORD=           // The password for the database connection.
DB_HOST=               // The host address of the database server.
DB_NAME=               // The name of the database to store the messages.
DATABASE_URL=          // The URL of the database server.

