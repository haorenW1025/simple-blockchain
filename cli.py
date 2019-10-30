import click
import sys
from blockchain import block_chain


@click.command()
@click.argument('mode', type=click.Choice(['AddBlock', 'PrintBlock', 'PrintChain']))
@click.option('--data', '-d', type=click.STRING,
            help="Specify data for new block, required if argument = 'AddBlock'")
@click.option('--height', '-h', type=click.INT,
            help="Specify the block's height to be print, required if argument = 'PrintBlock'")
def main(mode, data, height):
    """
    client implementation of block chain

    Argument : [AddBlock, PrintBlock, PrintChain]

        AddBlock : Mine a new block to the longest chain

        PrintBlock: Print the block of specify height

        PrintChain: Print the whole block chain
    """
    bc = block_chain()
    if mode == 'AddBlock':
        if data == None:
            sys.exit("Data not specify! --data/-d to specify data")
        bc.addBlock(data)
    elif mode == 'PrintChain':
        bc.printChain()
    elif mode == 'PrintBlock':
        if height == None:
            sys.exit("height not specify! --heihgt/-h to specify height")
        bc.printBlock(height)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
