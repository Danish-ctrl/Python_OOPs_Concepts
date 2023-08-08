class Books:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def info(self):
        print(f"The book with title {self.title}, author {self.author} and publication year {self.year}")


b = Books('Dani Den', 'Danish', '1995')
b.info()