import json,pathlib
D=pathlib.Path(__file__).parent
data=json.load(open(D/'data/sunflix.json'))
s=json.dumps(data,ensure_ascii=False).replace('</','<\\/')
(D/'index.html').write_text((D/'template.html').read_text().replace('__DATA__',s),encoding='utf-8')
print('ok',len(s))
