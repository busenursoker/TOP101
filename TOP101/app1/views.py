from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Favorite
from .forms import FavoriteForm
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404

def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites_list.html', {'favorites': favorites})

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["Email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "your account has been successfully created.")
        return redirect("signin")

    return render(request, 'register.html')

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.username
            return render(request, "home.html", {"fname": fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect("home")

    return render(request, 'login.html')

def favorites(request):
    if not request.user.is_authenticated:
        messages.info(request, "Sorry, you have to have an account to add to your favorites. Please register or sign in.")
        return render(request, 'home.html')  # Redirect to home or show a message
    return redirect('favorites_list')

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('signin') 

def movie(request):
    return render(request, 'movie.html')

def movies(request):
    movies_data = [
    {'title': 'The Godfather', 'type': 'Movie', 'rating': '9.2', 'genre': 'Crime, Drama', 'img': 'img/1.jpg'},
    {'title': 'Do the Right Thing', 'type': 'Movie', 'rating': '8.0', 'genre': 'Drama', 'img': 'img/Do the right thing.jpg'},
    {'title': 'Citizen Kane', 'type': 'Movie', 'rating': '8.3', 'genre': 'Drama, Mystery', 'img': 'img/citizen kane.jpg'},
    {'title': 'Before Sunrise', 'type': 'Movie', 'rating': '8.1', 'genre': 'Drama, Romance', 'img': 'img/before sunrise.jpg'},
    {'title': 'Boyhood', 'type': 'Movie', 'rating': '7.9', 'genre': 'Drama', 'img': 'img/boyhood.jpg'},
    {'title': '8½', 'type': 'Movie', 'rating': '8.0', 'genre': 'Drama, Fantasy', 'img': 'img/8.jpg'},
    {'title': '2001: A Space Odyssey', 'type': 'Movie', 'rating': '8.3', 'genre': 'Adventure, Sci-Fi', 'img': 'img/2001.jpg'},
    {'title': 'The Rules of the Game', 'type': 'Movie', 'rating': '8.0', 'genre': 'Comedy, Drama', 'img': 'img/the rules oh the day.jpg'},
    {'title': 'Toy Story', 'type': 'Movie', 'rating': '8.3', 'genre': 'Animation, Adventure', 'img': 'img/toy story.jpg'},
    {'title': 'Psycho', 'type': 'Movie', 'rating': '8.5', 'genre': 'Horror, Mystery', 'img': 'img/psyco.jpg'},
    {'title': 'Seven Samurai', 'type': 'Movie', 'rating': '8.6', 'genre': 'Action, Drama', 'img': 'img/seven.jpg'},
    {'title': 'The Muppet Movie', 'type': 'Movie', 'rating': '7.6', 'genre': 'Adventure, Comedy', 'img': 'img/the muppet öovie.jpg'},
    {'title': 'Bicycle Thieves', 'type': 'Movie', 'rating': '8.3', 'genre': 'Drama', 'img': 'img/bicycle-thieves.jpg'},
    {'title': 'Singin in the Rain', 'type': 'Movie', 'rating': '8.3', 'genre': 'Comedy, Musical', 'img': 'img/singin in the rain.jpg'},
    {'title': 'Beauty and the Beast', 'type': 'Movie', 'rating': '8.0', 'genre': 'Animation, Family', 'img': 'img/beauty and the beast.jpg'},
    {'title': 'E.T. the Extra-Terrestrial', 'type': 'Movie', 'rating': '7.9', 'genre': 'Adventure, Family', 'img': 'img/et.jpg'},
    {'title': 'Jaws', 'type': 'Movie', 'rating': '8.0', 'genre': 'Adventure, Thriller', 'img': 'img/jaws.jpg'},
    {'title': 'Groundhog Day', 'type': 'Movie', 'rating': '8.0', 'genre': 'Comedy, Fantasy', 'img': 'img/day.jpg'},
    {'title': 'Goodfellas', 'type': 'Movie', 'rating': '8.7', 'genre': 'Biography, Crime', 'img': 'img/good.jpg'},
    {'title': 'The Shining', 'type': 'Movie', 'rating': '8.4', 'genre': 'Drama, Horror', 'img': 'img/the.jpg'},
    {'title': 'Moonlight', 'type': 'Movie', 'rating': '7.4', 'genre': 'Drama', 'img': 'img/moon.jpg'},
    {'title': 'Some Like It Hot', 'type': 'Movie', 'rating': '8.2', 'genre': 'Comedy, Romance', 'img': 'img/some.jpg'},
    {'title': 'Eternal Sunshine of the Spotless Mind', 'type': 'Movie', 'rating': '8.3', 'genre': 'Drama, Romance', 'img': 'img/eternal.jpg'},
    {'title': 'The Shawshank Redemption', 'type': 'Movie', 'rating': '9.3', 'genre': 'Drama', 'img': 'img/shaw.jpg'},
    {'title': 'Die Hard', 'type': 'Movie', 'rating': '8.2', 'genre': 'Action, Thriller', 'img': 'img/die.jpg'},
    {'title': 'Blazing Saddles', 'type': 'Movie', 'rating': '7.7', 'genre': 'Comedy, Western', 'img': 'img/blazing.jpg'},
    {'title': 'The Lion King', 'type': 'Movie', 'rating': '8.5', 'genre': 'Animation, Adventure', 'img': 'img/lion.jpg'},
    {'title': 'Mulholland Drive', 'type': 'Movie', 'rating': '7.9', 'genre': 'Drama, Mystery', 'img': 'img/drive.jpg'},
    {'title': 'The Dark Knight', 'type': 'Movie', 'rating': '9.0', 'genre': 'Action, Crime', 'img': 'img/joker.jpg'},
    {'title': 'Pulp Fiction', 'type': 'Movie', 'rating': '8.9', 'genre': 'Crime, Drama', 'img': 'img/pulp.jpg'},
    {'title': 'Apocalypse Now', 'type': 'Movie', 'rating': '8.4', 'genre': 'Drama, War', 'img': 'img/now.jpg'},
    {'title': 'Gladiator', 'type': 'Movie', 'rating': '8.5', 'genre': 'Action, Adventure', 'img': 'img/glad.jpg'},
    {'title': 'Tokyo Story', 'type': 'Movie', 'rating': '8.2', 'genre': 'Drama', 'img': 'img/tokyo.jpg'},
    {'title': '12 Years a Slave', 'type': 'Movie', 'rating': '8.1', 'genre': 'Biography, Drama', 'img': 'img/12.jpg'},
    {'title': 'Titanic', 'type': 'Movie', 'rating': '7.8', 'genre': 'Drama, Romance', 'img': 'img/titanic.jpg'},
    {'title': 'Within Our Gates', 'type': 'Movie', 'rating': '6.8', 'genre': 'Drama', 'img': 'img/gates.jpg'},
    {'title': 'The Good, the Bad and the Ugly', 'type': 'Movie', 'rating': '8.8', 'genre': 'Western', 'img': 'img/thes.jpg'},
    {'title': 'Fargo', 'type': 'Movie', 'rating': '8.1', 'genre': 'Crime, Drama', 'img': 'img/fargo.jpg'},
    {'title': 'Forrest Gump', 'type': 'Movie', 'rating': '8.8', 'genre': 'Drama, Romance', 'img': 'img/gump.jpg'},
    {'title': 'The Piano', 'type': 'Movie', 'rating': '7.6', 'genre': 'Drama, Music', 'img': 'img/piano.jpg'}
]
    return render(request, 'movies.html', {'movies': movies_data})

def TVshows(request):
    tvshows_data = [
    {'title': 'Breaking Bad', 'type': 'TV Show', 'rating': '9.5', 'genre': 'Action, Thriller', 'img': 'img/breakingbad.jpeg'},
    {'title': 'Game of Thrones', 'type': 'TV Show', 'rating': '9.2', 'genre': 'Action, Thriller', 'img': 'img/R (7).jfif'},
    {'title': 'The Boys', 'type': 'TV Show', 'rating': '8.7', 'genre': 'Action', 'img': 'img/R (8).jfif'},
    {'title': 'Kaleidoscope', 'type': 'TV Show', 'rating': '6.6', 'genre': 'Mystery', 'img': 'img/R (9).jfif'},
    {'title': 'The 100', 'type': 'TV Show', 'rating': '7.6', 'genre': 'Mystery, Drama', 'img': 'img/R (10).jfif'},
    {'title': 'House of the Dragon', 'type': 'TV Show', 'rating': '8.4', 'genre': 'Action, Mystery', 'img': 'img/R (11).jfif'},
    {'title': 'Better Call Saul', 'type': 'TV Show', 'rating': '9.7', 'genre': 'Comedy, Action', 'img': 'img/R (12).jfif'},
    {'title': 'Vikings', 'type': 'TV Show', 'rating': '8.5', 'genre': 'Action, Thriller', 'img': 'img/m4UY3phABl58QO4MBLk42HNr5b3.jpg'},
    {'title': 'The Witcher', 'type': 'TV Show', 'rating': '4.9', 'genre': 'Action, Thriller', 'img': 'img/R (13).jfif'},
    {'title': 'Stranger Things', 'type': 'TV Show', 'rating': '7.2', 'genre': 'Action, Mystery', 'img': 'img/R (14).jfif'},
    {'title': 'Wednesday', 'type': 'TV Show', 'rating': '8.1', 'genre': 'Action, Horror', 'img': 'img/R (16).jfif'},
    {'title': 'La Casa de Papel', 'type': 'TV Show', 'rating': '8.2', 'genre': 'Action', 'img': 'img/ES-ES_Localised_LCDP_S5_Main_Vertical_RGB_PRE20210730-4607-1anz6ou.webp'},
    {'title': 'The Punisher', 'type': 'TV Show', 'rating': '8.4', 'genre': 'Action, Thriller', 'img': 'img/il_1140xN.3166750471_lg3i.jpg'},
    {'title': 'Peaky Blinders', 'type': 'TV Show', 'rating': '8.8', 'genre': 'Action', 'img': 'img/R (17).jfif'},
    {'title': 'Dahmer', 'type': 'TV Show', 'rating': '5.6', 'genre': 'Horror, Mystery', 'img': 'img/R (18).jfif'},
    {'title': 'Invincible', 'type': 'TV Show', 'rating': '8.0', 'genre': 'Action, Thriller', 'img': 'img/sblr1kd5ydp61.webp'},
]

    return render(request, 'TVshows.html',{'Tvshows': tvshows_data})

@login_required
def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites_list.html', {'favorites': favorites})

@login_required
def add_favorite(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        movie_type = request.POST.get('type')
        Favorite.objects.create(user=request.user, title=title, type=movie_type)
        messages.success(request, "Added to favorites")
        return redirect('movies')
    return redirect('movies')

@login_required
def remove_favorite(request, favorite_id):
    favorite = get_object_or_404(Favorite, id=favorite_id, user=request.user)
    favorite.delete()
    messages.success(request, "Removed from favorites")
    return redirect('favorites_list')
