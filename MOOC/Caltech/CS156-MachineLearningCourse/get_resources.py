import urllib
import youtube_dl


def get_lectures():
    for i in range(1, 19):
        urllib.urlretrieve("http://work.caltech.edu/slides/slides{}.pdf".format(
            str(i).zfill(2)), "./Lectures/slides{}.pdf".format(str(i).zfill(2)))


def get_videos():
    opts = ["-o", "./Videos/%(title)s.%(ext)s",
            "https://www.youtube.com/playlist?list=PLD63A284B7615313A"]
    youtube_dl.main(opts)


def main():
    get_lectures()
    get_videos()

if __name__ == '__main__':
    main()
