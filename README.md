# jiav-backend-command

> [!WARNING]
> This backend is risky since it allows users to execute arbitrary commands, and use it at your own risk.

> [!NOTE]
> This package does not install Ansible itself;

A command backend for [jiav](https://github.com/vkhitrin/jiav).

## Documentation

Visit <https://jiav.readthedocs.io/en/latest/command_backend.html>.

## Requirements

Install [jiav](<[jiav](https://github.com/vkhitrin/jiav)>).  
`jiav` requires Python `>= 3.8`.


## Installation

### Remote

Install from remote:

```bash
pip3 install jiav-backend-command
```

Inject to a `pipx` environment:

```bash
pipx inject jiav jiav-backend-command
```

### Local

Install from the local repository:

```bash
pip3 install .
```

Inject to a `pipx` environment:

```bash
pipx inject jiav ../jiav-backend-command
```

## Contributing

**All contributions are welcome!**
