import bot_utility


def get_response(message: str) -> str:
    # except the first char ? or !
    p_message = message.lower()[1:]

    if p_message[:5] == "troll":
        return bot_utility.randomize_case(p_message[5:])

    if p_message == 'roll':
        return bot_utility.roll()

    if p_message == 'coinflip' or p_message == 'coin':
        return bot_utility.coin_flip()

    if p_message == 'tip':
        return bot_utility

    if p_message == 'help' or p_message == 'commands':
        return help()

    return help()


def help():
    help_text = """
    Available commands:
    - `roll`                    prints 1-6 randomly
    - `coinflip/coin`           prints Heads or Tails
    - `troll string_to_troll`   JUST loOk aT ThIs
    """

    return help_text
