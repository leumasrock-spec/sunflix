#!/usr/bin/env python3
"""Gera data/sunflix.json a partir dos JSONs do yt-dlp em /tmp/pl_<id>.json (yt-dlp --extractor-args youtube:lang=pt --flat-playlist -J)."""
import json
cats=[
 ("PLiefZK1VyHwCDOau6tEvwgPH8ijgRljnr","celula","Biologia – Estrutura Celular","🔬","Samuel Rocha"),
 ("PLiefZK1VyHwDGoUTU4kvmH3WFhFs4lTfN","genetica","Genética","🧬","Samuel Rocha"),
 ("PLEQBXs2MZBrY","evolucao","Evolução das Espécies","🦕","Samuel Rocha"),
 ("PLQ_N0msRRr9o","corpo","Sistemas do Corpo","🫀","Samuel Rocha"),
 ("PLC8Licfb4CyU","ciencias","Ciências","🌱","Samuel Rocha"),
 ("PLiefZK1VyHwC3VOExpnsXE5Ij37Ok1Aad","quimica","Ciência – Química 9º ano","⚗️","Samuel Rocha"),
 ("PLYVSodBzQ5vo","leis","Leis Ambientais – Estudo","⚖️","Samuel Rocha"),
 ("PLHtEsGd9bQgT8ktUG9k5GMpDZmHE4DNNp","fiscal","Fiscal Ambiental","🌳","Luanda Medeiros"),
 ("PL_3Omi8Qsh0Uj03F2onoo2cjhUF7bteZi","direito","Direito Ambiental","🏛️","Supremo"),
]
out=[]
for pid,slug,label,icon,owner in cats:
    d=json.load(open(f'/tmp/pl_{pid}.json'))
    vids=[{"id":e["id"],"t":e["title"],"c":e.get("channel") or ""} for e in d["entries"] if e.get("title") and not e["title"].startswith("[")]
    out.append({"slug":slug,"label":label,"icon":icon,"owner":owner,"playlist":pid,"orig":d["title"],"videos":vids})
    print(label,len(vids))
out.append({"slug":"saneamento","label":"Saneamento – vídeos de referência","icon":"💧","owner":"Drive: videos.txt","playlist":None,"orig":"videos.txt",
 "videos":[{"id":"OzS8VZS3Axs","t":"Sistema de Abastecimento de Água para iniciantes","c":"Trecos de Engenharia"},
  {"id":"Cse-8p1R6Cs","t":"Episódio #2 – Tipos de reservatórios","c":"Eng. Aldo Gaiotto"},
  {"id":"f61JxBM8wrY","t":"Estação de Tratamento de Esgoto – Como funciona","c":"ITEC CURSOS"}]})
links=[l for l in json.load(open('/workspace/acesso-pdf/links.json')) if l['section'] not in ('self','sunflix')]
json.dump({"cats":out,"links":links},open('data/sunflix.json','w'),ensure_ascii=False,indent=1)
