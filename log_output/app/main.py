import time
import uuid
from datetime import UTC, datetime


def now_iso_timestamp() -> str:
    return datetime.now(UTC).isoformat(timespec="milliseconds")


def main() -> None:
    random_string = str(uuid.uuid4())

    while True:
        print(f"{now_iso_timestamp()}: {random_string}")
        time.sleep(5)


if __name__ == "__main__":
    main()