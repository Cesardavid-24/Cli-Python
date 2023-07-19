import click
from db_manager import get_data , set_data
users = []
@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', required=True, help='name of user')
@click.option('--email', required=True, help='email to login')
@click.option('--password',required=True, help='password to login')
@click.pass_context
def insert(ctx, name , email, password):
    if not name or not email or not password:
        ctx.fail("the fields are required")
    else:
        user = [name , email, password]
        sql = "INSERT INTO users (name , email, password) VALUES ('{}', '{}', '{}');".format(user[0] ,user[1], user[2])
        message = set_data(sql)
        if message:
            print("query execute")
            

@cli.command()
@click.argument('id')
def user(id):
    sql = f"SELECT userId ,name , email, password FROM users WHERE userId={id};"
    user = get_data(sql)
    if user != []:
        for data in user:
            userId = data[0]
            name = data[1]
            email = data[2]
            password = data[3]
            print(f"{userId} - {name} - {email} - {password}")
    else:
        print(f"user with id {id} not found")

@cli.command()
@click.option('--name', help='name to update')
@click.option('--email', help='email to update')
@click.option('--password', help='password to update')
@click.argument('id',required=True)
def update(id,name,email,password):
    fields_to_update = []

    if name is not None:
        fields_to_update.append(f"name='{name}'")
    if email is not None:
        fields_to_update.append(f"email='{email}'")
    if password is not None:
        fields_to_update.append(f"password='{password}'")

    if fields_to_update:
        sql = f"UPDATE users SET {', '.join(fields_to_update)} WHERE userId={id};"

    message = set_data(sql)
    if message:
        print("query execute")
            
    
@cli.command()
@click.argument('id',required=True)
def delete(id):
    sql = f"DELETE FROM users WHERE userId={id};"
    set_data(sql)
    print(f"user with id {id} delete succesfully")


@cli.command()
def users():
    query = 'SELECT userId , name , email FROM users;'
    users = get_data(query)
    for user in users:
        userId = user[0]
        name = user[1]
        email = user[2]
        password = user[3]
        print(f"{userId} - {name} - {email} - {password}")

if __name__ == "__main__":
    cli()

