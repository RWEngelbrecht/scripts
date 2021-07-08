import requests, typer, json

app = typer.Typer()

@app.command()
def define(word:str):
  response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_GB/{word}').json()
  meanings = response[0]['meanings']
  definitions = [{
    'pos': meaning['partOfSpeech'],
    'defs': [defi['definition'] for defi in meaning['definitions']]
  } for meaning in meanings]

  for definition in definitions:
    print(\
    f'''\
    PoS: {definition['pos']}
    Def: {definition['defs']}
    ''')
  pass

@app.command()
def synonym():
  print("Not yet implemented")
  pass

if __name__ == "__main__":
  app()
