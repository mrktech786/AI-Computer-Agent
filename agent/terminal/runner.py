import subprocess
from agent.security.policy import PermissionPolicy

SAFE_COMMANDS = {"python", "python3", "node", "npm", "git", "pwd", "whoami"}

class TerminalRunner:
    def __init__(self, policy: PermissionPolicy) -> None:
        self.policy = policy

    def run(self, command: list[str]) -> subprocess.CompletedProcess[str]:
        if not command or command[0].lower() not in SAFE_COMMANDS:
            raise PermissionError("Command is not in the Phase-1 allowlist.")
        if not self.policy.terminal_enabled:
            raise PermissionError("Terminal execution is disabled by configuration.")
        if not self.policy.approve(" ".join(command)):
            raise PermissionError("Action was not approved.")
        return subprocess.run(command, text=True, capture_output=True, timeout=60, check=False)
