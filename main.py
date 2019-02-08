import sqlite3
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/requirements')
def requirements():
    sql = 'SELECT * FROM requirements;'
    requirements = [r['note'] for r in query_db(sql)]
    return render_template('requirements.html', requirements=requirements)

def query_db(query, args=(), one=False):
    """
    指定されたSQLを実行して、その結果を返却する
    """
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.execute(query, args)
    conn.commit()
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def get_connection():
    """
    現在のappcontext内のコネクションを取得する
    """
    return sqlite3.connect('data.db')

app.run()
