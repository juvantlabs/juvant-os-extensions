# juvant-os extensions

[![validate](https://github.com/juvantlabs/juvant-os-extensions/actions/workflows/validate.yml/badge.svg)](https://github.com/juvantlabs/juvant-os-extensions/actions/workflows/validate.yml)
[![juvant-os](https://img.shields.io/badge/juvant--os-v2.1%2B-blue)](https://github.com/juvantlabs/juvant-os/releases)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Optional capabilities for a company's Chief of Staff.** An extension adds skills to a [juvant-os](https://github.com/juvantlabs/juvant-os) company, and can add stricter limits. It never loosens one. juvant-os installs, checks, updates and removes extensions. This repository is where the official ones are developed and released.

- [Why extensions, and not just more skills](#why-extensions-and-not-just-more-skills)
- [Catalogue](#catalogue)
- [For the CEO: using an extension](#for-the-ceo-using-an-extension)
- [What an extension can and can't do](#what-an-extension-can-and-cant-do)
- [For developers: writing an extension](#for-developers-writing-an-extension)
- [Releasing](#releasing)
- [Contributing, security, license](#contributing)

---

## Why extensions, and not just more skills

There were already two ways to give the Chief of Staff a new capability. Neither fits everything.

**A new skill in juvant-os** reaches *every* company at its next update. That's right for what every company needs: a contract review, a month-end close. It's wrong for what only some need, such as a meeting facilitator for Teams, a tool for one sector or one country's tax filing:
- every installed skill is one more thing the Chief of Staff weighs on every request;
- every framework release has to be reviewed and published for everyone;
- whoever writes the capability has to send it into juvant-os itself.

**A skill copied by hand into a company** reaches only that company, but nobody looks after it:
- nothing records where it came from or which version it is;
- nothing updates it, and nothing notices if someone edits it;
- an update of juvant-os may collide with it;
- its needs stay unstated. A connector, a service running elsewhere, a rule it relies on: nobody approves them, because nobody sees them.

**An extension** reaches only the companies that choose it, and is looked after like part of the framework:

| | Skill in juvant-os | Skill copied by hand | Extension |
|---|:-:|:-:|:-:|
| Only the companies that want it | ❌ | ✅ | ✅ |
| Its own releases, without a juvant-os release | ❌ | ✅ | ✅ |
| Known source and version, checked at every session | ✅ | ❌ | ✅ |
| Updated, restored and removed with a confirmation | ✅ | ❌ | ✅ |
| Its needs shown to the CEO and approved | n/a | ❌ | ✅ |
| Can bring stricter limits with it | n/a | ❌ | ✅ |
| Written by anyone, outside juvant-os | ❌ | ✅ | ✅ |

The rule of thumb: **what every company needs goes into juvant-os; what only some need becomes an extension.** A capability can start as an extension and move into the framework once most companies use it.

---

## Catalogue

| Extension | What it does | Permissions | Latest |
|---|---|---|---|
| [`hello`](hello/) | Greets the CEO. A demo of what an extension looks like, and a way to try the whole path. | none | [0.1.1](https://github.com/juvantlabs/juvant-os-extensions/releases/tag/hello-v0.1.1) |

More will follow. Each one is listed here once it has a published release.

---

## For the CEO: using an extension

You don't run anything yourself. Ask the Chief of Staff in plain words:

> "Install the `hello` extension from juvantlabs/juvant-os-extensions."

The Chief of Staff then:

1. **Prepares a plan.** It downloads the release, checks it, and installs nothing yet.
2. **Reads every file** as someone else's text, not as instructions. It looks for anything that would send data out, speak for the company or skip a confirmation.
3. **Tells you** what the extension does, who publishes it, what it needs and **what new permissions it asks for**, and gives you a recommendation.
4. **Asks for your confirmation.** juvant-os shows you a summary before anything is written. For `hello` it reads:

   ```
   INSTALL extension hello 0.1.1 from github.com/juvantlabs/juvant-os-extensions/hello, release hello-v0.1.1 (8a13243cd8).
   New permissions: none. Limits that disappear: none. 4 files.
   Its skills are instructions written outside the company: confirm only if you've read what it does.
   ```

5. **Installs it**, then commits with your ok. The new skills are available from the next session.

The same goes for the rest:

| You say | What happens |
|---|---|
| "Which extensions do we have?" | The list, with versions and where they come from |
| "Update `hello`" | A plan with what changes (`0.1.0 -> 0.1.1`), new permissions and limits that would disappear; you confirm |
| "Remove `hello`" | A plan with the files and the limits that go with it; you confirm |
| "Restore `hello`" | If a file was changed after installation, the approved version comes back; you confirm |

If a file of an extension changes after installation, the session warns you that it "isn't as approved", and the Chief of Staff stops using it until it's restored.

The details are in juvant-os's `extensions` skill.

---

## What an extension can and can't do

| An extension can | An extension can't |
|---|---|
| Add skills: instructions in Markdown, with JSON or text beside them | Carry code: scripts, executables, hooks, links, settings or agents |
| Add limits that **deny** or **ask** for tools and commands | Remove, soften or bypass any limit of juvant-os or of the company |
| Declare what it needs: an MCP role, folders under `memory/` or `docs/`, other extensions | Get any of it without the CEO seeing it in the confirmation |
| Name a companion service it relies on (a bot, a server) | Run that service: it lives in its own repository, set up by the company |
| Ship default settings the company can change | Write anywhere except its own folders |

**How trust works:**

- **Only published GitHub releases install.** juvant-os records each release by its commit and by the repository's numeric id, so a moved tag, or another repository put in its place, is noticed.
- **Every change is downloaded again when it is applied**, and must match what the CEO confirmed. If anything differs, nothing is installed.
- **The CEO confirms every install, update, restore and removal.** A session that runs unattended can't apply one.
- **Installed files are checked at every session start.** A file that differs from what was approved is reported.

These are guardrails, not a sandbox: an extension's skills are instructions the Chief of Staff reads, and the review in step 2 is part of the protection. Install only what you would let a new colleague read to your assistant.

**Third-party extensions.** juvant-os can install an extension from any GitHub repository that follows these rules, with the same checks and confirmation. This catalogue lists only the official ones.

---

## For developers: writing an extension

### The shape

One folder per extension, named after its id:

```
my-extension/
├── extension.json            what it is and what it needs
├── README.md                 for the CEO: what it does, in plain words
├── skills/
│   └── <name>/
│       ├── SKILL.md          the instructions (installed as skill <id>-<name>)
│       └── reference.md      more .md, .json or .txt files, if useful
├── limits.json               optional: extra rules that deny or ask
├── config.example.json       optional, with config.schema.json: the company's settings
├── config.schema.json
└── LICENSE                   optional (LICENSE, LICENSE.md or LICENSE.txt)
```

Nothing else is accepted. The quickest start is to copy [`hello/`](hello/) and rename it.

### `extension.json`

All keys are required, and no others are allowed.

```json
{
  "id": "hello",
  "version": "0.1.1",
  "framework": ">=2.1.0 <3.0.0",
  "license": "MIT",
  "skills": ["greet"],
  "requires_extensions": {},
  "mcp": [],
  "company_paths": [],
  "service": null,
  "exceptions": []
}
```

| Key | What it holds | Rules |
|---|---|---|
| `id` | The extension's name | Lower case, digits and single hyphens, up to 30 characters, the same as the folder. Reserved: `claude`, `code`, `company`, `ext`, `framework`, `juvant`, `juvant-os`, `lock`, `security`, `synced` |
| `version` | Its version | `1.2.3` or `1.2.3-rc.1`. It must match the release tag |
| `framework` | The juvant-os versions it works with | Space-separated terms such as `>=2.1.0 <3.0.0` (`>=`, `>`, `<=`, `<`, `=`) |
| `license` | Its license | A short identifier, such as `MIT` |
| `skills` | Its skills, by folder name | Up to 20. Each is installed as `<id>-<name>`. Can be empty if the extension only adds limits |
| `requires_extensions` | Other extensions it needs | `{"other-id": ">=1.0.0"}`. They must be installed first, and can't be removed while this one is installed |
| `mcp` | The connectors it uses | Up to 10 items `{"role": "calendar", "access": "read", "why": "…"}`. `access` is `read`, `draft` or `write`. The company decides which server plays the role |
| `company_paths` | Company folders it writes to | Up to 5, a folder of its own under `memory/` or `docs/`. `memory/decisions`, `memory/authorizations` and `memory/private.md` aren't allowed |
| `service` | A companion service outside the session | `null`, or exactly `repository`, `release`, `runs`, `data`, `permissions`, `sends`, `stop`: what it is, where it runs, what data it gets, what it can send and how to stop it |
| `exceptions` | Exceptions to a hard limit, for the service | Up to 10 items `{"limit": "…", "what": "…", "why": "…"}`. Only with a `service`, and each one needs the CEO's own recorded decision |

Everything in `mcp`, `company_paths`, `service`, `exceptions` and `requires_extensions` is shown to the CEO as a **new permission**. On an update, only what is new is shown.

### Skills

The folder `skills/<name>/` becomes the skill `<id>-<name>`. `SKILL.md` starts with exactly two one-line fields:

```markdown
---
name: hello-greet
description: "Greet the CEO on behalf of the hello extension. Use when the CEO asks to try the hello extension."
---

# Greet

Say hello to the CEO by name in one line, in their language.
```

- `name` is `<id>-<name>`. `description` says what it does and when to use it, in up to 600 characters. Quote it if it has a colon.
- Use only `.md`, `.json` and `.txt` files, in plain text: no control characters, invisible characters or text direction marks. Write at most six levels deep.
- Don't use file names a host loads on its own as instructions: `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `memory.md` and the like.
- Avoid three things the host would act on before anyone reads the skill:

  | Not allowed | Why |
  |---|---|
  | `$ARGUMENTS`, `$1`, `${…}` | The host substitutes them when the skill loads |
  | An exclamation mark before a backtick | The host runs it as a command when the skill loads |
  | `@` before a name (outside an email address) | The host attaches that file when the skill loads |

- Write for the Chief of Staff. Assume it follows the company's manifesto and hard limits. Don't tell it to skip a confirmation, act for the company or send data out: the review will flag it, and the CEO will see it.

### `limits.json` (optional)

Rules that make the company's limits stricter. They can only **deny** or **ask**:

```json
{
  "mcp":  { "deny": [ { "id": "no-delete", "pattern": "(^|_)delete(_|$)", "why": "this extension only reads" } ] },
  "bash": { "ask":  [ { "id": "exports", "pattern": "\\bexport-tool\\b", "why": "exports leave the company" } ] }
}
```

- Lists: `mcp.deny`, `mcp.ask`, `bash.deny`, `bash.ask`, `secrets`. Nothing that allows.
- Each rule is an `id`, a `pattern` (a Python regular expression, up to 120 characters) and an optional one-line `why`, up to 120 characters. Up to 20 rules.
- Patterns must stay fast, because the check runs before every call:
  - a repeat has a maximum (`{0,40}`, not `*` or `+`) and applies to one character or class;
  - no lookarounds or back references;
  - few alternatives.

  A pattern that matches everything is refused.
- The CEO sees every rule in the confirmation, and every rule that would disappear on an update or removal.
- The framework's own maintenance commands (update, extensions) can't be blocked by an extension's rule.

### Settings (optional)

`config.example.json` holds the defaults, and `config.schema.json` describes them. They go together. On first install juvant-os copies the example to `extensions/<id>.json` in the company repository. From then on it is the company's file: updates don't overwrite it. Skills read their settings from there.

### Check it

CI runs the installer's own checks on every push and pull request. To run them yourself, install juvant-os in a scratch folder and point the validator at it:

```bash
git clone -q --branch v2.1.1 https://github.com/juvantlabs/juvant-os.git /tmp/jos
bash /tmp/jos/setup.sh /tmp/scratch-co --company Example
python3 tools/validate.py /tmp/scratch-co            # every extension
python3 tools/validate.py /tmp/scratch-co my-extension
```

```
hello 0.1.1: OK, 4 files
```

The installer also refuses archives over 20 MB, a file over 400 KB, more than 200 files, or more than 4 MB of files in all.

To try the real path, publish a pre-release (`my-extension-v0.1.0-rc.1`) and install it by tag in a scratch company, as the CEO would.

---

## Releasing

Each extension has its own releases, tagged `<id>-v<version>`. The version is the one in `extension.json`:

```bash
# after the change is merged into main
gh release create hello-v0.1.2 --target <commit on main> --title "hello 0.1.2" --notes "What changed, for the CEO."
```

- juvant-os installs only **published** releases. Drafts are ignored. Pre-releases (`-rc.N`) install only when asked for by tag.
- Without a tag, juvant-os picks the newest stable release for that extension.
- **A published tag never moves.** juvant-os records the commit, and refuses an update whose tag now points elsewhere. To fix a release, publish a new version.
- A lower version can't replace a higher one. A candidate (`1.0.0-rc.1`) counts as older than its release (`1.0.0`).
- Write the release notes for the CEO: what changes for them, and any new permission.

---

## Contributing

- **New extension or change:** open a pull request with the folder, a README for the CEO and a passing `validate` check. Say what it needs and why.
- **Keep it small:** one job per extension, the fewest permissions that do it.
- **Services:** a bot or a server lives in its own repository. Here, the extension describes it in `service`.
- **Issues:** bugs and ideas in this repository's issues.

## Security

Please report vulnerabilities privately, as described in juvant-os's [SECURITY.md](https://github.com/juvantlabs/juvant-os/blob/main/SECURITY.md). Don't open public issues with reproduction details.

## License

[MIT](LICENSE). Each extension states its own license in `extension.json`.
