# *** Uncomment the line below *** #
#from api_token import *

def check_api():
    key_keeper = "api_token.py"
    parameter = "OPENAI_API_KEY"
    try:
        with open(key_keeper, "r", encoding="utf8") as config:
            token_line = config.readlines()
            for line in token_line:
                if parameter in line:
                    return
    except FileNotFoundError:
        print("Error: Configuration Not Found")
        return
    finally:
        config.close()

    api_key = str(input("Enter your 'OpenAI' API-Key: "))
    with open(key_keeper, "a", encoding="utf8") as config:
        if len(token_line) >= 0:
            config.write("\n")
            config.write(f"{parameter} = '{api_key}'")
            print("TOKEN was added successfully.")

    with open(key_keeper, "r+", encoding="utf8") as config:
        empty_lines = config.readlines()
        config.seek(0)
        config.writelines(line for line in empty_lines if line.strip())
        config.truncate()

check_api()