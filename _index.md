---
title: Számítástudományi és Információelméleti Tanszék
layout: home
content:
    - oktatas
    - kutatas
    - munkatarsak
    - rolunk
    - same_in_english
---
# Hírek

{% for item in this.news %}
## {{item.header.title}} 
{{item.body}}

({{item.header.date}})
{% endfor %}

[Archívum](./hirek/index.html)