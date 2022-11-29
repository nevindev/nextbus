import argparse


def get_user_input(args=None):
    parser = _create_argparser()

    user_input = parser.parse_args(args)

    return str(user_input.route), str(user_input.stop), str(user_input.direction)


def _create_argparser():
    argparser = argparse.ArgumentParser(
        prog="NextBus",
        description="Given a route, bus stop and travelling direction the program outputs how long until the next bus arrives."
    )

    argparser.add_argument('-r', '--route',
                           help="Name of the bus route",
                           required=True)

    argparser.add_argument('-s', '--stop',
                           help="Name of the bus stop on the route",
                           required=True)

    argparser.add_argument('-d', '--direction',
                           choices=['north', 'south', 'east', 'west'],
                           help="Cardinal direction the bus travels on the route",
                           required=True)

    return argparser
