"""
AttendeeList - Python library for People and Events.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the attendee type is invalid."""

    pass


def get_random_attendee(kind=None):
    """
    Return a list of random attendees as strings.

    :param kind: Optional "kind" of attendees.
    :type kind: list[str] or None
    :raise AttendeeList.InvalidKindError: If the kind is invalid.
    :return: The attendees list.
    :rtype: list[str]
    """
    return ["Peter", "Marta", "Yvonne"]
