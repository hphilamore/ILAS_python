def test_calculator_add_returns_correct_result():
    result = calc_add(2,2)
    assert result == 4


# def calc_add(x,y):
# 	pass

	# return x+y

    # if isinstance(x, number_types) and isinstance(y, number_types):
    #             return x + y
    #         else:
    #             raise ValueError("Non-numeric input given")





# def test_calculator_returns_error_message_if_both_args_not_numbers():
# 	try:
#             calc_add("two", "three")

#         except ValueError:
#             print("Exception caught")
#             assert True, "Fail: ValueError exception not caught"

#         except:
#             assert False, "Fail: Exception other than ValueError caught"

#         else: 
#             assert False, "Fail: No exception caught"




# def test_calculator_returns_error_message_if_both_args_not_numbers():
#      with pytest.raises(ValueError):
#             calc_add("two", "three")
            
# def test_calculator_returns_error_message_if_x_arg_not_number():
#      with pytest.raises(ValueError):
#             calc_add("two", 3)

# def test_calculator_returns_error_message_if_y_arg_not_number( ):
#      with pytest.raises(ValueError):
#             calc_add(2, "three")