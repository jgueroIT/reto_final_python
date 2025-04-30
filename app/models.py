from app.db import get_connection

def get_all_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, description FROM tasks;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": row[0], "title": row[1], "description": row[2]} for row in rows]

def get_task_by_id(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, description FROM tasks WHERE id = %s;", (task_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return {"id": row[0], "title": row[1], "description": row[2]} if row else None

def add_task(title, description):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title, description) VALUES (%s, %s) RETURNING id;", (title, description))
    task_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return task_id

def delete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s;", (task_id,))
    conn.commit()
    cur.close()
    conn.close()
