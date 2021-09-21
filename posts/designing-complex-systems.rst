.. title: The Only Way to Design a Complex System
.. author: alexjc
.. slug: designing-complex-systems
.. date: 2021-09-20 20:20 UTC
.. tags: the-HOW
.. type: rest
.. license: CC BY-NC-ND 4.0
.. previewimage: /images/forest-canopy.thumbnail.jpg
.. description: How do you intentionally design a system that you know is complex?  Gall's law says you should start from a simple one.  Then what?

For ``texture.design`` to fulfill its purpose as a service generating custom-tailored materials for anyone, we need a combination of work that's automated and augmented, data that's synthesized and captured, software that follows rules but also able to learn, people with experience and fresh perspectives, technology that's old-school but also cutting-edge, and probably much more!

The question is: how do you intentionally design a system that you know is complex?

**The answer is: don't design a complex system, intentionally evolve a simple one!**

In the `previous post </blog/elephant-in-the-room/>`_, we saw how AI will help incrementally upgrade existing services — so theoretically speaking it makes sense to start simple.  But it also makes sense from a practical perspective too.


.. class:: main-quote

The Evolution of Complex Systems
================================

Taking such a "bottom-up" approach matches with the philosophies of John Gall, a famous systems theorist and author of the book *Systemantics: How Systems Really Work and How They Fail*, who famously said:

    "A complex system that works is invariably found to have **evolved from a simple system** that worked. The inverse proposition also appears to be true: a complex system designed from scratch never works and cannot be made to work. You have to start over, beginning with a simple system."
    
    — **John Gall**, systems theorist

This is known as Gall's law.

In some ways, it's an unsatisfying answer because it implies that starting with "advanced" but complex technology is a recipe for failure, and there are no shortcuts.  On the other hand, it's reassuring that the simplest way to approach this is the only one that's likely to succeed.


Building Openly
===============

Early spikes relating to ``texture.design`` — such as `texturize on GitHub <https://github.com/photogeniq/texturize>`_ — were built entirely openly.  Once that tool was in place, we tried to understand how these types of high-quality algorithms fit into the big picture with more prototypes, and we often hacked code together that ended up looking like... a stock media website.

Aarg! Now you can understand why we had a love/hate relationship with these prototypes.  There are already many stock media websites, why exactly would we build another?!  But that was Gall's Law trying to give us hints: "start simple and let it evolve." (So let's run with it.)

**Let's build a simple website that provides stock textures from scratch!**

The main difference is that we're setting out to do this *on purpose* this time around, and we're making it `open-source <https://github.com/texturedesign>`_ and building it publicly too.  We know that new and unexpected things will come up, because that always happens with such prototypes when you intentionally set out with a hypothesis...


.. class:: main-quote

The Scientific Method
=====================

Besides just letting the system evolve, there are some techniques that can *intentionally* help it grow in a way that takes into account previous body of knowledge accumulated by a project:

    "What's often missing from 'start simple' advice is that you have to have a map or hypothesis to go complex. You build something that lets you validate and get feedback on specific things about your hypothesis."
    
    — Mikko Mononen [1]_

**We call this a culture of intentional experimentation!**

With that in mind let's dig into the research questions we'd like to address (or address better this time) with our prototype; each of these is based on everything we've learned so far through dozens of prototypes and experiments.


Open Questions
==============

How to process public domain or creative commons data.
    Processing data from online sources is surprisingly challenging to do efficiently, and especially when this data has inconsistent structure.  What are the ethics of using the work of others if they used a free license without understanding the implications?

How to efficiently serve large quantities of images.
    It's difficult enough to store and transfer large datasets, but that changes for the worse when there's a **generative model** at play!  What are ways to use deep learning to increase efficiency of storage and transfering?

How to reduce power consumption and optimize processing.
    Large corporations pay for expensive cloud infrastructure, and they feel the need to use it as much as possible to make the most of their investment!  What happens if we make the computation happen only when needed?

How to put more abilities into the hands of users.
    It's easy to justify putting expensive algorithms on a server, but it reduces the amount of agency users have.  How can we use generative models to put controls into the hands of users, and let them have fun too?

We'll dedicate a separate blog post to each of these open questions to list our hypotheses.  Further, as a result of openly building this open source version, we hope to also have:

* Datasets for machine learning hobbyists to try out and learn from!
* Technology for websites from the community serving CC0 materials.


It'll be a fun experiment for us, feel free to follow along and share your ideas!  Watch our coding progress `on GitHub <https://github.com/texturedesign>`_, get regular updates via `Mastodon <https://creative.ai/@texturedesign>`_ or `my personal Twitter <https://twitter.com/alexjc>`_, or subcribe to the blog's `RSS feed <https://texture.design/blog/rss.xml>`_ for notifications.


.. [1] See Mikko Mononen's `tweet <https://twitter.com/MikkoMononen/status/1440191895108345860>`_ about integrating the scientific method.
.. [2] Teaser photo by `kazuend <https://unsplash.com/@kazuend>`_ on Unsplash.
