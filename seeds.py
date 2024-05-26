from models import Authors, Quotes
import json

with open('authors.json') as f:
    lists = json.load(f)

for list in lists:
    u2 = Authors()
    u2 = u2.from_json(json.dumps(list)).save()

with open('qoutes.json') as f:
    lists = json.load(f)

for list in lists:
    quote = Quotes(quote=list.get('quote'), tags=list.get('tags'), author=Authors.objects(fullname=list.get('author')).first())
    quote.save()
