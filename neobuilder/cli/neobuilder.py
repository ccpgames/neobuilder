import argparse

from neobuilder.neobuilder import NeoBuilder


def main():
    parser = argparse.ArgumentParser(description='Builds neobuf packages with protoplasm.',
                                     epilog=(f'Neobuilder v{NeoBuilder.neobuilder_version()} - '
                                             f'Protoplasm v{NeoBuilder.protoplasm_version()}'))
    version_group = parser.add_mutually_exclusive_group()
    version_group.add_argument('-m', '--major', action="store_true",
                               help='Bump the major version number instead of the minor')
    version_group.add_argument('-p', '--patch', action="store_true",
                               help='Bump the patch version number instead of the minor')
    parser.add_argument('package', help='Package name')
    parser.add_argument('protopath', help='Path to the root of the protobuf files (default="./proto")',
                        default='./proto', nargs='?')
    parser.add_argument('-b', '--buildroot', help='Path to the root of the output build files (default="./build")',
                        default='./build', nargs='?')
    parser.add_argument('-v', '--verbose', action="store_true",
                        help='Spits out DEBUG level logs')

    args = parser.parse_args()

    n = NeoBuilder(
        package=args.package,
        protopath=args.protopath,
        build_root=args.buildroot,
        major=args.major,
        patch=args.patch,
        verbose=args.verbose,
    )
    n.build()


if __name__ == '__main__':
    main()
