from agent.config.settings import settings
from agent.computer.screen import ScreenController
from agent.security.policy import PermissionPolicy


def main() -> None:
    policy = PermissionPolicy(settings)
    screen = ScreenController()
    print("AI Computer Agent — Phase 1 MVP")
    print(f"Approval required: {policy.require_approval}")
    print(f"Terminal enabled: {policy.terminal_enabled}")
    print(f"Screen size: {screen.size()}")
    print("MVP initialized. No autonomous high-impact action is enabled.")
