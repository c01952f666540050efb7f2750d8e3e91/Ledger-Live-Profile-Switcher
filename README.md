# Ledger Live Profile Switcher

This is an experimental way to change the accounts that appear in Ledger Live.

Trying to follow the specs that are listed in this doc:
[https://github.com/LedgerHQ/ledger-live-common/blob/develop/docs/account.md]

The next thing would be to make sure this work as a standalone cli tool.
This is how we're oping it works by default:

1. Asks in a loop what addresses need to be added
2. Copies the original app.json and copies injected version in
3. Maybe launches ledger live

The next steps would be to add functionality that would back up the entire Ledger Live folder, and can "fully restore" when needed.

1. Run tool to back up folder with varying levels of depth
2. Inject folder either from a list of "saved" types or via adding as above
3. Restore from list of saved types when required

The next potential step after that would be to implement a minimal python web framework to run this in the browser.
This would be because some users might be more familiar with managing this as via the ledger live logs viewer.
