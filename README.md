# juvant-os-extensions

Extensions for [juvant-os](https://github.com/juvantlabs/juvant-os): optional capabilities a company adds to its Chief of Staff. juvant-os installs, checks, updates and removes them; they are developed here.

| Extension | What it does | State |
|---|---|---|
| [`hello`](hello/) | A greeting. Shows what an extension looks like and tests the whole path | Demo |

Needs juvant-os v2.1.0 or later.

## Use one

Ask the Chief of Staff, for example: "install the `hello` extension from juvantlabs/juvant-os-extensions". It shows you what the extension does and the permissions it wants, and you confirm.

## How an extension is made

One folder per extension, named after its id:

```
hello/
  extension.json            what it is and what it needs
  README.md                 for the CEO
  skills/<name>/SKILL.md    instructions, with more .md, .json or .txt beside them
  limits.json               optional: rules that deny or ask, never exemptions
  config.example.json       optional, with config.schema.json: the company's settings
```

Text only: no scripts, hooks, settings, agents or links. A skill's name is `<id>-<name>`, and its top has only a one-line `name` and `description`. CI runs the same checks as the installer (`tools/validate.py`).

A service that works outside the company's session (a bot, a server) has its own repository; the extension names it in `service`.

## Releases

Each extension has its own, with the tag `<id>-v<version>` matching `extension.json`. juvant-os installs only published releases, pinned to their commit: a published tag never moves.

## License

MIT. Security reports: see juvant-os's [SECURITY.md](https://github.com/juvantlabs/juvant-os/blob/main/SECURITY.md).
