---
title: Számítástudományi és Információelméleti Tanszék
layout: home
content:
    - oktatas
    - kutatas
    - munkatarsak
    - rolunk
    - angolul
---
# Hírek

{% for item in this.news %}
## {{item.header.title}} 
{{item.body}}

({{item.header.date}})
{% endfor %}

[Archívum](./hirek/index.html)