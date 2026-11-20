import  Lab_2.bmi as bmi

def test_bmi_normal_weight():
    result = 0
    assert result == bmi.calculate_bmi(1.75,74)
    
    
def test_bmi_over_weight():
    result = 1
    assert result == bmi.calculate_bmi(1.73,80)
    
def test_bmi_under_weight():
    result = -1
    assert result == bmi.calculate_bmi(1.73,50)