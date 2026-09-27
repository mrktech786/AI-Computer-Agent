from agent.config.settings import Settings
from agent.security.policy import PermissionPolicy

def test_terminal_disabled_by_default():
    policy = PermissionPolicy(Settings(require_approval=True, terminal_enabled=False))
    assert policy.terminal_enabled is False
