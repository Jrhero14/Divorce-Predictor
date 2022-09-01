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
    tanya = [
        "1. Jika salah satu dari kami meminta maaf saat diskusi memburuk, diskusi berakhir.",
        "2. Saya tahu kami dapat mengabaikan perbedaan kami, walaupun terkadang beberapa hal menjadi sulit.",
        "3. Jika kami memerlukannya, kami dapat mengajak diskusi bersama pasangan saya dari awal dan memperbaikinya.",
        "4. Saat saya berdiskusi dengan pasangan saya, untuk kontak dengannya akhirnya akan berhasil",
        "5. Menghabiskan waktu saya dengan istri saya adalah spesial bagi kami.",
        "6. Kami tidak memiliki waktu sebagai pasangan saat berada di rumah.",
        "7. Kami seperti dua orang asing yang berbagi lingkungan yang sama di rumah ketimbang sebagai keluarga.",
        "8. Saya menikmati liburan dengan istri saya.",
        "9. Saya menikmati bepergian dengan istri saya.",
        "10. Tujuan kami sebagian besar biasa bagi pasangan saya.",
        "11. Saya berpikir bahwa suatu hari di masa depan, jika saya melihat ke masa lalu, saya melihat diri saya dan pasangan saya telah harmonis satu sama lain.",
        "12. Pasangan saya dan saya memiliki martabat yang sama dalam hal kebebasan pribadi.",
        "13. Pasangan saya dan saya memiliki selera hiburan yang serupa",
        "14. Sebagian besar tujuan kami untuk orang-orang (anak-anak, teman-teman, dll) sama.",
        "15. Impian kami dengan pasangan saya serupa dan selaras",
        "16. Kami kompatibel dengan pasangan saya tentang bagaimana seharusnya cinta.",
        "17. Kami berbagi pandangan yang sama mengenai menjadi bahagia dalam hidup kami bersama pasangan saya.",
        "18. Pasangan saya dan saya mempunyai ide-ide yang serupa tentang bagaimana seharusnya pernikahan itu.",
        "19. Pasangan saya dan saya mempunyai ide-ide yang serupa tentang bagaimana seharusnya peranan di dalam sebuah pernikahan.",
        "20. Pasangan saya dan saya mempunyai derajat yang serupa dalam kepercayaan.",
        "21. Saya tahu betul apa kesukaan istri saya.",
        "22. Saya tahu apa yang pasangan saya inginkan dalam merawatnya ketika dia sakit.",
        "23. Saya tahu apa makanan kesukaan pasangan saya.",
        "24. Saya dapat menjelaskan apa jenis stres yang dihadapi pasangan saya dalam hidupnya.",
        "25. Saya tahu dunia batin pasangan saya.",
        "26. Saya tahu kekhawatiran dasar milik pasangan saya",
        "27. Saya tahu apa sumber stres saat ini pada pasangan saya",
        "28. Saya tahu apa harapan dan keinginan pasangan saya.",
        "29. Saya mengetahui pasangan saya dengan sangat baik.",
        "30. Saya mengetahui teman-teman pasangan saya dan hubungan sosial mereka.",
        "31. Saya merasa agresif saat berargumen dengan pasangan saya.",
        "32. Saat berdiskusi dengan pasangan saya, saya biasanya menggunakan ungkapan seperti 'kamu selalu' atau 'kamu tidak pernah'.",
        "33. Saya bisa menggunakan pendapat negatif mengenai kepribadian pasangan saya dalam diskusi kami.",
        "34. Saya dapat menggunakan ungkapan yang bersifat menyerang dalam diskusi kami.",
        "35.Saya dapat membuat kesal pasangan saya selama diskusi kami.",
        "36. Saya dapat menghina saat kami berdiskusi.",
        "37. Diskusi saya dengan pasangan tidak tenang.",
        "38. Saya membenci cara pasangan saya dalam membuka suatu topik.",
        "39. Diskusi kami sering muncul secara tiba-tiba.",
        "40. Kami berdiskusi begitu saja sebelum saya mengetahui apa yang sebenarnya terjadi.",
        "41. Saat saya berbicara sesuatu ke pasangan saya, tiba - tiba ketenangan saya hancur.",
        "42. Saat saya bertengkar dengan pasangan saya, saya hanya pergi dan tidak mengucapkan apapun.",
        "43. Saya biasanya diam untuk sedikit menenangkan suasana.",
        "44. Terkadang saya pikir ada baiknya untuk saya jika meninggalkan rumah untuk sementara waktu.",
        "45. Saya lebih baik diam daripada berdiskusi dengan pasangan saya.",
        "46. Bahkan jika saya benar dalam diskusi, saya tetap diam untuk menyakiti pasangan saya.",
        "47. Ketika saya berdiskusi dengan pasangan saya, saya tetap diam karena saya takut tidak bisa mengendalikan amarah saya.",
        "48. Saya merasa diri saya benar dalam diskusi kami.",
        "49. Saya tidak peduli apa yang telah dituduhkan kepada saya.",
        "50. Saya bukanlah yang bersalah atas tuduhan yang diberikan.",
        "51. Saya bukanlah yang salah atas masalah-masalah yang ada di rumah.",
        "52. Saya tidak ragu untuk mengatakan kepada pasangan saya mengenai kekurangannya.",
        "53. Saat saya berdiskusi, saya mengungkit kekurangan-kekurangan pasangan saya.",
        "54. Saya tidak takut untuk mengatakan ketidakmampuan milik pasangan saya.",
    ]

    fixData = [
        dataClass(None, i, idx,f"{idx}.0", f"{idx}.1", f"{idx}.2", f"{idx}.3", f"{idx}.4") for idx, i in enumerate(tanya)
    ]
    data = {
        "items": fixData
    }
    return render(request, "question.html", context=data)
