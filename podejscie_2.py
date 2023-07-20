import requests
import json
import xml.etree.ElementTree as ET

def get_trivia_question():
    url = "https://opentdb.com/api.php?amount=1&type=multiple"
    response = requests.get(url)

    if response.status_code == 200:
        content_type = response.headers.get('content-type')

        if 'json' in content_type.lower():
            data = response.json()
            question = data["results"][0]["question"]
            correct_answer = data["results"][0]["correct_answer"]
            incorrect_answers = data["results"][0]["incorrect_answers"]
            print("Question:", question)
            print("Correct Answer:", correct_answer)
            print("Incorrect Answers:", incorrect_answers)
        elif 'xml' in content_type.lower():
            data = ET.fromstring(response.content)
            question = data.find(".//question").text
            correct_answer = data.find(".//correct_answer").text
            incorrect_answers = [answer.text for answer in data.findall(".//incorrect_answer")]
            print("Question:", question)
            print("Correct Answer:", correct_answer)
            print("Incorrect Answers:", incorrect_answers)
        else:
            print("Unknown content type:", content_type)
    else:
        print("Failed to fetch data from the API.")

def main():
    get_trivia_question()

if __name__ == "__main__":
    main()