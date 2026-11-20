import employee_info as info
import pytest

def test_get_employees_by_age_range():
    result = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    
    assert result == info.get_employees_by_age_range(22,31)

def test_calculate_average_salary():
    result = 60166.66
    assert result == pytest.approx(info.calculate_average_salary())

def test_get_employees_by_dept():
    result = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert result == info.get_employees_by_dept("Engineering")
