"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://top.gg/bot/832137823309004800/invite

"""
import random
import discord
from discord.ext import commands
import aiohttp
from datetime import datetime

# lcoal imports
from src.utils import _fetch
from src.utils import weather_image_list, WEATHER_API_KEY

class APIBaseUserCommands(commands.Cog, name="External API Based User Commands Using aiohttp"):
    """ Collection of External API Based Commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="joke")
    async def get_random_joke(self, ctx):
        """ Get random jokes

        command: !joke
        API: https://v2.jokeapi.dev/
        """
        joke_api = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single'
        async with ctx.typing():
            try:
                result = await _fetch(joke_api)
                random_joke = result["joke"]
                await ctx.send(f"```{random_joke}```")
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    @commands.command(name="fact")
    async def get_random_fact(self, ctx):
        """ Get amazing random fact

        command: !fact
        API: https://uselessfacts.jsph.pl
        """
        fact_api = 'https://uselessfacts.jsph.pl//random.json?language=en'
        async with ctx.typing():
            try:
                result = await _fetch(fact_api)
                radnom_fact = result['text']
                await ctx.send(f"```{radnom_fact}```")
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    # not using the _fetch function because of content_type=None
    @commands.command(name="quote")
    async def get_random_quote(self, ctx):
        """ Get Random Quote by zenquote

        command: !quote
        API: https://zenquotes.io
        """
        url = 'https://zenquotes.io/api/random'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json(content_type=None)

                try:
                    random_quote = data[0]['q']
                    author = data[0]['a']
                    await ctx.send(f"```{random_quote} -{author} ```")
                except Exception as e:
                    await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    @commands.command(name="gh")
    async def get_github_userdata(self, ctx, username: str):
        """ Get Github User Data Using

        command: !gh <user_name>
        API: https://api.github.com
        """
        git_api = f'https://api.github.com/users/{username}'
        async with ctx.typing():
            try:
                user_data = await _fetch(git_api)
                user_embed = discord.Embed(
                    title=user_data['name'], description=user_data["company"])
                user_embed.add_field(
					name='Public Repos', value=user_data['public_repos'])
                user_embed.add_field(
                    name='Followers', value=user_data['followers'])
                user_embed.add_field(
                    name='Following', value=user_data['following'])
                user_embed.add_field(
                    name='Location', value=user_data['location'])
                user_embed.add_field(
                    name='Created At', value=user_data['created_at'][:10])
                user_embed.add_field(
                    name='Updated at', value=user_data['updated_at'][:10])
                user_embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
                user_embed.set_image(url=user_data['avatar_url'])

                await ctx.send(embed=user_embed)
            except Exception:
                await ctx.send(f'```{username} is not a GitHub user.```')

    @commands.command(name="ifsc")
    async def get_bankdata(self, ctx, ifsc_code: str):
        """ Get Indian Bank Details by IFSC Code

        command: !ifsc <ifsc_code>
        API: https://ifsc.razorpay.com
        """
        razorpay_api = f"https://ifsc.razorpay.com/{ifsc_code}"
        async with ctx.typing():
            try:
                bank_data = await _fetch(razorpay_api)
                embed = discord.Embed(
                    title=bank_data["BANK"], description=bank_data["ADDRESS"])
                embed.add_field(name="District", value=bank_data["DISTRICT"])
                embed.add_field(name="State", value=bank_data["STATE"])
                embed.add_field(name="UPI Available", value=bank_data["UPI"])
                embed.add_field(name="Contact Number",
                                value=bank_data["CONTACT"])
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
                await ctx.send(embed=embed)

            except Exception:
                await ctx.send(f'```{ifsc_code} is not a valid Ifsc Code.```')

    @commands.command(name="weather")
    async def get_weather(self, ctx, *args):
        """ Get Your City weather

        command: !weather <city_name>
        API: https://openweathermap.org/
        """
        city_name = ' '.join(args)
        weather_api = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={WEATHER_API_KEY}"
        async with ctx.typing():
            try:
                weather_data = await _fetch(weather_api)

                feels_like = round(weather_data["list"][0]["main"]["temp"] - 273.0)
                temp_min = round(weather_data["list"][0]["main"]["temp_min"] - 273.0)
                temp_max = round(weather_data["list"][0]["main"]["temp_max"] - 273.0)
                pressure = weather_data["list"][0]["main"]["pressure"]
                humidity = weather_data["list"][0]["main"]["humidity"]
                sea_level = weather_data["list"][0]["main"]["sea_level"]

                weather_embed = discord.Embed(
                    title=f'{weather_data["city"]["name"]}- {weather_data["city"]["country"]}', color=discord.Color.blue())
                weather_embed.add_field(
                    name="Weather", value=weather_data['list'][0]['weather'][0]['description'])
                weather_embed.add_field(name='Feels Like', value=feels_like)
                weather_embed.add_field(name="Min | Max", value=f'{temp_min}  |  {temp_max}')
                weather_embed.add_field(name="Pressure", value=pressure)
                weather_embed.add_field(name='Humidity', value=humidity)
                weather_embed.add_field(name='Sea Level', value=sea_level)

                weather_embed.set_thumbnail(
                    url=f"http://openweathermap.org/img/w/{weather_data['list'][0]['weather'][0]['icon']}.png")
                weather_embed.set_author(
                    name="OpenWeatherAPI", url="https://openweathermap.org/")
                weather_embed.set_image(
                    url=random.choice(weather_image_list))
                await ctx.send(embed=weather_embed)
            except Exception as e:
                await ctx.send(f'```I am not able to find the {city_name}.```')

    @commands.command(name="dog")
    async def get_random_dog_picture(self, ctx):
        """ Get Random Pictures Of Dogs

        command: !dog
        API: https://dog.ceo
        """
        dog_api = "https://dog.ceo/api/breeds/image/random"
        async with ctx.typing():
            try:
                result = await _fetch(dog_api)

                dog_picture_url = result["message"]
                embed = discord.Embed(title="bow! bow!")
                embed.set_image(url=dog_picture_url)
                embed.set_author(
                    name="Dog API", url='https://dog.ceo/dog-api/')
                await ctx.send(embed=embed)
            except Exception as e:
                await ctx.send(f'```{type(e).__name__} - {e}```')

    @commands.command(name="fox")
    async def get_random_fox_picture(self, ctx):
        """ Get Random Picture of Foxes

        command: !fox
        API: https://randomfox.ca
        """
        fox_api = 'https://randomfox.ca/floof/'
        async with ctx.typing():
            try:
                result = await _fetch(fox_api)

                fox_picture_url = result["image"]
                embed = discord.Embed(title="howls!")
                embed.set_image(url=fox_picture_url)
                embed.set_author(
                    name="foxAPI", url='https://randomfox.ca/')
                await ctx.send(embed=embed)
            except Exception as e:
                await ctx.send(f'```{type(e).__name__} - {e}```')

    @commands.command(name="cat")
    async def get_random_cat_picture(self, ctx):
        """ Get Random Pictures of cats

        Command: !cat
        Api: https://thatcopy.pw/catapi/rest/
        """
        cat_api = "https://thatcopy.pw/catapi/rest/"
        async with ctx.typing():
            try:
                result = await _fetch(cat_api)

                cat_picture_url = result["url"]
                embed = discord.Embed(title="Meow! Meow!")
                embed.set_image(url=cat_picture_url)
                embed.set_author(
                    name='catAPI', url='https://thatcopy.pw/catapi/')
                await ctx.send(embed=embed)
            except Exception as e:
                await ctx.send(f'```{type(e).__name__} - {e}```')


def setup(bot: commands.Cog):
    bot.add_cog(APIBaseUserCommands(bot))
