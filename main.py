class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True  # 标记书籍是否可借

    def check_availability(self):
        """检查书籍是否可借"""
        return self.is_available


class User:
    def __init__(self, name, card_number):
        self.name = name
        self.card_number = card_number
        self.borrowed_books = []  # 记录用户已借书籍


class LibrarySystem:
    def __init__(self):
        self.books = []  # 图书馆藏书
        self.users = []  # 图书馆用户

    def add_book(self, book):
        """将书籍加入图书馆"""
        self.books.append(book)

    def register_user(self, user):
        """注册用户"""
        self.users.append(user)

    def borrow_book(self, user, isbn):
        """用户借阅书籍"""
        # 查找书籍
        target_book = None
        for book in self.books:
            if book.isbn == isbn:
                target_book = book
                break
        
        if not target_book:
            return "书籍不存在"
        if not target_book.check_availability():
            return "书籍已被借出"
        
        # 执行借阅
        target_book.is_available = False
        user.borrowed_books.append(target_book)
        return f"借阅成功：《{target_book.title}》"

    def return_book(self, user, isbn):
        """用户归还书籍"""
        # 查找用户已借的书籍
        target_book = None
        for book in user.borrowed_books:
            if book.isbn == isbn:
                target_book = book
                break
        
        if not target_book:
            return "你未借阅此书籍"
        
        # 执行归还
        target_book.is_available = True
        user.borrowed_books.remove(target_book)
        return f"归还成功：《{target_book.title}》"


# 示例使用
if __name__ == "__main__":
    # 初始化图书馆
    lib = LibrarySystem()
    
    # 添加书籍
    book1 = Book("Python编程从入门到实践", "埃里克·马瑟斯", "9787115428028")
    book2 = Book("数据结构与算法", "邓俊辉", "9787302432298")
    lib.add_book(book1)
    lib.add_book(book2)
    
    # 注册用户
    user1 = User("张三", "C001")
    lib.register_user(user1)
    
    # 借阅书籍
    print(lib.borrow_book(user1, "9787115428028"))  # 借阅成功
    print(lib.borrow_book(user1, "9787115428028"))  # 书籍已被借出
    
    # 归还书籍
    print(lib.return_book(user1, "9787115428028"))  # 归还成功
