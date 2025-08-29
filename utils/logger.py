import logging
import os


def get_logger(test_name: str):
    """Create a unique logger for each test based on test name"""
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "messages.log")

    logger = logging.getLogger(test_name)
    logger.setLevel(logging.DEBUG)

    # Avoid duplicate handlers if logger is reused
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file, mode="a")
        formatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

# @pytest.fixture
# def test_logger(request):
#     """Fixture to provide a logger unique to each test"""
#     test_name = request.node.name  # pytest test function name
#     logger = get_logger(test_name)
#     return logger
