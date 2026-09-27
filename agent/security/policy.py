from dataclasses import dataclass
from agent.config.settings import Settings

@dataclass
class PermissionPolicy:
    settings: Settings

    @property
    def require_approval(self) -> bool:
        return self.settings.require_approval

    @property
    def terminal_enabled(self) -> bool:
        return self.settings.terminal_enabled

    def approve(self, action: str) -> bool:
        if not self.require_approval:
            return True
        answer = input(f'Approve action "{action}"? [y/N]: ').strip().lower()
        return answer in {"y", "yes"}
