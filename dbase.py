import sqlite3


def create_database():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE jobs (
            id INTEGER PRIMARY KEY,
            job_url TEXT,
            title TEXT,
            company TEXT,
            location TEXT,
            date_posted TEXT
        )
    ''')
    conn.commit()
    conn.close()


def create_table():
    # create table if it doesn't exist
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            job_url TEXT,
            title TEXT,
            company TEXT,
            location TEXT,
            date_posted TEXT
        )
    ''')
    conn.commit()
    conn.close()


def job_exists(job):
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('SELECT * FROM jobs WHERE title = ?', (job,))
    data = c.fetchall()
    conn.close()
    return len(data) > 0


def clear_jobs():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('DELETE FROM jobs')
    conn.commit()
    conn.close()


def add_job(job):
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO jobs (job_url, title, company, location, date_posted)
        VALUES (?, ?, ?, ?, ?)
    ''', (job['job_url'], job['title'], job['company'], job['location'], job['date_posted']))
    conn.commit()
    conn.close()

def add_jobs(jobs):
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.executemany('''
        INSERT INTO jobs (job_url, title, company, location, date_posted)
        VALUES (?, ?, ?, ?, ?)
    ''', [(job['job_url'], job['title'], job['company'], job['location'], job['date_posted']) for job in jobs])
    conn.commit()
    conn.close()




create_database()
create_table()
