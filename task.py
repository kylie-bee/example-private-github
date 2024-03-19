# This library is installed from a private repo or local source through the pre-run
#  script invoking the pip installation of the requirements-private.txt file.
import kylie_bee_private_shared_code

from robocorp.tasks import task


@task
def test():
    kylie_bee_private_shared_code.setup_log()
    print("Setup log worked!")
