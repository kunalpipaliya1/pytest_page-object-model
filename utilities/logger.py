import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(
            filename=r"C:\Users\Nmsworks\Documents\KunalLearning\Project\Pytest_Project\Logs\automation.log",
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filemode='a'  # append mode, can change to 'w' to overwrite
        )
        logger = logging.getLogger()
        return logger
