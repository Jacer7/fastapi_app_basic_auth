import pandas as pd

# Define the path to your Excel file
excel_file_path = "data/questions_en.xlsx"

# Function to append a new question to the Excel file
def append_question_to_excel(question_data):
    # Load the existing Excel file into a pandas DataFrame
    try:
        df_existing = pd.read_excel(excel_file_path)
    except FileNotFoundError:
        # If the file doesn't exist, create a new DataFrame with the appropriate columns
        df_existing = pd.DataFrame(columns=["question", "subject", "use", "correct", 
                                            "responseA", "responseB", "responseC", "responseD", "remark"])

    # Create a new DataFrame for the new question
    new_question_df = pd.DataFrame({
        "question": [question_data["question"]],
        "subject": [question_data["category"]],  # Assuming subject is the category
        "use": [question_data["test_type"]],
        "correct": [question_data["correct_answer"]],
        "responseA": [question_data["responseA"]],
        "responseB": [question_data["responseB"]],
        "responseC": [question_data["responseC"]],
        "responseD": [question_data["responseD"]],
        "remark": [question_data.get("remark", "")]  # Optional remark field, default is empty
    })

    # Append the new question to the existing DataFrame
    df_updated = pd.concat([df_existing, new_question_df], ignore_index=True)

    # Write the updated DataFrame back to the Excel file
    with pd.ExcelWriter(excel_file_path, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
        df_updated.to_excel(writer, index=False, sheet_name="questions")  # Assuming 'Sheet1' is the sheet name

    return "Question successfully appended to Excel file!"
