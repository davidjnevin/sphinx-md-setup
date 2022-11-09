% Sphinx-Next-Level documentation master file, created by
% sphinx-quickstart on Thu Nov  3 21:27:57 2022.
% You can adapt this file completely to your liking, but it should at least
% contain the root `toctree` directive.

```{include} ../../README.md
:relative-images:
```

```{warning}
This site is under heavy delvelopment.
```

So is this line appearing?

hello, {{project}} is the name of my project.

For more information read {doc}`usage`.

For installation instructions read {ref}`Installation`.

```{toctree}
:caption: 'Contents:'
:maxdepth: 3

usage
notebooks/TheZenOfPython
modules
```

## Indices and tables

```{eval-rst}
* :ref:`genindex`
* :ref:`modindex`
```
