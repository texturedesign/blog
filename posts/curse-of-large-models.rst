.. title: The Curse of Large Models
.. author: alexjc
.. slug: curse-of-large-models
.. date: 2021-10-05 19:19 UTC
.. tags: the-WHY
.. type: rest
.. license: CC BY-NC-ND 4.0
.. previewimage: /images/cemetery.thumbnail.jpg
.. description: Large models in ML are a manifestation of Silicon Valley excesses; luckily, they don't make sense from a business perspective either.


In the context of machine learning, let's call "Large Models" (LMs) those with hundreds of billions (B) parameters — for instance OpenAI's GPT-3.

Large models are a manifestation of Silicon Valley excesses: just scrape the internet without regard to license, train a larger version of an architecture invented elsewhere, throw massive amount of somebody else's resources at the problem, then brag about how simple the "solution" is while disregarding sustainability.

**Luckily, this doesn't make sense from a business perspective either!**

    “Large models are a manifestation of Silicon Valley excesses; luckily, they don't make sense from a business perspective either.”

In the early stages of ``texture·design``, we investigated the potential for LMs to help generate images and materials.  This post includes our analysis of large models, along with an exploration of the technology from a *business & product perspective*.  It should help to explain why:

* AGI-as-a-service makes less sense than people think.
* GPT-4 was announced to be the same size as GPT-3.
* OpenAI is focusing on specialized services for codegen.
* Large models are cursed to always take second place.

Any improvements in Machine Learning are worth investigating, for example to generate better quality media or to make computer interactions more creative.  Let's see how large models fit into the picture — with a bias towards computer graphics and computer vision.  (For related discussion about the ethics of *language* models [1]_ or sustainability aspects [2]_, please refer to the footnotes for references that cover this topic in-depth.)


Defining Large Models
=====================

While it's still a relatively new technology, there are some underlying patterns behind the large models that have been published to-date.

1. **Generative** — LMs do more than just understanding or classifying data.  They produce something, often in the form of sequences.
2. **End-To-End** — LMs process raw inputs (e.g. user instructions) and convert them into outputs (e.g. a paragraph of text).  They are trained on the entire problem end-to-end.
3. **Monolithic** — LMs operate as one large system with the same principles applied everywhere.  You can't remove or replace parts of it!
4. **General Architecture** — LMs tend to use general building-blocks in order to avoid domain-specific tricks (e.g. 2D image convolution).
5. **Large-Scale Dataset** — LMs rely on large quantities of *noisy* data with a rather *weak* structure (e.g. freeform text).
6. **Heavy Computation** — LMs require dedicated GPU farms to train, and even then requiring weeks or months to train.

As a consequence, large models perform differently than traditional machine learning and thus play a different role when deployed as solutions.


Roles of Machine Learning
=========================

In practice, there are different times and places where machine learning can be used.  How the model is used is more important its capacity!

* During **development**, certain kinds of models facilitate research and prototyping as they can be easily repurposed.  These models can be regular size but very flexible models (e.g. ResNet or VGG) or bigger in size and more general (e.g. large models).

* In a **live application**, there are different types of models deployed: a) for discovery and b) for producing.  Models for discovery help explore and understand ideas quickly, and models for producing will output media of near-final quality for direct use.

* The ideal "capacity" of a model depends on your application.  Sometimes you want a smaller network that runs in a browser or mobile, other times you might want a regular network to deploy to desktop clients, on occasion a very large cloud-only model makes sense.

Now, let's cross reference these different roles and go through the reasons that are commonly used to justify LMs.


Why Large Models?
=================

Hypothesis #1: Large models approximate datasets better.
    Taking academic metrics to assess the quality of a model on a fixed test set (e.g. "perplexity" in NLP) doesn't reflect the full picture, but it's a starting point!  While LMs may score better with these metrics, in practice it's often possible to reuse samples directly from the dataset itself, for example a database of textures.  In such case of "in-distribution" samples, the benefit of LMs is more questionable since the quality of the output will likely never match the original.

    | **Q: Is a LM any better than using the dataset itself for in-distribution samples?**
    | A: No. (likely never)  If there's appropriate data, use it.  If it's cheap to acquire, capture it.

Hypothesis #2: Large models can approximate datasets with plausible deniability.
    In some cases, you may not have the rights to the dataset itself and therefore can't use it directly.  In this case, large models can help!  Since LMs can't reliably reproduce all training inputs, and because these models are not transparent and explainable, they help provide plausible deniability when large companies circumvent copyright regulations.

    | **Q: Can a LM be used to circumvent copyright statutes and regulations?**
    | A: Yes. (for now)  As long as companies don't care about the ethics involved.

.. note::
    A major goal for ``texture·design`` is to build systems (algorithms, data and tools) that are jointly owned by their creators.  As such, we're not pursuing the business opportunities in such copyright laundering.

Hypothesis #3: Larger models are more creative in novel situations.
    How about out-of-distribution samples, such as textures that may be hard to capture and not available in a dataset?  In those cases, there are a variety of classic algorithms from computer vision that may serve the same purpose.  For instance, adjusting the color, replacing parts of an image, copying parts of another texture, mashing-up multiple sources...  These kinds of algorithms have matured significantly over decades, in particular over the last years thanks to deep learning.

    | **Q: Are out-of-distribution samples from a LM better than other algorithms?**
    | A: No. (open research)  The quality & flexibility of computer vision algorithms is high!

