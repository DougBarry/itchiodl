from getpass import getpass
import itchiodl


def main():
    user = input("Username: ")
    password = getpass("Password: ")

    l = itchiodl.LoginWeb(user, password)

    url = input("Bundle URL: ")
    page_start = int(input("Page no. to start at: ") or 1)

    b = itchiodl.Bundle(l, url)
    b.load_games(page_start)


if __name__ == "__main__":
    main()
