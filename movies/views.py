from django.shortcuts import render

# ข้อมูลตัวอย่าง (เปลี่ยนให้เป็นข้อมูลจริงจากฐานข้อมูลถ้าต้องการ)
movies = [
    "Your Name",
    "Spirited Away",
    "A Silent Voice",
    "Attack on Titan",
    "One Piece",
    "Naruto",
    "Demon Slayer",
    "My Neighbor Totoro",
    "Weathering With You",
    "Initial D",
]

def movie_list(request):
    context = {
        'movies': movies[:10],  # แสดงแค่ 10 เรื่อง
    }
    return render(request, 'movies/movie_list.html', context)
