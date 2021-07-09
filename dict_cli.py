import requests, typer, json

app = typer.Typer()

@app.command()
def define(word:str):
  response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_GB/{word}').json()
  if "title" not in response:
    # meanings = json.dumps(response[0]['meanings'], indent=2)
    # print(json.dumps(response, indent=2))
    meanings = response[0]['meanings']
    definitions = [{
      'pos': meaning['partOfSpeech'],
      'defs': [defi['definition'] for defi in meaning['definitions']]
    } for meaning in meanings]

    for definition in definitions:
      print(f'  PoS: {definition["pos"]}\n  Defs:')
      for defi in definition['defs']:
        print(f'\t{defi}')
      print('')
  else:
    print('\tGuess this dictionary doesn\'t have all the answers...\n\
        Or you did a typo.')


@app.command()
def synonym():
  print("Not yet implemented")
  pass

if __name__ == "__main__":
  app()
