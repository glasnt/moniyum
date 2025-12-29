---
layout: page
description: the plushie travel log
---

<style>
    .preview {             
        aspect-ratio: 1;
        object-fit: cover;
        object-position: top; border-radius: 5px;
    }
    .preview-list {
        display: flex;
        flex-wrap: wrap;
    }

    .post-preview {
        width: calc((100% - 24px) / 3); 
		display: inline-block;
		background-position: center;
		background-size: cover;
		margin: 3px 3px;
    }
    .post-preview>a { 
        text-decoration: none; 
    }
</style>

<i>The travelling 'ailurus fulgens'. Travel buddy of @glasnt. They/them.</i>

<div class="preview-list">
{% for post in site.posts %}
<div class="post-preview">
    <a href="{{ post.url | prepend: site.baseurl }}">
        <img class="preview" src="{{site.baseurl}}{{post.media}}">
    </a>
</div>
{% endfor %}
</div>
