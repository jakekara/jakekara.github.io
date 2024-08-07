---
layout: project
title: "Margo: Margin Notes for Jupyter Notebooks"
description: "For my software engineering master's degree thesis, I built and demonstrated uses for a system that uses Jupyter Notebooks as Python modules."
image: MargoDemo
alt: Screenshot of Margo parser Lark grammar
tags: 
    - Python
    - Jupyter
link: https://github.com/margo-notebooks/modular-notebook-tutorial
twitterImage: /assets/images/square/Margo-1200.png
---

<iframe width="100%" height="315" src="https://www.youtube.com/embed/6EgsAb56jY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

For my master's thesis in Software Engineering from Harvard Extension School, I
developed a suite of software for enhancing Jupyter Notebooks to be used as
Python modules, and in other unintended contexts.  

[Margo Loader](https://github.com/margo-notebooks/margo-loader-py) extends Python's `import` statement so you can import Jupyter Notebooks as if they were `.py` files.

Since you might not want to execute every cell in a notebook when you import it,
I developed a syntax called "Margo" for annotating cells with "margin notes" —
specially formatted comments that provide extra information to interpreters. If you use syntax like `# :: ignore-cell ::` you can instruct Margo Loader to skip that cell during import.

For a live tutorial on how to write modular Jupyter Notebooks, and on Margo in
general, check out [this notebook on binder](https://mybinder.org/v2/gh/margo-notebooks/modular-notebook-tutorial/HEAD?filepath=README.ipynb):

{% include imgset.html slug="MargoDemo" alt="A screenshot of my modular notebooks tutorial running in Binder" %}  

I designed Margo syntax to be flexible, so that `ignore-cell` keyword isn't
actually part of Margo's, it's just a directives that the Margo Loader software
considers meaningful. In addition to directives, Margo syntax supports arbitrary
data serialization in several formats. This allows you to effectively extend the
notebook format in a backwards compatible manner. I've demonstrated in my thesis
that Margin notes can be used to encode `requirements.txt` inside a notebook in
order to integrate a `.ipynb` file with `pip`, and they can be used to encode a
list of input and output files to integrate a notebook with a tool like GNU
Make.  

Taking this concept even further, I desmontrated that developers can build new
graphical interface features for Notebooks and serialize associated data in
margin notes. To demonstrate this I built a proof of concept editor UI that
supports hierarchical cell relationships.

For example, imagine this notebook with two cells, one which tests another cell:

{% include imgset.html slug="MargoEditor" alt="The Margo Editor UI prototype defining a cell that tests another cell" %}  

When serialized as a `.ipynb` file, the relationships are stored in Margo margin notes:

```python
# :: cell.id: 'e973c97f' ::

def say_hello(to="World"):
    return f"Hello, {to}!"
```

```python
# :: cell.id: 'dd974423' ::
# :: rel.tests: "e973c97f" ::
def test_say_hello():
    assert say_hello() == "Hello, World!"
```

## Links

* Modular Notebooks Tutorial live demo - [https://mybinder.org/v2/gh/margo-notebooks/modular-notebook-tutorial/HEAD?filepath=README.ipynb](https://mybinder.org/v2/gh/margo-notebooks/modular-notebook-tutorial/HEAD?filepath=README.ipynb)
* Modular Notebooks Tutorial code repo - [https://github.com/margo-notebooks/modular-notebook-tutorial](https://github.com/margo-notebooks/modular-notebook-tutorial)
* Margo Notebooks GitHub Organization - [https://github.com/margo-notebooks/](https://github.com/margo-notebooks/)
* Margo Loader GitHub repo - [https://github.com/margo-notebooks/margo-loader-py](https://github.com/margo-notebooks/margo-loader-py)
* Margo Parser GitHub repo - [https://github.com/margo-notebooks/margo-parser-py](https://github.com/margo-notebooks/margo-parser-py)
* Margo Editor live demo - [https://margo-editor.netlify.app/](https://margo-editor.netlify.app/)
* Margo Editor GitHub repo - [https://github.com/margo-notebooks/margo-editor-ts](https://github.com/margo-notebooks/margo-editor-ts)
* Color Extraction Methodology repo - [https://github.com/jakekara/color-extraction-methodology/](https://github.com/jakekara/color-extraction-methodology/)
* Color Extraction Methodology live demo - [https://mybinder.org/v2/zenodo/10.5281/zenodo.4554402/](https://mybinder.org/v2/zenodo/10.5281/zenodo.4554402/)
* Thesis on Harvard DASH - [https://nrs.harvard.edu/URN-3:HUL.INSTREPOS:37367613](https://nrs.harvard.edu/URN-3:HUL.INSTREPOS:37367613)
* Video tutorial on using Jupyter Notebooks as Python modules - [https://youtu.be/6EgsAb56jY0](https://youtu.be/6EgsAb56jY0)

