<p align="center">
  <a href="https://py-contributors.github.io/awesomeScripts/"><img src="https://capsule-render.vercel.app/api?type=rect&color=ffdd00&height=100&section=header&text=Cybel%202.0.0&fontSize=80%&fontColor=ffffff" alt="website title image"></a>

  <h2 align="center">👉 Discord Bot implemented in Python 👈</h2>
</p>

<img style="border-radius: 20%" align="right" src="images/cybel_icon.jpg" height="200" width="200" alt="pycontributors logo">

- [Features](#features)
  - [Report a Bug](#report-a-bug)
  - [How to use/test](#how-to-usetest)
    - [Server testing](#server-testing)
    - [Run with Docker](#run-with-docker)
    - [Run locally](#run-locally)
  - [Run in Debug Mode](#run-in-debug-mode)
  - [Beta Version](#beta-version)
- [Upcoming Feature](#upcoming-feature)
- [Changelog](#changelog)
- [Supported Versions](#supported-versions)
  - [V2.0.0 Release](#v200-release)
  - [v1.0.2 Release (19/12/2021)](#v102-release-19122021)
  - [V1.0.1 Release (14/12/2021)](#v101-release-14122021)
  - [v1.0.0 Release (12/12/2021)](#v100-release-12122021)
- [Under Review Features](#under-review-features)
- [Support Here](#support-here)
- [Author](#author)
- [Suggestion/Feedbacks](#suggestionfeedbacks)
- [Maintainers 😎](#maintainers-)
- [Social Channel 💻 - Connect with like minded people](#social-channel----connect-with-like-minded-people)
- [License](#license)

## Features

- Admin Commands for server management with powerful moderation
- Stay connected every time with 99% uptime
- Custom welcome message for each user when joining
- Separate DM message upon joining the server\
- Postgres Database for storing data
- Utility async APIs
- Log Everything with embed message
- AutoMod - Delete offensive word automatically
- Use the bot to its full potential without ever annoying anyone
- Modern Pythonic API using async/await syntax
- Easy to use with an object-oriented design
- Optimized for both speed and memory
- Member can report misconduct, malicious behavior, or inappropriate content.
- Published and approved on Top.gg website. check [here]
(https://top.gg/bot/832137823309004800/invite)
- [More Features]((#upcoming-feature)) coming soon...

Invite **Cybel** into your server

- [Cybel Stable](https://top.gg/bot/832137823309004800/invite)
- [Cybel Beta](https://discord.com/api/oauth2/authorize?client_id=831918257166090250&permissions=142337&scope=bot) # deprecated/removed

### Report a Bug

- [Report a Bug](https://github.com/orgs/Py-Contributors/discussions)

### How to use/test

#### Server testing

- if you want to test it in server please Use the Invite link [here](https://top.gg/bot/832137823309004800/invite)

#### Run with Docker

1. Create .env file in root directory and add the following variables. Sample env file is [here](/.env.sample)

```bash
DISCORD_TOKEN=Discord bot token [get it from here](https://discord.com/developers/applications)
WEATHER_API_KEY=OpenWeatherMap API key [get it from here](https://openweathermap.org/api)
DATABASE_URL=postgres://username:password@localhost:5432/database_name
```

2. Run the docker-compose command to run the bot

```bash
docker compose up
``` 


#### Run locally

1. Create .env file in root directory and add the following variables. Sample env file is [here](/.env.sample)

```bash
DISCORD_TOKEN=Discord bot token [get it from here](https://discord.com/developers/applications)
WEATHER_API_KEY= OpenWeatherMap API key [get it from here](https://openweathermap.org/api)
DATABASE_URL=postgres://username:password@localhost:5432/database_name
```

2. Create a virtual environment and install the dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the bot

```bash
python3 bot.py
```

### Run in Debug Mode

```bash
python app.py -d
```

### Beta Version

beta version deprecated in 1.0.0 release. It will be removed in v1.0.2 release.

## Upcoming Feature

- Role Upgrade
- Reactions Roles
- Music bot feature(play music in voice channel from youtube)
- Add database to keep record of server's activity
- Admin can access server's activity
- Some new useful apis
- `remindme`  the bot remind you about something in future
- More features coming soon...
- please use [discussion](https://github.com/codePerfectPlus/cybel/discussions) to suggest new features

## Changelog

check [changelog](/CHANGELOG.md) for full information

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |   Based on        | Status       |
| ------- | ------------------ | ----------        | -------      |
| 2.0.0   | :white_check_mark: | Discord.py v2.0.1 |  Not Stable  |
| 1.0.2   | :white_check_mark: | Discord.py v1.7.3 |  Stable      |

### V2.0.0 Release

- [x] Upgrading code base for Discord.py 2.0.0 documentation
- [x] Better code structure
- [x] Better Error commands handling
- [x] Under devlopment

### v1.0.2 Release (19/12/2021)

- [x]  More control over bot's behavior(change bot's avatar, name, nickname, status, etc): (added in v1.0.2)
- [x]  Bot notifications if user edit or delete the message in the server: (added in v1.0.2)
- [x]  Bot can change the nickname of the user in the server: (added in v1.0.2)
- [x]  postgresql database support: (added in v1.0.2)
- [x]  Admin can access the misconduct/spam behaviour report status of the member from db: (added in v1.0.2)
- [x]  Bot can have record of the user's report status in db: (added in v1.0.2)
- [x]  Optimize code for performance & bug fix: (added in v1.0.2)
- [x]  more...

### V1.0.1 Release (14/12/2021)

- [x]  `AutoMod`: Curse word deletion improved (added: v1.0.1)
- [x]  get bot latency : (added: v1.0.1)
- [x]  slot machine : (added: v1.0.1)
- [x]  change username of self(admin) : (added: v1.0.1)
- [x]  source code command : (added: v1.0.1)
- [x]  Bot can send message to user in DM: (added: v1.0.1)
- [x]  Optimize code for performance : (added: v1.0.1)
- [x]  Bug fixes
- [x]  more...

### v1.0.0 Release (12/12/2021)

- [x]  member can report someone to admin: like for bullying, bad behaviour : (added: v1.0.0)
- [x]  Create server Instant Invite : (added: v1.0.0)
- [x]  create bot invite : (added: v1.0.0)
- [x]  Kick/Ban User: (added: v1.0.0)
- [x]  Get user avatar : (added: v1.0.0)
- [x]  delete role : (added: v1.0.0)
- [x]  Server(Id, Name, Owner, Icon) : (added: v1.0.0)
- [x]  Get Member Avatar : (added: v1.0.0)
- [x]  Bug fix: (added: v1.0.0)
- [x]  optimize code for performance : (added: v1.0.0)


## Under Review Features

- one command role assignment to all members: (under review)
- send dm message to all member in server: (under review)

## Support Here

<a href="https://www.buymeacoffee.com/codeperfectplus"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a book&emoji=📖&slug=codeperfectplus&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff"></a>

## Author

- Project: Cybel[Discord Bot]
- Author: CodePerfectPlus
- Language: Python
- Github: [GitHub](https://github.com/codePerfectPlus)
- Website: [CodePerfectPlus](http://codeperfectplus.herokuapp.com/)
- Email: [Email Me](mailto:codeperfectplus@gmail.com)

## Suggestion/Feedbacks

- Official Discord Server: [PyContributors](https://discord.gg/JfbK3bS)

## Maintainers 😎

- [Deepak Raj](https://github.com/CodePerfectPlus)

## Social Channel 💻 - Connect with like minded people

- [Discord/PyContributors](https://discord.gg/FXyh2S3)

## License

- [MIT](https://github.com/Py-Contributors/cybel-discord.py/blob/main/LICENSE)

<p align="center">
<a href="https://api.github.com/repos/py-contributors/awesomescripts/contributors"><img src="http://ForTheBadge.com/images/badges/built-by-developers.svg" alt="Built by Developers"></a>
<a href="https://github.com/codePerfectPlus"><img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="built with love"></a>
</p>

