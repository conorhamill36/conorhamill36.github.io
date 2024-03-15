---
layout: page
title: Life outside data
description: A growing collection of your cool projects.
nav: false
nav_order: 4
display_categories: [Travel, Books, TV and movies, Music]
horizontal: false
---

{% if page.display_categories contains "Travel" %}
<section>
    <h2>Travel Section</h2>
    <p>This is the text for the travel section.</p>
</section>
{% endif %}

{% if page.display_categories contains "Books" %}
<section>
    <h2>Fun Section</h2>
    <p>This is the text for the books section.</p>
</section>
{% endif %}

{% if page.display_categories contains Tv and movies" %}
<section>
    <h2>Fun Section</h2>
    <p>This is the text for the tv and movies section.</p>
</section>
{% endif %}

{% if page.display_categories contains "Music" %}
<section>
    <h2>Fun Section</h2>
    <p>This is the text for the music section.</p>
</section>
{% endif %}