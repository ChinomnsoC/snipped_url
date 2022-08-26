
def id_to_short_url(id):
    map_url = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    short_url = ""

    # for each digit find the base 62
    while (id > 0):
        short_url += map_url[id % 62]
        id //= 62

    # reversing the short_url
    return short_url[len(short_url):: -1]


def short_url_to_id(short_url):
    url_id = 0
    for i in short_url:
        val_i = ord(i)
        if ord('a') <= val_i <= ord('z'):
            url_id = url_id * 62 + val_i - ord('a')
        elif ord('A') <= val_i <= ord('Z'):
            url_id = url_id * 62 + val_i - ord('A') + 26
        else:
            url_id = url_id * 62 + val_i - ord('0') + 52
    return url_id


# Press the green button in the gutter to run the script.

if __name__ == "__main__":
    url_id = 12345
    short_urls = id_to_short_url(url_id)
    print("Short URL from 12345 is : ", short_urls)
    print("ID from", short_urls, "is : ", short_url_to_id(short_urls))

