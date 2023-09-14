import sqlite3

# Read the file and copy content to a list
try:
    with open('stephen_king_adaptations.txt', 'r') as file:
        stephen_king_adaptations_list = [line.strip().split(',') for line in file]
except FileNotFoundError:
    print("The file 'stephen_king_adaptations.txt' does not exist.")
    exit()

# Establish a connection with the SQLite database and create a table
conn = sqlite3.connect('stephen_king_adaptations.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (
        movieID TEXT PRIMARY KEY,
        movieName TEXT,
        movieYear INTEGER,
        imdbRating REAL
    )
''')

# Insert content from the list into the table
cursor.executemany('''
    INSERT OR IGNORE INTO stephen_king_adaptations_table (movieID, movieName, movieYear, imdbRating)
    VALUES (?, ?, ?, ?)
''', stephen_king_adaptations_list)
conn.commit()

# User options to search for movies in the database
while True:
    choice = input("Choose an option (1-4):\n1. Movie name\n2. Movie year\n3. Movie rating\n4. STOP\n")

    if choice == "1":
        movie_name = input("Enter the movie name: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName = ?", (movie_name,))
        result = cursor.fetchall()
        if result:
            for row in result:
                print(f"Movie ID: {row[0]}, Movie Name: {row[1]}, Movie Year: {row[2]}, IMDB Rating: {row[3]}")
        else:
            print("No such movie exists in our database")

    elif choice == "2":
        movie_year = int(input("Enter the movie year: "))
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear = ?", (movie_year,))
        result = cursor.fetchall()
        if result:
            for row in result:
                print(f"Movie ID: {row[0]}, Movie Name: {row[1]}, Movie Year: {row[2]}, IMDB Rating: {row[3]}")
        else:
            print("No movies were found for that year in our database.")

    elif choice == "3":
        movie_rating = float(input("Enter the minimum IMDB rating: "))
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (movie_rating,))
        result = cursor.fetchall()
        if result:
            for row in result:
                print(f"Movie ID: {row[0]}, Movie Name: {row[1]}, Movie Year: {row[2]}, IMDB Rating: {row[3]}")
        else:
            print("No movies at or above that rating were found in the database.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()