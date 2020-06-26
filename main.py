
import sqlite3,json

class jsonExam:
    def __init__(self):
        self.my_json = {'veriler': []}
        self.connection = sqlite3.connect('D:\Projeler\Python Dersleri\Python Dersleri Tekrar\database.db')
        self.cursor = self.connection.cursor()

    def getData(self):
        self.cursor.execute("SELECT * FROM users")
        data = self.cursor.fetchall()

        while data:
            isim = data[0][0]
            sifre = data[0][1]

            data1 = {"username": isim,
                    "password": sifre}

            self.my_json["veriler"].append(data1)
            self.save(data1)

            data.pop(0)


    def save(self,isim):
        with open('data.json', 'w', encoding='UTF-8') as file:
            json.dump(self.my_json, file, indent=2, ensure_ascii=False)


    def readJson(self):
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        course_points = data["veriler"]
        for i in course_points:
            print(i["username"], end=" ")
            print(i["password"])


if __name__ == '__main__':
    #jsonExam().getData()
    jsonExam().readJson()