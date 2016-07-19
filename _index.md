---
title: Számítástudományi és Információelméleti Tanszék
layout: home
content:
    - oktatas
    - kutatas
    - munkatarsak
    - rolunk
---

# Hírek

{% for item in this.news %}
## {{item.header.date}} - {{item.header.title}}
{{item.body}}

{% endfor %}

<div class="col-md-3 col-md-offset-1">
<h3>Kapcsolat</h3>
<img alt="minipic" src="./fenykepek/katona.jpg" title="=100x20">
</div>
