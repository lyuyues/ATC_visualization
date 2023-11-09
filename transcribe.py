from openai import OpenAI
import os
# ------------------ using openai api to trascribe the files in foldder -----------------------
client = OpenAI()
# OpenAI.organization = "org-AdXGbVNxq7rD4cMNfwnV2wYK" # Personal
# OpenAI.api_key = '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' #personal

OpenAI.organization = "org-yArN5GKOP6FZ1X87WAVwQpDu" # Watvis
# OpenAI.api_key = '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' #watvis
OpenAI.api_key = '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' #watvis

def transcribe (audio_file_name: str, output_path: str):
    # print(audio_file_name)
    # print(output_path)
    audio_file= open(audio_file_name, "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )
    print(transcript)

    # Define the file path
    file_path = output_path + "/" + audio_file_name + '_transcript.json'
    with open(file_path, 'w') as file:
        file.write(transcript)



dir_name = "2023-11-05-17-14-32"
directory_path = 'data/' + dir_name
out_dir_path = 'data/' + dir_name + "_transcription"
# List all files in the directory
file_names = os.listdir(directory_path)

# Loop through the files and read each one
for file_name in file_names:
    file_path = os.path.join(directory_path, file_name)
    if os.path.isfile(file_path):  # Check if it's a file and not a directory
        with open(file_path, 'rb') as file:
            content = file.read()
            # Do something with the content
            transcribe(file_name, out_dir_path)
            # print(f"Contents of {file_name}:")
            # print(content)


