nameDict = {
    'Model_Architecture(CS200-E).h5': [77, "Acc_Curve_Harshit_Preprocessed_Data-CS200E.png", "Conf_Matrix_Harshit_Preprocessed_Data-CS200E.png"],
    'Model_Architecture(CS200-U).h5': [90, "Acc_Curve_Harshit_Preprocessed_Data-CS200U.png", "Conf_Matrix_Harshit_Preprocessed_Data-CS200U.png"],
    'Model_Architecture(CS250-E).h5': [64, "Acc_Curve_Harshit_Preprocessed_Data-CS250E.png", "Conf_Matrix_Harshit_Preprocessed_Data-CS250E.png"],
    'Model_Architecture(CS250-U).h5': [83, "Acc_Curve_Harshit_Preprocessed_Data-CS250U.png", "Conf_Matrix_Harshit_Preprocessed_Data-CS250U.png"],
    'Model_Architecture(CS300-E).h5': [88, "Acc_Curve_Harshit_Preprocessed_Data-CS300E.png", "Conf_Matrix_Harshit_Preprocessed_Data-CS300E.png"],
    'Model_Architecture(CS300-U).h5': [75, "Acc_Curve_Harshit_Preprocessed_Data-CS300U.png", "Conf_Matrix_Harshit_Preprocessed_Data-CS300U.png"]
}

print("| Model Name | Accuracy | Accuracy Curve | Confusion Matrix |\n |:----------:|:--------:|:--------------:|:----------------:|")

for model, values in nameDict.items():
    print(f"| {model} | {values[0]}% | ![Accuracy Curve](./result_imgs/{values[1]}) | ![Confusion Matrix](./result_imgs/{values[2]}) |")