Hypothesis #4: Larger models infer a rich latent space.
    Let's consider the kind of implicit knowledge that large models could learn.  It's possible LMs can provide some insights or understanding of the space of textures.  However, there are other approaches to help structure a dataset, for example: regular-sized models like convnets, procedurally authored parameter spaces, and example-based solutions.

    | **Q: Would the latents from LMs be any better than from a regular-size model?**
    | A: No. (tough chance)  Larger models are not explainaible or transparent, so harder to use.

    | **Q: Is a LM better than procedurally authored parameter space?**
    | A: No. (likely never)  Artists are experienced with procedural tools, interfaces are mature.

    | **Q: Are these parameter spaces better than an example-based approach?**
    | A: No. (just different)  There are great tools and UIs for finding examples from a database.

Hypothesis #5: Large models provide better interactions in natural language.
    This leads us into natural language.  Many large models are implemented with architectures designed for NLP, so that makes it easier to interact with language since they are generally designed for that.  However, for specific problems, smaller language models will work work faster, more reliably and with less risk (e.g. avoiding biased or offensive patterns from the training data).

    | **Q: Does a LM improve the experience for language-based interaction?**
    | A: Maybe. (somewhat)  It will provide more flexibility at a significant cost.

Hypothesis #6: Larger models can do few-shot learning. (prompting)
    Academic researchers in natural language are very excited about few-shot or even one-shot learning, where you can give a set of examples to a LM and have it produce results.  In the context of computer vision, it's easy to forget that a large number of existing algorithms are example-based, hence similar to one-shot.  There's great research combining example-based solutions with regular-sized deep learning models, but it's not been done for large models.

    | **Q: Can a LM do any better than example-based algorithms?**
    | A: No. (open research)  Specialized models combined w/ examples will likely remain better.

Hypothesis #7: Larger models are sample efficient for downstream tasks.
    There's also the argument that large models are better suited at known tasks they are not directly trained on.  You'd train on a web-scale dataset and then reuse the model to solve more specific tasks where less data is available.  However, it's a very expensive way of doing pre-training when many alternatives are available in computer vision.

    | **Q: Is a LM an improvement over alternative pre-training methods?**
    | A: No. (tough chance)  Techniques like fine-tuning or meta-learning are fine too.

Hypothesis #8: Larger models can generalize better to unknown problems.
    In mature businesses, there aren't that many unknown problems!  Indeed, it the company's job to make sure the problem is well defined and understood by the time the application is shipped to customers.  As such, the ability for large models to generalize in unknown domains is mostly interesting for the early stages of research & development.

    | **Q: Can large models help solve unknown problems?**
    | A: Maybe. (occasionally)  This will remain in the domain of prototyping, not production.

Hypothesis #9: Large models can be distilled to solve specialized problems.
    There's a reason why individuals and companies specialize, so they can solve problems better and more efficiently.  For large models, it's not computationally or logistically feasible to train them on all possible tasks with all expertise from all domains.  Even if that was possible, that knowledge could not be "compressed" down (or distilled) to the necessary quality without using domain-specific training data, procedural knowledge, or testing procedures.

    | **Q: Can large models be distilled to solve specific problems better?** 
    | A: No. (likely never)  There's no free lunch; you need to do the work!

    | **Q: Can large models be distilled with only 'general' algorithms?** 
    | A: No. (touch chance)  Any solution designed with domain insights will do better.


Unbundling Large Models
=======================

While many see LMs as the future of machine learning or even the future of software, our analysis here suggests a more pragmatic view.  Since there are many risks and questionable benefits for the deployment of LMs (as defined today), it makes more sense to break down each of their properties and see where the business trends are heading.

1. Fast vs. Slow
    | Assuming near identical quality, an output that's generated faster is better than slower.  You can produce more this way!  Market forces suggest models will be built to run faster, and thus likely as small as possible.
2. Explainable vs. Black Box
    | A model that's easier to understand is preferable for people to work with as they'll get better results with less effort.  Market forces push models to be easier to understand and control by their users.
3. End-to-End vs. Modular
    | A more modular system is easier to repurpose in other aspects of the product & business.  It's also easier to maintain and improve.  Market forces pressure models to be more modular and reusable.
4. Specialized vs. General
    | As specialized model requires fewer resources (both compute and data), is easier to understand and thus less risky.  Market forces suggest specialized models for high-value domains.

In summary, market forces are challenging every technical aspect of Large Models.  It's likely we'll see major changes in our approach to deep learning, also in the short term.  Even OpenAI has become skeptical about scaling up for GPT-4 [3]_, and is making strategic moves towards specializing its model for code generation rather than continuing to scale.

.. class:: summary

TL;DR. Large models suffer from being *Jack of All Trades* yet master of none, which makes their deployment hard to justify for pragmatic businesses.  As they are defined today, LMs will remain interesting for art projects, research & development, prototyping and other supporting roles in pre-production.  Whether for language or computer vision, we expect LMs to evolve into something radically different in the future!


.. [1] `On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? <https://dl.acm.org/doi/pdf/10.1145/3442188.3445922>`_ doi:10.1145/3442188.3445922
.. [2] `Energy and Policy Considerations for Deep Learning in NLP <https://arxiv.org/abs/1906.02243>`_, arXiv:1906.02243
.. [3] `Sam Altman Confirms Rumours about GPT-4 <https://analyticsindiamag.com/gpt-4-sam-altman-confirms-the-rumours/>`_
.. [4] Teaser photo by `Scott Rodgerson <https://unsplash.com/@scottrodgerson>`_ on Unsplash.
