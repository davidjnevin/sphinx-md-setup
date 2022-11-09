def replace_snippets(active=False) -> dict[str, str]:
    """replace_snippets.

    A dictionary of keys and their replacements.

    :param active:
    :rtype: dict[str, str]
    """
    if active:
        myst_substitutions: dict[str, str] = {
            "project": "I'm a **substitution**",
            "mysite": "[davidjnevin](https://www.davidjnevin.com)",
        }
    else:
        myst_substitutions: dict[str, str] = {}
    return myst_substitutions
