#!./python.exe

def cleanup():
    print("Cleaning up resources...")

def main():
    dictionary = {"key": "value"}

    defer cleanup()
    defer print(f"Final value: {dictionary['key']}")

    print("Start main function")

    # ... do some work ...

    print("Working...")
    dictionary["key"] = "new value"

    print("End main function")


if __name__ == "__main__":
    main()


    import dis
    dis.dis(main)
