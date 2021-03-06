import asyncio
import argparse
import json

from . import aehw4a1
from .commands import UpdateCommand
from .commands import ReadCommand
from .exceptions import *

def main():
    parser = argparse.ArgumentParser("aehw4a1")
    subs = parser.add_subparsers()
    subs.required = True
    subs.dest = 'choise'
    disc_parser = subs.add_parser('discovery', help='search for ACs')
    disc_parser.add_argument('--full', '-f', action='store_const', const=True, required=False,
                            help='force discovery on every interface')
    comm_parser = subs.add_parser('AC', help='run a command on the given AC')
    comm_parser.add_argument('--host', action='store', required=True,
                            help='IP of AC')
    comm_parser.add_argument('--command', '-c', action='store', required=False,
                            help='List on implemented commands on README.md')
    comm_parser = subs.add_parser('check', help='test for AC presence')
    comm_parser.add_argument('--host', action='store', required=True,
                            help='IP of AC')
    comm_parser = subs.add_parser('version', help='XMVersion')
    comm_parser.add_argument('--host', action='store', required=True,
                            help='IP of AC')
                            
    args = parser.parse_args()

    if args.choise == "discovery":
        client = aehw4a1.AehW4a1()
        print(asyncio.run(client.discovery(args.full)))

    elif args.choise == "AC":
        client = aehw4a1.AehW4a1(args.host)

        if args.command is None:
            command = "status_102_0"
        else:
            command = args.command

        if command in ReadCommand.__dict__:
            parsed = asyncio.run(client.command(command))
            print("AC",args.host,command,":\n",json.dumps(parsed, indent=4, sort_keys=False))
        elif command in UpdateCommand.__dict__:
            if asyncio.run(client.command(command)):
                parsed = asyncio.run(client.command("status_102_0"))
                print("AC",args.host,command,":\n",json.dumps(parsed, indent=4, sort_keys=False))
        else:
            raise UnkCmdError("Unknown command: {0}".format(command))

    elif args.choise == "check":
        client = aehw4a1.AehW4a1(args.host)
        if asyncio.run(client.check()):
            print("Found!")

    elif args.choise == "version":
        client = aehw4a1.AehW4a1(args.host)
        print(asyncio.run(client.version()))

if __name__ == "__main__":
    main()
