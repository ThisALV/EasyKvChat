import kivy
from kivy.lang.builder import Builder

import sys
import os


class InvalidArguments(ValueError):
    pass


def run(argv):
    try:
        kivy.resources.resource_add_path(argv[0])
        print("Ressources :", kivy.resources.resource_paths)

        from easykvchat.server.app import ServerApp  # noqa E402
        from easykvchat.client.app import ClientApp  # noqa E402

        if len(argv) < 1:
            raise InvalidArguments()

        mode = argv[1]
        if mode == "server":
            if len(argv) != 3:
                raise InvalidArguments()

            port = int(argv[2])
            if port < 0 or port > 65535:
                raise InvalidArguments()

            ServerApp(port).run()
        elif mode == "client":
            ClientApp().run()
        else:
            raise InvalidArguments()
    except InvalidArguments as err:
        print("Syntaxe : <chemin des ressources> <mode: client|server> [port (mode serveur uniquement)]")
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(run(sys.argv))
