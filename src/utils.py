import requests
import discord


def _getGitUserData(username):
    """ Function to get GitHUb User Data in json format """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        userData = response.json()
        return userData


def _sendEmbed(title, description, name, value, url):
    """ Send Discord Embed """
    embed = discord.Embed(title=title, description=description)
    embed.add_field(name=name, value=value)
    embed.set_image(url=url)
    return embed


def _IfscDetails(ifscCode):
    """ Function to get Bank details by IFSC number """
    url = f"https://ifsc.razorpay.com/{ifscCode}"
    response = requests.get(url)
    if response.status_code == 200:
        bankData = response.json()
        return bankData


def _UrlShortner(website):
    """ Url Shortner """
    data = {'url': website}
    response = requests.post('https://cleanuri.com/api/v1/shorten', data=data)
    if response.status_code == 200:
        shortUrl = response.json()['result_url']
        return shortUrl


def _getRandomDogPicture():
    """ Get Random Picture of Cats & Dogs """
    url = 'https://random.dog/woof.json'
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()

        fileSize = result['fileSizeBytes']
        print(fileSize)
        dogImageUrl = result['url']

        embed = _sendEmbed(title="Random Dog image",
                           description=f"File Size: {fileSize}",
                           name="CYBEL BoT",
                           value=f"ImageURL: {dogImageUrl}",
                           url=dogImageUrl)
        return embed


def _getRandomCatPicture():
    url = "https://thatcopy.pw/catapi/rest/"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()

        catPictureURL = result["url"]
        embed = _sendEmbed(title="Random Cat image",
                           description=f"File Size: Unknown",
                           name="CYBEL BoT",
                           value=f"ImageURL: {catPictureURL}",
                           url=catPictureURL)
        return embed