import sys
from playlist_utils import  parse_input, get_playlist_data

def main():
    ids = get_input()
    if parse_input(ids) != None:
        ID = parse_input(ids)
        print(get_playlist_data(ID))

def get_input():
    if len(sys.argv) >= 2:
        ids=sys.argv[1:]
    else:
        ids=[input("Enter a playlist ID or URL: ")]
    return ids

        # json_data = json.dumps(pl_response, indent=4)
        # print(json_data)

if __name__ == "__main__":
    main()
