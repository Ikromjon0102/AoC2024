'''

1 savolga javob:
Python dinamik til ekanligi hammaga ayon bo'lib, bu xususiyat orqali python compyuter xotirasidan dinamik joy olishi nazarda tutiladi, bu bir tomondan yaxshi ya'ni bir o'zafaruvchiniga katta xajmdagi data kiritilgan vaqtda ham xatoliksiz ishlay oladi, ikkinchi tomondan esa operatsion tizim python ishlayotgan paytda xotiraning katta qismi band bolib qolishidur, bu uning kamchiligi hisoblanadi.

2 savolga javob:
'''
fruits = ["olma", "anor", "banan", "olma", "anor"]
'''
bu pythonda list datatype hisoblanadi, yani ro'yxat (list) - o'zgaruvchan, tartiblangan, takrorlanadigan datalarni kolleksiyasini saqlash uchun foydalaniladi.
yuqoridagi shartni amalga oshirish uchun 
dastavval ro'yxatdan takrorlangan elementlarni o'chirib so'ngra tartiblash zarur
elementlarni o'chirish uchun:
'''
new_list = []
for fruit in fruits:
    if fruit not in new_list:
        new_list.append(fruit)
new_list.sort()
print(new_list)


'''
3 savolga javob:
Django-da ModelSerializer nima? Bu Serializer dan qanday farq qiladi?
ModelSerializer modelga asoslangan serializer hisoblanadi, Meta class yordamida model biriktiriladi
Serializerda esa qanday fieldlar kerak bo'lsa hammasini yozib chiqish zarur

misol uchun:
'''
class Profile(models.Model):
    first_name = models.Charfield(max_lengh = 30)
    last_name = models.Charfield(max_lengh = 30)
    email_name = models.Charfield(max_lengh = 30)
    password = models.Charfield(max_lengh = 128)

class RegisterSerializer(serializer.Serializer):
    first_name = serializer.Charfield(max_lengh=30)
    last_name = serializer.Charfield(max_lengh=30)
    email_name = serializer.Charfield(max_lengh=30)
    password = serializer.Charfield(max_lengh=128)

class RegisterSerializer(serializer.ModelSerializer):
    class Meta:
        model_name = Profile
        fields = __all__

'''
4 savolga javob:
Restful API nima va u qanday ishlaydi? Misol uchun, foydalanuvchini ro‘yxatdan o‘tkazadigan endpoint yozing.

bu savolga javobni bilmadim
'''

'''
5 savolga javob
Faylni o‘qib, undagi barcha so‘zlarni alifbo tartibida unikal holda ro‘yxatga qo‘shuvchi dastur yozing.
'''
with open('a_file.txt', 'r') as file:
    all_words = []
    all_data = file.read().split()
    for data in all_data:
        if data not in all_words:
            all_words.append(data)
    sorted(all_words)
print(all_words)


'''
6 savolga javob:

'''
def foo(x):
    return x + 1

def bar(x):
    return x * 2

def baz(x):
    return foo(x), bar(x)

print(baz(2))


'''
7 savolga javob:
Bitta SQL so‘rov bilan "users" jadvalidan foydalanuvchi sonini va ulardan nechtasi "active" ekanligini toping.

SELECT COUNT(id) as users, COUNT(active is True FROM users;
'''

'''
8 savolga javob:
Git branchlar bilan ishlashda qaysi vaqtda merge va qaysi vaqtda rebase ishlatiladi?
bu savolga javobni bilmayman.
'''

'''
9 savolga javob:
Quyidagi qatorni teskari o‘girish uchun kod yozing:
'''
text = "Python dasturlash juda qiziqarli"
# version 1
# print(text[::-1])

# version 2
# rev_text = ''
# for i in range(1, len(text)+1):
#     rev_text += text[i*-1]
# print(rev_text)

'''
10 savolga javob:
Kod xatolarini qanday topasiz va tuzatasiz? Siz qaysi asboblarni yoki usullarni afzal ko‘rasiz?
dasturni xatosi tekshirish uchun unittest yozib ko'rmanan, unittest yozish uchun pytest kutubxonasidan foydalanaman 
'''
