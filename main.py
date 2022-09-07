import requests
import account
import startWorkDataBase


def main():
    artists = requests.get("https://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key=" + account.api_key
                           + "&format=json")  # getter json top chart artist
    artists = (eval(artists.text))['artists']['artist']  # json text to dict and go to interesting dict

    index_element = 1
    for artist in artists:
        del artist['mbid'], artist['streamable'], artist['image']  # delete unuseful information
        artist['_id'] = index_element  # add index in slovar
        index_element += 1
    start_work_data_base(artists)


if __name__ == '__main__':
    main()
