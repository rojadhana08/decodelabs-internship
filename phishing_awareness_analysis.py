import re

def analyze_message(message):
    red_flags = []

    keywords = [
        "urgent", "verify", "password", "bank", "account",
        "click", "login", "winner", "prize", "free",
        "limited", "confirm", "update", "gift"
    ]

    lower = message.lower()

    for word in keywords:
        if word in lower:
            red_flags.append(f"Suspicious keyword: '{word}'")

    urls = re.findall(r'https?://\S+|www\.\S+', message)
    if urls:
        red_flags.append("Contains a link: " + ", ".join(urls))

    if "@" in message and (".ru" in lower or ".xyz" in lower):
        red_flags.append("Suspicious email domain detected")

    print("\n----- Phishing Analysis Report -----")
    if red_flags:
        print("Potential Phishing Detected!\n")
        for i, flag in enumerate(red_flags, 1):
            print(f"{i}. {flag}")
        print("\nReason: The message contains common phishing indicators.")
    else:
        print("No major phishing indicators found.")

message = input("Enter the email/message to analyze:\n")
analyze_message(message)
