from mongoengine import connect
import configparser


config = configparser.ConfigParser()
connect(host=f"""mongodb+srv://sturenko4:31122014@sturenko4.e02me8x.mongodb.net/base.authors?retryWrites=true&w=majority&appName=sturenko4""", ssl=True)
