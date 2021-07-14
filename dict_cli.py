"""
Small dictionary CLI that uses the Free Dictionary API.
Built using the Typer library.
Usage:
  $> python3 main.py <define/synonym> <word>
"""

import requests, typer, json

from typing import Optional

app = typer.Typer()
state = {'verbose': False}

# TODO: add -p flag to add pronunciation
@app.command("define")
def print_word_definitions(word:str, example:Optional[bool]=typer.Option(False, "--example", "-e")):
  response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_GB/{word}').json()
  if "title" not in response:
    # print(json.dumps(response, indent=2))
    meanings = response[0]['meanings']
    if not meanings:
      print("\n  Found the word, but no definitions.\n\tSorry, human :(")
      exit()
    definitions = [{
      'pos': meaning['partOfSpeech'],
      'defs': [defi['definition'] for defi in meaning['definitions']],
      'eg': [defi['example'] for defi in meaning['definitions'] if "example" in defi and example]
    } for meaning in meanings]

    for definition in definitions:
      print(f'  PoS:\t  {definition["pos"]}')
      print(f'  Defs:')
      for defi in definition['defs']:
        print(f'\t- {defi}')
      if example and definition['eg']:
        print(f'  E.g:\t  {definition["eg"][0]}')
      elif example: print('  E.g:\t  None given...')
      print('')
  else:
    print('\tGuess this dictionary doesn\'t have all the answers...\n\
        Or you did a typo, silly human...')


@app.command("synonym")
def print_word_synonyms(word:str):
  response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_GB/{word}').json()
  if "title" not in response:
    # print(json.dumps(response, indent=2))
    meanings = response[0]['meanings']
    synonyms = [{
      'pos': meaning['partOfSpeech'],
      'syns': [defi['synonyms'] for defi in meaning['definitions'] if "synonyms" in defi],
    } for meaning in meanings]

    for synonym in synonyms:
      print(f'  PoS:\t  {synonym["pos"]}')
      print('  Syns:')
      if len(synonym['syns']) > 0:
        for syn in synonym['syns']:
          print(f'\t  {", ".join(syn)}')
      else:
        print(f'\t  There is no other way of saying this...')
      print('')

  else:
    print('\tGuess this dictionary doesn\'t have all the answers...\n\
        Or you did a typo, silly human...')


@app.callback()
def main(verbose:Optional[bool]=typer.Option(False, "--verbose", "-v")):
  """
  It's a basic dictionary right here in your terminal... Rejoice!
  """

  print('  Let me look that up for you...')

  if verbose:
    state['verbose'] = True
    print('  Will write verbose output...')



if __name__ == "__main__":
  app()
