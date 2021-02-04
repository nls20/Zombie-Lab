from db.run_sql import run_sql
from models.biting import Biting

def save(biting):
    sql = "INSERT INTO bitings (human, zombie) VALUES (%s, %s) RETURNING id"
    values = [biting.human, biting.zombie]
    results = run_sql(sql, values)
    biting.id = results[0]['id']
    return biting

def select_all():
    bitings = []

    sql = "SELECT * FROM bitings"
    results = run_sql(sql)

    for row in results:
        biting = Biting(row['human'], row['zombie'], row['id'])
        bitings.append(biting)
    return bitings

def select(id):
    sql = "SELECT * FROM bitings WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    biting = Biting(result["human"], result["zombie"], result["id"])
    return biting

def delete(id):
    sql = "DELETE FROM bitings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)

def update(biting):
    sql = "UPDATE bitings SET (human_id, zombie_id) = %s WHERE id = %s"
    values = [biting.human, biting.zombie, biting.id]
    run_sql(sql, values)