from typing import Any, Dict, Union

FieldAndLevelStyles = Dict[str, Dict[str, Union[str, bool]]]

DEFAULT_FIELD_STYLES: FieldAndLevelStyles
DEFAULT_LEVEL_STYLES: FieldAndLevelStyles


def install(*args: Any, **kwargs: Any) -> Any : ...

def parse_encoded_styles(text: str) -> FieldAndLevelStyles : ...
