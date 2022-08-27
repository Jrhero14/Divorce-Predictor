from django.shortcuts import render
from django.shortcuts import redirect
import requests
# Create your views here.
def Home(request):
    return render(request, "index.html")

def Result(request):
    try:
        raw_data = []
        for key, val in request.POST.items():
            raw_data.append(val)
        raw_data = raw_data[1:]
        api_url = "https://divorce-ml-api.herokuapp.com/machine"
        result = requests.post(url=api_url, json={"input": list(raw_data)}).json()
        if (int(result["value"]) == 1):
            predict = True
        else:
            predict = False
        ctx = {'prediksi': predict}
        print(raw_data)
        print(result)
        return render(request, "result.html", context=ctx)
    except:
        return redirect('/')

class dataClass:
    def __init__(self, per: None, question, num, ri0, ri1, ri2, ri3, ri4):
        self.nothing = per,
        self.pertanyaan = question
        self.nomor = num
        self.radio0 = ri0
        self.radio1 = ri1
        self.radio2 = ri2
        self.radio3 = ri3
        self.radio4 = ri4

def Test(request):
    tanya = ["1. Jika salah satu dari kita meminta maaf ketika diskusi semakin memburuk, diskusi berakhir." ,
        "2. Saya tahu kita dapat mengabaikan perbedaan kita, bahkan jika hal-hal menjadi sulit kadang-kadang.",
    "3. Ketika kita membutuhkannya, kita dapat mengambil diskusi kita dengan pasangan saya dari awal dan memperbaikinya.",
"4. Ketika saya berdiskusi dengan pasangan saya, untuk menghubunginya pada akhirnya akan berhasil." ,
"5. Waktu yang saya habiskan bersama istri saya istimewa bagi kami." ,
"6. Kami tidak punya waktu di rumah sebagai sepasang suami-istri." ,
"7. Kami seperti dua orang asing yang berbagi lingkungan yang sama di rumah daripada keluarga." ,
"8. Saya menikmati liburan kami bersama pasangan saya." ,
"9. Saya menikmati bepergian dengan pasangan saya." ,
"10. Sebagian besar tujuan kami adalah umum bagi pasangan saya." ,
"11. Saya pikir suatu hari di masa depan, ketika saya melihat ke belakang, saya melihat bahwa pasangan saya dan saya telah selaras satu sama lain." ,
"12. Saya dan pasangan saya memiliki nilai-nilai yang sama dalam hal kebebasan pribadi." ,
"13. Saya dan pasangan saya memiliki rasa hiburan yang sama." ,
"14. Sebagian besar tujuan kami untuk orang-orang (anak-anak, teman, dll.) adalah sama.",
"15. Impian kami dengan pasangan saya serupa dan harmonis." ,
"16. Kami cocok dengan pasangan saya tentang apa yang seharusnya menjadi cinta.",
"17. Kami berbagi pandangan yang sama tentang menjadi bahagia dalam hidup kami dengan pasangan saya." ,
"18. Saya dan pasangan saya memiliki gagasan yang sama tentang bagaimana pernikahan seharusnya" ,
"19  Pasangan saya dan saya memiliki gagasan serupa tentang bagaimana peran seharusnya dalam pernikahan" ,
"20. Pasangan saya dan saya memiliki nilai-nilai yang sama dalam kepercayaan." ,
"21. Saya tahu persis apa yang disukai istri saya.",
"22. Saya tahu bagaimana pasangan saya ingin dirawat ketika dia sakit.",
"23. Saya tahu makanan favorit pasangan saya.",
"24. Saya dapat memberi tahu Anda tekanan seperti apa yang dihadapi pasangan saya dalam hidupnya.",
"25. Saya memiliki pengetahuan tentang dunia batin pasangan saya.",
"26. Saya tahu kecemasan dasar pasangan saya.",
"27. Saya tahu apa sumber stres pasangan saya saat ini.",
"28. Saya tahu harapan dan keinginan pasangan saya.",
"29. Saya mengenal pasangan saya dengan sangat baik.",
"30. Saya tahu teman-teman pasangan saya dan hubungan sosial mereka.",
'31. Saya merasa agresif ketika saya berdebat dengan pasangan saya.',
"32. Ketika berdiskusi dengan pasangan saya, saya biasanya menggunakan ekspresi seperti 'Anda selalu' atau 'Anda tidak pernah' .",
"33. Saya dapat menggunakan pernyataan negatif tentang kepribadian pasangan saya selama diskusi kami.",
"34. Saya dapat menggunakan ekspresi ofensif selama diskusi kita.",
"35. Saya dapat menghina pasangan saya selama diskusi kami.",
"36. Saya bisa memalukan ketika kita berdiskusi.",
"37. Diskusi saya dengan pasangan saya tidak tenang.",
"38. Saya benci cara pasangan saya membuka subjek.",
"39. Diskusi kita sering terjadi secara tiba-tiba.",
"40. Kami baru saja memulai diskusi sebelum saya tahu apa yang sedang terjadi.",
"41. Ketika saya berbicara dengan pasangan saya tentang sesuatu, ketenangan saya tiba-tiba pecah.",
"42. Ketika saya berdebat dengan pasangan saya, ı hanya keluar dan saya tidak mengatakan sepatah kata pun.",
"43. Saya kebanyakan tetap diam untuk sedikit menenangkan lingkungan.",
"44. Terkadang saya pikir itu baik bagi saya untuk meninggalkan rumah untuk sementara waktu.",
"45. Saya lebih suka diam daripada berdiskusi dengan pasangan saya.",
"46. Bahkan jika saya benar dalam diskusi, saya tetap diam untuk menyakiti pasangan saya.",
"47. Ketika saya berdiskusi dengan pasangan saya, saya tetap diam karena saya takut tidak mampu mengendalikan amarahku.",
"48. Saya merasa benar dalam diskusi kami. ",
"49. Saya tidak ada hubungannya dengan apa yang telah dituduhkan kepada saya.",
"50. Saya sebenarnya bukan orang yang bersalah atas apa yang saya tuduhkan.",
"51. Saya bukan orang yang salah tentang masalah di rumah.",
"52. Saya tidak akan ragu untuk memberi tahu pasangan saya tentang ketidakmampuannya.",
"53. Ketika saya berdiskusi, saya mengingatkan pasangan saya tentang ketidakmampuannya.",
"54. Saya tidak takut untuk memberi tahu pasangan saya tentang ketidakmampuannya."]

    fixData = [
        dataClass(None, i, idx,f"{idx}.0", f"{idx}.1", f"{idx}.2", f"{idx}.3", f"{idx}.4") for idx, i in enumerate(tanya)
    ]
    data = {
        "items": fixData
    }
    return render(request, "question.html", context=data)
