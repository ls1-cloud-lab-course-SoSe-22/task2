#!/usr/bin/env python3

import sys
from time import sleep
from testsupport import subtest, info, run
from socketsupport import run_client, run_master, run_server


def main() -> None:
    with subtest("Testing failure detection"):
        master_proc = run_master(1025)
        sleep(5)
        server_proc_one = run_server(1026, 1025)
        sleep(5)
        server_proc_two = run_server(1027, 1025)
        sleep(5)

        server_proc_two.terminate()
        sleep(20)

        for i in range(1, 21):
            client_ret = run_client(1026, "PUT", i, 1000, 1025, 0)
            if client_ret !=0:
                master_proc.terminate()
                server_proc_one.terminate()
                sys.exit(1)
            sleep(3)

        info(f"ran all clients successfully")

        master_proc.terminate()
        server_proc_one.terminate()



if __name__ == "__main__":
    main()