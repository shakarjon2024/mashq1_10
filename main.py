class Foydalanuvchi:

    jami_foydalanuvchilar = 0

    def __init__(self, ism, username):

        if not self.username_tekshirish(username):
            raise ValueError ("Username notogri")

        self.ism  = ism
        self.username = username
        self.__posts = []

        Foydalanuvchi.jami_foydalanuvchilar += 1


    def post_qoshish(self, matn):
        post = {
            "matn": matn,
            "like": 0
        }

        self.__posts.append(post)
        print("Post qoshildi")

    def postlarni_korish(self):

        if not self.__posts:
            print("Postlar yoq")
            return

        for i, post in enumerate(self.__posts, 1):
            print(f"{i}, {post['matn']} Like: {post['like']}")

    def like_bosish(self, post_index, boshqa_user):

        if self.username == boshqa_user.username:
            print("Oz postingizga like  bosolmaysiz")
            return

        try:
            boshqa_user.__posts[post_index]['like'] += 1
            print('Like bosildi')

        except IndexError:
            print("Post topilmadi")

    @classmethod
    def faol_foydalanuvchilar(cls):
        print(f"Jami foydalanuvchilar: {cls.jami_foydalanuvchilar}")

    @staticmethod
    def username_tekshirish():

        if 3 <= len(username)  <= 20 and username.isalnum():
            return  True

        return False


u1 = Foydalanuvchi("Ali", "ali123")
