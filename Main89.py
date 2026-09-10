# E46.Creating Command Line Utility in Python.
import argparse;
import requests;
def download_file(url, local_filename):
    if local_filename is None:
        local_filename = url.split("/")[-1]
        # NOTE the Stream = True Parameter Below.
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have Chunk Encoded Response Uncomment if.
                # And Set Chunk_Size Parameter to None.
                # If Chunk:
                f.write(chunk)
    return local_filename
parser = argparse.ArgumentParser()
# Add Command Line Arguments.
parser.add_argument("url", help="URL of the File to Download")
# parser.add_argument("output", help="by which name do you want to save your file").
parser.add_argument("-o", "--output", type=str, help="Name of the File", default=None)
# Parse the Arguments.
args = parser.parse_args()
# Use the Arguments in your Code.
print(args.url)
print(args.output, type(args.output))
download_file(args.url, args.output)