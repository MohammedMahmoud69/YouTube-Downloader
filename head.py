from pytube import YouTube
import emoji


link = input(emoji.emojize("Enter The YouTube Video URL :thinking_face: : "))

video = YouTube(link).streams.get_highest_resolution()

try:
    video.download("/Users/Hassaan/Documents/courses/")
except:
    print(emoji.emojize("Your Video Download Has a Problem :robot:"))

print(emoji.emojize("This Download Has Completed :partying_face:"))