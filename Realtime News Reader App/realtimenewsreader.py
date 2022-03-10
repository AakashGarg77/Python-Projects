import json, requests

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch('Sapi.SpVoice')
    speak.Speak(str)

def getnews(url):
    count = 1
    r = requests.get(url).text
    parsed = json.loads(r)
    speak("Here are your news")
    for i in parsed["articles"][:5]:
        print(i["title"])
        speak(i["title"])
        if count<5:
            speak("Next is ")
            count += 1
        else:
            speak("Thanks")


if __name__ == '__main__':
    print("Welcome To The Realtime News Reader App".center(100, '-'))
    speak("Welcome To The Realtime News Reader App")
    li = ["Top Headlines", "Business", "Entertainment", "Technology", "Health", "Science", "Sports"]
    speak("Choose one topic from the given list")
    user = input(f"Choose one topic from the given list:\n{li}\n").lower()
    if user=='top headlines':
        url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=e8271206a3be43fcb2772500d3a766c3'
        getnews(url)
    elif user=='business':
        url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=e8271206a3be43fcb2772500d3a766c3"
        getnews(url)
    elif user=='entertainment':
        url = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=e8271206a3be43fcb2772500d3a766c3"
        getnews(url)
    elif user=='technology':
        url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=e8271206a3be43fcb2772500d3a766c3"
        getnews(url)
    elif user=='health':
        url = "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=e8271206a3be43fcb2772500d3a766c3"
        getnews(url)
    elif user=='science':
        url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=e8271206a3be43fcb2772500d3a766c3"
        getnews(url)
    elif user=='sports':
        url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=e8271206a3be43fcb2772500d3a766c3"
        getnews(url)
    else:
        print('Invalid Input')