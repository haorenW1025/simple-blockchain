# pseudo-bitcoin implementation

simple implementation of bitcoin using python

## Table of Contents

* [Install Dependencies](#install-dependencies)
* [Usage](#usage)
* [Functionality](#functionality)

## Install Dependencies

- python3.4 or newer is required
```
pip install -r requirements.txt
```

## Usage

Note that if no blockchain database is found locally, running commands from below will generate a new blockchain add a new database block.db.
- Add a new block to a current block chain
```
python3 cli.py AddBlock --data [data of the block]
```
- Print the block with specify height
```
python3 cli.py PrintBlock --height [height]
```
- Print the whole block chain
```
python3 cli.py PrintChain
```

## Functionality
- Basic block chain prototype
- Proof-of-Work
- Database
- Client
