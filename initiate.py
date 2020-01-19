import sqlite3
import os
import persistence
def main():
    open("config.txt", "r")
#    if os.path.isfile('/home/joni/PycharmProjects/SPLCAFE/venv/include/moncafe.db'):
 #       os.remove('/home/joni/PycharmProjects/SPLCAFE/venv/include/moncafe.db')
    persistence.repo.create_tables()

if __name__ == "__main__":
    main()
