from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members (first_name, last_name, date_of_birth, address, tel_number, email, platinum_member) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.date_of_birth, member.address, member.tel_number, member.email, member.membership_type]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id

# def select(member):



# def select_all(member):




def update(member):
    sql = "UPDATE members SET(first_name, last_name, date_of_birth, address, tel_number, email, platinum_member) = ( %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.date_of_birth, member.address, member.tel_number, member.email, member.membership_type, member.id]
    run_sql(sql, values)


# def delete(member):