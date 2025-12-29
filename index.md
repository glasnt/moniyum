---
layout: page
description: the plushie travel log
---

<style>
    .preview {             
        aspect-ratio: 1;
        object-fit: cover;
        object-position: top;
    }
    .preview-list {
        display: flex;
        flex-wrap: wrap;
    }

    .post-preview {
        width: calc((100% - 2rem) / 3); 
		display: inline-block;
		background-position: center;
		background-size: cover;
		margin: 5px 5px;
    }
</style>

<div class="preview-list">
{% for post in site.posts limit: 10  %}
<div class="post-preview">
    <a href="{{ post.url | prepend: site.baseurl }}">
        <img class="preview" src="{{site.baseurl}}{{post.media}}">
    </a>
</div>
{% endfor %}
</div>
