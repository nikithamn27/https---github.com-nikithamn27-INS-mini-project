import key_utils
import signer
import verifier

def main():
    while True:
        print("\n--- DSS Mini Project ---")
        print("1. Generate Keys")
        print("2. Sign a Message")
        print("3. Verify a Signature")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            key_utils.generate_keys()
        elif choice == "2":
            signer.sign_message_terminal()
        elif choice == "3":
            verifier.verify_signature("files/signed_message.txt", "files/signature.sig")
        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
