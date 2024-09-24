import openpyxl
import random
import pandas as pd

def read_questions_from_xlsx(test_type: str, categories: list, num_questions: int):
    """
    Reads questions from an XLSX file, filters by test_type and categories, and returns
    a random selection of num_questions.
    
    :param file_path: Path to the Excel file
    :param test_type: Selected test type (e.g., "Positioning test", "Validation test")
    :param categories: List of selected categories (e.g., ["Databases", "Docker"])
    :param num_questions: Number of questions to return (5, 10, or 20)
    :return: A list of randomly selected questions
    """
    file_path="app/data/questions_en.xlsx"
    workbook = pd.read_excel(file_path, sheet_name="questions")
    workbook.fillna("", inplace=True)
    
    workbook['use'] = workbook['use'].str.strip().str.lower()
    workbook['subject'] = workbook['subject'].str.strip().str.lower()
    # Normalize user inputs as well
    test_type = test_type.strip().lower()
    categories = [category.strip().lower() for category in categories]

    # Filter the DataFrame based on the test_type and categories
    filtered_questions = workbook[
        (workbook['use'] == test_type) & (workbook['subject'].isin(categories))
    ]
    # If no questions are found, return an empty list
    if filtered_questions.empty:
        return []
    questions = filtered_questions.to_dict(orient="records")
    random.shuffle(questions)
    return questions[:num_questions]



def get_unique_test_types_and_categories(file_path="app/data/questions_en.xlsx"):
    # Load the Excel file into a pandas DataFrame
    workbook = pd.read_excel(file_path, sheet_name="questions")

    # Replace NaN or None values with empty strings or appropriate defaults
    workbook.fillna("", inplace=True)

    # Get unique test types and categories
    test_types = workbook['use'].str.strip().unique().tolist()
    categories = workbook['subject'].str.strip().unique().tolist()

    return test_types, categories


if __name__ == "__main__":
    # print(read_questions_from_xlsx("Positioning test", ["Databases", "Docker"], 5))
    print(get_unique_test_types_and_categories())