---
layout: page
permalink: /life_outside_data/
title: Life outside data
description: A growing collection of your cool projects.
nav: false
nav_order: 4
display_categories: [Travel, Books, TV and movies, Music]
horizontal: false
---

{% if page.display_categories contains "Travel" %}
<section>
    <h2>Travel</h2>
    <p>I'm a keen traveller and enjoy seeing different cultures and foods from other places. I've been fortunate in having being able tot travel to many places, including some as part of my PhD travels. Some of my personal highlights of my travels have included the Southern USA, Tokyo, Munich, and Rome. </p>
</section>
{% endif %}

{% if page.display_categories contains "Books" %}
<section>
    <h2>Book</h2>
    <p>I've always enjoyed esponiage novels, alongside fantasty and thrillers, and bits and pieces of non-fiction. I have a
    <a
    href="https://www.goodreads.com/user/show/46128883-conor-hamill" rel="external nofollow noopener" target="_blank">Goodreads account</a> which is really just a database of things I've read and want to read. Some of my person favourites are below.</p>
</section>
{% endif %}

{% if page.display_categories contains "TV and movies" %}
<section>
    <h2>Tv and movies</h2>
    <p>This is the text for the tv and movies section.</p>
</section>
{% endif %}

{% if page.display_categories contains "Music" %}
<section>
    <h2>Music</h2>
    <p>This is the text for the music section.</p>
</section>
{% endif %}
