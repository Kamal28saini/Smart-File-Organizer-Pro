
from src.database import initialize_database
from gui.dashboard import launch_app
from src.logger import logger


def main():

    initialize_database()

    logger.info("Application started")

    launch_app()


if __name__ == "__main__":

    main()
