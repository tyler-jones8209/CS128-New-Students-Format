# Current Format: [id,last_name,first_name,email]
# Desired Format: [FIRSTNAME:LASTNAME:USERNAME:EMAIL:/bin/bash]

def format():
    with open("fall2024_128.txt", "r") as input_file, open("fall2024_128-complete.txt", "a") as output_file:
        for line in input_file:
            line = line.strip()
            USERNAME, LASTNAME, FIRSTNAME, EMAIL = line.split(',')

            # Handle cases with hyphens or spaces in the last name
            if "-" in LASTNAME:
                LASTNAME = "-".join(x.strip() for x in LASTNAME.split("-"))
            elif " " in LASTNAME:
                LASTNAME = LASTNAME.split(" ")[0]

            # Remove instructors from being added
            if (FIRSTNAME, LASTNAME) in [("First", "Last"), ("First", "Last"), ("First", "Last")]:
                continue

            # Format and write the output line
            output_file.write(f"{FIRSTNAME}:{LASTNAME}:{USERNAME}:{EMAIL}:/bin/bash\n")

format()
