"""Bob yang sedikit kosa kata menjawab"""
def response(hey_bob):
    """respon's Bob"""
    message = hey_bob.strip()
    if message.endswith(" "):
        return "Whatever."
    if message.isupper() and message.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if message.isupper():
        return "Whoa, chill out!"
    if message.endswith("?"):
        return "Sure."
    if message.endswith("!"):
        return "Whatever."
    if message == "":
        return "Fine. Be that way!"
    return "Whatever." 
