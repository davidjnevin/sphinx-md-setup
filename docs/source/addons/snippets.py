def replace_snippets() -> dict[str, str]:
    """replace_snippets.

    A dictionary of keys and their replacements.

    :rtype: dict[str, str]
    """
    myst_substitutions: dict[str, str] = {
        "project": "I'm a **substitution**",
    }
    return myst_substitutions
