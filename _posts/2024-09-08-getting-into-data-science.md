---
layout: post
title: So you want to get into data science?
date: 2024-09-08 17:30:00
description: Some advice on how I would go about moving into data science if I had to do it again
tags: data-science
categories: posts
---

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/hike-unsplash-image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/dashboard-unsplash-image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Images taken from <a href="https://unsplash.com">unsplash.com </a>.
</div>

## Introduction

As with all the content on this website and in my blog posts, the opinions expressed here are my own and now those of my employer.
More and more often recently, I've been asked by students and others "So, what do I need to do to get a job as a data scientist?".
I've realised, although I've lots of thoughts on this, the answers I've been giving have been rather rambling and unstructured answers, with more points than any person can reasonably hold to while talking to me at a careers fair.
So I decided to write this blog post to bring these thoughts together in one place.
This article will be biased towards someone with a degree in natural sciences (e.g. physics), who has had some experience in programming and statistical analysis, and obviously it will also be biased towards my personal opinions and recollections.

## Do you really want to get into data science?

As always before embarking on anything new which will take up a lot of your time, you should ask yourself two key questions: 1. why do I want to do this? and 2. do I really know what I'm getting into?
I highlight these two questions because putting a lot of effort into breaking into data science before realising that it isn't really what you want to do or it isn't really what you thought it would be, would be less than ideal.
Data science is often not as glamorous as as it is depicted, although the perception is now a bit more grounded than it was in the days of "the sexiest job of the 21st century".
As a data scientist, you are required to undertake several different roles at once, stay up to date with a technology landscape that changes extremely quickly, work with requirements that are often unclear and shifting, and, most crucially, you are required to make an impact on the business; to senior management you are a relatively new investment and they want a return on that investment.
Many technology and software-based roles have these aspects to various degrees, but these are all realities of being a data scientist nonetheless.
Part of this comes from data scientist roles looking different across different teams and how the rapid change in the world of data and AI has led to high expectations from business leaders.
My personal opinion however is that if you want a job that uses programming and statistical modelling to solve problems and you want to convince business leaders you've solved those problems, you could do far worse than a role as a data scientist.

## Roles in data beyond data science

A point sometimes neglected is that the volume and variety of data roles beyond data scientist are growing year-on-year.
As data science practices mature in businesses, the range of professions is increasing, with more defined roles than before.
This trend seems to closely follow that of business that you need a much more extensive procedure than just training a model to really transform a business.
Some roles, especially data engineers and machine learning engineers, are more sought after than data scientists, and will commonly pay better.
There are roles that require a different range of skills and still provide substantial business value.
FOr example, data analysts can give great insights from data and clearly inform business decision making, without the need for python and complex algorithms.
In short, it will be well worth you're time exploring which one of these roles you think might best fit your skill set and what you enjoy doing.

## How would I got about learning data science again

So, you've looked the other roles and decided it's for you; what do you need to learn and how do you sell yourself?
If I was to go back in time and try again to move into data science again, I would still follow the same high-level path I took before:

1. Learn the required skills
2. Complete some personal projects to exhibit those skills
3. Advertise those personal projects to prospective employers

I will describe each of this in order in more detail below.

### Learning the skills you need

There are a wide range of skills that data scientists need to have, some of which you need to excel at, while knowing the basics of others can suffice.
Knowing which of these is which can be tricky.

Before picking which resources you want to use to learn, consider through what medium you best learn.
I find I personally learn the best through textbooks, but collections of videos seem to be very effective for others.
Additionally, be wary of falling into the trap of using bite-sized pieces of knowledge to give yourself the illusion of learning, when you're really just skimming the surface of the required knowledge and missing deeper connections.
Andrej Karpathy described this very well in this [recent post on X/Twitter](https://x.com/karpathy/status/1756380066580455557?lang=en), from which I highlight a paragraph that I find quite impactful:

> So for those who actually want to learn. Unless you are trying to learn something narrow and specific, close those tabs with quick blog posts. Close those tabs of "Learn XYZ in 10 minutes". Consider the opportunity cost of snacking and seek the meal - the textbooks, docs, papers, manuals, longform. Allocate a 4 hour window. Don't just read, take notes, re-read, re-phrase, process, manipulate, learn.

&nbsp;&nbsp;&nbsp;&nbsp; Andrej Karpathy, [Twitter/X](https://x.com/karpathy/status/1756380066580455557?lang=en)

Below I describe roughly the order I would undertake learning, assuming a prior degree in some sort of science.
Many of these resources are described in my [page on data science resources](/data_science_resources/).

- Learn software development:
  - with [the missing semester course from MIT](https://missing.csail.mit.edu/).
  - this might feel like a dry one to start off with, but since this is probably the most fundamental skill here and all others rely on it, it is a good place to start. Being comfortable with you terminal and being able to collaborate using Git will make future learnings and your eventual job much easier.
- Learn python:
  - I don't have an exact python course I would recommend and given there are many different levels you may be starting at, I would steer you towards the [choice of python learning paths on Real Python](https://realpython.com/learning-paths/).
  - The main python website [python.org](https://www.python.org/about/gettingstarted/) has also indexed many useful resources
  - Out of all the skills here, python is the one you probably want to put the most time into being good at, because it will be the end product you will be producing a lot of the time.
- Learn statistical modelling:
  - The book "An Introduction to Statistical Learning" is available with examples in R or Python [here](https://www.statlearning.com/). I've found this book to cover the level of detail needed to understand modelling as a data scientist in a very digestible way.
- Learn how to do machine learning:
  - This point has a lot of similarities with the above, but I think this one begins the focus on the python packages used more
  - Andrew Ng's [machine learning specialisation](https://www.deeplearning.ai/courses/machine-learning-specialization/) on Coursera remains a classic for a reason, although pytorch has established itself over Tensorflow as the python deep learning framework of choice
  - For a book alternative, I would recommend "Machine Learning with PyTorch and Scikit-Learn"
- Learn (some) cloud computing:
  - How much you need to know will vary role by role, but understanding the fundamentals is good.
  - I don't have a stand-out recommendation for learning cloud computing, but have had a good experience learning with Udemy's courses on AWS in the past. This [one may be a good introduction](https://www.udemy.com/course/introduction-to-cloud-computing-on-amazon-aws-for-beginners/) for those new to AWS or cloud computing.

After (or maybe while) you have learnt the above skills, you can begin to undertake some personal projects.

### Doing some personal projects

You need to show that you can use your skills to solve problems and explain why you've made the choices that you have.
Picking a good personal project can be tricky; you want something that is complex enough to challenge yourself, but not something that isn't fundamentally fixable.
Remember that training a good machine learning model is only one of the components of provifing a business-ready solution - if you are able to implement an end-to-end solution, possibly deploying in the cloud, that can be very impressive (but do remain vigilant of AWS costs piling up rapidly!).

Do something that is either relevant to an industry you're interested in or that you're personally interested in. This makes it mroe likely the problem and solution will be more relevant to roles you're looking for and more interesting all round.
Alternatively, if you can apply some data science to your current role, that is an excellent way to show you can take initative and solve problems.

### Advertise these projects to potential employers

Finally, you want to make sure that potential recruiters will see these projects, and you can set yourself apart from other applicants.
Put the code that you have developed in a public Github repository and make sure it has a story behind it -

## Conclusions

## Resources