def get_input(prompt, cast_func):
    while True:
        try:
            return cast_func(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {cast_func.__name__}.")
            