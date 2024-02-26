# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20230038
# Date: 10/12/2023
from graphics import *
import os
poss_outcomes = [0, 20, 40, 60, 80, 100, 120]
def get_cred():  
    ps_cred = int(input("Enter pass credits: "))
    def_cred = int(input("Enter defer credits: "))
    fa_cred = int(input("Enter fail credits: "))
    return ps_cred, def_cred, fa_cred
def print_progression(data):
    if data[0] >= 100:
        if data[0] == 120:
            print("Progress -", ', '.join(map(str, data)))
        else:
            print("Progress (module trailer) -", ', '.join(map(str, data)))
    elif 80 >= data[0] >= 0 and 60 >= data[2] >= 0:
        print("Module retriever -", ', '.join(map(str, data)))
    elif data[2] >= 80:
        print("Exclude -", ', '.join(map(str, data)))

# Check if student or teacher
check = input("Are you a member of staff (press any key to continue, else press 'n')?: ").lower()
if check != "n":
    # Staff Logic
    print("Welcome dear member of staff.")
    progression_data = []

    def cont_choice():
        choice = input("Would you like to add more marks? Press 'q' to quit or any key to continue: ").lower()
        return choice

    def write_to_text_file(file_name, data):
        with open(file_name, 'w') as file:
            for entry in data:
                for label, values_list in entry.items():
                    if label == "Progress":
                        if values_list[0] >= 100:
                            if values_list[0] == 120:
                                file.write("Progress - ")
                            else:
                                file.write("Progress (module trailer) - ")
                        elif 0<=values_list[0]<100 and values_list[2]<=60:
                            file.write("Module retriever - ")
                        elif values_list[2]>=80:
                            file.write("Exclude - ")
                    file.write(', '.join(map(str, values_list)))
                    file.write("\n")

    def read_from_text_file(file_name):#(reads from text file converting it to a list of dictionaries)
        data_list = []

        try:
            with open(file_name, 'r') as file:
                for line in file:
                    parts = line.strip().split(' - ')
                    if len(parts) == 2:
                        label = parts[0]
                        values = [int(value) for value in parts[1].split(',')]
                        entry = {label: values}
                        data_list.append(entry)
        except FileNotFoundError:
            print("File not found. There's no data to read.")

        return data_list
    
    # Verification
    if __name__ == "__main__":
        file_name = os.path.abspath('progression_data.txt')  
        while True:
            try:
                ps_cred, def_cred, fa_cred = get_cred()
                if (ps_cred + def_cred + fa_cred == 120
                    and all(cred in poss_outcomes for cred in [ps_cred, def_cred, fa_cred])):
                    progression_data.append({"Progress": [ps_cred, def_cred, fa_cred]})
                    if ps_cred >= 100:
                        if ps_cred == 120:
                            print("Progress")
                        else:
                            print("Progress (module trailer)")
                    elif 80 >= ps_cred >= 0 and 60 >= fa_cred >= 0:
                        print("Module retriever")
                    elif fa_cred >= 80:
                        print("Exclude")
                else:
                    if ps_cred + def_cred + fa_cred != 120:
                        print("Total credits do not add up to 120")
                    else:
                        print("Invalid integer or out of range")

                choice = cont_choice()
                if choice == 'q':
                    # Write all the data to the text file after the loop
                    write_to_text_file(file_name, progression_data)
                    break
            except ValueError:
                print("Invalid input. Please enter integers for credits")

    # Drawing Histogram
        def draw_histogram(win, title, data, colors, labels, total_students):
            win.setBackground("light grey")

            title_text = Text(Point(win.getWidth() / 2, 20), title)
            title_text.setSize(20)
            title_text.draw(win)

            bar_width = 100
            spacing = 30
            x_position = 20
            y_position = 100

            # Display total student data 
            total_students_text = Text(Point(win.getWidth() - 80, 20), f"Total Students: {total_students}")
            total_students_text.setSize(14)
            total_students_text.draw(win)

            for value, color, label in zip(data, colors, labels):
                bar = Rectangle(Point(x_position, y_position), Point(x_position + bar_width, y_position - value))
                bar.setFill(color)
                bar.draw(win)
                label_text = Text(Point(x_position + bar_width / 2, y_position + 10), label)
                label_text.draw(win)
                value_label = Text(Point(x_position + bar_width / 2, y_position - value - 10), str(value))
                value_label.draw(win)
                x_position += bar_width + spacing

        def main():
            try:
                win = GraphWin("Results Histogram", 800, 200)

                pro_count = sum(1 for data in progression_data if data.get("Progress", [])[0] == 120)
                mod_tra_count = sum(1 for data in progression_data if 100 == data.get("Progress", [])[0])
                mod_ret_count = sum(1 for data in progression_data if 80 >= data.get("Progress", [])[0] >= 0 and 60 >= data.get("Progress", [])[2])
                ex_count = sum(1 for data in progression_data if data.get("Progress", [])[2] >= 80)

                data = [pro_count, mod_tra_count, mod_ret_count, ex_count]
                colors = ["dark green", "light yellow", "orange", "red"]
                labels = ["PROGRESS", "TRAILER", "RETRIEVE", "EXCLUDE"]
                total_students = len(progression_data)  # Calculate total students
                draw_histogram(win, "Histogram Results", data, colors, labels, total_students)
                if not win.isClosed():
                    win.getMouse()
            except GraphicsError as e:
                print("")
            finally:
                if not win.isClosed():
                    win.close()

        if __name__ == "__main__":
            main()

        # Part 2 – List (extension)
        print("\nPart 2:")
        for data in progression_data:
            if data.get("Progress", [])[0] >= 100:
                if data.get("Progress", [])[0] == 120:
                    print("Progress -", ', '.join(map(str, data.get("Progress", []))))
                else:
                    print("Progress (module trailer) -", ', '.join(map(str, data.get("Progress", []))))
            elif 80 >= data.get("Progress", [])[0] >= 0 and 60 >= data.get("Progress", [])[2] >= 0:
                print("Module retriever -", ', '.join(map(str, data.get("Progress", []))))
            elif data.get("Progress", [])[2] >= 80:
                print("Exclude -", ', '.join(map(str, data.get("Progress", []))))

        # Part 3-reading and printing data from the text file
        read_data = read_from_text_file(file_name)
        if read_data:
            print("\nPart 3:")
            for entry in read_data:
                for label, values_list in entry.items():
                    if label == "Progress":
                        print(f"Progress - {values_list[0]}, {values_list[1]}, {values_list[2]}")
                    elif label == "Progress (module trailer)":
                        print(f"Progress (module trailer) - {values_list[0]}, {values_list[1]}, {values_list[2]}")
                    elif label == "Module retriever":
                        print(f"Module retriever - {values_list[0]}, {values_list[1]}, {values_list[2]}")
                    elif label == "Exclude":
                        print(f"Exclude - {values_list[0]}, {values_list[1]}, {values_list[2]}")
            print()  # Add an extra line between entries   
        print("THANK YOU")
