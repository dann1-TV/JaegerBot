import bot_basic
import tarkov

def get_response(message: str, tarkov_data: dict) -> str:
    command = message.lower()[1:] # except the first char ? or !

    # troll is the keyword and the rest of the maessage is trolled
    if command[:5] == "troll":
        return bot_basic.randomize_case(command[5:])

    if command == 'roll' or command == 'dice':
        return bot_basic.dice()

    if command == 'coinflip' or command == 'coin':
        return bot_basic.coin()

    if command == 'tip':
        return tarkov.random_tip(tarkov_data['tips'])

    # TODO: Tag tips with PvP, PvE, money, hideout
    # TODO: Tip search
    if command == 'map':
        return tarkov.random_map(tarkov_data['maps'])

    # EFT Money making playlist
    if command == 'money':
        return "https://www.youtube.com/playlist?list=PLhxeo6sgtUlo3_2d8salSzhAz6gZcvbYa"

    if command == 'about' or command == 'code' or command == 'source':
        return "https://github.com/dann1-TV/JaegerBot"


    if command == 'help' or command == 'commands':
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

    Prepend a `!`/`?` to the command for a **public**/**private** reply
    """