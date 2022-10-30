Installation
=========

Run it locally
---------

1. Create .evn file in root directory and add the following variables. Sample Env file is [here](/.env.sample)

.. code-block:: bash

    # .env file
    DISCORD_TOKEN= Discord bot token [get it from here](https://discord.com/developers/applications)
    WEATHER_API_KEY= OpenWeatherMap API key [get it from here](https://openweathermap.org/api)
    DATABASE_URL=postgres://username:password@localhost:5432/database_name

2. Create a virtual environment and install the dependencies

.. code-block:: bash

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

3. Run the bot

.. code-block:: bash

    $ python3 bot.py

### Run in Debug Mode

.. code-block:: bash

    $ python3 bot.py --debug

Supported Versions
----------

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |   Based on        | Status       |
| ------- | ------------------ | ----------        | -------      |
| 2.0.0   | :white_check_mark: | Discord.py v2.0.1 |  Not Stable  |
| 1.0.2   | :white_check_mark: | Discord.py v1.7.3 |  Stable      |

