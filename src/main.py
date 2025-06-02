from dotenv import load_dotenv
from atscribe import Atscribe

def main():
    Atscribe.ask()


if __name__ == "__main__":
    load_dotenv()
    main()
