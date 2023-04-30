import requests
import sys
import os


def remove_text(image_path, clipdrop_key):
    output_folder_path = "output"
    image_file = open(image_path, 'rb')
    file_extension = os.path.splitext(image_path)[1].lower()

    if file_extension not in ['.jpeg', '.jpg', '.png']:
        raise ValueError('Unsupported file type')

    response = requests.post('https://clipdrop-api.co/remove-text/v1',
      files = {
        'image_file': ('image.jpg', image_file, 'image/jpeg')
        },
      headers = { 'x-api-key': clipdrop_key}
    )

    if (response.ok):
        image_data = response.content

        # create result folder if it does not exist
        if not os.path.exists(output_folder_path):
            os.mkdir(output_folder_path)

        file_name_with_path, file_extension = os.path.splitext(image_path)
        file_name = os.path.basename(file_name_with_path)

        new_file_path = os.path.join(output_folder_path, f"{file_name}{file_extension}")

        with open(new_file_path, 'wb') as f:
            f.write(image_data)
        return new_file_path
    else:
      response.raise_for_status()

if __name__ == '__main__':
    image_path = sys.argv[1]
    clipdrop_key = sys.argv[2]

    new_file_path = remove_text(image_path, clipdrop_key)
    print(new_file_path)
