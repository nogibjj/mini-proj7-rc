"""
Command line query script
"""
import sqlite3
import click

@click.command()
@click.argument("database")
def command_line(database):
    '''
        Hi, this is a command line tool to do some queries.
        Give me your database name, I can create a user table 
        and insert some users for you.
        Enjoy it :)
    '''
    conn = sqlite3.connect("database")
    cursor = conn.cursor()

    
    # Create a table
    click.echo("Creating table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL
        )
    """)
    click.echo("inserting...")
    cursor.execute("INSERT INTO users (username) VALUES ('rc381')")
    cursor.execute("INSERT INTO users (username) VALUES ('ab123')")
    cursor.execute("INSERT INTO users (username) VALUES ('cd567')")
    # Delete
    click.echo("Deleting...")
    cursor.execute("DELETE from users where username = 'rc381'")
    # Read
    click.echo("Querying...")
    cursor.execute("SELECT username FROM users")
    users = cursor.fetchall()
    
    click.echo("current users:")
    for user in users:
        click.echo(user)

    click.echo("Closing connection...")
    conn.close()
    click.echo("Finished")

if __name__ == "__main__":
    command_line()