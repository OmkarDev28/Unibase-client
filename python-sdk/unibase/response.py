from dataclasses import dataclass
from typing import Any, Dict, Optional, Union, List

@dataclass
class UnibaseResponse:
    success: bool
    message: str
    data: Union[Dict[str, Any], List[Any], None] = None
    status_code: int = 200

    @classmethod
    def from_dict(cls, payload: Dict[str, Any], status_code: int = 200) -> "UnibaseResponse":
        return cls(
            success=payload.get("success", False),
            message=payload.get("message", ""),
            data=payload.get("data"),
            status_code=status_code
        )
