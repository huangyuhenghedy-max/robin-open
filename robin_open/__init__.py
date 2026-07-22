"""Robin Open: transparent multi-agent workflow primitives."""

from .providers import openai_compatible_worker
from .runtime import Candidate, Event, Workflow, WorkflowResult

__all__ = ["Candidate", "Event", "Workflow", "WorkflowResult", "openai_compatible_worker"]
__version__ = "0.2.0"
