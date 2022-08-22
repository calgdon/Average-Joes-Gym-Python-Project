from db.run_sql import run_sql
from models.member import Member


#  Save a new member to the database

def save(member):
    sql = "INSERT INTO members (first_name, last_name, date_of_birth, address, tel_number, email, platinum_member) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.date_of_birth, member.address, member.tel_number, member.email, member.platinum_member]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id

# Select a single member

def select(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        member = Member(result['first_name'], result['last_name'], result['date_of_birth'],
        result['address'], result['tel_number'], result['email'], result['platinum_member'], result['id'])
    return member


# Select all members 

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['date_of_birth'], row['address'], row['tel_number'], row['email'], row['platinum_member'], row['id'])
        members.append(member)
    return members

# Update a member by name

def update(member):
    sql = "UPDATE members SET (first_name, last_name, date_of_birth, address, tel_number, email, platinum_member) = ( %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.date_of_birth, member.address, member.tel_number, member.email, member.platinum_member, member.id]
    run_sql(sql, values)

# Delete a member by id

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Delete all members

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)