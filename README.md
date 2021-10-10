<h1 align="center"><b>❤ Sophia v3 ❤</b></h1>


<p align="center"><a href="https://t.me/SophiaSupport_Official"><img src="https://telegra.ph/file/f6afa44d010598c379503.jpg" width="400"></a></p>
<p align="center">
  <h4 align="center"><b>A Powerful, Smart And Simple Group Manager <br> ... Written with  Pyrogram and Telethon...</b></h4>  

<p align="center">
    <a href="https://github.com/dihanofficial/sophiabot/stargazers"><img src="https://img.shields.io/github/stars/dihanofficial/Sophia?label=Stars&style=flat-square&logo=github&color=F10070" alt="Stars" /></a>
</p>
<p align="center">
    <a href="https://app.codacy.com/manual/dihanofficial/Sophiabot/dashboard"> <img src="https://img.shields.io/codacy/grade/4d58f2a402b54aed8a7d95f7add45a81?color=brightgreen&logo=codacy&logoColor=green&style=for-the-badge" alt="Codacy" /></a>
    <a href="https://github.com/dihanofficial/sophiabot"> <img src="https://img.shields.io/github/repo-size/dihanofficial/sophiabot?color=orange&logo=github&logoColor=green&style=for-the-badge" /></a>
    <a href="https://github.com/dihanofficial/sophiabot/commits/dihanofficial"> <img src="https://img.shields.io/github/last-commit/dihanofficial/sophiabot?color=brown&logo=github&logoColor=green&style=for-the-badge" /></a>
    <a href="https://github.com/dihanofficial/sophia/issues"> <img src="https://img.shields.io/github/issues/dihanofficial/sophia?color=blueviolet&logo=github&logoColor=green&style=for-the-badge" /></a>
    <a href="https://github.com/dihanofficial/sophiabot/network/members"> <img src="https://img.shields.io/github/forks/dihanofficial/sophiabot?color=red&logo=github&logoColor=green&style=for-the-badge" /></a>  
    <a href="https://pypi.org/project/Telethon/"> <img src="https://img.shields.io/pypi/v/telethon?color=yellow&label=telethon&logo=python&logoColor=green&style=for-the-badge" /></a>
</p>


 <b> ⭐️ Thanks to everyone who starred Sophia, That is the greatest pleasure we have ! </b> 



## Avaiilable on Telegram as [@SophiaSLBot](https://t.me/sophiaslbot)



### Deploy To Heroku</h4>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/dihanofficial/Sophiabot)




## Join my Updates Channel & Support Chats
<a href="https://t.me/SophiaSUPPort_official"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram"></a>
<a href="https://t.me/SophiaUpdates"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>



### Configuration

There are two possible ways of configuring your bot: a config.py file, or ENV variables.

