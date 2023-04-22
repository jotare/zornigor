import re

from pydantic import ConstrainedStr


class Slug(ConstrainedStr):
    regex = re.compile(r"^[a-z0-9-]+$")
