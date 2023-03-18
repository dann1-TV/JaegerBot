import bot_basic
import tarkov

def get_response(message: str, tarkov_data: dict) -> str:
    p_message = message.lower()[1:] # except the first char ? or !

    # troll is the keyword and the rest of the maessage is trolled
    if p_message[:5] == "troll":
        return bot_basic.randomize_case(p_message[5:])

    if p_message == 'roll' or p_message == 'dice':
        return bot_basic.dice()

    if p_message == 'coinflip' or p_message == 'coin':
        return bot_basic.coin()

    if p_message == 'tip':
        return tarkov.random_tip(tarkov_data['tips'])

    # TODO: Tag tips with PvP, PvE, money, hideout
    # TODO: Tip search
    if p_message == 'map':
        return tarkov.random_map(tarkov_data['maps'])

    # EFT Money making playlist
    if p_message == 'money':
        return "https://www.youtube.com/playlist?list=PLhxeo6sgtUlo3_2d8salSzhAz6gZcvbYa"

    if p_message == 'about' or message == 'code' or message == 'source':
        return "https://github.com/dann1-TV/JaegerBot"


    if p_message == 'help' or p_message == 'commands':
        return help()

    return help()


def help():
    return  """
    Available commands:
    - `roll`                    prints 1-6 randomly
    - `coinflip/coin`           prints Heads or Tails
    - `troll string_to_troll`   JUST loOk aT ThIs
    - `tip`                     Jaeger will give you a tip to improve
    - `map`                     prints a random map name
    - `money`                   How to make easy money
    - `about/source/code`       Developer information
    """