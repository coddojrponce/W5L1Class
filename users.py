from mysqlconnection import connectToMySQL


class User:

    db="facegram"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']



    #CREATE
    @classmethod
    def save(cls,data):
        
        query="""
        INSERT INTO users(first_name,last_name,email,password) 
        VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    #READ
    @classmethod
    def get_all(cls):
        query="SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        users =[]
        for row in results:
            users.append(cls(row))
        return users
    
    @classmethod
    def get_one_by_email(cls,email):
        data={
            "email":email
        }
        query="""
        SELECT * FROM users WHERE email=%(email)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_one(cls,id):
        data={
            "id":id
        }
        query="""
        SELECT * FROM users WHERE id=%(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    #UPDATE
    @classmethod
    def update(cls, data):
        query = """
        UPDATE users 
        SET first_name = %(first_name)s,
        last_name = %(last_name)s,
        email = %(email)s,
        password = %(password)s 
        WHERE id = %(id)s;"""

        results = connectToMySQL(cls.db).query_db(query, data)
        return results


    #DELETE
    @classmethod
    def delete(cls,id):
        data={
            'id':id
        }
        query="""
        DELETE FROM users
        WHERE id=%(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
        