else:
    # Student Logic
    print("Welcome dear student")
    ps_cred, def_cred, fa_cred = get_cred()
    if ps_cred + def_cred + fa_cred == 120:
        if ps_cred>=100:
            if ps_cred == 120:
                print("Progress")
            else:
                print("Progress (module trailer)")
        elif 80 >= ps_cred >= 0 and 60 >= fa_cred >= 0:
            print("Module retriever")
        elif fa_cred >= 80:
            print("Exclude")
    else:
        if ps_cred + def_cred + fa_cred != 120:
            print("Total credits do not add up to 120")
        else:
            print("Invalid integer or out of range")
    print("THANK YOU")
"""
REFERENCES
Use of f-strings in python: - https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
                            - https://docs.python.org/3/reference/lexical_analysis.html#f-strings
                            - https://realpython.com/python-f-strings/
Use of map() function in python: - https://www.w3schools.com/python/ref_func_map.asp
                                    - https://docs.python.org/3/library/functions.html#map
Use of join() function:     - https://pythonbasics.org/join/
Use of OS module in python: - https://www.edureka.co/blog/os-module-in-python#:~:text=The%20OS%20module%20in%20Python%20is%20a%20part%20of%20the,in%20day%20to%20day%20programming.
                            - https://www.geeksforgeeks.org/python-os-path-abspath-method-with-example/"""

