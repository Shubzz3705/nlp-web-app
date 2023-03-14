import paralleldots
paralleldots.set_api_key('tzBMqEHMltDPhInoKwWDfT8onL2dBqi4i60hQThHEoQ')

def ner(text):
    ner = paralleldots.ner(text)
    return ner