The preferred version is to use a `config.py` file, as it makes it easier to see all your settings grouped together.
This file should be placed in your `SophiaBot` folder, alongside the `__main__.py` file. 
This is where your bot token will be loaded from, as well as your database URI (if you're using a database), and most of 
your other settings.

It is recommended to import sample_config and extend the Config class, as this will ensure your config contains all 
defaults set in the sample_config, hence making it easier to upgrade.

An example `config.py` file could be:
```
from SophiaBot.sample_config import Config

class Development(Config):
    OWNER_ID = 12345  # your telegram ID
    OWNER_USERNAME = "dihanrandila"  # your telegram username
    API_KEY = "your bot api key"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [12345678]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
```

If you can't have a config.py file (EG on Heroku), it is also possible to use environment variables.
The following env variables are supported:
 - `ENV`: Setting this to ANYTHING will enable env variables

 - `TOKEN`: Your bot token, as a string.
 - `OWNER_ID`: An integer of consisting of your owner ID
 - `OWNER_USERNAME`: Your username

 - `DATABASE_URL`: Your database URL
 - `MESSAGE_DUMP`: optional: a chat where your replied saved messages are stored, to stop people deleting their old 
 - `LOAD`: Space-separated list of modules you would like to load
 - `NO_LOAD`: Space-separated list of modules you would like NOT to load
 - `WEBHOOK`: Setting this to ANYTHING will enable webhooks when in env mode
 messages
 - `URL`: The URL your webhook should connect to (only needed for webhook mode)

 - `SUDO_USERS`: A space-separated list of user_ids which should be considered sudo users
 - `SUPPORT_USERS`: A space-separated list of user_ids which should be considered support users (can gban/ungban,
 nothing else)
 - `WHITELIST_USERS`: A space-separated list of user_ids which should be considered whitelisted - they can't be banned.
 - `DONATION_LINK`: Optional: link where you would like to receive donations.
 - `CERT_PATH`: Path to your webhook certificate
 - `PORT`: Port to use for your webhooks
 - `DEL_CMDS`: Whether to delete commands from users which don't have rights to use that command
 - `STRICT_GBAN`: Enforce gbans across new groups as well as old groups. When a gbanned user talks, he will be banned.
 - `WORKERS`: Number of threads to use. 8 is the recommended (and default) amount, but your experience may vary.
 __Note__ that going crazy with more threads wont necessarily speed up your bot, given the large amount of sql data 
 accesses, and the way python asynchronous calls work.
 - `BAN_STICKER`: Which sticker to use when banning people.
 - `ALLOW_EXCL`: Whether to allow using exclamation marks ! for commands as well as /.

### Python dependencies

Install the necessary Python dependencies by moving to the project directory and running:

`pip3 install -r requirements.txt`.

This will install all the necessary python packages.

  ### Database

If you wish to use a database-dependent module (eg: locks, notes, userinfo, users, filters, welcomes),
you'll need to have a database installed on your system. I use Postgres, so I recommend using it for optimal compatibility.

In the case of Postgres, this is how you would set up a database on a Debian/ubuntu system. Other distributions may vary.

- install postgresql:

`sudo apt-get update && sudo apt-get install postgresql`

- change to the Postgres user:

`sudo su - postgres`

- create a new database user (change YOUR_USER appropriately):

`createuser -P -s -e YOUR_USER`

This will be followed by you need to input your password.

- create a new database table:

`createdb -O YOUR_USER YOUR_DB_NAME`

Change YOUR_USER and YOUR_DB_NAME appropriately.

- finally:

`psql YOUR_DB_NAME -h YOUR_HOST YOUR_USER`

This will allow you to connect to your database via your terminal.
By default, YOUR_HOST should be 0.0.0.0:5432.

You should now be able to build your database URI. This will be:

`sqldbtype://username:pw@hostname:port/db_name`

Replace sqldbtype with whichever DB you're using (eg Postgres, MySQL, SQLite, etc)
repeat for your username, password, hostname (localhost?), port (5432?), and DB name.

  ## Modules
   ### Setting load order.

The module load order can be changed via the `LOAD` and `NO_LOAD` configuration settings.
These should both represent lists.

If `LOAD` is an empty list, all modules in `modules/` will be selected for loading by default.

If `NO_LOAD` is not present or is an empty list, all modules selected for loading will be loaded.

If a module is in both `LOAD` and `NO_LOAD`, the module will not be loaded - `NO_LOAD` takes priority.

   ### Creating your own modules.

Creating a module has been simplified as much as possible - but do not hesitate to suggest further simplification.

All that is needed is that your .py file is in the modules folder.

To add commands, make sure to import the dispatcher via

`from SophiaBot import dispatcher`.

You can then add commands using the usual

`dispatcher.add_handler()`.

Assigning the `__help__` variable to a string describing this modules' available
commands will allow the bot to load it and add the documentation for
your module to the `/help` command. Setting the `__mod_name__` variable will also allow you to use a nicer, user-friendly name for a module.

The `__migrate__()` function is used for migrating chats - when a chat is upgraded to a supergroup, the ID changes, so 
it is necessary to migrate it in the DB.

The `__stats__()` function is for retrieving module statistics, eg number of users, number of chats. This is accessed 
through the `/stats` command, which is only available to the bot owner.

## Starting the bot.

Once you've set up your database and your configuration is complete, simply run the bat file(if on windows) or run (Linux):

`python3 -m SophiaBot`

You can use [nssm](https://nssm.cc/usage) to install the bot as service on windows and set it to restart on /gitpull 
Make sure to edit the start and restart bats to your needs. 
Note: the restart bat requires that User account control be disabled.

For queries or any issues regarding the bot please open an issue ticket or visit us at [Support](https://t.m/SophiaSupport_Official)
## How to setup on Heroku 
For starters click on this button 
</details>  






#### Contributors
- [Dihan Randila](https://github.com/dihanofficial): Dev / Owner
- [InukaAsith](https://github.com/InukaAsith): Dev 
- [Deshadeeth Thisarana](https://github.com/Deshadeeth-Thisarana) 
- [Percy Official](https://github.com/PercyOfficial)

## Special Credits

- [DaisyX](https://github.com/teamdaisyx/daisyx)
- [TroJanzHEX](https://github.com/TroJanzHEX)
- [infotechbro](https://github.com/infotechbro/)
- [Thehamkercat](https://github.com/thehamkercat)
- [FridayUserbot](https://github.com/DevsExpo/FridayUserbot)
- [MissJuliaRobot](https://github.com/MissJuliaRobot/MissJuliaRobot)
- [ADV-Auto-Filter-Bot-V2](https://github.com/AlbertEinsteinTG/Adv-Auto-Filter-Bot-V2)
- [Image-Editor](https://github.com/TroJanzHEX/Image-Editor/)
- [WilliamButcherBot](https://github.com/thehamkercat/WilliamButcherBot)
- [Mr-Dark-Prince](https://github.com/Mr-Dark-Prince/)
- [Im-Janindu](https://github.com/imjanindu)

