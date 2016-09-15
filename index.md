---
content: [oktatas, kutatas, munkatarsak, rolunk, same_in_english]
layout: home
news:
- body: "\n2016 szeptember\xE9t\u0151l \xFAj doktori t\xE1rgyat ind\xEDtunk Halad\xF3\
    \ adatszerkezetek \xE9s algoritmuselemz\xE9si technik\xE1k c\xEDmmel. A t\xE1\
    rgy keret\xE9ben a hallgat\xF3k megismerkedhetnek  n\xE9h\xE1ny modern, j\xF3\
    l haszn\xE1lhat\xF3 adatszerkezettel, a kurzus c\xE9lja, hogy bemutassa \xE9s\
    \ szeml\xE9ltesse a v\xE9letlen (\xE1tlagos) esetekre vonatkoz\xF3 becsl\xE9sek\
    \ n\xE9h\xE1ny m\xF3dszer\xE9t, \xE9s m\xE1s manaps\xE1g sokszor alkalmazott technik\xE1\
    t (pl. sim\xEDtott vagy param\xE9teres bonyolults\xE1gi elemz\xE9s).\n\n[Tant\xE1\
    rgyi adatlap](https://portal.vik.bme.hu/kepzes/targyak/VISZDV05/)\n\n"
  header: {date: 2016-08-30, layout: page, title: "\xDAj doktori t\xE1rgy"}
- body: "2016 szeptember\xE9t\u0151l \xFAj koll\xE9g\xE1nk, Kaszanitzky Vikt\xF3ria\
    \ csatlakozik tansz\xE9k\xFCnkh\xF6z. Vikt\xF3ria f\u0151leg a n\xE9met nyelv\u0171\
    \ k\xE9pz\xE9sbe \xE9s a Rendszeroptimaliz\xE1l\xE1s t\xE1rgy oktat\xE1s\xE1ba\
    \ fog bekapcsol\xF3dni. \n\n\n"
  header: {date: 2016-08-29, layout: page, title: "\xDAj munkat\xE1rsunk"}
- body: "\nWiener G\xE1bor, tansz\xE9k\xFCnk egyetemi docense a BME idei \xFCnnepi\
    \ szen\xE1tusi \xFCl\xE9s\xE9n habilit\xE1ci\xF3s oklevelet vehetett \xE1t. \n\
    \n[http://www.bme.hu/hirek/20160530/Orom_buszkeseg_es_elismeresek_hetvegeje](http://www.bme.hu/hirek/20160530/Orom_buszkeseg_es_elismeresek_hetvegeje)\n\
    \n"
  header: {date: 2016-06-07, layout: page, title: "Habilit\xE1ci\xF3"}
- body: "\nSzeszl\xE9r D\xE1vid, tansz\xE9k\xFCnk egyetemi docense a BME idei \xFC\
    nnepi szen\xE1tusi \xFCl\xE9s\xE9n a M\u0171egyetem Kiv\xE1l\xF3 Oktat\xF3ja elismer\xE9\
    sben r\xE9szes\xFClt. \nEbben a kit\xFCntet\xE9sben azok az oktat\xF3k r\xE9szes\xFC\
    lhetnek \u2013 az Egyetemi Hallgat\xF3i K\xE9pviselet javaslat\xE1ra \u2013 akiket\
    \ az \xF6sszes \xE1ltaluk oktatott kurzuson \xF6sszesen legal\xE1bb 100 hallgat\xF3\
    \ v\xE9lem\xE9nyezett \xE9s a kialakult sorrendben az egyetemi \xF6sszes\xEDt\xE9\
    sben az els\u0151 \xF6t helyen szerepeltek.\n\n[http://www.bme.hu/hirek/20160530/Orom_buszkeseg_es_elismeresek_hetvegeje](http://www.bme.hu/hirek/20160530/Orom_buszkeseg_es_elismeresek_hetvegeje)"
  header: {date: 2016-06-06, layout: page, title: "M\u0171egyetem Kiv\xE1l\xF3 Oktat\xF3\
      ja elismer\xE9s"}
title: "Sz\xE1m\xEDt\xE1studom\xE1nyi \xE9s Inform\xE1ci\xF3elm\xE9leti Tansz\xE9k"

---
# Hírek

{% for item in this.news %}
## {{item.header.title}} 
{{item.body}}

({{item.header.date}})
{% endfor %}

[Archívum](./hirek/index.html)