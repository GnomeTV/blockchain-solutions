import requests

def get_all_blocks():
    r = requests.get("https://bcschain.info/api/recent-blocks?count=500")
    blocks = r.json()
    return blocks[::-1]

# def get_detail_block(block_height):
#     r = requests.get("https://bcschain.info/api//block/{block_height}")
#     blocks = r.json()
#     return blocks
